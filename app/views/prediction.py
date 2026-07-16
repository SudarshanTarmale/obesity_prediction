"""
Prediction Page
"""

import streamlit as st
import pandas as pd
import plotly.express as px

from src.predict import ObesityPredictor


@st.cache_resource
def load_predictor():
    """
    Load trained ML pipeline only once.
    """
    return ObesityPredictor()

def show_prediction():

    predictor = load_predictor()

    st.title("🔮 Obesity Prediction")

    st.caption(
        "Predict obesity level using eating habits and physical condition."
    )

    st.divider()
    
    left, right = st.columns([1.2, 1])
    with left:

        st.subheader("👤 Personal Information")

        gender = st.selectbox(
            "Gender",
            ["select","Male", "Female"]
        )

        age = st.number_input(
            "Age",
            1,
            100,
            25
        )

        height = st.number_input(
            "Height (m)",
            1.00,
            2.50,
            1.70,
            step=0.01
        )

        weight = st.number_input(
            "Weight (kg)",
            20.0,
            250.0,
            70.0
        )

        bmi = weight / (height ** 2)

        st.info(
            f"### BMI : {bmi:.2f}"
        )

        st.divider()

        st.subheader("🍎 Lifestyle")

        # lifestyle inputs
        family_history = st.selectbox(
            "Family History with Overweight",
            ["no", "yes"]
        )

        favc = st.selectbox(
            "Frequent High Calorie Food",
            ["yes", "no"]
        )

        fcvc = st.slider(
            "Vegetable Consumption",
            1,
            3,
            2
        )

        ncp = st.slider(
            "Main Meals",
            1,
            4,
            3
        )

        caec = st.selectbox(
            "Food Between Meals",
            [
                "no",
                "Sometimes",
                "Frequently",
                "Always"
            ]
        )

        smoke = st.selectbox(
            "Smoking",
            ["no", "yes"]
        )

        ch2o = st.slider(
            "Water Intake (Liters)",
            1.0,
            3.0,
            2.0
        )

        scc = st.selectbox(
            "Calories Monitoring",
            ["yes", "no"]
        )

        faf = st.slider(
            "Physical Activity",
            0.0,
            3.0,
            1.0
        )

        tue = st.slider(
            "Technology Usage",
            0.0,
            2.0,
            1.0
        )

        calc = st.selectbox(
            "Alcohol Consumption",
            [
                "no",
                "Sometimes",
                "Frequently",
                "Always"
            ]
        )

        mtrans = st.selectbox(
            "Transportation",
            [
                "Walking",
                "Bike",
                "Motorbike",
                "Public_Transportation",
                "Automobile"
            ]
        )
        # predict button
        predict = st.button(
            "🔍 Predict",
            use_container_width=True
        )
        if predict:

            input_data = {

                "Gender": gender,

                "Age": age,

                "Height": height,

                "Weight": weight,

                "family_history_with_overweight": family_history,

                "FAVC": favc,

                "FCVC": fcvc,

                "NCP": ncp,

                "CAEC": caec,

                "SMOKE": smoke,

                "CH2O": ch2o,

                "SCC": scc,

                "FAF": faf,

                "TUE": tue,

                "CALC": calc,

                "MTRANS": mtrans,

                "BMI": bmi,

            }

            result = predictor.predict(input_data)
        
    # right panel
    with right:
        if not predict:

            st.info(
                    "👈 Fill in the information and click **Predict** to view the results."
            )
        else:

            st.subheader("🏆 Prediction Result")

            prediction = result["prediction"]

            confidence = result["confidence"]

            probabilities = result["probabilities"]

            # ------------------------------------------------------
            # Prediction Card
            # ------------------------------------------------------

            if "Normal" in prediction:

                st.success(f"### {prediction.replace('_', ' ')}")

            elif "Overweight" in prediction:

                st.warning(f"### {prediction.replace('_', ' ')}")

            else:

                st.error(f"### {prediction.replace('_', ' ')}")

            # metrics    
            c1, c2 = st.columns(2)

            with c1:

                st.metric(
                    "Confidence",
                    f"{confidence:.2%}"
                )

            with c2:

                st.metric(
                    "BMI",
                    f"{bmi:.2f}"
                )

            # probability chart
            st.divider()

            st.subheader("📊 Prediction Probabilities")

            probability_df = pd.DataFrame({

                "Category": list(probabilities.keys()),

                "Probability": list(probabilities.values())

            })

            probability_df["Probability"] *= 100

            fig = px.bar(

                probability_df,

                x="Probability",

                y="Category",

                orientation="h",

                text="Probability",

                color="Probability",

                color_continuous_scale="Blues"

            )

            fig.update_traces(

                texttemplate="%{text:.1f}%",

                textposition="outside"

            )

            fig.update_layout(

                height=420,

                coloraxis_showscale=False,

                xaxis_title="Probability (%)",

                yaxis_title="",

                margin=dict(

                    l=10,

                    r=10,

                    t=20,

                    b=20

                )

            )

            st.plotly_chart(

                fig,

                use_container_width=True

            )
            #risk level
            st.divider()

            st.subheader("🚦 Risk Level")

            if "Insufficient" in prediction:

                st.warning(
                    "Low Body Weight"
                )

            elif "Normal" in prediction:

                st.success(
                    "Healthy Weight"
                )

            elif "Overweight" in prediction:

                st.warning(
                    "Moderate Risk"
                )

            else:

                st.error(
                    "High Risk"
                )

            # quick recommendation
            st.divider()

            st.subheader("💡 Quick Recommendation")

            if "Normal" in prediction:

                st.success(
                    """
                    Continue maintaining a healthy diet,
                    regular physical activity and
                    good hydration.
                    """
                )

            elif "Overweight" in prediction:

                st.warning(
                    """
                    Increase physical activity,
                    reduce processed food,
                    and monitor calorie intake.
                    """
                )

            elif "Insufficient" in prediction:

                st.info(
                    """
                    Improve nutritional intake,
                    eat balanced meals,
                    and consult a nutritionist if necessary.
                    """
                )

            else:

                st.error(
                    """
                    Medical consultation is recommended.
                    Combine dietary changes,
                    exercise and professional guidance.
                    """
                )