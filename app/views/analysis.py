"""
Data Analysis Page
"""

import streamlit as st
import pandas as pd
import plotly.express as px

from src.config import RAW_DATA_PATH


@st.cache_data
def load_dataset():
    """
    Load the obesity dataset.
    """
    df = pd.read_csv(RAW_DATA_PATH)

    df["BMI"] = df["Weight"] / (df["Height"] ** 2)

    return df

def show_analysis():

    st.title("📊 Data Analysis")

    st.caption(
        "Exploratory analysis of the obesity dataset."
    )

    st.divider()

    df = load_dataset()

# dataset overview
    st.subheader("Dataset Overview")

    c1, c2, c3 = st.columns(3)

    c1.metric("Records", len(df))

    c2.metric("Features", df.shape[1])

    c3.metric("Missing Values", int(df.isna().sum().sum()))

    st.dataframe(

        df.head(10),

        use_container_width=True,

        hide_index=True,

    )

# target distribution
    st.divider()

    col1, col2 = st.columns(2)

# left
    with col1:

        st.subheader("Obesity Classes")

        fig = px.histogram(

            df,

            x="NObeyesdad",

            color="NObeyesdad",

        )

        fig.update_layout(

            showlegend=False,

            xaxis_title="",

            yaxis_title="Count",

        )

        st.plotly_chart(

            fig,

            use_container_width=True,

        )

# right
    with col2:

        st.subheader("Gender Distribution")

        gender = df["Gender"].value_counts().reset_index()

        gender.columns = ["Gender", "Count"]

        fig = px.pie(

            gender,

            names="Gender",

            values="Count",

            hole=0.45,

        )

        st.plotly_chart(

            fig,

            use_container_width=True,

        )

# Age % BMI
    st.divider()

    c1, c2 = st.columns(2)

# age
    with c1:

        st.subheader("Age Distribution")

        fig = px.histogram(

            df,

            x="Age",

            nbins=25,

        )

        st.plotly_chart(

            fig,

            use_container_width=True,

        )

# BMI
    with c2:

        st.subheader("BMI Distribution")

        fig = px.histogram(

            df,

            x="BMI",

            nbins=30,

        )

        st.plotly_chart(

            fig,

            use_container_width=True,

        )

# Correlation Heatmap
    st.divider()

    st.subheader("Correlation Heatmap")
    corr = df.select_dtypes("number").corr()
    fig = px.imshow(

        corr,

        text_auto=".2f",

        color_continuous_scale="RdBu_r",

        aspect="auto",

    )

    st.plotly_chart(

        fig,

        use_container_width=True,

    )

# numerical summary
    st.divider()

    st.subheader("Numerical Summary")

    st.dataframe(

        df.describe(),

        use_container_width=True,

    )     