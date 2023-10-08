import pytest
from src.Types import DataType
from src.StudentSetProc import StudentSetProc


class TestStudentSetProc:

    @pytest.fixture()
    def input_data(self) -> DataType:
        data = {
            'Abramov Petr Sergeevich':
                [('Math', 80), ('Russian_language', 76), ('Programming', 100)],
            'Petrov Igor Vladimirovich':
                [('Programming', 78), ('Literature', 97)]
        }
        return data

    def test_find_students_with_min_scores(self, input_data: DataType) -> None:
        students_with_min_scores = \
            StudentSetProc.find_students_with_min_scores(input_data)
        expected_result = ['Abramov Petr Sergeevich']
        assert students_with_min_scores == expected_result
