import streamlit as st
from datetime import date
from model_logic.zscore.who_expanded_zscore import lms
from dotenv import load_dotenv
import os

load_dotenv()
zscore_password = os.getenv("ZSCORE_PASSWORD")

# Initialize the session state for password verification
if "zscore_password_correct" not in st.session_state:
    st.session_state.zscore_password_correct = False

# Password Check
if not st.session_state["zscore_password_correct"]:
    with st.form("login_form_zscore"):
        password = st.text_input("Enter the password to access this page:", type="password")
        submit_button = st.form_submit_button("Login")
    
    if submit_button:  # Check occurs only if the button is pressed
        if password == zscore_password:
            st.session_state.zscore_password_correct = True
            st.rerun()  # Rerun the script to update the state across the app
        else:
            st.error("Incorrect password. Please try again.")
            st.stop()  # Stop execution here if the password is incorrect
else:
    # Place all the page content within this block
    st.title('**:material/child_care: Toddler Z-Score Calculator**')

    now = date.today()


    st.write('''The Z-score calculator for toddler measurement allows you to easily determine how a child's height and weight compare to standardized growth charts, helping to assess whether their growth is within a healthy range or if there may be potential concerns.''')
    st.divider()

    if 'use_dob' not in st.session_state:
        st.session_state.use_dob = False

    gender_options = {
        'Male': 'M',
        'Female': 'F'
    }

    measurement_position_options = {
        'Berbaring': 'telentang',
        'Berdiri': 'berdiri'
    }

    div_main = st.container()
    div1 = div_main.container()
    col1, col2, col3 = div1.columns(3)

    col1.write('**1. Gender**')
    gender = col1.radio(
        'Please select gender:', gender_options.keys(),
        index = None
    )

    if st.session_state.use_dob:
        col2.write('**2. Date of Birth**')
        dob = col2.date_input(
            'Please input date of birth:',
            value = now
        )
        delta = now - dob
        st.session_state.age = delta.days
        col2.toggle("Use Date of Birth", key='use_dob')
    else:
        col2.write('**2. Months of Age**')
        st.session_state.age = round(col2.number_input(
            'Please input months of age:',
            min_value = 0,
            max_value = 59
        ) * 30.4167, 0)
        col2.toggle("Use Date of Birth", key='use_dob')

    col3.write('**3. Measurements**')
    measurement_position = col3.radio(
        'Measurement position:', measurement_position_options.keys(),
        index = None
    )
    weight = col3.number_input(
        'Weight (kg):',
        min_value = 0.0,
        max_value = 100.0,
        format = '%0.1f',
        step = 0.1
    )
    height = col3.number_input(
        'Height or length (cm):',
        min_value = 0.0,
        max_value = 100.0,
        format = '%0.1f',
        step = 0.1
    )

    def adjusted_lenhei(lenhei, age_days, method):
        if method == 'berdiri' and age_days < 731:
            lenhei += 0.7
        elif method == 'telentang' and age_days >= 731:
            lenhei -= 0.7
        return lenhei

    def compute_zscore(y, l, m, s):
        return ((pow(y / m, l)) - 1) / (s * l)

    def calc_sd(sd, l, m, s):
        return m * pow(1 + l * s * sd, 1/l)

    def adjusted_zscore(y, l, m, s):
        zscore = compute_zscore(y, l, m, s)
        SD3pos = calc_sd(3, l, m, s)
        SD3neg = calc_sd(-3, l, m, s)
        SD23pos = SD3pos - calc_sd(2, l, m, s)
        SD23neg = calc_sd(-2, l, m, s) - SD3neg
        not_zscore_na = zscore != None
        if not_zscore_na == True and zscore > 3:
            zscore = (3 + (y - SD3pos) / SD23pos)
        elif not_zscore_na == True and zscore < -3:
            zscore = (-3 + (y - SD3neg) / SD23neg)
        return round(zscore, 2)

    if measurement_position != None and height > 0 and gender != None:
        try:
            adjusted_height = adjusted_lenhei(height, st.session_state.age, measurement_position_options[measurement_position])
            bmi = round(weight / pow(adjusted_height/100, 2), 2)

            # z-score tbu
            lms_tbu = lms("lhfa", st.session_state.age, gender_options[gender])
            zscore_tbu = adjusted_zscore(
                adjusted_height,
                lms_tbu["L"],
                lms_tbu["M"],
                lms_tbu["S"]
            )

            # z-score bbu
            lms_bbu = lms("wfa", st.session_state.age, gender_options[gender])
            zscore_bbu = adjusted_zscore(
                weight,
                lms_bbu["L"],
                lms_bbu["M"],
                lms_bbu["S"]
            )

            # z-score bbtb
            if measurement_position_options[measurement_position] == 'telentang':
                cat = "wfl"
            else:
                cat = "wfh"
            lms_bbtb = lms(cat, height, gender_options[gender])
            zscore_bbtb = adjusted_zscore(
                weight,
                lms_bbtb["L"],
                lms_bbtb["M"],
                lms_bbtb["S"]
            )

            # z-score imtu
            lms_imtu = lms("bfa", st.session_state.age, gender_options[gender])
            zscore_imtu = adjusted_zscore(
                bmi,
                lms_imtu["L"],
                lms_imtu["M"],
                lms_imtu["S"]
            )

            div1.divider()

            div2 = div_main.container()
            div2_col1, div2_col2, div2_col3, div2_col4 = div2.columns(4)

            def colorize(z, div2col):
                if z > -1:
                    return div2col.success(f'''**{z}**''', icon='✅')
                elif z <= -1 and z > -2:
                    return div2col.warning(f'''**{z}**''', icon='⚠️')
                elif z <= -2:
                    return div2col.error(f'''**{z}**''', icon='🚨')

            div2_col1.write('**Weight for Length**')
            colorize(zscore_bbtb, div2_col1)
            div2_col2.write('**Weight for Age**')
            colorize(zscore_bbu, div2_col2)
            div2_col3.write('**Height for Age**')
            colorize(zscore_tbu, div2_col3)
            div2_col4.write('**BMI for Age**')
            colorize(zscore_imtu, div2_col4)
        except:
            div1.divider()