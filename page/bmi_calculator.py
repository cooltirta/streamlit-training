import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

LANGUAGE_PACK = {
    'title': {
        'ID': 'Kalkulator IMT (Indeks Massa Tubuh)',
        'EN': 'BMI (Body Mass Index) Calculator'
    },
    'underweight': {
        'ID': 'Berat badan kurang',
        'EN': 'Underweight'
    },
    'normalweight': {
        'ID': 'Berat badan normal',
        'EN': 'Normal weight'
    },
    'overweight': {
        'ID': 'Berat badan lebih',
        'EN': 'Overweight'
    },
    'obese': {
        'ID': 'Obesitas',
        'EN': 'Obese'
    },
    'linelabel': {
        'ID': 'IMT anda',
        'EN': 'Your BMI'
    },
    'bmivalues': {
        'ID': 'Nilai IMT',
        'EN': 'BMI Values'
    },
    'bmiscale': {
        'ID': 'Skala IMT',
        'EN': 'BMI Scale'
    },
    'weightlabel': {
        'ID': 'Masukkan berat badan anda (kg)',
        'EN': 'Enter your weight (kg)'
    },
    'heightlabel': {
        'ID': 'Masukkan tinggi badan anda (cm)',
        'EN': 'Enter your height (cm)'
    },
    'button': {
        'ID': 'Hitung IMT',
        'EN': 'Calculate BMI'
    },
    'res1': {
        'ID': 'IMT anda adalah',
        'EN': 'Your BMI is'
    },
    'res2': {
        'ID': 'Kategori',
        'EN': 'Category'
    },
    'heightwarning': {
        'ID': 'Tinggi badan harus lebih dari nol!',
        'EN': 'Height must be greater than zero!'
    }
}

st.title(LANGUAGE_PACK["title"][st.session_state.language])

div_main = st.container()
col1, col2 = div_main.columns(2, vertical_alignment="center")

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = LANGUAGE_PACK["underweight"][st.session_state.language]
    elif 18.5 <= bmi < 24.9:
        category = LANGUAGE_PACK["normalweight"][st.session_state.language]
    elif 25 <= bmi < 29.9:
        category = LANGUAGE_PACK["overweight"][st.session_state.language]
    else:
        category = LANGUAGE_PACK["obese"][st.session_state.language]
    return bmi, category

def plot_bmi_chart(bmi):
    categories = [
        LANGUAGE_PACK["underweight"][st.session_state.language],
        LANGUAGE_PACK["normalweight"][st.session_state.language],
        LANGUAGE_PACK["overweight"][st.session_state.language],
        LANGUAGE_PACK["obese"][st.session_state.language]
    ]
    values = [18.5, 6.4, 5, 5.1]  # Stacked values for better representation
    colors = ["blue", "green", "orange", "red"]
    
    fig, ax = plt.subplots(figsize=(8, 0.5))  # Reduce height
    left = 0
    for category, value, color in zip(categories, values, colors):
        ax.barh(LANGUAGE_PACK["bmiscale"][st.session_state.language], value, left=left, color=color, label=category, alpha=0.6)
        left += value
    
    # Mark user's BMI
    ax.axvline(x=bmi, color='black', linestyle='--', linewidth=2, label=f'''{LANGUAGE_PACK["linelabel"][st.session_state.language]}: {bmi:.2f}''')
    
    # Adjust legend position to the right
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)
    
    plt.xlabel(LANGUAGE_PACK["bmivalues"][st.session_state.language], fontsize=8)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    
    col2.pyplot(fig)

weight = col1.number_input(LANGUAGE_PACK["weightlabel"][st.session_state.language], min_value=1.0, step=0.1)
height = col1.number_input(LANGUAGE_PACK["heightlabel"][st.session_state.language], min_value=10.0, step=0.1) / 100

if col1.button(LANGUAGE_PACK["button"][st.session_state.language]):
    if height > 0:
        bmi, category = calculate_bmi(weight, height)
        col1.success(f'''{LANGUAGE_PACK["res1"][st.session_state.language]} {bmi:.2f}. {LANGUAGE_PACK["res2"][st.session_state.language]}: {category}''')
        plot_bmi_chart(bmi)
    else:
        col1.error(LANGUAGE_PACK["heightwarning"][st.session_state.language])