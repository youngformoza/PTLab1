import argparse
import sys
from src.CalcRating import CalcRating
from src.TextDataReader import TextDataReader
from src.YAMLDataReader import YamlDataReader
from src.StudentSetProc import StudentSetProc


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p",
                        dest="path",
                        type=str,
                        required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)

    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    if path.endswith('.txt'):
        reader = TextDataReader()
    else:
        reader = YamlDataReader()

    students = reader.read(path)
    print("All students")
    for student, subjects in students.items():
        print(f"\t{student}:")
        for subject, score in subjects:
            print(f"\t\t{subject}, {score}")
    ratings = CalcRating(students).calc()
    print("\nRatings")
    for student, rating in ratings.items():
        print(f"\t{student}: {rating}")

    analyzer = StudentSetProc()
    students_with_min_scores = analyzer.find_students_with_min_scores(students)

    print("\n\nAnalyzer with 76 min points results")

    if students_with_min_scores:
        print("\tStudents with at least 76 points in at least three subjects:")
        for student in students_with_min_scores:
            print(f"\t\t{student}")
    else:
        print("\tNo students with at least 76 points "
              "in at least three subjects found.")


if __name__ == "__main__":
    main()
