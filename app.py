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
    models = data["models"]


    X = vectorizer.transform(df["email_text"])
    y = df["label"]

    model = models[model_name]
    predictions = model.predict(X)

    st.subheader("📊 Classification Report")
    st.text(classification_report(y, predictions))

    st.subheader("📉 Confusion Matrix")
    st.write(confusion_matrix(y, predictions))

