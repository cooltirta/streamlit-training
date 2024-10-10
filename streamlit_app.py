import streamlit as st
from st_pages import add_page_title, get_nav_from_toml
import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

st.set_page_config(layout="wide")
image_base64 = image_to_base64("./main_logo.png")
st.markdown(
    f"""
    <style>
    .align-right {{
        text-align: right;
    }}
    </style>
    <div class="align-right">
        <img src="data:image/jpeg;base64,{image_base64}" width="300" />
    </div>
    """,
    unsafe_allow_html=True
)

# Get navigation menu from toml & show it
nav = get_nav_from_toml(".streamlit/pages_sections.toml")
pg = st.navigation(nav)

st.logo("Data Science Team Logo wide project showcase.png")

# Run the app with navigation
pg.run()