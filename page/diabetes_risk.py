import streamlit as st
from model_logic.py_functions import gensimplecomponent, gencomponent
import streamlit.components.v1 as components
import joblib
import pandas as pd
from dotenv import load_dotenv
import os
import requests

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
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&icon_names=warning" rel="stylesheet" />
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
            margin-top: 25px;
            margin-bottom: 15px;
        }

        .formtitle {
            font-size: 40px;
            font-weight: 600;
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
            background: #7FAA2B;
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
            background: #111B47 !important;
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
            background: #7FAA2B !important;
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

        .formbg {
            background: #DADFE9;
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
    <div style="max-width:fit-content; margin-left:auto; margin-right:auto;"><button class="cekrisikobtn" id="cekrisikobtn">Cek Risiko</button></div>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0&icon_names=warning" />
''', unsafe_allow_html=True)
col_top1.markdown('''
    <div style="padding-bottom:10px;">
        <div style="margin-left:auto; margin-right:auto; max-width: fit-content; background:#FFFCE7; padding:10px, 20px, 10px, 20px; color:#926c05; text-align:center;">⚠️ Catatan: Hasil prediksi ini hanya sebagai pemeriksaan dini, bukan diagnosis medis</div>
    </div>
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

    div_main.markdown('<p class="medium50" style="font-weight:700; text-align:center;" id="risiko">Yuk, isi form ini buat cek risiko DM2 kamu!</p>', unsafe_allow_html=True)
    div_main.divider()
    div_main.markdown('<p class="formtitle" style="text-align:center;">Identitas diri</p>', unsafe_allow_html=True)

# define columns    
    col_top21, col_top22, col_top23 = div_main.columns(3, vertical_alignment="center")
    
    col_top21.markdown('<p class="formquestion">Nama Pasien</p>', unsafe_allow_html=True)
    placeholder_name = col_top21.empty()

    col_top22.markdown('<p class="formquestion">NIK</p>', unsafe_allow_html=True)
    placeholder_nik = col_top22.empty()

    col_top23.markdown('<p class="formquestion">Tempat pemeriksaan</p>', unsafe_allow_html=True)
    placeholder_place = col_top23.empty()

    div_main.markdown('<p style="padding-top:20px;">&nbsp;</p>', unsafe_allow_html=True)
    div_main.divider()
    div_main.markdown('<p class="formtitle" style="text-align:center;">Risiko diri</p>', unsafe_allow_html=True)

# define columns
    col_mid1, col_mid2 = div_main.columns(2, gap="large")

# input form placeholders
    col_mid1.markdown('<p class="formquestion">Berapakah usia pasien saat ini?</p>', unsafe_allow_html=True)
    placeholder_age = col_mid1.empty()
    col_mid1.markdown('<p class="regular16" style="color:#505F98;">Semakin bertambah usia, risiko terkena DM2 juga cenderung meningkat.</p>', unsafe_allow_html=True)

    col_mid2.markdown('<p class="formquestion">Berapakah tekanan darah sistolik pasien?</p>', unsafe_allow_html=True)
    placeholder_systolic = col_mid2.empty()
    col_mid2.markdown('<p class="regular16" style="color:#505F98;">Tekanan darah sistolik merupakan angka atas pada pengukuran tekanan darah. Peningkatan tekanan darah sistolik dapat meningkatkan potensi risiko DM2.</p>', unsafe_allow_html=True)

    col_mid21, col_mid22 = div_main.columns(2, gap="large")

    col_mid21.markdown('<p class="formquestion" style="padding-top:50px;">Apakah pasien memiliki orang tua atau saudara yang menderita diabetes?</p>', unsafe_allow_html=True)
    placeholder_family_history = col_mid21.empty()
    col_mid21.markdown('<p class="regular16" style="color:#505F98;">Riwayat keluarga dengan diabetes dapat meningkatkan risiko Anda terkena DM2. Mengetahui faktor ini bisa membantu Anda lebih waspada dan mengambil langkah pencegahan yang tepat sejak dini.</p>', unsafe_allow_html=True)

    col_mid22.markdown('<p class="formquestion" style="padding-top:50px;">Apakah pasien rutin berolahraga, setidaknya 2 jam dalam seminggu?</p>', unsafe_allow_html=True)
    placeholder_exercise = col_mid22.empty()
    col_mid22.markdown('<p class="regular16" style="color:#505F98;">Memiliki kebiasaan berolahraga secara teratur dapat berpengaruh terhadap penurunan risiko terkena DM2.</p>', unsafe_allow_html=True)

    col_mid31, col_mid32, col_mid33 = div_main.columns(3)

    col_mid32.markdown('<p class="formquestion" style="padding-top:50px;">Apakah pasien mengkomsumsi 5 porsi buah sayur tiap harinya?</p>', unsafe_allow_html=True)
    placeholder_diet = col_mid32.empty()
    col_mid32.markdown('<p class="regular16" style="color:#505F98;">Pola makan yang sehat, termasuk rutin mengonsumsi buah dan sayur, dapat membantu mengurangi risiko terkena diabetes.</p>', unsafe_allow_html=True)

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

        probabilities  = clf.predict_proba(df)[:, 1]

        threshold = 0.037
        prediction = (probabilities >= threshold).astype(int)

        result = "Tinggi" if prediction[0] == 1 else "Rendah"

        df['prediction'] = result

        url = f'''https://docs.google.com/forms/d/e/1FAIpQLSfWP-9GW9NSUL2gvae4c0xDZ1dxTfeh5k7t8QIWXy6POBUqHw/formResponse?usp=pp_url&entry.1911041054={obj['olahraga'][0]}&entry.104049788={obj['konsumsi_sayur_buah'][0]}&entry.185650305={obj['umur'][0]}&entry.1560480851={obj['sistol'][0]}&entry.761892027={obj['riwayat_keluarga_dm'][0]}&entry.1623306659={result}'''
        response = requests.get(url)

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
    col_mid41, col_mid42, col_mid43, col_mid44 = div_main.columns(4, vertical_alignment="center")

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
    name = placeholder_name.text_input(
        "Nama kamu siapa?",
        placeholder="Nama Lengkap",
        label_visibility="collapsed",
        key="name"
    )

    nik = placeholder_nik.text_input(
        "NIK kamu?",
        placeholder="0123456789012345",
        label_visibility="collapsed",
        key="nik"
    )

    place = placeholder_place.text_input(
        "Dimana kamu diperiksa?",
        placeholder="Lokasi Periksa",
        label_visibility="collapsed",
        key="place"
    )

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