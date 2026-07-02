import streamlit as st


def about():

    st.title("ℹ️ About Project")

    st.write(
        """
        This Employee Attrition Prediction System is a Machine Learning
        project developed to predict whether an employee is likely to
        leave the organization based on various employee attributes.
        """
    )

    st.divider()

    st.subheader("🎯 Objective")

    st.write("""
    - Predict employee attrition.
    - Help HR identify employees at risk.
    - Support better employee retention strategies.
    """)

    st.subheader("📂 Dataset")

    st.write("""
    IBM HR Analytics Employee Attrition Dataset

    - Total Records : 1470
    - Features : 35
    - Target Variable : Attrition
    """)

    st.subheader("🤖 Machine Learning Model")

    st.write("""
    - Algorithm : Logistic Regression
    - Data Scaling : StandardScaler
    - Encoding : Label Encoding
    """)

    st.subheader("🛠️ Technologies Used")

    st.write("""
    - Python
    - Streamlit
    - Pandas
    - NumPy
    - Scikit-learn
    - Plotly
    - Joblib
    """)

    st.subheader("👩‍💻 Developed By")

    st.write("""
    **Vanshika Agrawal & Vaishnavi Keshari**

    AIML Summer Internship Project

    IIHMF, MNNIT Allahabad
    """)

    st.success("Employee Attrition Prediction System")