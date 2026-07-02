import streamlit as st
import pandas as pd
import joblib
from streamlit_option_menu import option_menu

# -----------------------------
# Page Configuration
# -----------------------------

hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)


st.set_page_config(
    page_title="Employee Attrition Prediction System",
    page_icon="👨‍💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Load CSS
# -----------------------------
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

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
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("👨‍💼 HR Analytics")

    st.markdown("---")

    selected = option_menu(
        menu_title=None,

        options=[
            "Dashboard",
            "Predict",
            "Analytics",
            "About"
        ],

        icons=[
            "speedometer2",
            "person-fill",
            "bar-chart-fill",
            "info-circle-fill"
        ],

        default_index=0,
    )

    st.markdown("---")

    st.caption("Employee Attrition Prediction")
    st.caption("Summer Internship Project")

# -----------------------------
# Routing
# -----------------------------

if selected == "Dashboard":

    from my_pages.dashboard import dashboard
    dashboard()

elif selected == "Predict":

    from my_pages.predict import predict
    predict()

elif selected == "Analytics":

    from my_pages.analytics import analytics
    analytics()

elif selected == "About":

    from my_pages.about import about
    about()