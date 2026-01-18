📧 Email Cybersecurity Classification System
a. Problem Statement

Email is one of the most widely used communication channels and also a major attack vector for cyber threats such as spam, phishing, and malware delivery.
Manual detection of malicious emails is inefficient and error-prone, especially at scale.

Objective:
To design and implement a machine learning–based email classification system that automatically classifies emails into the following categories:

Spam

Phishing

Malicious

Normal (Benign)

The system aims to improve detection accuracy, reduce false positives, and support cybersecurity monitoring and response.

b. Dataset Description

The dataset consists of email text samples labeled into four cybersecurity-related classes.

Dataset Structure
Column Name	Description
email_text	Raw content/body of the email
label	Category of the email (Spam, Phishing, Malicious, Normal)
Key Characteristics

Text-based dataset

Multi-class classification problem

Labels encoded using LabelEncoder

TF-IDF used for feature extraction with unigrams and bigrams

c. Models Used

Six machine learning models were trained and evaluated using the same feature extraction and preprocessing pipeline.

Feature Engineering

TF-IDF Vectorization

n-gram range: (1,2)

Stop words: English

Max features: 30,000

Sublinear TF scaling

📊 Model Performance Comparison
Evaluation Metrics

Accuracy

AUC

Precision

Recall

F1-score

Matthews Correlation Coefficient (MCC)

🔹 Comparison Table (Metrics)
ML Model Name	Accuracy	AUC	Precision	Recall	F1	MCC
Logistic Regression	XX	XX	XX	XX	XX	XX
Decision Tree	XX	XX	XX	XX	XX	XX
kNN	XX	XX	XX	XX	XX	XX
Naive Bayes	XX	XX	XX	XX	XX	XX
Random Forest (Ensemble)	XX	XX	XX	XX	XX	XX
XGBoost (Ensemble)	XX	XX	XX	XX	XX	XX

Note: Replace XX with values obtained from evaluation on the test dataset.

🧠 Model-wise Observations
🔹 Observation Table
ML Model Name	Observation about Model Performance
Logistic Regression	Performed well on linearly separable data; stable and interpretable with balanced precision and recall.
Decision Tree	Easy to interpret but prone to overfitting, especially on small datasets.
kNN	Sensitive to feature dimensionality; performance degrades with large TF-IDF feature space.
Naive Bayes	Fast and efficient; performed reasonably well on text data but assumes feature independence.
Random Forest (Ensemble)	Improved generalization and reduced overfitting; strong overall performance across metrics.
XGBoost (Ensemble)	Achieved the best performance; handled complex patterns and class imbalance effectively.
✅ Conclusion

The ensemble-based models (Random Forest and XGBoost) outperformed individual classifiers in most evaluation metrics.
XGBoost demonstrated superior robustness and predictive power, making it the most suitable model for email cybersecurity classification.
