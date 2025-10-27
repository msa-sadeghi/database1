import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

DB_CONFIG = {
    'host':os.getenv('DB_HOST', 'localhost'),
    'port':os.getenv('DP_PORT', '5432'),
    'database':os.getenv('DB_NAME', ''),
    'user':os.getenv('DB_USER', ''),
    'password':os.getenv('DB_PASSWORD', '')
}

