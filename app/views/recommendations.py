"""
Recommendations Page
"""

import streamlit as st


RECOMMENDATIONS = {

    "Insufficient_Weight": {

        "risk": "🟡 Low Body Weight",

        "diet": [
            "Increase calorie intake using nutrient-rich foods.",
            "Consume more lean proteins and healthy fats.",
            "Eat 5–6 small meals throughout the day."
        ],

        "exercise": [
            "Light strength training.",
            "Avoid excessive cardio.",
            "Focus on muscle gain."
        ],

        "water": "2–2.5 litres/day",

        "advice": "Consult a dietitian if underweight for a prolonged period."

    },

    "Normal_Weight": {

        "risk": "🟢 Healthy",

        "diet": [
            "Maintain a balanced diet.",
            "Eat fruits and vegetables daily.",
            "Limit processed foods."
        ],

        "exercise": [
            "150 minutes of moderate exercise/week.",
            "Strength training twice a week."
        ],

        "water": "2–3 litres/day",

        "advice": "Maintain your current healthy lifestyle."

    },

    "Overweight_Level_I": {

        "risk": "🟠 Moderate Risk",

        "diet": [
            "Reduce sugar intake.",
            "Increase fibre consumption.",
            "Control portion sizes."
        ],

        "exercise": [
            "30–45 minutes walking daily.",
            "Cardio + resistance training."
        ],

        "water": "2.5–3 litres/day",

        "advice": "Monitor weight regularly."

    },

    "Overweight_Level_II": {

        "risk": "🟠 Moderate Risk",

        "diet": [
            "Avoid sugary drinks.",
            "Reduce processed food.",
            "Increase vegetables."
        ],

        "exercise": [
            "45 minutes cardio.",
            "Strength training."
        ],

        "water": "2.5–3 litres/day",

        "advice": "Consult a nutrition professional."

    },

    "Obesity_Type_I": {

        "risk": "🔴 High Risk",

        "diet": [
            "Follow a calorie-controlled diet.",
            "Increase vegetables.",
            "Reduce saturated fat."
        ],

        "exercise": [
            "Daily walking.",
            "Low-impact cardio."
        ],

        "water": "3 litres/day",

        "advice": "Medical supervision is recommended."

    },

    "Obesity_Type_II": {

        "risk": "🔴 High Risk",

        "diet": [
            "Strict dietary monitoring.",
            "Reduce refined carbohydrates.",
            "Increase protein intake."
        ],

        "exercise": [
            "Physician-approved exercise plan."
        ],

        "water": "3 litres/day",

        "advice": "Seek professional healthcare guidance."

    },

    "Obesity_Type_III": {

        "risk": "🚨 Severe Risk",

        "diet": [
            "Immediate medical nutrition therapy.",
            "Avoid processed foods completely."
        ],

        "exercise": [
            "Exercise only under medical supervision."
        ],

        "water": "As advised by your physician.",

        "advice": "Consult a healthcare professional immediately."

    }

}

# main function
def show_recommendations():

    st.title("🥗 Health Recommendations")

    st.caption(
        "General lifestyle guidance for each obesity category."
    )

    st.divider()

    category = st.selectbox(

        "Select Obesity Category",

        list(RECOMMENDATIONS.keys())

    )

    recommendation = RECOMMENDATIONS[category]

# risk level
    st.subheader("🚦Risk Level")  

    st.info(recommendation["risk"])

# three columns
    col1, col2, col3 = st.columns(3)
    # diet
    with col1:
        st.subheader("🥗 Diet")
        for item in recommendation["diet"]:
            st.write(f"- {item}")
    # exercise
    with col2:
        st.subheader("🏃 Exercise")
        for item in recommendation["exercise"]:
            st.write(f"- {item}")
    # water
    with col3:

        st.subheader("💧 Water Intake")

        st.success(recommendation["water"])

    # advice
    st.divider()

    st.subheader("🩺 General Advice")

    st.warning(recommendation["advice"])

    # desclaimer
    st.divider()

    st.caption(
        """
        **Disclaimer**

        These recommendations are intended for educational purposes only
        and should not replace professional medical advice, diagnosis,
        or treatment. Always consult a qualified healthcare professional
        for personalized guidance.
        """
    )
