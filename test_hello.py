from click.testing import CliRunner
from hello import with_input
from hellocli import callcolor


def test_hello_cli():
    """ this is my command line tool"""
    runner = CliRunner()
    result = runner.invoke(callcolor, ['--color', 'yellow'])
    assert result.exit_code == 0
    assert 'yellow' in result.output


def test_with_input():
    result = with_input("blue")
    assert result["old"] == "blue"


def setup_function(function):
    print(f" Running Setup: {function.__name__}")


def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
