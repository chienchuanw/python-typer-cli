# imports CliRunner from typer.testing.
from typer.testing import CliRunner

# imports a few required objects from your todo package.
from todo import __app_name__, __version__, cli

# creates a CLI runner by instantiating CliRunner.
runner = CliRunner()


# defines the first unit test for testing the application’s version.
def test_version():
    # calls .invoke() on runner to run the application with the --version option. And store the result of this call in result.
    result = runner.invoke(cli.app, ["--version"])
    # asserts that the application’s exit code (result.exit_code) is equal to 0 to check that the application ran successfully.
    assert result.exit_code == 0
    # asserts that the application’s version is present in the standard output, which is available through result.stdout.
    assert f"{__app_name__} v{__version__}\n" in result.stdout
