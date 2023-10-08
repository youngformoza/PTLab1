from src.Types import DataType


class StudentSetProc:
    @staticmethod
    def find_students_with_min_scores(data: DataType) -> list[str]:
        students_with_min_scores = []
        for student, scores in data.items():
            min_score_count = sum(score >= 76 for _, score in scores)
            if min_score_count >= 3:
                students_with_min_scores.append(student)

        return students_with_min_scores
