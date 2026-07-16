"""
Utility Functions

Common helper functions used throughout the project.
"""

from pathlib import Path
import joblib


def create_directories() -> None:
    """
    Create all required project directories if they don't exist.
    """

    from src.config import (

        MODEL_DIR,

        REPORTS_DIR,

        PLOTS_DIR,

        PROCESSED_DATA_DIR,

    )

    directories = [

        MODEL_DIR,

        REPORTS_DIR,

        PLOTS_DIR,

        PROCESSED_DATA_DIR,

    ]

    for directory in directories:

        Path(directory).mkdir(

            parents=True,

            exist_ok=True

        )


def save_object(obj, filepath: Path) -> None:
    """
    Save any Python object using Joblib.
    """

    filepath.parent.mkdir(

        parents=True,

        exist_ok=True

    )

    joblib.dump(

        obj,

        filepath

    )


def load_object(filepath: Path):
    """
    Load a saved Python object.
    """

    return joblib.load(filepath)