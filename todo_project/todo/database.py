import configparser
from pathlib import Path

from todo import DB_WRITE_ERROR, SUCCESS

# define DEFAULT_DB_FILE_PATH to hold the default database file path. The application will use this path if the user doesn’t provide a custom one.
DEFAULT_DB_FILE_PATH = Path.home().joinpath("." + Path.home().stem + "_todo.json")


# define get_database_path(). This function takes the path to the app’s config file as an argument, reads the input file using ConfigParser.read(), and returns a Path object representing the path to the to-do database on your file system. The ConfigParser instance stores the data in a dictionary. The "General" key represents the file section that stores the required information. The "database" key retrieves the database path.
def get_database_path(config_file: Path) -> Path:
    """Return the current path to the to-do database."""
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return Path(config_parser["General"]["database"])


# define init_database(). This function takes a database path and writes a string representing an empty list. You call .write_text() on the database path, and the list initializes the JSON database with an empty to-do list. If the process runs successfully, then init_database() returns SUCCESS. Otherwise, it returns the appropriate error code.
def init_database(db_path: Path) -> int:
    """Create the to-do database."""
    try:
        db_path.write_text("[]")  # create an empty to-do list
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR
