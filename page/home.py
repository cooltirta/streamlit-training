import streamlit as st

st.title(' ')

main_div = st.container()
col1, col2, col3 = main_div.columns(3)
col2.image('dash_logo.png')
main_div.markdown(
    '''
    <div style="text-align: justify; font-size:19px;">
        &emsp;&emsp;Welcome to <b>DASH</b>, the project hub of the Data Science Team at DTO, Ministry of Health. Here, we showcase our work in applying data science to address key challenges in public health. From AI and machine learning to data visualization and predictive modeling, our projects are designed to provide real-world solutions with measurable impact.
        <br>
        &emsp;&emsp;Explore our projects through the menu on the left, and see our projects visualized. We’re excited to share our progress with you.
    </div>
    ''', 
    unsafe_allow_html=True
)

col21, col22, col23, col24, col25 = main_div.columns(5)
col23.markdown(
    '''
        <div style="text-align: center; padding-top: 50px;">
            <i>Developed by:</i>
        </div>
    ''',
    unsafe_allow_html=True
)
col23.image('ds_logo_comp_crop.jpeg')
st.markdown('''
    <style>
    button[title="View fullscreen"]{
        visibility: hidden;}
    </style>
''', unsafe_allow_html=True)