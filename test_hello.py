from hello import with_input


def test_with_input():
    result = with_input("blue")
    assert result["old"] == "blue"


def setup_function(function):
    print(f" Running Setup: {function.__name__}")


def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
