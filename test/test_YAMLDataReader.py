import pytest
from src.Types import DataType
from src.YAMLDataReader import YamlDataReader


class TestYAMLDataReader:

    @pytest.fixture()
    def yaml_file_and_data_content(self) -> tuple[str, DataType]:
        yaml_content = """
        Abramov Petr Sergeevich:
          - ('Math', 80)
          - ('Russian_language', 76)
          - ('Programming', 100)
        Petrov Igor Vladimirovich:
          - ('Programming', 78)
          - ('Literature', 97)
        """
        data = {
            'Abramov Petr Sergeevich':
                [('Math', 80), ('Russian_language', 76), ('Programming', 100)],
            'Petrov Igor Vladimirovich':
                [('Programming', 78), ('Literature', 97)]
        }
        return yaml_content, data

    @pytest.fixture()
    def yaml_filepath_and_data(self,
                               yaml_file_and_data_content:
                               tuple[str, DataType], tmpdir) \
            -> tuple[str, DataType]:
        yaml_file = tmpdir.mkdir("datadir").join("my_data.yaml")
        yaml_file.write_text(yaml_file_and_data_content[0], encoding='utf-8')
        return str(yaml_file), yaml_file_and_data_content[1]

    def test_read_yaml(self,
                       yaml_filepath_and_data: tuple[str, DataType]) \
            -> None:
        yaml_data = YamlDataReader().read(yaml_filepath_and_data[0])
        assert yaml_data == yaml_filepath_and_data[1]
