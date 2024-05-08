"""This module provides the RP To-Do database functionality."""

import configparser
from pathlib import Path
from todo import DB_WRITE_ERROR, SUCCESS, JSON_ERROR, DB_READ_ERROR

import json
from typing import Any, NamedTuple, Dict, List


# define DEFAULT_DB_FILE_PATH to hold the default database file path. The application will use this path if the user doesn’t provide a custom one.

# DEFAULT_DB_FILE_PATH = Path.home().joinpath("." + Path.home().stem + "_todo.json")

# 原本上面那段，創造出來的檔案會是一個隱藏的 json 檔案，因為檔名前面有 .
# 這邊會是資料庫 json 的存放路徑
DEFAULT_DB_FILE_PATH = Path.home().joinpath(Path.home().stem + "_todo.json")


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


class DBResponse(NamedTuple):
    todo_list: List[Dict[str, Any]]
    error: int


class DatabaseHandler:
    def __init__(self, db_path: Path) -> None:
        self._db_path = db_path

    def read_todos(self) -> DBResponse:
        try:
            with self._db_path.open("r") as db:
                try:
                    return DBResponse(json.load(db), SUCCESS)
                except json.JSONDecodeError:
                    return DBResponse([], JSON_ERROR)
        except OSError:
            return DBResponse([], DB_READ_ERROR)

    def write_todos(self, todo_list: List[Dict[str, Any]]) -> DBResponse:
        try:
            with self._db_path.open("w") as db:
                json.dump(todo_list, db, indent=4)
            return DBResponse(todo_list, SUCCESS)
        except OSError:
            return DBResponse(todo_list, DB_WRITE_ERROR)
