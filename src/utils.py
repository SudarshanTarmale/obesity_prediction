"""
Utility Functions
"""

import joblib
from pathlib import Path


def save_object(obj, filepath: Path):
    """
    Save any Python object.
    """
    filepath.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(obj, filepath)


def load_object(filepath: Path):
    """
    Load a saved Python object.
    """
    return joblib.load(filepath)