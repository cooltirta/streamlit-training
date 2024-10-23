import streamlit as st
from model_logic.py_functions import gensimplecomponent, gencomponent
import streamlit.components.v1 as components
import joblib
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

# get password from env
diabetes_password = st.secrets["DIABETES_PASSWORD"]
# diabetes_password = os.getenv("DIABETES_PASSWORD")

# set default values
AGE = 15
SYSTOLIC = 60
FAMILY_HISTORY = None
EXERCISE = None
DIET = None

# set default session var
if "diabetes_password_correct" not in st.session_state:
    st.session_state.diabetes_password_correct = False

if "age" not in st.session_state:
    st.session_state.age = AGE

if "systolic" not in st.session_state:
    st.session_state.systolic = SYSTOLIC

if "family_history" not in st.session_state:
    st.session_state.family_history = FAMILY_HISTORY

if "exercise" not in st.session_state:
    st.session_state.exercise = EXERCISE

if "diet" not in st.session_state:
    st.session_state.diet = DIET

# get model
clf = joblib.load('./model_logic/dm_risk/lightgbm_ASIK_pickle_clean_5f.pkl')

# CSS Library
st.markdown('''
    <style>
        button[title="View fullscreen"] {
            visibility: hidden;
        }
        
        .medium50 {
            font-size: 50px;
            font-weight: 600;
        }
            
        .medium24 {
            font-size: 24px;
            font-weight: 600;
        }

        .regular18 {
            font-size: 18px;
            font-weight: 400;
        }

        .regular16 {
            font-size: 16px;
            font-weight: 400;
        }

        .cekrisikobtn {
            width: 289px;
            height: 55px;
            gap: 0px;
            border-radius: 47px;
            opacity: 0px;
            border: none;
            background: #111B47;
            color: white;
            font-size: 24px;
            font-weight: 600;
            text-align: center;
            margin-left: 100px;
        }

        .formquestion {
            font-size: 32px;
            font-weight: 600;
        }

        .cekhasilbtn {
            width: 233px;
            height: 55px;
            gap: 0px;
            border-radius: 47px;
            opacity: 0px;
            border: none;
            background: #111B47;
            color: white;
            font-size: 24px;
            font-weight: 600;
            text-align: center;
        }

        .skriningulangbtn {
            width: 233px;
            height: 55px;
            gap: 0px;
            border-radius: 47px;
            opacity: 0px;
            border: none;
            background: #A3185B;
            color: white;
            font-size: 24px;
            font-weight: 600;
            text-align: center;
        }

        button[kind="secondary"] {
            width: 233px !important;
            height: 55px !important;
            gap: 0px !important;
            border-radius: 47px !important;
            opacity: 0px !important;
            border: none !important;
            background: #A3185B !important;
            color: white !important;
            font-size: 24px !important;
            font-weight: 600 !important;
            text-align: center !important;
        }
            
        button[kind="primary"] {
            width: 233px !important;
            height: 55px !important;
            gap: 0px !important;
            border-radius: 47px !important;
            opacity: 0px !important;
            border: none !important;
            background: #111B47 !important;
            color: white !important;
            font-size: 24px !important;
            font-weight: 600 !important;
            text-align: center !important;
        }

        .inf {
            font-size: 20px;
            font-weight: 700;
            line-height: 26px;
            text-align: left;
        }
    </style>
''', unsafe_allow_html=True)

# define title
st.title('**:material/glucose: Early Detection Diabetes Risk**')

# define main div
div_main = st.container()

# define columns
col_top1, col_top2, = div_main.columns(2, vertical_alignment="center")

col_top1.markdown('<p class="medium50">Mari ketahui risiko diabetesmu!</p>', unsafe_allow_html=True)
col_top1.markdown('''
    <p class="regular18" style="color:#505F98;">Diabetes merupakan penyakit yang berbahaya bagi tubuhmu.<br>
    Mengetahui risiko diabetes tipe 2 anda hanya memerlukan beberapa menit.</p>\n
    <p class="regular18" style="color:#505F98;">Sebelum mengisi, siapkan alat pengukur tekanan darah juga ya.</p>\n
    <button class="cekrisikobtn" id="cekrisikobtn">Cek Risiko</button>
''', unsafe_allow_html=True)
col_top2.image('Frame_4.png')

