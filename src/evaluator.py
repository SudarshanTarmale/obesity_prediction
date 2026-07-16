"""
Model Evaluation Module

Evaluates trained machine learning models and saves
performance reports.
"""

from pathlib import Path

import pandas as pd

from sklearn import pipeline
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

from src.config import (
    REPORTS_DIR,
    CLASSIFICATION_REPORT_FILE,
    TARGET_CLASSES,
)

from src.utils import create_directories


class ModelEvaluator:
    
    """
    Utility class for evaluating classification models.
    """
    
    @staticmethod
    def evaluate(model, X_test, y_test):
        """
        Evaluate a trained model.

        Parameters
        ----------
        model : sklearn Pipeline
        X_test : pd.DataFrame
        y_test : pd.Series

        Returns
        -------
        dict
            Evaluation metrics.
        """

        predictions = model.predict(X_test)

        metrics = {

            "Accuracy": accuracy_score(
                y_test,
                predictions
            ),

            "Precision": precision_score(
                y_test,
                predictions,
                average="weighted",
                zero_division=0,
            ),

            "Recall": recall_score(
                y_test,
                predictions,
                average="weighted",
                zero_division=0,
            ),

            "F1 Score": f1_score(
                y_test,
                predictions,
                average="weighted",
                zero_division=0,
            ),

        }

        return metrics
    
    @staticmethod
    def save_classification_report(
        model,
        X_test,
        y_test,
    ):
        """
        Save classification report.
        """

        predictions = model.predict(X_test)

        report = classification_report(

            y_test,

            predictions,

            target_names=TARGET_CLASSES,

            output_dict=True,

            zero_division=0,

        )

        create_directories()

        pd.DataFrame(report).transpose().to_csv(

            CLASSIFICATION_REPORT_FILE,

            index=True,

        )

    @staticmethod
    def get_confusion_matrix(
        model,
        X_test,
        y_test,
    ):
        """
        Return confusion matrix.
        """

        predictions = model.predict(X_test)

        return confusion_matrix(
            y_test,
            predictions,
        )
    
    @staticmethod
    def get_feature_importance(pipeline):
        """
        Return feature importance if supported.
        """

        classifier = pipeline.named_steps["classifier"]

        if not hasattr(classifier, "feature_importances_"):
            return None

        preprocessor = pipeline.named_steps["preprocessor"]

        feature_names = preprocessor.get_feature_names_out()

        importance = pd.DataFrame({

        "Feature": feature_names,

        "Importance": classifier.feature_importances_,

        })

        importance.sort_values(

        by="Importance",

        ascending=False,

        inplace=True,

        )

        return importance