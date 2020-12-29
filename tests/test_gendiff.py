from gendiff.gendiff_process import generate_diff


def test_json_gendiff():
    path_to_json_file1 = './tests/fixtures/jsons/file1.json'
    path_to_json_file2 = './tests/fixtures/jsons/file2.json'

    with open('./tests/fixtures/jsons/diff_result.txt') as file:
        line = file.read()
    diff = generate_diff(path_to_json_file1, path_to_json_file2)

    assert diff == line


def test_yaml_gendiff():
    path_to_yaml_file1 = './tests/fixtures/yamls/file1.yaml'
    path_to_yaml_file2 = './tests/fixtures/yamls/file2.yaml'

    with open('./tests/fixtures/yamls/diff_result.txt') as file:
        line = file.read()
    diff = generate_diff(path_to_yaml_file1, path_to_yaml_file2)

    assert diff == line
