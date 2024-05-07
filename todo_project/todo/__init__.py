# Define app name and app current version.
__app_name__ = "todo"
__version__ = "0.1.0"

# Assign integer numbers to each variable of all the situation.
# For instance, if we print SUCCESS, we will get 0 as result. If we print ID_ERROR, we will get 7.
(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(7)

# Use a dictionary to map code to human-readable messages.
ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    DB_READ_ERROR: "database read error",
    DB_WRITE_ERROR: "database write error",
    ID_ERROR: "to-do id error",
}
