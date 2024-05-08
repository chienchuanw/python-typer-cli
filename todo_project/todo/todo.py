"""This module provides the To-Do model-controller."""

from typing import Any, Dict, NamedTuple


class CurrentTodo(NamedTuple):
    todo: Dict[str, Any]
    error: int
