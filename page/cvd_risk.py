import streamlit as st
import streamlit.components.v1 as components

js_files = [
    './cvd_risk_diabetic_nonsmoker.js',
    './cvd_risk_diabetic_smoker.js',
    './cvd_risk_nondiabetic_nonsmoker.js',
    './cvd_risk_nondiabetic_smoker.js',
    './cvd_risk_nulldiabetic_nonsmoker.js',
    './cvd_risk_nulldiabetic_smoker.js'
]

js_scripts = {}

for file in js_files:
    with open(file, 'r') as f:
        js_scripts[file.lstrip('./')] = f.read()

# Page Title  
st.title('**:material/heart_check: Cardiovascular Disease Risk**')

# Page description
st.write('This calculator shows the likelihood of a person developing heart or blood vessel disease, whether fatal or not, in the next 10 years. The prediction is based on several factors, such as gender, age, blood pressure, cholesterol levels, smoking habits, and whether or not the person has diabetes.')

# Source URL
url = 'https://www.thelancet.com/journals/langlo/article/PIIS2214-109X(19)30318-3/fulltext'
st.write('Source: [World Health Organization cardiovascular disease risk charts: revised models to estimate risk in 21 global regions](%s)' %url)

# Horizontal row
st.divider()

# Main Container
div_main = st.container()

# Define 3 columns for layout
fcol1, fcol2, fcol3 = div_main.columns(3)

# Define session var use_bmi
if "use_bmi" not in st.session_state:
    st.session_state.use_bmi = False

# --------------- radio buttons options start ---------------
is_diabetes_options = {
    "Yes": 1,
    "No": 0
}

gender_options = {
    "Male": "m",
    "Female": "f"
}

is_smoker_options = {
    "Yes": 1,
    "No": 0
}
# --------------- radio buttons options end ---------------

# --------------- column 1 layout start ---------------
fcol1.markdown('**1. Diabetes Diagnosis**')
is_diabetes = fcol1.radio(
    "Do you have a diagnosis of diabetes?", is_diabetes_options.keys(),
    index=None,
)

fcol1.divider()

fcol1.markdown('**4. Age**')
age = fcol1.number_input(
    "Please enter your age (in year):", min_value=40, max_value=74, placeholder="Age..."
)
# --------------- column 1 layout end ---------------

# --------------- column 2 layout start ---------------
fcol2.markdown('**2. Gender**')
gender = fcol2.radio(
    "Please select your gender:", gender_options.keys(),
    index=None,
)

fcol2.divider()

fcol2.markdown('**5. Systolic Blood Pressure**')
systolic = fcol2.number_input(
    "Please enter your systolic blood pressure (mmHg):", min_value=0, placeholder="Systolic..."
)
# --------------- column 2 layout end ---------------

# --------------- column 3 layout start ---------------
fcol3.markdown('**3. Smoker Status**')
is_smoker = fcol3.radio(
    "Are you currently a smoker?", is_smoker_options.keys(),
    index=None,
)

fcol3.divider()

if is_diabetes == None:
    fcol3.markdown('**6. Cholesterol Level**')
    cholesterol = fcol3.number_input(
        "Please enter your cholesterol level (mg/dl):", min_value=0, placeholder="Cholesterol..."
    )
elif is_diabetes_options[is_diabetes] == 0:
    if st.session_state.use_bmi:
        fcol3.markdown('**6. Body Mass Index (BMI)**')
        bmi = fcol3.number_input(
            "Please enter your BMI (Body Mass Index):", min_value=0, placeholder="BMI..."
        )
    else:
        fcol3.markdown('**6. Cholesterol Level**')
        cholesterol = fcol3.number_input(
            "Please enter your cholesterol level (mg/dl):", min_value=0, placeholder="Cholesterol..."
        )
    fcol3.toggle("Use BMI", key='use_bmi')

else:
    fcol3.markdown('**6. Cholesterol Level**')
    cholesterol = fcol3.number_input(
        "Please enter your cholesterol level (mg/dl):", min_value=0, placeholder="Cholesterol..."
    )
# --------------- column 3 layout end ---------------

