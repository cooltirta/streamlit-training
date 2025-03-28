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
NAME = None
NIK = None
PLACE = None
AGE = None
SYSTOLIC = None
FAMILY_HISTORY = None
EXERCISE = None
DIET = None
# GDS = 40

LANGUAGE_PACK = {
    'title': {
        'ID': 'Ketahui Risiko Diabetes Kamu',
        'EN': 'Know Your Diabetes Risk'
    },
    'subtitle1': {
        'ID': 'Pengukuran risiko ini disertai deskripsi untuk memudahkan masyarakat menjawab setiap pertanyaan faktor risiko diabetes melitus (DM) tipe 2. Mohon mengisi dengan benar karena akan mempengaruhi hasil pengukuran.',
        'EN': 'This risk assessment includes descriptions to help the public answer each question related to type 2 diabetes mellitus (DM) risk factors. Please provide accurate responses, as they will affect the assessment results.'
    },
    'subtitle2': {
        'ID': 'Informasi lebih lanjut pengenai DM tipe 2 dapat dilihat melalui <a href="www.p2ptm.kemkes.go.id/informasi-p2ptm/penyakit-diabetes-melitus">www.p2ptm.kemkes.go.id/informasi-p2ptm/penyakit-diabetes-melitus</a>',
        'EN': 'Further information about type 2 diabetes mellitus (DM) can be accessed through (in Bahasa Indonesia): <a href="www.p2ptm.kemkes.go.id/informasi-p2ptm/penyakit-diabetes-melitus">www.p2ptm.kemkes.go.id/informasi-p2ptm/penyakit-diabetes-melitus</a>'
    },
    'formbtn': {
        'ID': 'Isi Formulir',
        'EN': 'Fill Out the Form'
    },
    'formheader': {
        'ID': 'Isi formulir ini dengan data diri pasien',
        'EN': 'Fill out this form with the patient\'s personal information'
    },
    'formbtn': {
        'ID': 'Isi Formulir',
        'EN': 'Fill Out the Form'
    },
    'form1header': {
        'ID': 'Identitas Pasien',
        'EN': 'Patient Identity'
    },
    'form1name': {
        'ID': 'Nama Pasien',
        'EN': 'Patient Name'
    },
    'form1nik': {
        'ID': 'NIK Pasien',
        'EN': 'Patient ID'
    },
    'form1location': {
        'ID': 'Fasilitas Kesehatan Tingkat Pertama (FKTP) JKN',
        'EN': '</br>Primary Healthcare Facility'
    },
    'form2header': {
        'ID': 'Risiko diri',
        'EN': 'Personal Risk'
    },
    'form2age': {
        'ID': 'Berapakah usia pasien saat ini?',
        'EN': 'What is the patient\'s current age?'
    },
    'form2agedesc': {
        'ID': 'Resiko mengalami DM tipe 2 cenderung meningkat seiring bertambah usia.',
        'EN': 'The risk of developing type 2 diabetes mellitus (DM) tends to increase with age.'
    },
    'form2systolic': {
        'ID': 'Berapa tekanan darah sistolik pasien?',
        'EN': 'What is the patient\'s systolic blood pressure?'
    },
    'form2systolicdesc': {
        'ID': 'Tekanan darah sistolik merupakan angka atas pada pengukuran tekanan darah. Peningkatan tekanan darah sistolik dapat meningkatkan risiko mengalami DM tipe 2. Jika Anda telah terdiagnosa hipertensi sebelumnya, harap masukan hasil tekanan darah tertinggi dari pemeriksaan sebelumnya.',
        'EN': 'Systolic blood pressure is the upper number in a blood pressure measurement. An increase in systolic blood pressure can raise the risk of developing type 2 diabetes. If you have been previously diagnosed with hypertension, please enter the highest recorded blood pressure from your past examinations.'
    },
    'form2family': {
        'ID': 'Apakah pasien memiliki orang tua atau saudara kandung yang menderita diabetes?',
        'EN': 'Does the patient have a parent or sibling with diabetes?'
    },
    'form2familydesc': {
        'ID': 'Adanya riwayat keluarga (ayah, ibu, saudara kandung) mengalami DM tipe 2 dapat meningkatkan risiko. Mengetahui faktor risiko ini dapat membantu Anda lebih waspada serta mengambil langkah pencegahan yang tepat sejak dini.',
        'EN': 'A family history of type 2 diabetes (father, mother, or siblings) can increase the risk. Recognizing this risk factor can help you stay vigilant and take appropriate preventive measures early.'
    },
    'form2activity': {
        'ID': 'Apakah pasien rutin berolahraga, setidaknya 150 menit dalam seminggu?',
        'EN': 'Does the patient exercise regularly for at least 150 minutes per week?'
    },
    'form2activitydesc1': {
        'ID': 'Memiliki kebiasaan berolahraga secara teratur dapat berpengaruh terhadap penurunan risiko mengalami DM tipe 2. Olahraga yang teratur berupa melakukan aktivitas fisik selama 150 menit dalam 1 minggu setara dengan salah satu kegiatan berikut:',
        'EN': 'Maintaining a regular exercise habit can help reduce the risk of developing type 2 diabetes. Regular physical activity consists of 150 minutes per week, which is equivalent to one of the following activities:'
    },
    'form2activitydesc2a': {
        'ID': 'Jalan kaki selama 30 menit, sebanyak 5x seminggu;',
        'EN': 'Walking for 30 minutes, 5 times a week;'
    },
    'form2activitydesc2b': {
        'ID': 'Bersepeda selama 50 menit, sebanyak 3x seminggu;',
        'EN': 'Cycling for 50 minutes, 3 times a week;'
    },
    'form2activitydesc2c': {
        'ID': 'Yoga selama 45 menit, sebanyak 3x seminggu;',
        'EN': 'Yoga for 45 minutes, 3 times a week;'
    },
    'form2activitydesc2d': {
        'ID': 'Senam aerobik/Zumba selama 30-40 menit, sebanyak 4-5x seminggu; atau',
        'EN': 'Aerobic exercise/Zumba for 30-40 minutes, 4-5 times a week; or'
    },
    'form2activitydesc2e': {
        'ID': 'Berenang santai selama 30 menit, sebanyak 5x seminggu.',
        'EN': 'Leisure swimming for 30 minutes, 5 times a week.'
    },
    'form2diet': {
        'ID': 'Apakah pasien mengonsumsi 5 porsi buah atau sayur tiap harinya?',
        'EN': 'Does the patient consume 5 servings of fruits or vegetables daily?'
    },
    'form2dietdesc1': {
        'ID': 'Pola makan yang sehat, termasuk rutin mengkonsumsi buah dan sayur, sebanyak 5 porsi per hari dapat membantu mengurangi risiko terkena DM tipe 2. Satu porsi buah terdiri atas:',
        'EN': 'A healthy diet, including consuming five servings of fruits and vegetables per day, can help reduce the risk of developing type 2 diabetes. One serving of fruit consists of:'
    },
    'form2dietdesc2a': {
        'ID': '1 buah apel / pisang / jambu / jeruk;',
        'EN': '1 apple / banana / guava / orange;'
    },
    'form2dietdesc2b': {
        'ID': '½ buah alpukat / pir;',
        'EN': '½ avocado / pear;'
    },
    'form2dietdesc2c': {
        'ID': '¾ buah mangga;',
        'EN': '¾ mango;'
    },
    'form2dietdesc2d': {
        'ID': '3 buah kurma;',
        'EN': '3 dates;'
    },
    'form2dietdesc2e': {
        'ID': '4 buah stroberi atau buah beri lainnya;',
        'EN': '4 strawberries or other berries;'
    },
    'form2dietdesc3a': {
        'ID': '*Buah yang baik dikonsumsi untuk kesehatan: apel, jeruk, pir, stroberi, pepaya',
        'EN': '*Fruits that are good for health: apples, oranges, pears, strawberries, papayas.'
    },
    'form2dietdesc3b': {
        'ID': '*Buah dengan kadar gula yang tinggi dan patut dibatasi: mangga, nanas, semangka, kurma, buah beri',
        'EN': '*Fruits with high sugar content that should be limited: mangoes, pineapples, watermelons, dates, berries.'
    },
    'form2dietdesc3c': {
        'ID': '*Perhatikan: hindari buah kering, jus buah yang sudah diolah',
        'EN': '*Note: Avoid dried fruits and processed fruit juices.'
    },
    'submitbtn': {
        'ID': 'Submit Hasil',
        'EN': 'Submit Results'
    },
    'ya': {
        'ID': 'Ya',
        'EN': 'Yes'
    },
    'tidak': {
        'ID': 'Tidak',
        'EN': 'No'
    },
    'formincomplete': {
        'ID': 'Formulir belum lengkap:',
        'EN': 'Form incomplete:'
    },
    'formincompletenik': {
        'ID': 'NIK harus angka dan 16 karakter.',
        'EN': 'NIK must be a 16-digit numeric value.'
    },
    'errorlist': {
        'ID': [
            'Nama',
            'NIK',
            'Tempat Pemeriksaan',
            'Usia',
            'Tekanan Darah Sistolik',
            'Riwayat Keluarga',
            'Olahraga',
            'Konsumsi'
        ],
        'EN': [
            'Name',
            'NIK',
            'Examination Location',
            'Age',
            'Systolic Blood Pressure',
            'Family History',
            'Exercise',
            'Consumption'
        ]
    },
    'resultheader': {
        'ID': 'Hasil Skrining',
        'EN': 'Screening Results'
    },
    'resultinfo': {
        'ID': 'Informasi di bawah berisi saran dan informasi bagi masyarakat sesuai jawaban atas faktor risiko yang dimiliki.',
        'EN': 'The information below provides recommendations and guidance based on the individual\'s responses to identified risk factors.'
    },
    'result1': {
        'ID': 'Hasil skrining menunjukkan bahwa Anda memiliki',
        'EN': 'The screening results indicate that you have a'
    },
    'resulthigh': {
        'ID': 'Risiko Tinggi',
        'EN': 'High Risk'
    },
    'resultlow': {
        'ID': 'Risiko Rendah',
        'EN': 'Low Risk'
    },
    'resulthighdesc': {
        'ID': 'Kami menyarankan Anda untuk berkonsultasi dengan dokter atau tenaga medis profesional di Puskesmas, Klinik, atau fasilitas kesehatan terdekat untuk pemeriksaan lebih lanjut. Anda mungkin perlu menjalani tes tambahan berupa pemeriksaan Gula Darah Puasa, Gula Darah 2 jam setelah makan, atau HbA1c serta berdiskusi mengenai faktor risiko DM tipe 2.',
        'EN': 'We recommend that you consult a doctor or a healthcare professional at the nearest health center, clinic, or medical facility for further examination. You may need additional tests such as Fasting Blood Glucose, Postprandial Blood Glucose (2 hours after eating), or HbA1c, and discuss your risk factors for type 2 diabetes.'
    },
    'resultlowdesc1': {
        'ID': 'Teruskan menjaga gaya hidup sehat dengan cara berikut:',
        'EN': 'Continue maintaining a healthy lifestyle by following these steps:'
    },
    'resultlowdesca': {
        'ID': 'Menjaga berat badan ideal (<a href="./bmi_calculator" target="_blank">ukur disini</a>)',
        'EN': 'Maintain an ideal body weight (<a href="./bmi_calculator" target="_blank">measure here</a>)'
    },
    'resultlowdescb': {
        'ID': 'Melakukan aktivitas fisik selama 30 menit per hari, 5 kali seminggu secara teratur',
        'EN': 'Engage in physical activity for 30 minutes per day, at least 5 times a week'
    },
    'resultlowdescc': {
        'ID': 'Menjaga pola makan yang sehat, yaitu rendah gula, garam dan lemak jenuh, disertai dengan 3-5 porsi buah dan sayuran sehari',
        'EN': 'Maintain a healthy diet that is low in sugar, salt, and saturated fats, accompanied by 3-5 servings of fruits and vegetables daily'
    },
    'resultlowdescd': {
        'ID': 'Konsumsi air putih minimal 8 gelas sehari',
        'EN': 'Drink at least 8 glasses of water per day'
    },
    'resultlowdesce': {
        'ID': 'Hindari penggunaan tembakau (merokok, tembakau kunyah) dan alkohol',
        'EN': 'Avoid tobacco use (smoking, chewing tobacco) and alcohol'
    },
    'resultlowdescf': {
        'ID': 'Mengelola stres dan istirahat cukup',
        'EN': 'Manage stress and ensure adequate rest'
    },
    'resultlowdesc2': {
        'ID': 'Kami juga menyarankan Anda untuk dapat berkonsultasi secara langsung dengan dokter atau tenaga medis profesional untuk berdiskusi mengenai faktor risiko DM tipe 2.',
        'EN': 'We also recommend that you consult directly with a doctor or healthcare professional to discuss your risk factors for type 2 diabetes.'
    },
    'locationoption': {
        'ID': 'Tidak Tahu',
        'EN': 'Unknown'
    },
    'nameplaceholder': {
        'ID': 'Nama Lengkap',
        'EN': 'Full Name'
    },
    'locationplaceholder': {
        'ID': 'Lokasi Periksa',
        'EN': 'Examination Location'
    },
}

