import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API key from .env
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# App settings
CORRECTION_DELAY = 0.8
ENABLE_GRAMMAR = True
ENABLE_SPELLCHECK = True