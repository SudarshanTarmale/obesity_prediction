"""
Train multiple machine learning models and automatically
save the best performing model.

Author: Your Name
"""

import warnings
warnings.filterwarnings("ignore")

import joblib
import pandas as pd

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

from xgboost import XGBClassifier

from src.config import *

# ----------------------------------------------------------


class ModelTrainer:

    def __init__(self):

        self.models = {

            "Logistic Regression":

                LogisticRegression(max_iter=1000),

            "Decision Tree":

                DecisionTreeClassifier(
                    random_state=RANDOM_STATE
                ),

            "Random Forest":

                RandomForestClassifier(

                    random_state=RANDOM_STATE,

                    n_estimators=300

                ),

            "XGBoost":

                XGBClassifier(

                    random_state=RANDOM_STATE,

                    eval_metric="mlogloss"

                )

        }

        self.results = []

    # ------------------------------------------------------

    def load_data(self):

        X_train = pd.read_csv(
            PROCESSED_DATA_DIR / "X_train.csv"
        )

        X_test = pd.read_csv(
            PROCESSED_DATA_DIR / "X_test.csv"
        )

        y_train = pd.read_csv(
            PROCESSED_DATA_DIR / "y_train.csv"
        ).values.ravel()

        y_test = pd.read_csv(
            PROCESSED_DATA_DIR / "y_test.csv"
        ).values.ravel()

        return X_train, X_test, y_train, y_test

    # ------------------------------------------------------

    def evaluate(

        self,

        name,

        model,

        X_test,

        y_test

    ):

        prediction = model.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            prediction
        )

        precision = precision_score(

            y_test,

            prediction,

            average="weighted"

        )

        recall = recall_score(

            y_test,

            prediction,

            average="weighted"

        )

        f1 = f1_score(

            y_test,

            prediction,

            average="weighted"

        )

        self.results.append({

            "Model": name,

            "Accuracy": round(accuracy, 4),

            "Precision": round(precision, 4),

            "Recall": round(recall, 4),

            "F1 Score": round(f1, 4)

        })

        return accuracy

    # ------------------------------------------------------

    def train(self):

        X_train, X_test, y_train, y_test = self.load_data()

        best_model = None

        best_accuracy = 0

        best_name = ""

        for name, model in self.models.items():

            print(f"\nTraining {name}...")

            model.fit(

                X_train,

                y_train

            )

            accuracy = self.evaluate(

                name,

                model,

                X_test,

                y_test

            )

            if accuracy > best_accuracy:

                best_accuracy = accuracy

                best_model = model

                best_name = name

        print("\nBest Model :", best_name)

        print("Accuracy :", round(best_accuracy, 4))

        joblib.dump(

            best_model,

            MODEL_FILE

        )

        metrics = pd.DataFrame(

            self.results

        )

        metrics.to_csv(

            MODEL_METRICS,

            index=False

        )

        if hasattr(

            best_model,

            "feature_importances_"

        ):

            importance = pd.DataFrame({

                "Feature":

                    X_train.columns,

                "Importance":

                    best_model.feature_importances_

            })

            importance.sort_values(

                by="Importance",

                ascending=False,

                inplace=True

            )

            importance.to_csv(

                FEATURE_IMPORTANCE,

                index=False

            )

        print("\nTraining Completed Successfully")


# ----------------------------------------------------------

if __name__ == "__main__":

    trainer = ModelTrainer()

    trainer.train()