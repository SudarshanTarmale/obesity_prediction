"""
Project Configuration

Central configuration file for the Obesity Prediction project.
Contains all project paths, constants, feature definitions,
and model settings.
"""

from pathlib import Path

# =============================================================================
# PROJECT PATHS
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

RAW_DATA_PATH = DATA_DIR / "raw" / "ObesityDataSet_raw_and_data_sinthetic.csv"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODEL_DIR = BASE_DIR / "models"

REPORTS_DIR = BASE_DIR / "reports"

PLOTS_DIR = REPORTS_DIR / "plots"

# =============================================================================
# SAVED ARTIFACTS
# =============================================================================

PIPELINE_FILE = MODEL_DIR / "obesity_pipeline.pkl"

MODEL_METRICS_FILE = REPORTS_DIR / "model_metrics.csv"

FEATURE_IMPORTANCE_FILE = REPORTS_DIR / "feature_importance.csv"

CLASSIFICATION_REPORT_FILE = REPORTS_DIR / "classification_report.csv"

# =============================================================================
# DATASET SETTINGS
# =============================================================================

TARGET_COLUMN = "NObeyesdad"

TEST_SIZE = 0.20

RANDOM_STATE = 42

CV_FOLDS = 5

# =============================================================================
# FEATURE DEFINITIONS
# =============================================================================

NUMERICAL_FEATURES = [

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

CATEGORICAL_FEATURES = [

    "Gender",

    "family_history_with_overweight",

    "FAVC",

    "CAEC",

    "SMOKE",

    "SCC",

    "CALC",

    "MTRANS"

]

# =============================================================================
# TARGET CLASSES
# =============================================================================

TARGET_CLASSES = [

    "Insufficient_Weight",

    "Normal_Weight",

    "Overweight_Level_I",

    "Overweight_Level_II",

    "Obesity_Type_I",

    "Obesity_Type_II",

    "Obesity_Type_III"

]