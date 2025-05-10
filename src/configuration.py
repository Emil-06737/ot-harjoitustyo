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

SIZE = os.getenv("SIZE") or DEFAULT_SIZE
try:
    SIZE = int(SIZE)
except ValueError:
    SIZE = DEFAULT_SIZE

LENGTH = os.getenv("LENGTH") or DEFAULT_LENGTH
try:
    LENGTH = int(LENGTH)
except ValueError:
    LENGTH = DEFAULT_LENGTH

PLAYERS = os.getenv("PLAYERS") or DEFAULT_PLAYERS
try:
    PLAYERS = int(PLAYERS)
except ValueError:
    PLAYERS = DEFAULT_PLAYERS
