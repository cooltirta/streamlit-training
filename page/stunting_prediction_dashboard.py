import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

# get password from env
stunting_dashboard_password = st.secrets["STUNTING_DASHBOARD_PASSWORD"]
# stunting_dashboard_password = os.getenv("STUNTING_DASHBOARD_PASSWORD")

if "stunting_dashboard_password_correct" not in st.session_state:
    st.session_state.stunting_dashboard_password_correct = False

# Password Check
if not st.session_state["stunting_dashboard_password_correct"]:
    with st.form("login_form_cvd"):
        password = st.text_input("Enter the password to access this feature:", type="password")
        submit_button = st.form_submit_button("Login")
    
    if submit_button:  # Check occurs only if the button is pressed
        if password == stunting_dashboard_password:
            st.session_state.stunting_dashboard_password_correct = True
            st.rerun()  # Rerun the script to update the state across the app
        else:
            st.error("Incorrect password. Please try again.")
            st.stop()  # Stop execution here if the password is incorrect
else:

    st.title('**:material/space_dashboard: Stunting Prediction Dashboard**')
    main_div = st.container()
    main_div.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Stunting Prediction Dashboard is a comprehensive tool to provide insights into the projected stunting status of toddlers across Indonesia for the coming year. This dashboard offers an in-depth look at both the predicted numbers of stunted and non-stunted children nationwide and the provincial distribution of stunting cases, helping to inform targeted interventions and policy planning.")
    st.markdown('''<a href="https://lookerstudio.google.com/reporting/2514dd35-4b24-496c-abfe-bf72850aebb2" >Open in new tab <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20,300,0,0" /><span class="material-symbols-outlined">open_in_new</span>''', unsafe_allow_html=True)
    st.markdown('''<iframe src="https://lookerstudio.google.com/embed/reporting/2514dd35-4b24-496c-abfe-bf72850aebb2/page/p_nsprqn53jd" title="description" style="height:550px; width:100%; border:solid; border-width: thin;" ></iframe>''', unsafe_allow_html=True)