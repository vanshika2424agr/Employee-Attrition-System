import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_data
def load_data():
    return pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv")


def analytics():

    df = load_data()

    st.title("📈 Employee Analytics")
    st.write("Detailed analysis of employee attrition.")

    st.divider()

    # ----------------------------
    # Attrition by Age
    # ----------------------------
    fig = px.histogram(
        df,
        x="Age",
        color="Attrition",
        nbins=20,
        title="Age vs Attrition"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ----------------------------
    # Income vs Attrition
    # ----------------------------
    fig = px.box(
        df,
        x="Attrition",
        y="MonthlyIncome",
        color="Attrition",
        title="Monthly Income vs Attrition"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ----------------------------
    # Job Satisfaction
    # ----------------------------
    fig = px.histogram(
        df,
        x="JobSatisfaction",
        color="Attrition",
        barmode="group",
        title="Job Satisfaction vs Attrition"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ----------------------------
    # Years at Company
    # ----------------------------
    fig = px.scatter(
        df,
        x="YearsAtCompany",
        y="MonthlyIncome",
        color="Attrition",
        title="Years at Company vs Income"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("Dataset Preview")

    st.dataframe(df.head(20), use_container_width=True)