import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score
import streamlit as st

# Load Datasets
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

# Add labels
fake["label"] = 0
true["label"] = 1

# Combine datasets
data = pd.concat([fake, true])

# Shuffle dataset
data = data.sample(frac=1).reset_index(drop=True)

# Combine title and text for better prediction
data["content"] = data["title"] + " " + data["text"]

# Features and labels
x = data["content"]
y = data["label"]

# Split dataset
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_df=0.7
)

tfidf_train = vectorizer.fit_transform(x_train)
tfidf_test = vectorizer.transform(x_test)

# Train Model
model = PassiveAggressiveClassifier(max_iter=1000)

model.fit(tfidf_train, y_train)

# Predict accuracy
y_pred = model.predict(tfidf_test)

score = accuracy_score(y_test, y_pred)

# Streamlit UI
st.title("📰 Fake News Detection App")

st.subheader("AI/ML Mini Project")

st.write(
    "This application predicts whether a news article is REAL or FAKE using Machine Learning."
)

st.write(f"### Model Accuracy: {round(score * 100, 2)}%")

# User input
user_input = st.text_area("Enter News Article Text")

# Prediction button
if st.button("Predict"):

    # Empty input validation
    if user_input.strip() == "":
        st.warning("Please enter some news text.")

    else:
        input_data = vectorizer.transform([user_input])

        prediction = model.predict(input_data)

        if prediction[0] == 0:
            st.error("🚨 Fake News")

        else:
            st.success("✅ Real News")

# Footer
st.markdown("---")
st.write("Developed by Chaitanya Sai")