import streamlit as st

st.title('**:material/waving_hand: Welcome!**')

main_div = st.container()
col1, col2 = main_div.columns(2)
# col1.write('''Welcome to our Data Science Team's Project Showcase! Here, we highlight our innovative work, where data meets creativity to solve real-world problems. Our projects span various domains, showcasing our expertise in AI machine learning, data visualization, predictive modeling, and more. \nWhether you're here to explore our latest breakthroughs, gain insights into complex data challenges, or find inspiration for your own projects, you'll discover how we turn data into actionable insight. Join us on this journey as we push the boundaries of what's possible with data.''')
col1.markdown(
    '''
    <div style="text-align: justify;">
        Welcome to our Data Science Team's Project Showcase! Here, we highlight our innovative work, where data meets creativity to solve real-world problems. Our projects span various domains, showcasing our expertise in AI, machine learning, data visualization, predictive modeling, and more. <br><br>
        Whether you're here to explore our latest breakthroughs, gain insights into complex data challenges, or find inspiration for your own projects, you'll discover how we turn data into actionable insight. Join us on this journey as we push the boundaries of what's possible with data.
    </div>
    ''', 
    unsafe_allow_html=True
)

col2.image('Data Science Team Logo.png', width=500)
st.markdown('''
    <style>
    button[title="View fullscreen"]{
        visibility: hidden;}
    </style>
''', unsafe_allow_html=True)