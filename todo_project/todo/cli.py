from typing import Optional
import typer
from todo import __app_name__, __version__, ERRORS, config, database

from pathlib import Path

# Creates an explicit Typer application, app.
app = typer.Typer()


# define init() as a Typer command using the @app.command() decorator.
@app.command()
def init(
    # define a Typer Option instance and assign it as a default value to db_path.
    # To provide a value for this option, your users need to use --db-path or -db followed by a database path.
    # The prompt argument displays a prompt asking for a database location.
    # It also allows you to accept the default path by pressing [Enter]
    db_path: str = typer.Option(
        str(database.DEFAULT_DB_FILE_PATH),
        "--db-path",
        "-db",
        prompt="to-do database location?",
    ),
) -> None:
    """Initialize the to-do database."""
    # calls init_app() to create the application’s configuration file and to-do database.
    app_init_error = config.init_app(db_path)

    # check if the call to init_app() returns an error. If so, lines 25 to 28 print an error message. Line 29 exits the app with a typer.Exit exception and an exit code of 1 to signal that the application terminated with an error.
    if app_init_error:
        typer.secho(
            f'Creating config file failed with "{ERRORS[app_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    # calls init_database() to initialize the database with an empty to-do list.
    db_init_error = database.init_database(Path(db_path))
    # check if the call to init_database() returns an error. If so, then display an error message, and exits the application. Otherwise, prints a success message in green text.
    # secho mean "echo in styles"
    # To print the messages in this code, you use typer.secho(). This function takes a foreground argument, fg, that allows you to use different colors when printing text to the screen. Typer provides several built-in colors in typer.colors. There you’ll find RED, BLUE, GREEN, and more. You can use those colors with secho() as you did here.
    if db_init_error:
        typer.secho(
            f'Creating database failed with "{ERRORS[db_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    else:
        typer.secho(f"The to-do database is {db_path}", fg=typer.colors.GREEN)


# Define _version_callback().
# This function takes a Boolean argument called value.
# If value is True, then the function prints the application’s name and version using echo().
# After that, it raises a typer.Exit exception to exit the application cleanly.
def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


# Define main() as a Typer callback using the @app.callback() decorator.
@app.callback()
def main(
    # define main() as a Typer callback using the @app.callback() decorator.
    # This means it can be either of bool or None type.
    # The version argument defaults to a typer.Option object, which allows you to create command-line options in Typer.
    version: Optional[bool] = typer.Option(
        None,
        "--version",  # Set the command-line names for the version option: -v and --version.
        "-v",
        help="Show the application's version and exit.",  # Provides a help message for the version option.
        callback=_version_callback,  # Attaches a callback function, _version_callback(), to the version option, which means that running the option automatically calls the function.
        is_eager=True,  # Sets the is_eager argument to True. This argument tells Typer that the version command-line option has precedence over other commands in the current application.
    )
) -> None:
    return
