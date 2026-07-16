"""
Model Performance Page
"""

import streamlit as st
import pandas as pd
import plotly.express as px

from src.config import (
    MODEL_METRICS_FILE,
    CLASSIFICATION_REPORT_FILE,
    FEATURE_IMPORTANCE_FILE,
)

@st.cache_data
def load_reports():

    metrics = pd.read_csv(MODEL_METRICS_FILE)

    report = pd.read_csv(CLASSIFICATION_REPORT_FILE)

    importance = pd.read_csv(FEATURE_IMPORTANCE_FILE)

    return metrics, report, importance

def show_performance():

    st.title("📈 Model Performance")

    st.caption(
        "Comparison of all trained machine learning models."
    )

    st.divider()

    metrics, report, importance = load_reports()

    # best model card
    best = metrics.sort_values(

        by="Cross Validation",

        ascending=False

    ).iloc[0]

    st.success(

        f"""
        🏆 Best Model

        **{best['Model']}**

        Validation Accuracy:
        **{best['Cross Validation']:.2%}**
        """
    )

    # model comparison model
    st.subheader("📋 Model Comparison")

    st.dataframe(
        report.style.format(
            {
                "precision": "{:.2f}",
                "recall": "{:.2f}",
                "f1-score": "{:.2f}",
                "support": "{:.0f}",
            }
        ),

        use_container_width=True,
        hide_index=True,
    )

    # accuracy chart
    st.divider()

    st.subheader("📊 Cross Validation Accuracy")

    fig = px.bar(

        metrics,

        x="Model",

        y="Cross Validation",

        text="Cross Validation",

        color="Cross Validation",

        color_continuous_scale="Blues",

    )

    fig.update_traces(

        texttemplate="%{text:.2%}",

        textposition="outside"

    )

    fig.update_layout(

        height=450,

        coloraxis_showscale=False,

        yaxis_tickformat=".0%"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )   

    # feature importance
    st.divider()

    st.subheader("⭐ Top Feature Importance")

    top_features = importance.head(15)

    fig = px.bar(

        top_features,

        x="Importance",

        y="Feature",

        orientation="h",

        color="Importance",

        color_continuous_scale="Viridis"

    )

    fig.update_layout(

        height=600,

        coloraxis_showscale=False

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # classification report
    st.divider()

    st.subheader("📑 Classification Report")

    st.dataframe(

        report,

        use_container_width=True,

        hide_index=True

    )

    # summary
    st.divider()

    st.subheader("📝 Summary")

    st.info(

        f"""
        • Total Models Trained: **{len(metrics)}**

        • Best Performing Model: **{best['Model']}**

        • Cross Validation Accuracy:
        **{best['Cross Validation']:.2%}**

        • This model has been saved as
        **obesity_pipeline.pkl**
        """
    )