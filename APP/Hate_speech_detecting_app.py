import streamlit as st
import pickle
import os

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Hate Speech Detection",
    page_icon="🛡️",
    layout="centered"
)

# ----------------------------
# Load Model and Vectorizer
# ----------------------------
# Get current directory (APP/)
BASE_DIR = "/mount/src/sbi-hackathon-project/APP"


# Paths to the pickle files
model_path = os.path.join(BASE_DIR, "hate_speech_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "tfidf_vectorizer.pkl")

# Load model
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Load vectorizer
with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)

# ----------------------------
# Streamlit UI
# ----------------------------
st.title("🛡️ Hate Speech Detection App")
st.write("Enter text below and the app will predict whether it contains hate speech.")

user_input = st.text_area("✍️ Enter your text here:")

if st.button("🔍 Analyze"):
    if user_input.strip():
        # Transform text
        features = vectorizer.transform([user_input])
        prediction = model.predict(features)[0]

        # Show results
        if prediction == 1:
            st.error("⚠️ Hate Speech Detected")
        else:
            st.success("✅ No Hate Speech Detected")
    else:
        st.warning("⚠️ Please enter some text to analyze.")
