"""
Project Configuration
"""

from pathlib import Path

# -----------------------------------------------------------------------------
# Paths
# -----------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

RAW_DATA = DATA_DIR / "raw" / "ObesityDataSet_raw_and_data_sinthetic.csv"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODEL_DIR = BASE_DIR / "models"

# -----------------------------------------------------------------------------
# Saved Artifacts
# -----------------------------------------------------------------------------

MODEL_FILE = MODEL_DIR / "obesity_model.pkl"

SCALER_FILE = MODEL_DIR / "scaler.pkl"

LABEL_ENCODERS_FILE = MODEL_DIR / "label_encoders.pkl"

TARGET_ENCODER_FILE = MODEL_DIR / "target_encoder.pkl"

# -----------------------------------------------------------------------------
# Dataset Split
# -----------------------------------------------------------------------------

TEST_SIZE = 0.20

RANDOM_STATE = 42