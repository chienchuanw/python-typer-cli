# Build a Python Typer CLI

## Overview

In this project, we want to build a user-friend;y command-line interface that allows users to interact with the app and manage the to-do lists.  
The CLI should provide the following global options:  

- `-v` or `--version` shows the current version and exits the application.
- `--help` shows the global help message for the entire application.

The application will also provide commands to initialize the app, add and remove to-dos, and manage the to-do completion status:

- `init`: Initializes the application's to-do database
- `add`: Adds a new to-do the database with a description
- `list`: Lists all the to-dos in the database
- `complete`: Completes a to-do by setting it as done using its ID
- `remove`: Removes a to-do from the database using its ID
- `clear`: Removes all the to-dos by clearing the database

Additionally, this is a project based on [Build a Command-Line To-Do App With Python and Typer](https://realpython.com/python-typer-cli/)  

## Objectives

1. Build a functional to-do application with a Typer CLI in Python

    - Build a command-line interface capable of taking and processing commands, options, and arguments.
    - Select an appropriate data type to represent your to-dos
    - Implement a way to persistently store the to-do list
    - Define a way to connect that user interface with the to-do data
  
2. Use Typer to add commands, arguments, and options to your to-do app
3. Test your Python to-do application with Typer’s CliRunner and pytest

## How to

### Step 1: Set up the To-Do Project

1. Create a Python virtual environment in the project directory

    ```console
    <!-- Create project directory -->
    mkdir <Project Folder>
    cd <Project Folder>

    <!-- Create pyproject.toml -->
    poetry init -n

    <!-- Activate virtual environment -->
    poetry shell
    ```

2. Install project-related packages

    - Typer: To create the CLI application
    - Colorama: To ensures the colors work correctly on the command line window
    - Shellingham: A library for detecting the current running shell
    - Pytest: To test the application's code

    ```console
    <!-- Install Typer -->
    poetry add typer

    <!-- Install Colorama -->
    poetry add colorama

    <!-- Install Shellingham -->
    poetry add shellingham

    <!-- Install Pytest -->
    poetry add pytest
    ```

3. Define the Project layout
We have to create packages, modules and files that will frame the application layout. The app's core package should live in `todo_project/todo/`.  
Inside the package directory, there should be these contents below:

    - `__init__.py`: Enables `todo/` to be a Python package
    - `__main__.py`: Provides an entry-point scripts to run the app from the package using the `python -m todo` command
    - `cli.py`: Provides the Typer command-line interface for the application
    - `config.py`: Contains code to handle the applications configuration file
    - `database.py`: Contains code to handle the application's to-do database
    - `todo.py`: Provides code to connect the CLI with to-do database

Meanwhile, you'll also need a `tests/` directory containing a `__init__.py` file to turn the directory into a package and a `test_todo.py` file to hold unit tests for the application.

### Step 2: Set up the To-Do CLI app with Python and Typer

1. Define module-level names to hold the application's name and version
2. Define a series of return and error codes
3. Create the Typer CLI application with support for `--help`, `-v`, and `--version` options
4. Create an Entry-point script