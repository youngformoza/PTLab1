import yaml
from src.Types import DataType
from src.DataReader import DataReader


class YamlDataReader(DataReader):
    def read(self, path: str) -> DataType:
        with open(path, 'r') as file:
            data = yaml.safe_load(file)

        # Convert the strings to tuples in the data
        for student, subjects in data.items():
            data[student] = [eval(subject) for subject in subjects]

        return data
