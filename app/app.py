"""
Main Streamlit Application

Author: Sudarshan Tarmale
"""

import streamlit as st
from streamlit_option_menu import option_menu

from pages.home import show_home
from pages.analysis import show_analysis
from pages.performance import show_performance
from pages.prediction import show_prediction
from pages.recommendation import show_recommendations


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(

    page_title="Obesity Prediction",

    page_icon="🏥",

    layout="wide",

    initial_sidebar_state="expanded",

)

# ============================================================
# Load CSS
# ============================================================

with open("app/assets/styles.css") as f:

    st.markdown(

        f"<style>{f.read()}</style>",

        unsafe_allow_html=True,

    )

# ============================================================
# Sidebar
# ============================================================
with st.sidebar:

    selected = option_menu(
        menu_title="Obesity Prediction",
        options=[
            "Home",
            "Prediction",
            "Model Performance",
            "Data Analysis",
            "Recommendations",
        ],
        icons=[
            "house-fill",
            "magic",
            "graph-up-arrow",
            "bar-chart-fill",
            "clipboard-check",
        ],
        menu_icon="activity",
        default_index=0,
        styles={
            "container": {
                "padding": "5!important",
                "background-color": "#2C2F32",
            },
            "icon": {
                "color": "#2563EB",
                "font-size": "18px",
            },
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "5px",
                "--hover-color": "#6990D4",
                "border-radius": "8px",
            },
            "nav-link-selected": {
                "background-color": "#2563EB",
                "color": "white",
            },
        },
    )

st.sidebar.markdown("---")

st.sidebar.info(

    "Machine Learning Based Obesity Prediction"

)

# ============================================================
# Routing
# ============================================================

if selected == "Home":

    show_home()

elif selected == "Prediction":

    show_prediction()

elif selected == "Model Performance":

    show_performance()

elif selected == "Data Analysis":

    show_analysis()

elif selected == "Recommendations":

    show_recommendations()