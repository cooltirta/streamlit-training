import streamlit as st

st.title('**:material/waving_hand: Welcome!**')

main_div = st.container()
col1, col2 = main_div.columns(2)
col1.write('''Welcome to **PULSE**<br>A "**Platform for Unified Learning, Scientific Analysis, and Models**".<br>PULSE is a platform for our data science team’s models, calculators, and analysis, offering an interactive hub for internal showcase and stakeholder presentations.''', unsafe_allow_html=True)
col2.image('PULSE LOGO big.png', width=250)
st.markdown('''
    <style>
    button[title="View fullscreen"]{
        visibility: hidden;}
    </style>
''', unsafe_allow_html=True)