# Password Check
if not st.session_state["diabetes_password_correct"]:
    with st.form("login_form_cvd"):
        password = st.text_input("Enter the password to access this feature:", type="password")
        submit_button = st.form_submit_button("Login")
    
    if submit_button:  # Check occurs only if the button is pressed
        if password == diabetes_password:
            st.session_state.diabetes_password_correct = True
            st.rerun()  # Rerun the script to update the state across the app
        else:
            st.error("Incorrect password. Please try again.")
            st.stop()  # Stop execution here if the password is incorrect
else:

    div_main.markdown('<p class="medium50" style="font-weight:700; text-align:center;" id="risiko">Risiko Diabetes</p>', unsafe_allow_html=True)
    div_main.markdown('<p class="regular18" style="font-size:24px; color:#505F98; text-align:center;">Hasil prediksi ini tidak dimaksudkan untuk menggantikan pengukuran sebenarnya di fasilitas kesehatan, namun untuk membantu memberikan peringatan dini mengenai risiko kamu</p>', unsafe_allow_html=True)
    div_main.markdown('<p style="padding-top:100px;">&nbsp;</p>', unsafe_allow_html=True)

# define columns
    col_mid1, col_mid2 = div_main.columns(2, gap="large")

# input form placeholders
    col_mid1.markdown('<p class="formquestion">Berapa umurmu?</p>', unsafe_allow_html=True)
    placeholder_age = col_mid1.empty()
    col_mid1.markdown('<p class="regular16" style="color:#505F98;">Semakin panjang usia, kemungkinan terkena diabetes tipe 2 semakin tinggi</p>', unsafe_allow_html=True)

    col_mid2.markdown('<p class="formquestion">Berapa tekanan sistolmu?</p>', unsafe_allow_html=True)
    placeholder_systolic = col_mid2.empty()
    col_mid2.markdown('<p class="regular16" style="color:#505F98;">Tekanan sistol merupakan angka atas pada pengukuran tekanan darah. Kenaikan sistol meningkatkan potensi risiko diabetes tipe 2</p>', unsafe_allow_html=True)

    col_mid21, col_mid22 = div_main.columns(2, gap="large")

    col_mid21.markdown('<p class="formquestion" style="padding-top:50px;">Apakah kamu memiliki orang tua atau saudara yang menderita diabetes?</p>', unsafe_allow_html=True)
    placeholder_family_history = col_mid21.empty()
    col_mid21.markdown('<p class="regular16" style="color:#505F98;">Memiliki kerabat yang menderita diabetes mempunyai risiko yang tinggi terhadap DM2</p>', unsafe_allow_html=True)

    col_mid22.markdown('<p class="formquestion" style="padding-top:50px;">Apakah kamu sering berolahraga, sekiranya 2 jam dalam seminggu?</p>', unsafe_allow_html=True)
    placeholder_exercise = col_mid22.empty()
    col_mid22.markdown('<p class="regular16" style="color:#505F98;">Memiliki kebiasaan olahraga mengurangi risiko terkena DM2</p>', unsafe_allow_html=True)

    col_mid31, col_mid32, col_mid33 = div_main.columns(3)

    col_mid32.markdown('<p class="formquestion" style="padding-top:50px;">Apakah kamu mengkomsumsi 5 porsi buah sayur tiap harinya?</p>', unsafe_allow_html=True)
    placeholder_diet = col_mid32.empty()
    col_mid32.markdown('<p class="regular16" style="color:#505F98;">Pola makan sehat membantu mencegah diabetes</p>', unsafe_allow_html=True)

    div_main.markdown('<p style="padding-top:100px;">&nbsp;</p>', unsafe_allow_html=True)

