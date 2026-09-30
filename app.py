import streamlit as st
import numpy as np
import joblib

st.set_page_config(
    page_title="Prediksi Kelulusan SDG 4",
    page_icon="🎓",
    layout="centered"
)

@st.cache_resource
def load_model():
    model = joblib.load("model_logistic_regression.pkl")
    scaler = joblib.load("scaler.pkl")
    return model, scaler

model, scaler = load_model()

st.title("🎓 Prediksi Kelulusan Siswa")
st.subheader("SDG 4 – Pendidikan Berkualitas")
st.write(
    "Aplikasi ini menggunakan **Logistic Regression** untuk mengklasifikasikan "
    "status kelulusan berdasarkan indikator akademik sederhana."
)
st.info(
    "⚠️ Dataset yang digunakan adalah data simulasi untuk tugas pembelajaran. "
    "Prediksi bukan penilaian resmi terhadap siswa."
)

st.markdown("### Masukkan data siswa")
col1, col2 = st.columns(2)

with col1:
    attendance = st.number_input(
        "Kehadiran (%)", min_value=55.0, max_value=100.0,
        value=85.0, step=1.0
    )
    study_hours = st.number_input(
        "Jam belajar per hari", min_value=1.0, max_value=8.0,
        value=4.0, step=0.5
    )

with col2:
    assignment_score = st.number_input(
        "Nilai tugas", min_value=45.0, max_value=100.0,
        value=80.0, step=1.0
    )
    exam_score = st.number_input(
        "Nilai ujian", min_value=40.0, max_value=100.0,
        value=80.0, step=1.0
    )

if st.button("🔍 Prediksi Kelulusan", use_container_width=True):
    input_data = np.array([[
        attendance,
        study_hours,
        assignment_score,
        exam_score
    ]])

    input_scaled = scaler.transform(input_data)
    prediction = int(model.predict(input_scaled)[0])
    probabilities = model.predict_proba(input_scaled)[0]
    probability = float(probabilities[prediction])

    st.markdown("---")
    if prediction == 1:
        st.success("### Hasil Prediksi: LULUS")
    else:
        st.error("### Hasil Prediksi: TIDAK LULUS")

    st.metric("Probabilitas kelas yang diprediksi", f"{probability:.2%}")

    with st.expander("Lihat data input"):
        st.write({
            "Kehadiran (%)": attendance,
            "Jam belajar/hari": study_hours,
            "Nilai tugas": assignment_score,
            "Nilai ujian": exam_score
        })

st.caption("Tugas Pengganti IT Incubation | SDG 4 – Pendidikan Berkualitas")
