import os
from dotenv import load_dotenv
from os.path import join, dirname

# Initialize env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_TOKEN = os.environ.get("API_TOKEN")