def use_script(dm, smoker):
    if dm == 1 and smoker == 0:
        return js_scripts['cvd_risk_diabetic_nonsmoker.js']
    elif dm == 1 and smoker == 1:
        return js_scripts['cvd_risk_diabetic_smoker.js']
    elif dm == 0 and smoker == 0:
        return js_scripts['cvd_risk_nondiabetic_nonsmoker.js']
    elif dm == 0 and smoker == 1:
        return js_scripts['cvd_risk_nondiabetic_smoker.js']
    elif dm == None and smoker == 0:
        return js_scripts['cvd_risk_nulldiabetic_nonsmoker.js']
    elif dm == None and smoker == 1:
        return js_scripts['cvd_risk_nulldiabetic_smoker.js']

@st.dialog("Risk Level:", width="large")
def cvd_risk (is_dm, gender, is_smoker, age, systolic, x):
    use_js_script = use_script(is_dm, is_smoker)
    components.html(
    f"""
        <style>
            .green {{ color: #99cc00; }}
            .yellow {{ color: #ffff00; }}
            .orange {{ color: #ff9933; }}
            .red {{ color: #cc0000; }}
            .darkred {{ color: #990033; }}
        </style>
        <div
            id="result"
            style="
                text-align: center;
                font-size: 50px;
                font-family: sans-serif;
                font-weight: bold;
                text-shadow: -1px -1px 0 #9e9f9b, 1px -1px 0 #9e9f9b, -1px 1px 0 #9e9f9b, 1px 1px 0 #9e9f9b;
            ">
        </div>
        <hr>
        <div
            id="recommendation"
            style="
                font-family: sans-serif;
                padding-top: 10px;
            ">
        </div>
        <script>
            {use_js_script}
            function calculate_risk() {{
                switch({is_dm}) {{
                    case 1:
                        if ({is_smoker} == 1) {{
                            return cvd_risk_diabetic_smoker('{gender}', {age}, {systolic}, {x});
                        }} else if ({is_smoker} == 0) {{
                            return cvd_risk_diabetic_nonsmoker('{gender}', {age}, {systolic}, {x});
                        }}
                        break;
                    case 0:
                        if ({is_smoker} == 1) {{
                            return cvd_risk_nondiabetic_smoker('{gender}', {age}, {systolic}, {x});
                        }} else if ({is_smoker} == 0) {{
                            return cvd_risk_nondiabetic_nonsmoker('{gender}', {age}, {systolic}, {x});
                        }}
                        break;
                    case null:
                        if ({is_smoker} == 1) {{
                            return cvd_risk_nulldiabetic_smoker('{gender}', {age}, {systolic}, {x});
                        }} else if ({is_smoker} == 0) {{
                            return cvd_risk_nulldiabetic_nonsmoker('{gender}', {age}, {systolic}, {x});
                        }}
                        break;
                }}
            }}

            function descriptions(n) {{
                if (n < 5) {{
                    document.getElementById("result").className = "green"
                    return {{
                        "label": "Low Risk",
                        "recommendations": [
                            "<b>Lifestyle Modifications</b>:<blockquote>Encourage patients to maintain a healthy lifestyle to keep their risk low. This includes a balanced diet, regular physical activity, avoiding tobacco use, and moderating alcohol consumption.</blockquote>",
                            "<b>Routine Monitoring</b>:<blockquote>Regular check-ups every 2-5 years to reassess risk and ensure that it remains low.</blockquote>",
                            "<b>Medication</b>:<blockquote>Typically, medication is not required unless other risk factors (e.g., high blood pressure or diabetes) are present</blockquote>."
                        ]
                    }}
                }} else if (n >= 5 && n < 10) {{
                    document.getElementById("result").className = "yellow"
                    return {{
                        "label": "Moderate Risk",
                        "recommendations": [
                            "<b>Lifestyle Modifications</b>:<blockquote>As with low-risk patients, strong emphasis on adopting and maintaining a healthy lifestyle to reduce risk.</blockquote>",
                            "<b>Routine Monitoring</b>:<blockquote>Check-ups every 1-2 years to monitor risk factors.</blockquote>",
                            "<b>Medication</b>:<blockquote>Consider initiating treatment if the patient has additional risk factors (e.g., persistent hypertension or diabetes) or if lifestyle changes do not sufficiently reduce risk.</blockquote>",
                            "<b>Education</b>:<blockquote>Educate the patient on recognizing early signs of CVD and the importance of adherence to lifestyle and treatment plans</blockquote>."

                        ]
                    }}
                }} else if (n >= 10 && n < 20) {{
                    document.getElementById("result").className = "orange"
                    return {{
                        "label": "Moderate to High Risk",
                        "recommendations": [
                            "<b>Intensive Lifestyle Modifications</b>:<blockquote>More aggressive lifestyle changes, including dietary counseling, structured physical activity programs, and smoking cessation support.</blockquote>",
                            "<b>Routine Monitoring</b>:<blockquote>Check-ups at least annually, possibly more frequently if risk factors are poorly controlled.</blockquote>",
                            "<b>Medication</b>:<blockquote>Strong consideration for starting pharmacological treatment (e.g., statins for cholesterol, antihypertensives for blood pressure) in addition to lifestyle interventions. Aspirin may be considered depending on individual patient circumstances.</blockquote>",
                            "<b>Risk Communication</b>:<blockquote>Detailed discussion with the patient about the potential benefits of reducing their risk and the importance of medication adherence</blockquote>."
                        ]
                    }}
                }} else if (n >= 20 && n < 30) {{
                    document.getElementById("result").className = "red"
                    return {{
                        "label": "High Risk",
                        "recommendations": [
                            "Intensive Lifestyle Modifications</b>:<blockquote>As above, with even greater emphasis on the urgency of lifestyle changes.</blockquote>",
                            "Routine Monitoring</b>:<blockquote>Frequent monitoring (e.g., every 3-6 months) to ensure that risk factors are being managed effectively.</blockquote>",
                            "Medication</b>:<blockquote>Pharmacological treatment is typically recommended. This includes statins, antihypertensives, and possibly aspirin, based on individual risk and patient factors.</blockquote>",
                            "Referral</b>:<blockquote>Consider referral to a specialist if risk factors are not well controlled with initial management</blockquote>."
                        ]
                    }}
                }} else if (n >= 30) {{
                    document.getElementById("result").className = "darkred"
                    return {{
                        "label": "Very High Risk",
                        "recommendations": [
                            "<b>Urgent Lifestyle Modifications</b>:<blockquote>Immediate and aggressive lifestyle interventions, possibly involving multidisciplinary care (e.g., dietitians, exercise specialists).</blockquote>",
                            "<b>Routine Monitoring</b>:<blockquote>Very frequent monitoring, at least every 3 months, to closely track and manage risk factors.</blockquote>",
                            "<b>Medication</b>:<blockquote>Comprehensive pharmacological treatment is usually necessary, addressing all modifiable risk factors (e.g., statins, antihypertensives, antiplatelet agents like aspirin).</blockquote>",
                            "<b>Referral</b>:<blockquote>Strong consideration for specialist referral for comprehensive cardiovascular risk management and potential treatment of underlying conditions.</blockquote>",
                            "<b>Patient Education</b>:<blockquote>Emphasize the seriousness of their condition and the need for strict adherence to both lifestyle changes and medication</blockquote>."
                        ]
                    }}
                }}
            }}

            result = calculate_risk()
            description = descriptions(result)
            document.getElementById("result").innerHTML = result + "%<br>" + description['label'];
            fulltext = "";
            for (i = 0; i < description['recommendations'].length; i++) {{
                fulltext += description['recommendations'][i] + "<br>"
            }}
            document.getElementById("recommendation").innerHTML = fulltext;
        </script>
    """, height=500, scrolling=True)

if st.button("Calculate Risk!", type="primary"):
    if is_diabetes != None and gender != None and is_smoker != None:
        if st.session_state.use_bmi:
            cvd_risk(is_diabetes_options[is_diabetes], gender_options[gender], is_smoker_options[is_smoker], age, systolic, bmi)
        else:
            cvd_risk(is_diabetes_options[is_diabetes], gender_options[gender], is_smoker_options[is_smoker], age, systolic, cholesterol)
    else:
        st.warning('Please complete the form first!', icon="⚠️")