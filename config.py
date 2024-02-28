import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

HERE = Path(__name__).parent

class Config:
    URL = os.getenv('URL')