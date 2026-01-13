import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics import classification_report, confusion_matrix

st.set_page_config(page_title="Email Cybersecurity Classifier", layout="centered")

st.title("📧 Email Cybersecurity Classification System")
st.write("Classifies emails as Spam, Phishing, Malicious, or Normal")

uploaded_file = st.file_uploader(
    "Upload TEST CSV (columns: email_text, label)", type="csv"
)

model_name = st.selectbox(
    "Select Machine Learning Model",
    [
        "Logistic Regression",
        "Decision Tree",
        "KNN",
        "Naive Bayes",
        "Random Forest",
        "XGBoost"
    ]
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    with open("model/saved_models.pkl", "rb") as f:
        data = pickle.load(f)

    vectorizer = data["vectorizer"]
    label_encoder = data["label_encoder"]
    models = data["models"]



X = vectorizer.transform(df["email_text"])
y_true = df["label"]

model = models[model_name]
y_pred_encoded = model.predict(X)
y_pred = label_encoder.inverse_transform(y_pred_encoded)

st.subheader("📊 Classification Report")
st.text(classification_report(y_true, y_pred))

st.subheader("📉 Confusion Matrix")
st.write(confusion_matrix(y_true, y_pred))


