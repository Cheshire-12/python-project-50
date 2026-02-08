import os

from gendiff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def test_generate_diff_json():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected_output = get_fixture_path('result_stylish.txt')

    with open(expected_output) as f:
        expected = f.read().strip()

    assert generate_diff(file1, file2) == expected