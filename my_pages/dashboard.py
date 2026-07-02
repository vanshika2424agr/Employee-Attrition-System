import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Load Dataset
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv")


def dashboard():

    df = load_data()

    st.title("📊 HR Analytics Dashboard")
    st.write("Employee Attrition Analysis using IBM HR Analytics Dataset")

    st.divider()

    # ---------------- KPI ---------------- #

    total_employees = len(df)

    attrition_rate = (
        len(df[df["Attrition"] == "Yes"]) / total_employees
    ) * 100

    avg_income = df["MonthlyIncome"].mean()

    avg_age = df["Age"].mean()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("👨 Employees", total_employees)
    c2.metric("🚪 Attrition Rate", f"{attrition_rate:.2f}%")
    c3.metric("💰 Avg Income", f"₹{avg_income:,.0f}")
    c4.metric("🎂 Avg Age", f"{avg_age:.1f} Years")

    st.divider()

    # ---------------- Charts Row 1 ---------------- #

    col1, col2 = st.columns(2)

    with col1:

        dept = (
            df.groupby(["Department", "Attrition"])
            .size()
            .reset_index(name="Employees")
        )

        fig = px.bar(
            dept,
            x="Department",
            y="Employees",
            color="Attrition",
            barmode="group",
            title="Department-wise Attrition"
        )

        fig.update_layout(
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        fig = px.pie(
            df,
            names="Attrition",
            hole=0.45,
            title="Attrition Distribution"
        )

        fig.update_layout(
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ---------------- Charts Row 2 ---------------- #

    col3, col4 = st.columns(2)

    with col3:

        fig = px.histogram(
            df,
            x="MonthlyIncome",
            nbins=30,
            title="Monthly Income Distribution"
        )

        fig.update_layout(
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col4:

        overtime = (
            df.groupby(["OverTime", "Attrition"])
            .size()
            .reset_index(name="Employees")
        )

        fig = px.bar(
            overtime,
            x="OverTime",
            y="Employees",
            color="Attrition",
            barmode="group",
            title="OverTime vs Attrition"
        )

        fig.update_layout(
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ---------------- Department Summary ---------------- #

    st.subheader("📋 Department Summary")

    summary = (
        df.groupby("Department")
        .agg(
            Employees=("Department", "count"),
            Avg_Age=("Age", "mean"),
            Avg_Income=("MonthlyIncome", "mean")
        )
        .reset_index()
    )

    summary["Avg_Age"] = summary["Avg_Age"].round(1)
    summary["Avg_Income"] = summary["Avg_Income"].round(0)

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )
