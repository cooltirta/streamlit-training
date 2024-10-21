import streamlit as st
# from dotenv import load_dotenv
# import os

# load_dotenv()


# hypertension_password = st.secrets["HYPERTENSION_PASSWORD"]
# hypertension_password = os.getenv("HYPERTENSION_PASSWORD")

# Initialize the session state for password verification
# if "hypertension_password_correct" not in st.session_state:
#     st.session_state.hypertension_password_correct = False

# Password Check
# if not st.session_state["hypertension_password_correct"]:
#     with st.form("login_form_hypertension"):
#         password = st.text_input("Enter the password to access this page:", type="password")
#         submit_button = st.form_submit_button("Login")
    
#     if submit_button:  # Check occurs only if the button is pressed
#         if password == hypertension_password:
#             st.session_state.hypertension_password_correct = True
#             st.rerun()  # Rerun the script to update the state across the app
#         else:
#             st.error("Incorrect password. Please try again.")
#             st.stop()  # Stop execution here if the password is incorrect
# else:

st.title('**:material/cardiology: Early Detection Hypertension Risk**')

st.markdown('''<a href="https://hypertension-ai-platform-dev.dto.kemkes.go.id/" >Open in new tab <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20,300,0,0" /><span class="material-symbols-outlined">open_in_new</span>''', unsafe_allow_html=True)
st.markdown('''<iframe src="https://hypertension-ai-platform-dev.dto.kemkes.go.id/" title="description" style="height:550px; width:100%; border:solid; border-width: thin;" ></iframe>''', unsafe_allow_html=True)