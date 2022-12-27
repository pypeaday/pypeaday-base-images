from typing import Union

import pytest
from python_hello_world import main


@pytest.mark.parametrize(
    ("x", "y", "z", "error"),
    [
        ("a string", 69, 42.0, None),
        ("a string", 69, 420, None),
        # (1111, 69, 420, ValueError),
        ("a string", 69.0, 420, ValueError),
        # ("a string", 69, "420", ValueError),
    ],
)
def test_a_type_hinted_function(
    x: str,
    y: int,
    z: Union[int, float],
    error: ValueError,
) -> None:
    if error is None:
        r = main.a_type_hinted_function(x, y, z)
        assert r["string argument"] == x
        assert r["integer argument"] == y
        assert r["integer or float argument"] == z
    else:
        with pytest.raises(ValueError):
            main.a_type_hinted_function(x, y, z)


def test_main() -> None:
    assert main.main() == 0


@pytest.mark.skip(reason="Example of skipping a pytest test")
def test_will_be_skipped():
    ...


def test_will_also_be_skipped():
    pytest.skip("Skipping imperatively")
