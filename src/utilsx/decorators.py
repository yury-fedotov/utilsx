"""Profiling pipeline nodes."""

from collections.abc import Callable
from functools import wraps
from typing import Any

__all__ = [
    "return_element",
]


def return_element(index: int) -> Callable[[Callable[..., tuple[Any, ...]]], Callable[..., Any]]:
    """Makes a function returning a tuple return only the element at the given index.

    Implemented as a decorator factory.

    Args:
        index: The index of the tuple element to return.

    Returns:
        A decorator.
    """

    def decorator(func: Callable[..., tuple[Any, ...]]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
            return result[index]

        return wrapper

    return decorator
