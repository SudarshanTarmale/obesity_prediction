"""
Project Configuration
"""

from pathlib import Path

# Root Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data
RAW_DATA = BASE_DIR / "data" / "raw" / "ObesityDataSet_raw_and_data_sinthetic.csv"

PROCESSED_DATA = BASE_DIR / "data" / "processed"

# Models
MODEL_DIR = BASE_DIR / "models"

MODEL_FILE = MODEL_DIR / "obesity_model.pkl"

SCALER_FILE = MODEL_DIR / "scaler.pkl"

ENCODER_FILE = MODEL_DIR / "label_encoder.pkl"

# Random State
RANDOM_STATE = 42

# Test Split
TEST_SIZE = 0.20