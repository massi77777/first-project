import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺", layout="centered")

@st.cache_resource
def load_model():
    with open("best_model.pkl", "rb") as f: model = pickle.load(f)
    with open("scaler.pkl",     "rb") as f: scaler = pickle.load(f)
    with open("features.pkl",   "rb") as f: features = pickle.load(f)
    return model, scaler, features

model, scaler, FEATURE_NAMES = load_model()

FEATURE_INFO = {
    "Pregnancies":              ("Number of Pregnancies",          0,   20,  3,    1),
    "Glucose":                  ("Blood Glucose Level (mg/dL)",    0,  300, 117,   1),
    "BloodPressure":            ("Diastolic Blood Pressure (mmHg)",0,  150,  72,   1),
    "SkinThickness":            ("Skin Fold Thickness (mm)",       0,  100,  23,   1),
    "Insulin":                  ("Insulin Level (mu U/ml)",        0,  900,  30,   1),
    "BMI":                      ("Body Mass Index (BMI)",          0.0, 70.0, 32.0, 0.1),
    "DiabetesPedigreeFunction": ("Diabetes Pedigree Function",     0.0,  3.0,  0.3, 0.01),
    "Age":                      ("Age (years)",                    1,  120,  33,   1),
}

st.title("🩺 Diabetes Prediction System")
st.markdown("Adjust the medical values below, then press **Analyze**.")
st.markdown("---")

col1, col2 = st.columns(2)
values = {}

for i, feat in enumerate(FEATURE_NAMES):
    if feat in FEATURE_INFO:
        label, mn, mx, default, step = FEATURE_INFO[feat]
        col = col1 if i % 2 == 0 else col2
        if isinstance(step, float):
            values[feat] = col.slider(label, float(mn), float(mx), float(default), step)
        else:
            values[feat] = col.slider(label, int(mn), int(mx), int(default), step)
    else:
        values[feat] = st.number_input(feat, value=0.0)

st.markdown("---")

if st.button("🔍 Analyze", use_container_width=True, type="primary"):
    input_data   = np.array([values[f] for f in FEATURE_NAMES]).reshape(1, -1)
    input_scaled = scaler.transform(input_data)
    prediction   = model.predict(input_scaled)[0]
    probability  = model.predict_proba(input_scaled)[0] if hasattr(model, "predict_proba") else None

    st.markdown("### 📋 Result")

    if prediction == 1:
        st.error("🔴 **Diabetic** — High Risk")
        st.warning("⚠️ Please consult a doctor and get tested as soon as possible.")
    else:
        st.success("🟢 **Not Diabetic** — Low Risk")
        st.info("✅ Keep up your healthy lifestyle!")

    if probability is not None:
        pct = float(probability[1])
        st.markdown(f"**📊 Probability of Diabetes: `{pct:.1%}`**")
        st.progress(pct)

    st.caption("⚕️ This tool is for educational purposes only and does not replace medical advice.")
