from src.main import get_path_from_arguments
import pytest


@pytest.fixture()
def correct_arguments_string() -> tuple[list[str], str]:
    return ["-p",
            "D:/university/magic/1year/tpsai/lab1/data/data.txt"], \
           "D:/university/magic/1year/tpsai/lab1/data/data.txt"


@pytest.fixture()
def non_correct_arguments_string() -> list[str]:
    return ["D:/university/magic/1year/tpsai/lab1/data/data.txt"]


def test_get_path_from_correct_arguments(
        correct_arguments_string: [list[str], str]) -> None:
    path = get_path_from_arguments(correct_arguments_string[0])
    assert path == correct_arguments_string[1]


def test_get_path_from_non_correct_arguments(
        non_correct_arguments_string: list[str]) -> None:
    with pytest.raises(SystemExit) as e:
        get_path_from_arguments(non_correct_arguments_string[0])
    assert e.type == SystemExit
