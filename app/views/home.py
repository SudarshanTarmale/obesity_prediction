"""
Home Page
"""

import streamlit as st


def show_home():

    # ==========================================================
    # Header
    # ==========================================================

    st.title("🏥 Obesity Prediction Dashboard")

    st.caption(
        "Estimate obesity levels using Machine Learning"
    )

    st.divider()

    # ==========================================================
    # KPI Cards
    # ==========================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Dataset",
            "2,111",
            "Samples"
        )

    with col2:
        st.metric(
            "Features",
            "17"
        )

    with col3:
        st.metric(
            "Target Classes",
            "7"
        )

    with col4:
        st.metric(
            "Models",
            "4"
        )

    st.divider()

    # ==========================================================
    # About + Dataset
    # ==========================================================

    st.subheader("📖 About the Project")

    st.write(
        """
        The **Obesity Prediction System** is an end-to-end machine learning
        application that estimates an individual's obesity category based on
        eating habits, lifestyle, and physical condition.

        The project is built using the **UCI Obesity Dataset** and demonstrates
        a complete machine learning workflow including data preprocessing,
        feature engineering, model comparison, prediction, and interactive
        visualization through a Streamlit dashboard.
        """
    )

    st.divider()

    st.subheader("✨ Project Highlights")

    with st.container(border=True):
        st.markdown("""
                    
            - ✅ **BMI Feature Engineering**
                - Automatically calculates Body Mass Index from height and weight.

            - ✅ **Scikit-Learn Pipeline**
                - End-to-end preprocessing and prediction using a reusable pipeline.

            - ✅ **4 Machine Learning Models**
                - Logistic Regression, Decision Tree, Random Forest, and XGBoost.

            - ✅ **5-Fold Cross Validation**
                - Robust evaluation using Stratified K-Fold.

            - ✅ **Interactive Dashboard**
                - Streamlit application with visual analytics and prediction.

            - ✅ **Personalized Health Insights**
                - Provides obesity prediction, confidence score, and recommendations.
        """)
    

    # ==========================================================
    # Technology Stack
    # ==========================================================

    st.subheader("⚙ Technology Stack")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.success("Python")

    with c2:
        st.success("Scikit-Learn")

    with c3:
        st.success("XGBoost")

    with c4:
        st.success("Streamlit")

    st.divider()

    # ==========================================================
    # Workflow
    # ==========================================================


    st.subheader("🧠 Machine Learning Workflow")

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        with st.container(border=True):
            st.markdown(
                """
                <div style="text-align:center">
                    <h1>📂</h1>
                    <h4>Dataset</h4>
                    <p>Load the UCI Obesity Dataset</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with c2:
        with st.container(border=True):
            st.markdown(
                """
                <div style="text-align:center">
                    <h1>🧹</h1>
                    <h4>Preprocessing</h4>
                    <p>Cleaning, Validation & BMI Feature</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with c3:
        with st.container(border=True):
            st.markdown(
                """
                <div style="text-align:center">
                    <h1>🤖</h1>
                    <h4>ML Models</h4>
                    <p>Train & Compare 4 Algorithms</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with c4:
        with st.container(border=True):
            st.markdown(
                """
                <div style="text-align:center">
                    <h1>❤️</h1>
                    <h4>Prediction</h4>
                    <p>Predict Obesity Level</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with c5:
        with st.container(border=True):
            st.markdown(
                """
                <div style="text-align:center">
                    <h1>🥗</h1>
                    <h4>Recommendation</h4>
                    <p>Health Insights & Guidance</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.divider()

    # ==========================================================
    # Target Classes
    # ==========================================================

    st.subheader("🎯 Obesity Categories")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        - Insufficient Weight
        - Normal Weight
        - Overweight Level I
        - Overweight Level II
        """)

    with col2:

        st.markdown("""
        - Obesity Type I
        - Obesity Type II
        - Obesity Type III
        """)

    st.divider()

    # ==========================================================
    # Footer
    # ==========================================================

    st.caption(
        "Developed using Streamlit • Scikit-Learn • XGBoost"
    )