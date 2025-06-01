import streamlit as st
import joblib

# Load saved model and vectorizer
model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

st.title("📬 SMS Spam Classifier")

message = st.text_area("Enter an SMS message:")

if st.button("Predict"):
    msg_vector = vectorizer.transform([message])
    prediction = model.predict(msg_vector)[0]
    result = "🚫 Spam" if prediction else "✅ Not Spam"
    st.success(f"Prediction: {result}")
