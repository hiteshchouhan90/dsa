from functools import wraps
from typing import get_type_hints


def enforce_types(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        hints = get_type_hints(func)
        for arg_name, arg_value in zip(hints.keys(), args):
            if not isinstance(arg_value, hints[arg_name]):
                raise TypeError(
                    f"Argument '{arg_name}' must be of type {hints[arg_name].__name__}, "
                    f"got {type(arg_value).__name__}"
                )
        return func(*args, **kwargs)

    return wrapper


@enforce_types
def add(a: int, b: int) -> int:
    return a + b


print(add(1, 2))  # Works fine
print(add(1, "two"))  # Raises TypeError
