from typing import Optional
import typer
from todo import __app_name__, __version__

# Creates an explicit Typer application, app.
app = typer.Typer()


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
