"""
Data Preprocessing Module

This module loads the raw obesity dataset, performs data validation,
cleans the data, engineers additional features, and creates train/test
datasets for model training.

Author: Your Name
"""

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from src.config import (
    RAW_DATA_PATH,
    PROCESSED_DATA_DIR,
    TARGET_COLUMN,
    TARGET_CLASSES,
    TEST_SIZE,
    RANDOM_STATE,
)

from src.utils import create_directories


class DataPreprocessor:
    """
    Handles loading, validation, cleaning and preparation
    of the obesity dataset.
    """

    def __init__(self):

        self.df = pd.DataFrame()

    # ==========================================================
    # Load Dataset
    # ==========================================================

    def load_data(self) -> None:

        print("\nLoading dataset...")

        if not RAW_DATA_PATH.exists():

            raise FileNotFoundError(
                f"Dataset not found:\n{RAW_DATA_PATH}"
            )

        self.df = pd.read_csv(RAW_DATA_PATH)

        print(f"Dataset Loaded Successfully")
        print(f"Shape : {self.df.shape}")

    # ==========================================================
    # Validate Dataset
    # ==========================================================

    def validate_dataset(self) -> None:

        print("\nValidating dataset...")

        if self.df.empty:

            raise ValueError("Dataset is empty.")

        if TARGET_COLUMN not in self.df.columns:

            raise ValueError(
                f"Target column '{TARGET_COLUMN}' not found."
            )

        if self.df.isnull().sum().sum() > 0:

            print("Missing values found.")

        else:

            print("No missing values found.")

        print("Validation Complete")

    # ==========================================================
    # Clean Dataset
    # ==========================================================

    def clean_data(self) -> None:

        print("\nCleaning dataset...")

        duplicate_rows = self.df.duplicated().sum()

        if duplicate_rows > 0:

            self.df.drop_duplicates(inplace=True)

            self.df.reset_index(drop=True, inplace=True)

            print(f"Removed {duplicate_rows} duplicate rows.")

        else:

            print("No duplicate rows found.")

    # ==========================================================
    # Feature Engineering
    # ==========================================================

    def feature_engineering(self) -> None:

        print("\nCreating BMI feature...")

        self.df["BMI"] = (
            self.df["Weight"] /
            (self.df["Height"] ** 2)
        )

        print("BMI Feature Added.")

    # ==========================================================
    # Target Encoding
    # ==========================================================

    def encode_target(self) -> None:

        print("\nEncoding target labels...")

        mapping = {

            label: index

            for index, label in enumerate(TARGET_CLASSES)

        }

        self.df[TARGET_COLUMN] = self.df[TARGET_COLUMN].map(mapping)

        if self.df[TARGET_COLUMN].isnull().sum() > 0:

            raise ValueError(
                "Unknown class detected in target column."
            )

        self.df[TARGET_COLUMN] = (
            self.df[TARGET_COLUMN].astype(int)
        )

    # ==========================================================
    # Train Test Split
    # ==========================================================

    def split_dataset(self):

        print("\nCreating Train/Test Split...")

        train_df, test_df = train_test_split(

            self.df,

            test_size=TEST_SIZE,

            random_state=RANDOM_STATE,

            stratify=self.df[TARGET_COLUMN]

        )

        print(f"Training Samples : {len(train_df)}")
        print(f"Testing Samples  : {len(test_df)}")

        return train_df, test_df

    # ==========================================================
    # Save Processed Dataset
    # ==========================================================

    def save_processed_data(

        self,

        train_df,

        test_df

    ) -> None:

        print("\nSaving processed dataset...")

        create_directories()

        train_df.to_csv(

            PROCESSED_DATA_DIR / "train.csv",

            index=False

        )

        test_df.to_csv(

            PROCESSED_DATA_DIR / "test.csv",

            index=False

        )

        print("Processed datasets saved successfully.")

    # ==========================================================
    # Pipeline
    # ==========================================================

    def preprocess(self):

        self.load_data()

        self.validate_dataset()

        self.clean_data()

        self.feature_engineering()

        self.encode_target()

        train_df, test_df = self.split_dataset()

        self.save_processed_data(

            train_df,

            test_df

        )

        print("\nPreprocessing Completed Successfully!")


# ==============================================================
# Main
# ==============================================================

if __name__ == "__main__":

    processor = DataPreprocessor()

    processor.preprocess()