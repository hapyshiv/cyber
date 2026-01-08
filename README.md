# Email Cybersecurity Classification System

## Problem Statement
The objective of this project is to build and deploy multiple machine learning
classification models to identify cybersecurity threats in emails. Emails are
classified into Spam, Phishing, Malicious, or Normal categories.

## Dataset Description
- Dataset Type: Email cybersecurity dataset
- Number of Instances: 5,000+
- Number of Features: TF-IDF text features (3000)
- Target Classes: Spam, Phishing, Malicious, Normal
- Source: Public Kaggle Dataset

## Models Used and Evaluation Metrics

| Model | Accuracy | AUC | Precision | Recall | F1 | MCC |
|------|---------|-----|-----------|-------|----|-----|
| Logistic Regression | | | | | | |
| Decision Tree | | | | | | |
| KNN | | | | | | |
| Naive Bayes | | | | | | |
| Random Forest | | | | | | |
| XGBoost | | | | | | |

## Observations

| Model | Observation |
|------|------------|
| Logistic Regression | Performs well on linear text data |
| Decision Tree | Can overfit without tuning |
| KNN | Sensitive to high dimensionality |
| Naive Bayes | Very effective for text classification |
| Random Forest | Robust and stable performance |
| XGBoost | Best overall accuracy |
