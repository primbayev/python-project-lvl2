from gendiff.generate_diff import generate_diff


def test_generate_diff():
    path_to_json_file1 = './tests/fixtures/file1.json'
    path_to_json_file2 = './tests/fixtures/file2.json'

    with open('./tests/fixtures/diff_result.txt') as file:
        line = file.read()
    diff = generate_diff(path_to_json_file1, path_to_json_file2)

    assert diff == line
