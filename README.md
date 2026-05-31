📰 Fake News Detection using Machine Learning

A Machine Learning and Natural Language Processing (NLP) project that classifies news articles as Real News or Fake News using the Passive Aggressive Classifier and TF-IDF Vectorization.

🎯 Project Objective

The objective of this project is to automatically identify fake news articles and help reduce the spread of misinformation by analyzing the textual content of news articles.

🚀 Features
Detects Fake and Real News
Uses Machine Learning for classification
Interactive Streamlit Web Application
High Accuracy (~99%)
User-friendly interface
Real-world Kaggle dataset
🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Streamlit
TF-IDF Vectorizer
Passive Aggressive Classifier
Natural Language Processing (NLP)
📂 Dataset Information

Dataset: Fake and Real News Dataset

Source: Kaggle

https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

Dataset Files
Fake.csv → Fake News Articles
True.csv → Real News Articles
Dataset Statistics
Category	Records
Fake News	23,481
Real News	21,417
Total	44,898
⚙️ Project Workflow
Data Collection
       ↓
Data Preprocessing
       ↓
Data Labeling
       ↓
TF-IDF Vectorization
       ↓
Train-Test Split
       ↓
Model Training
       ↓
Model Testing
       ↓
Prediction
       ↓
Streamlit Deployment
🤖 Machine Learning Model
TF-IDF Vectorizer

Converts textual news content into numerical vectors while preserving the importance of words.

Passive Aggressive Classifier

A supervised machine learning algorithm suitable for large-scale text classification tasks and known for its fast training and high accuracy.

📊 Results
Model Accuracy

99.5% Accuracy

Predictions

The application predicts:

✅ Real News
🚨 Fake News
📸 Project Screenshots

Screenshots are available in the Screenshots folder.

Included screenshots:

Home Screen
Fake News Prediction
Real News Prediction
VS Code Source Code
Terminal Execution
▶️ How to Run the Project
Clone Repository
git clone https://github.com/igchaitanyasai/FakeNewsDetector.git
Navigate to Project Folder
cd FakeNewsDetector
Install Dependencies
pip install -r requirements.txt
Run Application
streamlit run app.py
📁 Repository Structure
FakeNewsDetector/
│
├── Screenshots/
├── Bora Chaitanya Sai_FakeNewsDetector.pdf
├── Fake.csv
├── True.csv
├── app.py
├── requirements.txt
└── README.md
📄 Project Report

The complete project report is available in:

Bora Chaitanya Sai_FakeNewsDetector.pdf
🔮 Future Enhancements
Integration with BERT and Transformer Models
Live News URL Analysis
Cloud Deployment
Real-time News Verification
Improved Generalization on Latest News Articles
👨‍💻 Author

Bora Chaitanya Sai

Computer Science and Engineering (CSE)

Malla Reddy University

Academic Year: 2025–2026

⭐ Project Status

✅ Completed

Developed as part of an AI/ML Mini Project submission.
