import streamlit as st
import os
import joblib
from PIL import Image
from test_data import spam_emails, non_spam_emails

model_path = "train/trained_model.pkl"
tfidf_path = "train/tfidf_vectorizer.pkl"

# Check if the model and vectorizer files exist
if not os.path.exists(model_path) or not os.path.exists(tfidf_path):
    st.error("If you see this message, it means that you haven't trained the model yet. Please follow the instructions below to train the model.")
    st.write("""
        ## 📝 How to Run the Jupyter Notebook for Training
        To train the model and generate the necessary files, follow these steps:

        1. **Navigate to the project**
           ```bash
           cd ati-final
           ```

        2. **Run the Jupyter Notebook:**
           The training process and model saving are done within the Jupyter notebook. 
           Execute the `train_model.ipynb` notebook to train and save the model and TF-IDF vectorizer:
           ```bash
           python train_model.py
           ```

        3. **Stop and rerun the app**
           Once the model and vectorizer are saved, rerun the Streamlit app to load the trained model and vectorizer.

        **Note:** This process will generate the required files (`trained_model.pkl` and `tfidf_vectorizer.pkl`) in the `train` directory.
    """)
    st.stop() 

st.sidebar.markdown("# **Email Classification**")

# Sidebar navigation
nav_selection = st.sidebar.radio(
    "navigation", 
    ["🏠 Introduction", "📜 Spam Email List", "✅ Ham Email List", "🔍 Classify Email"] 
    
)

# Function to classify emails
def classify_email(test_input):
    input_data_features = tfidf_vectorizer.transform([test_input])
    prediction = model.predict(input_data_features)
    return prediction[0]

if nav_selection == "🏠 Introduction":
    st.markdown("<h1 style='font-size: 36px;'>📧 EMAIL CLASSIFICATION - ATI FINAL</h1>", unsafe_allow_html=True)
    st.markdown("""
    ## Why 4 Tabs?

    This Streamlit app is designed to provide a comprehensive overview of the email classification project and its functionalities. The 4-tab navigation structure is chosen to enhance user experience and clarity:

    - **Introduction**: This tab provides a general introduction to the project, its goals, and the underlying technology.
    - **Spam Email List**: This tab showcases a list of sample spam emails to illustrate the types of messages the model is trained to identify.
    - **Ham Email List**: This tab presents a list of sample ham emails to demonstrate the types of legitimate messages the model can correctly classify.
    - **Classify Email**: This tab offers an interactive feature where users can input their own email and receive a classification prediction from the trained model.

    By dividing the content into these 4 distinct tabs, the app becomes more organized, user-friendly, and informative.

    ## 5W1H            
    **Who?** This application is designed for anyone interested in classifying emails as spam or ham (legitimate). This could be individuals managing their inboxes, businesses filtering incoming messages, or developers exploring machine learning for text classification.

    **What?** This Streamlit app utilizes a machine learning model trained to classify emails into two categories: spam and ham. Users can't directly interact with the model in the app, but the provided code snippet demonstrates how to test a new email message.

    **When?** Users can access this app anytime to gain insights into the project's functionalities and underlying technologies.

    **Where?** This app can be deployed on a web server, allowing users to access it through a web browser.

    **Why?** This project aims to:

    - Demonstrate building a machine learning model for email classification using Python libraries.
    - Provide a basic understanding of email spam filtering and its potential benefits.
    - Showcase the use of Streamlit for creating interactive data applications.

    **How?**

    This project leverages the following technologies:

    - **streamlit (version 1.40.1)**: A Python library used for rapidly creating web applications with minimal coding.
    - **scikit-learn (version 1.5.2)**: A popular machine learning library in Python offering various algorithms for classification, regression, clustering, and more. In this project, it's used for feature extraction and model training.
    - **pandas**: A powerful library for data manipulation and analysis. It's likely used for loading and preprocessing the email data.
    - **joblib (version 1.4.2)**: A library for model persistence, allowing you to save and load trained models for future use.
    - **ipykernel (version 6.29.5)**: A kernel for Jupyter Notebook, providing interactive computing environments.
    - **matplotlib (version 3.9.2)**: A plotting library for creating static, animated, and interactive visualizations.
    - **seaborn (version 0.13.2)**: A data visualization library based on matplotlib, providing a high-level interface for creating attractive and informative statistical graphics.   
    - **nbformat (version 5.10.4)**: A library for reading and writing Jupyter Notebook files.
    - **nbconvert (version 7.16.4)**: A library for converting Jupyter Notebooks to various formats, such as HTML, PDF, and Python scripts.
    """)

# Spam Email List Page
elif nav_selection == "📜 Spam Email List":
    st.title("📜 Spam Email List")
    st.info("Here are some examples of **Spam Emails** used for training the model.")
    for email in spam_emails:
        with st.expander(email[:50] + "...", expanded=False):  # Email preview
            st.code(email)

# Not Spam Email List Page
elif nav_selection == "✅ Ham Email List":
    st.title("✅ Ham Email List")
    st.success("Here are some examples of **Legitimate Emails** used for training the model.")
    for email in non_spam_emails:
        with st.expander(email[:50] + "...", expanded=False):  # Email preview
            st.code(email)

# Classify Email Page
elif nav_selection == "🔍 Classify Email":
    st.title("🔍 Classify an Email")
    st.caption("Input a custom email to classify as **Spam** or **Not Spam** using our trained model.")
    model = joblib.load(model_path)
    tfidf_vectorizer = joblib.load(tfidf_path)
    input_text = st.text_area("📩 Enter email content here:", max_chars=500)
    
    if st.button("Classify"):
        if input_text.strip():
            result = classify_email(input_text)
            if result == 1:
                col1, col2, col3 = st.columns(3)
                with col2:
                    st.image("assets/alert.png", use_container_width=True)
                st.error("Prediction: **Spam Email**")
            else:
                col1, col2, col3 = st.columns(3)
                with col2:
                    st.image("assets/ok.png", use_container_width=True)
                st.success("Prediction: **Ham Email**")
        else:
            st.warning("Please enter some text to classify.")