mapping_y_t = {"Ya": LANGUAGE_PACK["ya"][st.session_state.language], "Tidak": LANGUAGE_PACK["tidak"][st.session_state.language]}

# set default session var
if "diabetes_password_correct" not in st.session_state:
    st.session_state.diabetes_password_correct = False

if "name" not in st.session_state:
    st.session_state.name = NAME

if "nik" not in st.session_state:
    st.session_state.nik = NIK

if "place" not in st.session_state:
    st.session_state.place = PLACE

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

# if "gds" not in st.session_state:
#     st.session_state.gds = GDS

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
            font-size: 50px !important;
            font-weight: 600;
        }
            
        .medium24 {
            font-size: 24px !important;
            font-weight: 600;
        }

        .regular18 {
            font-size: 18px !important;
            font-weight: 400;
        }

        .regular16 {
            font-size: 16px !important;
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
            font-size: 24px !important;
            font-weight: 600;
            text-align: center;
            margin-top: 25px;
            margin-bottom: 15px;
        }

        .formtitle {
            font-size: 40px !important;
            font-weight: 600;
        }

        .formquestion {
            font-size: 32px !important;
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
            font-size: 24px !important;
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
            font-size: 24px !important;
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
            font-size: 20px !important;
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
# st.title('**:material/glucose: Early Detection Diabetes Risk**')

# define main div
div_main = st.container()

# define columns
col_top1, col_top2, = div_main.columns(2, vertical_alignment="center")

col_top1.markdown(f'''<p class="medium50">{LANGUAGE_PACK["title"][st.session_state.language]}</p>''', unsafe_allow_html=True)
col_top1.markdown(f'''
    <p class="regular18" style="color:#505F98;">{LANGUAGE_PACK["subtitle1"][st.session_state.language]}</p>\n
    <p class="regular18" style="color:#505F98;">{LANGUAGE_PACK["subtitle2"][st.session_state.language]}</p>\n
    <div style="max-width:fit-content; margin-left:auto; margin-right:auto;"><button class="cekrisikobtn" id="cekrisikobtn">{LANGUAGE_PACK["formbtn"][st.session_state.language]}</button></div>
''', unsafe_allow_html=True)
# col_top1.markdown('''
#     <div style="padding-bottom:10px;">
#         <div style="margin-left:auto; margin-right:auto; max-width: fit-content; background:#FFFCE7; padding:10px, 20px, 10px, 20px; color:#926c05; text-align:center;">⚠️ Catatan: Hasil prediksi ini hanya sebagai pemeriksaan dini, bukan diagnosis medis</div>
#     </div>
# ''', unsafe_allow_html=True)
col_top2.image('Frame_4.png')

# Password Check
# if not st.session_state["diabetes_password_correct"]:
#     with st.form("login_form_cvd"):
#         password = st.text_input("Enter the password to access this feature:", type="password")
#         submit_button = st.form_submit_button("Login")
    
#     if submit_button:  # Check occurs only if the button is pressed
#         if password == diabetes_password:
#             st.session_state.diabetes_password_correct = True
#             st.rerun()  # Rerun the script to update the state across the app
#         else:
#             st.error("Incorrect password. Please try again.")
#             st.stop()  # Stop execution here if the password is incorrect
# else:

div_main.markdown(f'''<p class="medium50" style="font-weight:700; text-align:center;" id="risiko">{LANGUAGE_PACK["formheader"][st.session_state.language]}</p>''', unsafe_allow_html=True)
div_main.divider()
div_main.markdown(f'''<p class="formtitle" style="text-align:center;">{LANGUAGE_PACK["form1header"][st.session_state.language]}</p>''', unsafe_allow_html=True)

# define columns    
col_top21, col_top22, col_top23 = div_main.columns(3, vertical_alignment="center")

col_top21.markdown(f'''<p class="formquestion"></br>{LANGUAGE_PACK["form1name"][st.session_state.language]}</p>''', unsafe_allow_html=True)
placeholder_name = col_top21.empty()

col_top22.markdown(f'''<p class="formquestion"></br>{LANGUAGE_PACK["form1nik"][st.session_state.language]}</p>''', unsafe_allow_html=True)
placeholder_nik = col_top22.empty()

col_top23.markdown(f'''<p class="formquestion">{LANGUAGE_PACK["form1location"][st.session_state.language]}</p>''', unsafe_allow_html=True)
placeholder_place = col_top23.empty()

div_main.markdown('<p style="padding-top:20px;">&nbsp;</p>', unsafe_allow_html=True)
div_main.divider()
div_main.markdown(f'''<p class="formtitle" style="text-align:center;">{LANGUAGE_PACK["form2header"][st.session_state.language]}</p>''', unsafe_allow_html=True)

# define columns
col_mid1, col_mid2 = div_main.columns(2, gap="large")

# input form placeholders
col_mid1.markdown(f'''<p class="formquestion">{LANGUAGE_PACK["form2age"][st.session_state.language]}</p>''', unsafe_allow_html=True)
placeholder_age = col_mid1.empty()
col_mid1.markdown(f'''<p class="regular16" style="color:#505F98;">{LANGUAGE_PACK["form2agedesc"][st.session_state.language]}</p>''', unsafe_allow_html=True)

col_mid2.markdown(f'''<p class="formquestion">{LANGUAGE_PACK["form2systolic"][st.session_state.language]}</p>''', unsafe_allow_html=True)
placeholder_systolic = col_mid2.empty()
col_mid2.markdown(f'''<p class="regular16" style="color:#505F98;">{LANGUAGE_PACK["form2systolicdesc"][st.session_state.language]}</p>''', unsafe_allow_html=True)

col_mid21, col_mid22 = div_main.columns(2, gap="large")

col_mid21.markdown(f'''<p class="formquestion" style="padding-top:50px;">{LANGUAGE_PACK["form2family"][st.session_state.language]}</p>''', unsafe_allow_html=True)
placeholder_family_history = col_mid21.empty()
col_mid21.markdown(f'''<p class="regular16" style="color:#505F98;">{LANGUAGE_PACK["form2familydesc"][st.session_state.language]}</p>''', unsafe_allow_html=True)

col_mid22.markdown(f'''<p class="formquestion" style="padding-top:50px;">{LANGUAGE_PACK["form2activity"][st.session_state.language]}</p>''', unsafe_allow_html=True)
placeholder_exercise = col_mid22.empty()
col_mid22.markdown(f'''<p class="regular16" style="color:#505F98;">{LANGUAGE_PACK["form2activitydesc1"][st.session_state.language]}</p><ul><li class="regular16" style="color:#505F98;">{LANGUAGE_PACK["form2activitydesc2a"][st.session_state.language]}</li><li class="regular16" style="color:#505F98;">{LANGUAGE_PACK["form2activitydesc2b"][st.session_state.language]}</li><li class="regular16" style="color:#505F98;">{LANGUAGE_PACK["form2activitydesc2c"][st.session_state.language]}</li><li class="regular16" style="color:#505F98;">{LANGUAGE_PACK["form2activitydesc2d"][st.session_state.language]}</li><li class="regular16" style="color:#505F98;">{LANGUAGE_PACK["form2activitydesc2e"][st.session_state.language]}</li></ul>''', unsafe_allow_html=True)

col_mid31, col_mid32 = div_main.columns(2, gap="large")

col_mid31.markdown(f'''<p class="formquestion" style="padding-top:50px;">{LANGUAGE_PACK["form2diet"][st.session_state.language]}</p>''', unsafe_allow_html=True)
placeholder_diet = col_mid31.empty()
col_mid31.markdown(f'''<p class="regular16" style="color:#505F98;">{LANGUAGE_PACK["form2dietdesc1"][st.session_state.language]}</p><ul><li class="regular16" style="color:#505F98;">{LANGUAGE_PACK["form2dietdesc2a"][st.session_state.language]}</li><li class="regular16" style="color:#505F98;">{LANGUAGE_PACK["form2dietdesc2b"][st.session_state.language]}</li><li class="regular16" style="color:#505F98;">{LANGUAGE_PACK["form2dietdesc2c"][st.session_state.language]}</li><li class="regular16" style="color:#505F98;">{LANGUAGE_PACK["form2dietdesc2d"][st.session_state.language]}</li><li class="regular16" style="color:#505F98;">{LANGUAGE_PACK["form2dietdesc2e"][st.session_state.language]}</li></ul><p class="regular16" style="color:#505F98;">{LANGUAGE_PACK["form2dietdesc3a"][st.session_state.language]}<br>{LANGUAGE_PACK["form2dietdesc3b"][st.session_state.language]}<br>{LANGUAGE_PACK["form2dietdesc3c"][st.session_state.language]}</p>''', unsafe_allow_html=True)

div_main.markdown(f'''<p style="padding-top:100px;">&nbsp;</p>''', unsafe_allow_html=True)

# start modal dialog and def calculation
@st.dialog(LANGUAGE_PACK["resultheader"][st.session_state.language], width="large")
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

    sensitivity_80 = 0.037
    ppv_80 = 0.66
    
    predict_sensitivity = (probabilities >= sensitivity_80).astype(int)
    predict_ppv = (probabilities >= ppv_80).astype(int)

    result_sensitivity = "Tinggi" if predict_sensitivity[0] == 1 else "Rendah"
    result_ppv = "Tinggi" if predict_ppv[0] == 1 else "Rendah"

    res_lang = "High Risk" if st.session_state.language == "EN" else "Low"

    df['pred_risk_category_snsv_80'] = result_sensitivity
    df['pred_risk_category_ppv_80'] = result_ppv

    # Real URL
    url = f'''https://docs.google.com/forms/d/e/1FAIpQLSfWP-9GW9NSUL2gvae4c0xDZ1dxTfeh5k7t8QIWXy6POBUqHw/formResponse?usp=pp_url&entry.1461253234={obj['name'][0]}&entry.97617893={obj['nik'][0]}&entry.771091418={obj['place'][0]}&entry.1911041054={obj['olahraga'][0]}&entry.104049788={obj['konsumsi_sayur_buah'][0]}&entry.185650305={obj['umur'][0]}&entry.1560480851={obj['sistol'][0]}&entry.761892027={obj['riwayat_keluarga_dm'][0]}&entry.955067944={probabilities[0]}&entry.2101683913={result_sensitivity}&entry.499972384={result_ppv}'''
    
    # Temp URL
    # url = f'''https://docs.google.com/forms/d/e/1FAIpQLSds_08qqDJYZa1vSVK23W61geve_Dsutd9dPgOBBCfAW0exag/formResponse?usp=pp_url&entry.1538448013={obj['name'][0]}&entry.2143466818={obj['nik'][0]}&entry.1065295258={obj['place'][0]}&entry.707008583={obj['olahraga'][0]}&entry.387539202={obj['konsumsi_sayur_buah'][0]}&entry.1145229138={obj['umur'][0]}&entry.716607690={obj['sistol'][0]}&entry.1076908574={obj['riwayat_keluarga_dm'][0]}&entry.651167561={probabilities[0]}&entry.550007886={result_sensitivity}&entry.132927484={result_ppv}'''
    
    response = requests.get(url)

    # res = '<b style="color:#CF2B2E;">Tinggi</b>' if result_ppv == 'Tinggi' else '<b style="color:#57855D;">Rendah</b>'''
    div_modal = st.container()
    # div_modal.success('Terima kasih kepada tenaga kesehatan dan relawan yang telah mengisi formulir pilot diabetes untuk memvalidasi dan menyempurnakan pemodelan kecerdasan artifisial dalam prediksi risiko DM', icon="✅")

    st.session_state.name = NAME
    st.session_state.nik = NIK
    st.session_state.place = PLACE
    st.session_state.age = AGE
    st.session_state.systolic = SYSTOLIC
    st.session_state.family_history = FAMILY_HISTORY
    st.session_state.exercise = EXERCISE
    st.session_state.diet = DIET
    # st.session_state.gds = GDS

    div_modal.info(f'''{LANGUAGE_PACK["resultinfo"][st.session_state.language]}''', icon="ℹ️")

    if result_sensitivity == "Tinggi":
        div_modal.markdown(f'''
            <p class="regular16" style="text-align:center;">{LANGUAGE_PACK["result1"][st.session_state.language]} <b style="color:red;">{LANGUAGE_PACK["resulthigh"][st.session_state.language]}</b>.</p>
            <p class="regular16" style="text-align:center;">{LANGUAGE_PACK["resulthighdesc"][st.session_state.language]}</p>
        ''', unsafe_allow_html=True)
    else:
        div_modal.markdown(f'''
            <p class="regular16" style="text-align:center;">{LANGUAGE_PACK["result1"][st.session_state.language]} <b style="color:green;">{LANGUAGE_PACK["resultlow"][st.session_state.language]}</b>.</p>
            <p class="regular16" style="text-align:center;">{LANGUAGE_PACK["resultlowdesc1"][st.session_state.language]}</p>
            <ul>
                <li class="regular16">{LANGUAGE_PACK["resultlowdesca"][st.session_state.language]}</li>
                <li class="regular16">{LANGUAGE_PACK["resultlowdescb"][st.session_state.language]}</li>
                <li class="regular16">{LANGUAGE_PACK["resultlowdescc"][st.session_state.language]}</li>
                <li class="regular16">{LANGUAGE_PACK["resultlowdescd"][st.session_state.language]}</li>
                <li class="regular16">{LANGUAGE_PACK["resultlowdesce"][st.session_state.language]}</li>
                <li class="regular16">{LANGUAGE_PACK["resultlowdescf"][st.session_state.language]}</li>
            </ul>
            <p class="regular16" style="text-align:center;">{LANGUAGE_PACK["resultlowdesc2"][st.session_state.language]}</p>
        ''', unsafe_allow_html=True)
    # div_modal.markdown(f'''
    #     <p class="medium50" style="text-align:center;">Kamu Beresiko {res}</p>\n
    #     <p class="regular18" style="color:#505F98; background-color:#D2E0B7; text-align:center;">Hasil skrining bukan hasil pemeriksaan medis. Konsultasikan dengan tenaga profesional untuk informasi lanjutan</p>\n
    #     <p class="regular18" style="text-align:center; font-weight:500; padding-top:50px;"><b>Mengenal risiko diabetes pada skrining ini:</b></p>
    # ''', unsafe_allow_html=True)

    # col_mod1, col_mod2 = div_modal.columns(2)
    # col_mod1.markdown('''
    #     <p class="medium24">Risiko yang tidak dapat dirubah</p>
    #     <p class="regular16" style="color:#505F98;">Risiko ini tidak dapat dihindari, sehingga lebih fokuslah kepada faktor yang bisa berubah</p>
    #     <ul>
    #         <li class="inf">Umur</li>
    #         <li class="inf">Riwayat keluarga</li>
    #     </ul>
    # ''', unsafe_allow_html=True)

    # col_mod2.markdown('''
    #     <p class="medium24">Risiko yang dapat dirubah</p>
    #     <p class="regular16" style="color:#505F98;">Risiko ini dapat dikurangi atau dirubah dengan cara menjaga lifestyle saudara</p>
    #     <ul>
    #         <li class="inf">Tekanan darah sistolik</li>
    #         <li class="inf">Olahraga</li>
    #         <li class="inf">Konsumsi sayur-buah</li>
    #     </ul>
    # ''', unsafe_allow_html=True)

@st.dialog("Error", width="small")
def show_error(obj):
    div_modal = st.container()
    value = {i for i in obj if obj[i]==None}
    div_modal.error(f'''{LANGUAGE_PACK["formincomplete"][st.session_state.language]} {value}''', icon="🚨")

@st.dialog("Error", width="small")
def nik_error():
    div_modal = st.container()
    div_modal.error(f'''{LANGUAGE_PACK["formincompletenik"][st.session_state.language]}''', icon="🚨")

# define columns
col_mid41, col_mid42, col_mid43, col_mid44 = div_main.columns(4, vertical_alignment="center")

if col_mid42.button(f'''**{LANGUAGE_PACK["submitbtn"][st.session_state.language]}**''', type="primary"):
    if st.session_state.name == None or st.session_state.nik == None or st.session_state.place == None or st.session_state.age == None or st.session_state.systolic == None or st.session_state.family_history == None or st.session_state.exercise == None or st.session_state.diet == None:
        show_error(
            {
                LANGUAGE_PACK["errorlist"][st.session_state.language][0]: st.session_state.name,
                LANGUAGE_PACK["errorlist"][st.session_state.language][1]: st.session_state.nik,
                LANGUAGE_PACK["errorlist"][st.session_state.language][2]: st.session_state.place,
                LANGUAGE_PACK["errorlist"][st.session_state.language][3]: st.session_state.age,
                LANGUAGE_PACK["errorlist"][st.session_state.language][4]: st.session_state.systolic,
                LANGUAGE_PACK["errorlist"][st.session_state.language][5]: st.session_state.family_history,
                LANGUAGE_PACK["errorlist"][st.session_state.language][6]: st.session_state.exercise,
                LANGUAGE_PACK["errorlist"][st.session_state.language][7]: st.session_state.diet
                # "Gula Darah": st.session_state.gds
            }
        )
    elif not st.session_state.nik.isdigit() or len(st.session_state.nik) != 16:
        nik_error()
    else:
        olahraga = None
        makanan = None

        if st.session_state.exercise == 'Ya':
            olahraga = 'CUKUP'
        elif st.session_state.exercise == 'Tidak':
            olahraga = 'KURANG'

        if st.session_state.diet == 'Ya':
            makanan = 'CUKUP'
        elif st.session_state.diet == 'Tidak':
            makanan = 'KURANG'

        calculate_risk(
            {
                "name": [st.session_state.name],
                "nik": [st.session_state.nik],
                "place": [st.session_state.place],
                "umur": [st.session_state.age],
                "sistol": [st.session_state.systolic],
                "riwayat_keluarga_dm": [st.session_state.family_history.upper()],
                "olahraga": [olahraga],
                "konsumsi_sayur_buah": [makanan]
                # "gds": [st.session_state.gds]
            }

        )

if col_mid43.button('**Reset Form**', type='secondary'):
    st.session_state.name = NAME
    st.session_state.nik = NIK
    st.session_state.place = PLACE
    st.session_state.age = AGE
    st.session_state.systolic = SYSTOLIC
    st.session_state.family_history = FAMILY_HISTORY
    st.session_state.exercise = EXERCISE
    st.session_state.diet = DIET
    # st.session_state.gds = GDS

# define input forms
name = placeholder_name.text_input(
    "Nama kamu siapa?",
    placeholder=LANGUAGE_PACK["nameplaceholder"][st.session_state.language],
    label_visibility="collapsed",
    key="name"
)

nik = placeholder_nik.text_input(
    "NIK kamu?",
    placeholder="0123456789012345",
    label_visibility="collapsed",
    key="nik"
)

place = placeholder_place.selectbox(
    "Dimana kamu diperiksa?",
    (LANGUAGE_PACK["locationoption"][st.session_state.language], "Puskesmas Cakung", "Puskesmas Tanjung Priok"),
    placeholder=LANGUAGE_PACK["locationplaceholder"][st.session_state.language],
    label_visibility="collapsed",
    key="place"
)

age = placeholder_age.number_input(
    "Berapa umurmu?",
    min_value=15,
    max_value=100,
    value=None,
    label_visibility="collapsed",
    key="age"
)

systolic = placeholder_systolic.number_input(
    "Berapa tekanan sistolmu?",
    min_value=60,
    max_value=600,
    value=None,
    label_visibility="collapsed",
    key="systolic"
)

family_history = placeholder_family_history.radio(
    "Apakah kamu memiliki orang tua atau saudara yang menderita diabetes?",
    ("Ya", "Tidak"),
    format_func=lambda x: mapping_y_t[x],
    index=None,
    label_visibility="collapsed",
    key="family_history"
)

exercise = placeholder_exercise.radio(
    "Apakah kamu sering berolahraga, sekiranya 2 jam dalam seminggu?",
    ("Ya", "Tidak"),
    format_func=lambda x: mapping_y_t[x],
    index=None,
    label_visibility="collapsed",
    key="exercise"
)

diet = placeholder_diet.radio(
    "Apakah kamu mengonsumsi 5 porsi buah sayur tiap harinya?",
    ("Ya", "Tidak"),
    format_func=lambda x: mapping_y_t[x],
    index=None,
    label_visibility="collapsed",
    key="diet"
)

# gds = placeholder_gds.number_input(
#     "Berapakah gula darah sewaktu pasien saat ini?",
#     min_value=40,
#     max_value=650,
#     label_visibility="collapsed",
#     key="gds"
# )

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