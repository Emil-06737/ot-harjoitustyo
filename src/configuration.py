import os
from dotenv import load_dotenv

DEFAULT_NAME_OF_DATABASE_FILE = "database.sqlite"
DEFAULT_SIZE = 13
DEFAULT_LENGTH = 5
DEFAULT_PLAYERS = 2

current_directory = os.path.dirname(__file__)
try:
    load_dotenv(dotenv_path=os.path.join(current_directory, "..", ".env"))
except FileNotFoundError:
    pass

NAME_OF_DATABASE_FILE = os.getenv("NAME_OF_DATABASE_FILE") or DEFAULT_NAME_OF_DATABASE_FILE
if NAME_OF_DATABASE_FILE[-7:] != ".sqlite":
    NAME_OF_DATABASE_FILE = DEFAULT_NAME_OF_DATABASE_FILE

PATH_OF_DATABASE_FILE = os.path.join(
    current_directory, "..", "data", NAME_OF_DATABASE_FILE)

try:
    SIZE = int(os.getenv("SIZE"))
except (ValueError, TypeError) as e:
    SIZE = DEFAULT_SIZE

try:
    LENGTH = int(os.getenv("LENGTH"))
except (ValueError, TypeError) as e:
    LENGTH = DEFAULT_LENGTH

try:
    PLAYERS = int(os.getenv("PLAYERS"))
except (ValueError, TypeError) as e:
    PLAYERS = DEFAULT_PLAYERS
