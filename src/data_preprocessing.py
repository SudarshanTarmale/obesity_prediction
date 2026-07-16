"""
Data Preprocessing Pipeline

Author: Your Name
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from src.config import *
from src.utils import save_object


class DataPreprocessor:

    def __init__(self):

        self.df = None

        self.label_encoders = {}

        self.target_encoder = LabelEncoder()

        self.scaler = StandardScaler()

    # -----------------------------------------------------

    def load_data(self):

        print("Loading dataset...")

        self.df = pd.read_csv(RAW_DATA)

        print(f"Dataset Shape : {self.df.shape}")

    # -----------------------------------------------------

    def clean_data(self):

        print("Cleaning dataset...")

        self.df.drop_duplicates(inplace=True)

        self.df.reset_index(drop=True, inplace=True)

    # -----------------------------------------------------

    def feature_engineering(self):

        print("Creating BMI feature...")

        self.df["BMI"] = self.df["Weight"] / (
            self.df["Height"] ** 2
        )

    # -----------------------------------------------------

    def encode_features(self):

        categorical_columns = [

            "Gender",

            "family_history_with_overweight",

            "FAVC",

            "CAEC",

            "SMOKE",

            "SCC",

            "CALC",

            "MTRANS"

        ]

        for column in categorical_columns:

            encoder = LabelEncoder()

            self.df[column] = encoder.fit_transform(
                self.df[column]
            )

            self.label_encoders[column] = encoder

        self.df["NObeyesdad"] = self.target_encoder.fit_transform(
            self.df["NObeyesdad"]
        )

    # -----------------------------------------------------

    def split_data(self):

        X = self.df.drop("NObeyesdad", axis=1)

        y = self.df["NObeyesdad"]

        return train_test_split(

            X,

            y,

            test_size=TEST_SIZE,

            random_state=RANDOM_STATE,

            stratify=y

        )

    # -----------------------------------------------------

    def scale_data(self, X_train, X_test):

        numerical_columns = [

            "Age",

            "Height",

            "Weight",

            "FCVC",

            "NCP",

            "CH2O",

            "FAF",

            "TUE",

            "BMI"

        ]

        X_train[numerical_columns] = self.scaler.fit_transform(
            X_train[numerical_columns]
        )

        X_test[numerical_columns] = self.scaler.transform(
            X_test[numerical_columns]
        )

        return X_train, X_test

    # -----------------------------------------------------

    def save_processed_data(

        self,

        X_train,

        X_test,

        y_train,

        y_test

    ):

        PROCESSED_DATA_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        X_train.to_csv(
            PROCESSED_DATA_DIR / "X_train.csv",
            index=False
        )

        X_test.to_csv(
            PROCESSED_DATA_DIR / "X_test.csv",
            index=False
        )

        y_train.to_csv(
            PROCESSED_DATA_DIR / "y_train.csv",
            index=False
        )

        y_test.to_csv(
            PROCESSED_DATA_DIR / "y_test.csv",
            index=False
        )

        save_object(
            self.scaler,
            SCALER_FILE
        )

        save_object(
            self.label_encoders,
            LABEL_ENCODERS_FILE
        )

        save_object(
            self.target_encoder,
            TARGET_ENCODER_FILE
        )

    # -----------------------------------------------------

    def preprocess(self):

        self.load_data()

        self.clean_data()

        self.feature_engineering()

        self.encode_features()

        X_train, X_test, y_train, y_test = self.split_data()

        X_train, X_test = self.scale_data(

            X_train,

            X_test

        )

        self.save_processed_data(

            X_train,

            X_test,

            y_train,

            y_test

        )

        print("\nPreprocessing Completed Successfully!")


if __name__ == "__main__":

    processor = DataPreprocessor()

    processor.preprocess()