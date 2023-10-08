from src.main import get_path_from_arguments
import pytest


@pytest.fixture()
def correct_arguments_string() -> list[tuple[list[str], str]]:
    return [
        (["-p",
          "D:/university/magic/1year/tpsai/lab1/data/data.txt"],
         "D:/university/magic/1year/tpsai/lab1/data/data.txt"),
        (["-p",
          "D:/university/magic/1year/tpsai/lab1/data/data.yaml"],
         "D:/university/magic/1year/tpsai/lab1/data/data.yaml")
    ]


@pytest.fixture()
def non_correct_arguments_string() -> list[str]:
    return ["D:/university/magic/1year/tpsai/lab1/data/data.txt",
            "D:/university/magic/1year/tpsai/lab1/data/data.yaml"]


def test_get_path_from_correct_arguments(
        correct_arguments_string: [list[str], str]) -> None:
    for args, expected_path in correct_arguments_string:
        path = get_path_from_arguments(args)
        assert path == expected_path


def test_get_path_from_non_correct_arguments(
        non_correct_arguments_string: list[str]) -> None:
    with pytest.raises(SystemExit) as e:
        get_path_from_arguments(non_correct_arguments_string[0])
    assert e.type == SystemExit
