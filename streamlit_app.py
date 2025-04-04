import streamlit as st
from st_pages import add_page_title, get_nav_from_toml
# from streamlit_js_eval import get_page_location
import base64
from urllib.parse import unquote

def change_language():
    st.session_state.language = st.session_state.selected_language

if "language" not in st.session_state:
    st.session_state.language = "ID"

st.session_state.selected_language = st.session_state.language

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

st.set_page_config(layout="wide")

language = st.segmented_control(
    "Pilih Bahasa / Select Language:",
    ["ID", "EN"],
    key="selected_language",
    on_change=change_language,
    label_visibility="collapsed"
)

image_base64 = image_to_base64("./main_logo.png")
st.markdown(
    f"""
    <style>
    .align-right {{
        text-align: right;
        float: right;
    }}
    </style>
    <div class="align-right">
        <img src="data:image/jpeg;base64,{image_base64}" width="300" />
    </div>
    """,
    unsafe_allow_html=True
)

pages = {
    "Welcome!": [
        st.Page("./page/home.py", title="Homepage")
    ],
    "Showcase Apps": [
        st.Page("./page/cvd_risk.py", title="Cardiovascular Disease Risk"),
        st.Page("./page/hypertension_risk.py", title="Early Detection Hypertension Risk"),
        st.Page("./page/zscore.py", title="Toddler Z-Score Calculator"),
        st.Page("./page/diabetes_risk.py", title="Early Detection Diabetes Risk"),
        st.Page("./page/stunting_prediction_dashboard.py", title="Stunting Prediction Dashboard"),
        st.Page("./page/dm_risk_prediction_dashboard.py", title="Diabetes Risk Prediction Dashboard"),
        st.Page("./page/bmi_calculator.py", title="BMI Calculator")
    ],
}

# Get navigation menu from toml & show it
# nav = get_nav_from_toml(".streamlit/pages_sections.toml")
pg = st.navigation(pages, position='hidden')

# st.logo("Data Science Team Logo wide project showcase.png")

# Run the app with navigation
pg.run()