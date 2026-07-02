


import streamlit as st
import pandas as pd
import joblib


st.markdown("""
<div style="display:flex; align-items:center; gap:15px;">
    <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width="50"/>
    <h1 style="margin:0; color:#1f4e79;">HR Analytics Dashboard</h1>
</div>
""", unsafe_allow_html=True)
# -----------------------------
# Load Dataset
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv")


df = load_data()

# -----------------------------
# Load Model Files
# -----------------------------
@st.cache_resource
def load_models():
    model = joblib.load("model/model.pkl")
    scaler = joblib.load("model/scaler.pkl")
    label_encoders = joblib.load("model/label_encoders.pkl")
    return model, scaler, label_encoders


model, scaler, label_encoders = load_models()


# -----------------------------
# Prediction Page
# -----------------------------
def predict():

    # Create Prediction History
    if "history" not in st.session_state:
        st.session_state.history = []

    st.title("👨 Employee Attrition Prediction")
    st.write("Enter employee details below to predict attrition.")

    st.divider()

    col1, col2 = st.columns(2)

    # ---------------- LEFT ---------------- #

    with col1:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=60,
            value=30
        )

        distance = st.number_input(
            "Distance From Home",
            min_value=1,
            max_value=30,
            value=5
        )

        environment = st.selectbox(
            "Environment Satisfaction",
            [1, 2, 3, 4]
        )

        job_involvement = st.selectbox(
            "Job Involvement",
            [1, 2, 3, 4]
        )

        job_level = st.selectbox(
            "Job Level",
            [1, 2, 3, 4, 5]
        )

        job_satisfaction = st.selectbox(
            "Job Satisfaction",
            [1, 2, 3, 4]
        )

        marital = st.selectbox(
            "Marital Status",
            sorted(df["MaritalStatus"].unique())
        )

    # ---------------- RIGHT ---------------- #

    with col2:

        income = st.number_input(
            "Monthly Income",
            min_value=1000,
            max_value=25000,
            value=5000
        )

        overtime = st.selectbox(
            "OverTime",
            sorted(df["OverTime"].unique())
        )

        stock = st.selectbox(
            "Stock Option Level",
            [0, 1, 2, 3]
        )

        total_years = st.number_input(
            "Total Working Years",
            min_value=0,
            max_value=40,
            value=10
        )

        worklife = st.selectbox(
            "Work Life Balance",
            [1, 2, 3, 4]
        )

        years_company = st.number_input(
            "Years At Company",
            min_value=0,
            max_value=40,
            value=5
        )

        years_role = st.number_input(
            "Years In Current Role",
            min_value=0,
            max_value=20,
            value=3
        )

        years_manager = st.number_input(
            "Years With Current Manager",
            min_value=0,
            max_value=20,
            value=3
        )

    st.divider()

    # ---------------- Prediction ---------------- #

    if st.button("🔍 Predict Attrition", use_container_width=True):

        # Encode categorical values
        marital_encoded = label_encoders["MaritalStatus"].transform([marital])[0]
        overtime_encoded = label_encoders["OverTime"].transform([overtime])[0]

        # Create DataFrame
        input_df = pd.DataFrame([{
            "Age": age,
            "DistanceFromHome": distance,
            "EnvironmentSatisfaction": environment,
            "JobInvolvement": job_involvement,
            "JobLevel": job_level,
            "JobSatisfaction": job_satisfaction,
            "MaritalStatus": marital_encoded,
            "MonthlyIncome": income,
            "OverTime": overtime_encoded,
            "StockOptionLevel": stock,
            "TotalWorkingYears": total_years,
            "WorkLifeBalance": worklife,
            "YearsAtCompany": years_company,
            "YearsInCurrentRole": years_role,
            "YearsWithCurrManager": years_manager
        }])

        # Scale Data
        input_scaled = scaler.transform(input_df)

        # Prediction
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1]

        # Save History
        st.session_state.history.append({
            "Age": age,
            "Income": income,
            "OverTime": overtime,
            "Prediction": "High Risk" if prediction == 1 else "Low Risk",
            "Probability": f"{probability*100:.2f}%"
        })

        st.divider()

        # Display Result
        if prediction == 1:

            st.error("🚨 High Risk of Employee Attrition")

        else:

            st.success("✅ Low Risk of Employee Attrition")

        st.metric(
            "Attrition Probability",
            f"{probability*100:.2f}%"
        )

        st.progress(float(probability))

        # Recommendations
        st.subheader("📌 HR Recommendations")

        if prediction == 1:

            st.warning("""
- Conduct one-on-one discussion

- Review salary and benefits

- Improve work-life balance

- Offer career growth opportunities

- Increase employee engagement
            """)

        else:

            st.info("""
- Continue employee engagement

- Recognize employee performance

- Maintain healthy work culture

- Encourage learning opportunities
            """)

    # ---------------- Prediction History ---------------- #

    st.divider()

    st.subheader("📋 Prediction History")

    if len(st.session_state.history) > 0:

        history_df = pd.DataFrame(st.session_state.history)

        st.dataframe(
            history_df,
            use_container_width=True,
            hide_index=True
        )

        csv = history_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇ Download Prediction History",
            data=csv,
            file_name="prediction_history.csv",
            mime="text/csv",
            use_container_width=True
        )

    else:

        st.info("No predictions made yet.")