# start modal dialog and def calculation
    @st.dialog("Hasil Skrining", width="large")
    def calculate_risk(obj):
        df = pd.DataFrame(obj)

        df = df[[
            'olahraga',
            'konsumsi_sayur_buah',
            'umur',
            'sistol',
            'riwayat_keluarga_dm'
        ]]

        df = df.astype({
            'umur': 'float64',
            'sistol': 'float64',
            'riwayat_keluarga_dm': 'category',
            'konsumsi_sayur_buah': 'category',
            'olahraga': 'category'
        })

        probabilities  = clf.predict_proba(df)[:, 1]  # Assuming your model is trained to predict on similar features

        threshold = 0.037
        prediction = (probabilities >= threshold).astype(int)

        result = "Tinggi" if prediction[0] == 1 else "Rendah"

        df['prediction'] = result

        file_path = './diabetes_predictions.csv'

        if not os.path.isfile(file_path):
            df.to_csv(file_path, index=False)  # Save with header if file does not exist
        else:
            df.to_csv(file_path, mode='a', header=False, index=False)  # Append without hea

        res = '<b style="color:#CF2B2E;">Tinggi</b>' if result == 'Tinggi' else '<b style="color:#57855D;">Rendah</b>'''
        div_modal = st.container()
        div_modal.markdown(f'''
            <p class="medium50" style="text-align:center;">Kamu Beresiko {res}</p>\n
            <p class="regular18" style="color:#505F98; background-color:#D2E0B7; text-align:center;">Hasil skrining bukan hasil pemeriksaan medis. Konsultasikan dengan tenaga profesional untuk informasi lanjutan</p>\n
            <p class="regular18" style="text-align:center; font-weight:500; padding-top:50px;"><b>Mengenal risiko diabetes pada skrining ini:</b></p>
        ''', unsafe_allow_html=True)

        col_mod1, col_mod2 = div_modal.columns(2)
        col_mod1.markdown('''
            <p class="medium24">Risiko yang tidak dapat dirubah</p>
            <p class="regular16" style="color:#505F98;">Risiko ini tidak dapat dihindari, sehingga lebih fokuslah kepada faktor yang bisa berubah</p>
            <ul>
                <li class="inf">Umur</li>
                <li class="inf">Riwayat keluarga</li>
            </ul>
        ''', unsafe_allow_html=True)

        col_mod2.markdown('''
            <p class="medium24">Risiko yang dapat dirubah</p>
            <p class="regular16" style="color:#505F98;">Risiko ini dapat dikurangi atau dirubah dengan cara menjaga lifestyle saudara</p>
            <ul>
                <li class="inf">Tekanan sistol</li>
                <li class="inf">Olahraga</li>
                <li class="inf">Konsumsi sayur-buah</li>
            </ul>
        ''', unsafe_allow_html=True)

# define columns
    col_mid41, col_mid42, col_mid43, col_mid44 = div_main.columns(4)

    if col_mid42.button("**Cek Hasil**", type="primary"):
        calculate_risk(
            {
                "umur": [st.session_state.age],
                "sistol": [st.session_state.systolic],
                "riwayat_keluarga_dm": [st.session_state.family_history],
                "olahraga": [st.session_state.exercise],
                "konsumsi_sayur_buah": [st.session_state.diet]
            }

        )

    if col_mid43.button('**Skrining Ulang**', type='secondary'):
        st.session_state.age = AGE
        st.session_state.systolic = SYSTOLIC
        st.session_state.family_history = FAMILY_HISTORY
        st.session_state.exercise = EXERCISE
        st.session_state.diet = DIET

# define input forms
    age = placeholder_age.number_input(
        "Berapa umurmu?",
        min_value=15,
        max_value=100,
        label_visibility="collapsed",
        key="age"
    )

    systolic = placeholder_systolic.number_input(
        "Berapa tekanan sistolmu?",
        min_value=60,
        max_value=600,
        label_visibility="collapsed",
        key="systolic"
    )

    family_history = placeholder_family_history.radio(
        "Apakah kamu memiliki orang tua atau saudara yang menderita diabetes?",
        ["Ya", "Tidak"],
        index=None,
        label_visibility="collapsed",
        key="family_history"
    )

    exercise = placeholder_exercise.radio(
        "Apakah kamu sering berolahraga, sekiranya 2 jam dalam seminggu?",
        ["Ya", "Tidak"],
        index=None,
        label_visibility="collapsed",
        key="exercise"
    )

    diet = placeholder_diet.radio(
        "Apakah kamu mengkomsumsi 5 porsi buah sayur tiap harinya?",
        ["Ya", "Tidak"],
        index=None,
        label_visibility="collapsed",
        key="diet"
    )

# Javascripts
    js = '''
    <script>
        window.parent.document.querySelector("#cekrisikobtn").
        onclick = function () {
            var goto = window.parent.document.querySelector("#risiko");
            goto.scrollIntoView({ behavior: 'smooth' });
        }
    </script>
    '''
    components.html(js)