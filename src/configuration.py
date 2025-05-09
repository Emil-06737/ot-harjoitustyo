import os
from dotenv import load_dotenv

current_directory = os.path.dirname(__file__)
try:
    load_dotenv(dotenv_path=os.path.join(current_directory, "..", ".env"))
except FileNotFoundError:
    pass
NAME_OF_DATABASE_FILE = os.getenv("NAME_OF_DATABASE_FILE") or "database.sqlite"
PATH_OF_DATABASE_FILE = os.path.join(
    current_directory, "..", "data", NAME_OF_DATABASE_FILE)
