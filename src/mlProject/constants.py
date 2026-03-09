from pathlib import Path

# Configuration File Paths
CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")

# Data Ingestion Constants
ARTIFACTS_ROOT = Path("artifacts")
DATA_INGESTION_ROOT_DIR = ARTIFACTS_ROOT / "data_ingestion"
DATA_INGESTION_SOURCE_URL = "https://github.com/Swanish34/Branching-Tutorial/raw/refs/heads/main/winequality-data.zip"
DATA_INGESTION_LOCAL_DATA_FILE = DATA_INGESTION_ROOT_DIR / "data.zip"
DATA_INGESTION_UNZIP_DIR = DATA_INGESTION_ROOT_DIR