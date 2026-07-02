# 👨‍💼 Employee Attrition Prediction System

## 📌 Overview

The **Employee Attrition Prediction System** is a Machine Learning-based web application developed to predict whether an employee is likely to leave an organization. The system analyzes various employee attributes such as age, job role, monthly income, overtime, work-life balance, job satisfaction, and other HR-related factors to estimate the probability of attrition.

This application provides HR professionals with a simple and interactive interface to make data-driven decisions for improving employee retention and workforce planning.

---

## 🎯 Problem Statement

Employee attrition is a major challenge for organizations as it leads to increased recruitment costs, productivity loss, and knowledge gaps. Identifying employees who are at a higher risk of leaving enables HR teams to take proactive measures and improve employee retention.

This project aims to develop a predictive system that assists HR departments in identifying potential attrition risks using Machine Learning techniques.

---

## 🚀 Features

* Interactive Streamlit web application
* Real-time employee attrition prediction
* User-friendly employee data input form
* Machine Learning-based prediction model
* Clean and responsive interface
* Fast prediction using a trained model
* Easy-to-use navigation

---

## 🛠️ Technology Stack

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Web Framework

* Streamlit

### Model Serialization

* Joblib

---

## 📂 Project Structure

```text
Employee_Attrition_System/
│
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── model/
│   ├──label_encoders.pkl
|   |──scaler.pkl
│   └──model.pkl
│
├── my_pages/
│   ├── predict.py
│   ├── dashboard.py
│   └── about.py
│   |── analytics.py
├── assets/
│   ├── logo.png
│   ├── hero.png
│   └── avatar.png
│
└── data/
    └── Employee_Attrition_Model.ipynb
```

---

## 📊 Dataset

This project uses the **IBM HR Analytics Employee Attrition & Performance** dataset.

The dataset contains employee-related information including:

* Age
* Gender
* Department
* Job Role
* Monthly Income
* Education
* Business Travel
* Marital Status
* Overtime
* Job Satisfaction
* Work-Life Balance
* Years at Company
* Performance Rating
* Environment Satisfaction
* Distance From Home
* Training Times Last Year
* and several additional HR features.

---

## ⚙️ Project Workflow

1. Load the employee dataset.
2. Perform data preprocessing and feature engineering.
3. Train a Machine Learning classification model.
4. Evaluate the model using standard performance metrics.
5. Save the trained model.
6. Develop an interactive Streamlit application.
7. Accept employee details from the user.
8. Predict whether the employee is likely to leave or stay.
9. Display the prediction result instantly.

---

## 📈 Machine Learning Workflow

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Feature Encoding
* Feature Scaling
* Model Training
* Model Evaluation
* Model Serialization
* Streamlit Deployment

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/vanshika2424agr/Employee-Attrition-System.git
```

Move into the project directory:

```bash
cd Employee-Attrition-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 💡 Future Enhancements

* Probability-based attrition prediction
* Explainable AI using SHAP values
* Interactive analytics dashboard
* Model comparison
* Cloud deployment
* HR recommendation system
* Employee retention suggestions

---

## 🎓 Learning Outcomes

Through this project, the following concepts were implemented:

* Machine Learning Classification
* Data Preprocessing
* Feature Engineering
* Model Deployment
* Streamlit Web Development
* GitHub Project Management
* Data Visualization

---

## 👩‍💻 Developed By

**Vanshika Agrawal & Vaishnavi Keshri**

AIML Summer Internship Project

Indian Institute of Information Management and Finance (IIHMF)

Motilal Nehru National Institute of Technology (MNNIT), Prayagraj

---

## ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.
