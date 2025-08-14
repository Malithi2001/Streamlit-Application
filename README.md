Wine Quality Prediction with Streamlit
Project Overview
This project predicts the quality of wine based on its physicochemical properties. Using the Wine Quality Dataset from Kaggle, we build a machine learning model to classify wine quality, then deploy it as an interactive Streamlit web application.

The app allows users to:
    Explore the dataset through visualisations

    Test different input values and get quality predictions

    View model performance metrics
                 
Dataset
    /Users/sachith/Desktop/Stremlit/Data/WineQT.csv

Steps in the Project

    1. Data Analysis & Preprocessing

        Performed EDA to understand feature relationships

        Checked and handled missing values

        Created visualisations (heatmaps, histograms, scatter plots)

        Applied feature engineering if required

        Split data into training & testing sets

    2. Model Training

        Trained:

            Logistic Regression

            Random Forest Classifier

        Evaluated using accuracy, precision, recall, and F1-score

        Selected the best-performing model (Random Forest)

        Saved the model using pickle

    3. Streamlit Application

        Sidebar navigation for sections:

            Dataset Overview

            Visualisations

            Model Prediction

            Model Performance

        Input widgets for user feature values

        Real-time predictions with probability scores

    4. Deployment

        Pushed code to GitHub

        Deployed on Streamlit Cloud

        Public URL will be available for testing

Project Stucture 
    STREAMLIT
├── app.py                     
├── requirements.txt           
├── model.pkl                  
├── data/
│   └── winequality.csv        
├── notebooks/
│   └── model_training.ipynb   
└── README.md 