"""
Home Page
"""

import streamlit as st


def show_home():

    st.title("🏥 Obesity Prediction System")

    st.markdown("---")

    st.write(

        """
        Welcome to the **Obesity Prediction System**.

        This application predicts obesity levels based on
        eating habits and physical condition using
        Machine Learning.
        """
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(

        "Dataset",

        "2,111 Samples",

    )

    col2.metric(

        "Features",

        "17",

    )

    col3.metric(

        "Target Classes",

        "7",

    )

    st.markdown("---")

    st.subheader("Workflow")

    st.image(

        "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/scikitlearn.svg",

        width=80,

    )

    st.markdown(

        """
        Dataset

        ➜ Preprocessing

        ➜ Machine Learning

        ➜ Prediction

        ➜ Recommendation
        """
    )