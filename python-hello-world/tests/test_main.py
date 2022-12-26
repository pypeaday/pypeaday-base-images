import pytest
from python_hello_world import main


@pytest.mark.parametrize(
    ("x", "y", "z", "error"),
    [
        ("a string", 69, 42.0, None),
        ("a string", 69, 420, None),
        (1111, 69, 420, AssertionError),
        ("a string", 69.0, 420, AssertionError),
        ("a string", 69, "420", AssertionError),
    ],
)
def test_a_type_hinted_function(x, y, z, error):
    if error is None:
        r = main.a_type_hinted_function(x, y, z)
        assert r["string argument"] == x
        assert r["integer argument"] == y
        assert r["integer or float argument"] == z
    else:
        with pytest.raises(AssertionError):
            main.a_type_hinted_function(x, y, z)


def test_main():
    assert main.main() == 0
