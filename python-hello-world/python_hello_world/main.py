import os
from typing import Any, Dict, Union

import typer
from rich import print


def main():
    """main."""
    print("[bold red]Alert![/bold red] [green]Portal gun[/green] shooting! :boom:")
    print(f"APP VERSION = {os.environ.get('APP_VERSION', 'NO VERSION FOUND')}")
    return 0


def a_type_hinted_function(
    string_argument: str,
    integer_argument: int,
    integer_or_float_argument: Union[int, float],
) -> Dict[str, Any]:
    """Summary of a_type_hinted_function.

    Type hints in Python enable safer and faster development with the help of the LSP.
    Note that types are not enforced by the interpreter at all...
    ie. Type hinting doesn't affect the runtime of a script... they're hints, not law

    Args:
        string_argument: An argument with type designated as str
        integer_argument: An argument with type designated as int
        integer_or_float_argument: An argument that can be either an integer or a float
    """
    assert isinstance(string_argument, str)
    assert isinstance(integer_argument, int)
    assert isinstance(integer_or_float_argument, int) or isinstance(
        integer_or_float_argument, float
    )
    return {
        "example key": list(range(10)),
        "string argument": string_argument,
        "integer argument": integer_argument,
        "integer or float argument": integer_or_float_argument,
    }


if __name__ == "__main__":
    typer.run(main)
