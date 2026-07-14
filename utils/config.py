from pathlib import Path
import os
from dotenv import load_dotenv

# Get project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Full path to .env
ENV_PATH = BASE_DIR / ".env"

print(f"Project Root : {BASE_DIR}")
print(f"ENV Path     : {ENV_PATH}")
print(f"ENV Exists   : {ENV_PATH.exists()}")

# Load .env
load_dotenv(dotenv_path=ENV_PATH)

BASE_URL = os.getenv("BASE_URL")
HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
TIMEOUT = int(os.getenv("TIMEOUT", "30000"))
BROWSER = os.getenv("BROWSER","chromium")

print(f"BASE_URL = {BASE_URL}")
