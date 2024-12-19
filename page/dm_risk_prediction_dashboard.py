import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

# get password from env
dm_password = st.secrets["DM_PASSWORD"]
# dm_password = os.getenv("DM_PASSWORD")

if "dm_password_correct" not in st.session_state:
    st.session_state.dm_password_correct = False

# Password Check
if not st.session_state["dm_password_correct"]:
    with st.form("login_form_cvd"):
        password = st.text_input("Enter the password to access this feature:", type="password")
        submit_button = st.form_submit_button("Login")
    
    if submit_button:  # Check occurs only if the button is pressed
        if password == dm_password:
            st.session_state.dm_password_correct = True
            st.rerun()  # Rerun the script to update the state across the app
        else:
            st.error("Incorrect password. Please try again.")
            st.stop()  # Stop execution here if the password is incorrect
else:
    st.title('**:material/space_dashboard: Diabetes Risk Prediction Dashboard**')
    main_div = st.container()
    main_div.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Introducing the Type 2 Diabetes Risk Prediction Dashboard, an annual tool for assessing diabetes risk levels across Indonesia. This dashboard categorizes individuals into low- and high-risk groups and provides a provincial map showing the distribution of predicted high-risk cases. Additionally, a lifestyle profiling table allows for a detailed comparison between high-risk and low-risk populations, supporting targeted lifestyle interventions and public health strategies.")
    st.markdown('''<a href="https://lookerstudio.google.com/reporting/0974db57-7691-4674-8914-14ead70c07d9" >Open in new tab <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20,300,0,0" /><span class="material-symbols-outlined">open_in_new</span>''', unsafe_allow_html=True)
    st.markdown('''<iframe src="https://lookerstudio.google.com/embed/reporting/0974db57-7691-4674-8914-14ead70c07d9/page/r0UIE" title="description" style="height:550px; width:100%; border:solid; border-width: thin;" ></iframe>''', unsafe_allow_html=True)