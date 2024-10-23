import streamlit as st

st.title(' ')

main_div = st.container()
col1, col2, col3 = main_div.columns(3)
col2.image('dash_logo.png')
main_div.markdown(
    '''
    <div style="text-align: justify;">
        Welcome to the DASH!! of the Data Science Team at DTO Ministry of Health <br><br> 
        Here, we highlight our innovative work, where data meets creativity to solve real-world problems and creating beneficial impact to the society. Our projects span various domains, showcasing our expertise in AI, machine learning, data visualization, predictive modeling, and more. <br><br>
        Whether you're here to explore our latest breakthroughs, gain insights into complex data challenges, or find inspiration for your own projects, you'll discover how we turn data into actionable insight. <br><br>
        Kindly navigate the <u>left menu</u> to discover our projects. <br><br> 
        Join us on this journey as we push the boundaries of what's possible with data.
    </div>
    ''', 
    unsafe_allow_html=True
)

col21, col22, col23, col24, col25 = main_div.columns(5)
col23.markdown(
    '''
        <div style="text-align: center; padding-top: 50px;">
            <b><i>Developed by:</i></b>
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