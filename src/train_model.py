"""
Model Training Module

Builds preprocessing pipelines, trains multiple machine learning
models, compares their performance using cross-validation,
and prepares the best pipeline for deployment.

Author: Sudarshan Tarmale
"""

from pathlib import Path

import warnings
warnings.filterwarnings("ignore")

import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from sklearn.impute import SimpleImputer

from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler,
)

from sklearn.model_selection import (
    StratifiedKFold,
    cross_val_score,
)

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier

from src.config import (

    PROCESSED_DATA_DIR,

    TARGET_COLUMN,

    NUMERICAL_FEATURES,

    CATEGORICAL_FEATURES,

    RANDOM_STATE,

    CV_FOLDS,

    MODEL_METRICS_FILE,

    FEATURE_IMPORTANCE_FILE,

    PIPELINE_FILE,
)

from src.utils import create_directories

from src.evaluator import ModelEvaluator


class ModelTrainer:
    """
    Train, compare and evaluate multiple ML models.
    """

    def __init__(self):

        create_directories()

        self.train_df = pd.read_csv(
            PROCESSED_DATA_DIR / "train.csv"
        )

        self.test_df = pd.read_csv(
            PROCESSED_DATA_DIR / "test.csv"
        )

        self.results = []

        self.best_pipeline = None

        self.best_score = 0.0

        self.best_model_name = ""

    # ======================================================
    # Feature Split
    # ======================================================

    def split_features(self):

        X_train = self.train_df.drop(
            columns=[TARGET_COLUMN]
        )

        y_train = self.train_df[TARGET_COLUMN]

        X_test = self.test_df.drop(
            columns=[TARGET_COLUMN]
        )

        y_test = self.test_df[TARGET_COLUMN]

        return (

            X_train,

            X_test,

            y_train,

            y_test,

        )

    # ======================================================
    # Build Preprocessor
    # ======================================================

    @staticmethod
    def build_preprocessor():

        numeric_pipeline = Pipeline(

            steps=[

                (

                    "imputer",

                    SimpleImputer(

                        strategy="median"

                    )

                ),

                (

                    "scaler",

                    StandardScaler()

                ),

            ]

        )

        categorical_pipeline = Pipeline(

            steps=[

                (

                    "imputer",

                    SimpleImputer(

                        strategy="most_frequent"

                    )

                ),

                (

                    "encoder",

                    OneHotEncoder(

                        handle_unknown="ignore"

                    )

                ),

            ]

        )

        preprocessor = ColumnTransformer(

            transformers=[

                (

                    "numerical",

                    numeric_pipeline,

                    NUMERICAL_FEATURES,

                ),

                (

                    "categorical",

                    categorical_pipeline,

                    CATEGORICAL_FEATURES,

                ),

            ]

        )

        return preprocessor

    # ======================================================
    # Model Registry
    # ======================================================

    @staticmethod
    def get_models():

        return {

            "Logistic Regression":

                LogisticRegression(

                    max_iter=1000,

                    random_state=RANDOM_STATE,

                ),

            "Decision Tree":

                DecisionTreeClassifier(

                    random_state=RANDOM_STATE,

                ),

            "Random Forest":

                RandomForestClassifier(

                    n_estimators=300,

                    random_state=RANDOM_STATE,

                ),

            "XGBoost":

                XGBClassifier(

                    random_state=RANDOM_STATE,

                    eval_metric="mlogloss",

                ),

        }

    # ======================================================
    # Build Pipeline
    # ======================================================

    @staticmethod
    def build_pipeline(

        preprocessor,

        classifier,

    ):

        return Pipeline(

            steps=[

                (

                    "preprocessor",

                    preprocessor,

                ),

                (

                    "classifier",

                    classifier,

                ),

            ]

        )

    # ======================================================
    # Cross Validation
    # ======================================================

    @staticmethod
    def cross_validate(

        pipeline,

        X_train,

        y_train,

    ):

        cv = StratifiedKFold(

            n_splits=CV_FOLDS,

            shuffle=True,

            random_state=RANDOM_STATE,

        )

        scores = cross_val_score(

            pipeline,

            X_train,

            y_train,

            cv=cv,

            scoring="accuracy",

            n_jobs=-1,

        )

        return scores.mean()

    # ======================================================
    # Train All Models
    # ======================================================

    def train_models(self):

        X_train, X_test, y_train, y_test = (

            self.split_features()

        )

        preprocessor = self.build_preprocessor()

        models = self.get_models()

        for model_name, classifier in models.items():

            print(f"\nTraining {model_name}...")

            pipeline = self.build_pipeline(

                preprocessor,

                classifier,

            )

            cv_accuracy = self.cross_validate(

                pipeline,

                X_train,

                y_train,

            )

            pipeline.fit(

                X_train,

                y_train,

            )

            print(

                f"Cross Validation Accuracy : "

                f"{cv_accuracy:.4f}"

            )

            if cv_accuracy > self.best_score:

                self.best_score = cv_accuracy

                self.best_pipeline = pipeline

                self.best_model_name = model_name

    # ======================================================
    # Evaluate Models
    # ======================================================

    def evaluate_models(self):

        X_train, X_test, y_train, y_test = self.split_features()

        preprocessor = self.build_preprocessor()

        models = self.get_models()

        self.results = []

        for model_name, classifier in models.items():

            print(f"\nEvaluating {model_name}...")

            pipeline = self.build_pipeline(

                preprocessor,

                classifier,

            )

            pipeline.fit(

                X_train,

                y_train,

            )

            metrics = ModelEvaluator.evaluate(

                pipeline,

                X_test,

                y_test,

            )

            metrics["Model"] = model_name

            metrics["Cross Validation"] = self.cross_validate(

                pipeline,

                X_train,

                y_train,

            )

            self.results.append(metrics)

            if model_name == self.best_model_name:

                ModelEvaluator.save_classification_report(

                    pipeline,

                    X_test,

                    y_test,

                )

                importance = (

                    ModelEvaluator.get_feature_importance(

                        pipeline,

                    )

                )

                if importance is not None:

                    importance.to_csv(

                        FEATURE_IMPORTANCE_FILE,

                        index=False,

                    )



                        # ======================================================
    # Save Metrics
    # ======================================================

    def save_metrics(self):

        metrics_df = pd.DataFrame(

            self.results

        )

        metrics_df = metrics_df[

            [

                "Model",

                "Accuracy",

                "Precision",

                "Recall",

                "F1 Score",

                "Cross Validation",

            ]

        ]

        metrics_df.sort_values(

            by="Cross Validation",

            ascending=False,

            inplace=True,

        )

        metrics_df.to_csv(

            MODEL_METRICS_FILE,

            index=False,

        )

        print("\nModel metrics saved.")





            # ======================================================
    # Save Best Pipeline
    # ======================================================

    def save_pipeline(self):

        joblib.dump(

            self.best_pipeline,

            PIPELINE_FILE,

        )

        print(

            f"\nBest Model : {self.best_model_name}"

        )

        print(

            f"Cross Validation : "

            f"{self.best_score:.4f}"

        )

        print(

            "\nPipeline saved successfully."

        )




            # ======================================================
    # Execute
    # ======================================================

    def run(self):

        print("=" * 60)

        print("Training Machine Learning Models")

        print("=" * 60)

        self.train_models()

        self.evaluate_models()

        self.save_metrics()

        self.save_pipeline()

        print("\nTraining Completed Successfully!")




        # ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    trainer = ModelTrainer()

    trainer.run()