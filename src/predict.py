"""
Prediction Module

Loads the trained obesity prediction pipeline and performs
predictions on new user data.

Author: Your Name
"""

from pathlib import Path

import joblib
import pandas as pd

from src.config import (
    PIPELINE_FILE,
    TARGET_CLASSES,
)


class ObesityPredictor:
    """
    Prediction class for the Obesity Prediction System.
    """

    def __init__(self):

        self.pipeline = self.load_pipeline()

    # ==========================================================
    # Load Pipeline
    # ==========================================================

    @staticmethod
    def load_pipeline():
        """
        Load trained pipeline.
        """

        if not PIPELINE_FILE.exists():

            raise FileNotFoundError(

                f"Pipeline not found:\n{PIPELINE_FILE}"

            )

        return joblib.load(PIPELINE_FILE)

    # ==========================================================
    # Prepare Input
    # ==========================================================

    @staticmethod
    def prepare_input(user_data):

        """
        Convert dictionary into DataFrame.

        Parameters
        ----------
        user_data : dict

        Returns
        -------
        pd.DataFrame
        """

        if isinstance(user_data, pd.DataFrame):

            return user_data

        return pd.DataFrame([user_data])

    # ==========================================================
    # Predict
    # ==========================================================

    def predict(self, user_data):

        """
        Predict obesity level.

        Returns
        -------
        dict
        """

        input_df = self.prepare_input(user_data)

        prediction = self.pipeline.predict(input_df)[0]

        probabilities = self.pipeline.predict_proba(input_df)[0]

        confidence = probabilities.max()

        predicted_class = TARGET_CLASSES[prediction]

        return {

            "prediction": predicted_class,

            "confidence": float(confidence),

            "probabilities": {

                TARGET_CLASSES[i]: float(probabilities[i])

                for i in range(len(TARGET_CLASSES))

            }

        }

    # ==========================================================
    # Batch Prediction
    # ==========================================================

    def predict_batch(self, dataframe):

        """
        Predict multiple samples.

        Parameters
        ----------
        dataframe : pd.DataFrame

        Returns
        -------
        pd.DataFrame
        """

        predictions = self.pipeline.predict(dataframe)

        prediction_names = [

            TARGET_CLASSES[p]

            for p in predictions

        ]

        probabilities = self.pipeline.predict_proba(dataframe)

        confidence = probabilities.max(axis=1)

        results = dataframe.copy()

        results["Prediction"] = prediction_names

        results["Confidence"] = confidence

        return results


# ==============================================================
# Example Usage
# ==============================================================

if __name__ == "__main__":

    sample = {

        "Gender": "Male",

        "Age": 24,

        "Height": 1.78,

        "Weight": 80,

        "family_history_with_overweight": "yes",

        "FAVC": "yes",

        "FCVC": 2,

        "NCP": 3,

        "CAEC": "Sometimes",

        "SMOKE": "no",

        "CH2O": 2,

        "SCC": "no",

        "FAF": 2,

        "TUE": 1,

        "CALC": "Sometimes",

        "MTRANS": "Public_Transportation",

        "BMI": 80 / (1.78 ** 2),

    }

    predictor = ObesityPredictor()

    result = predictor.predict(sample)

    print("\nPrediction")

    print(result["prediction"])

    print("\nConfidence")

    print(f"{result['confidence']:.2%}")

    print("\nProbabilities")

    for label, prob in result["probabilities"].items():

        print(f"{label:<25} {prob:.3f}")