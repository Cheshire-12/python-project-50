import os

from gendiff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def test_generate_diff_json():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected_output = get_fixture_path('res_stylish.txt')

    with open(expected_output) as f:
        expected = f.read().strip()

    assert generate_diff(file1, file2) == expected
    

def test_generate_diff_yaml():
    file1 = get_fixture_path('file1.yaml')
    file2 = get_fixture_path('file2.yaml')
    expected_output = get_fixture_path('res_stylish.txt')

    with open(expected_output) as f:
        expected = f.read().strip()

    assert generate_diff(file1, file2) == expected
    

def test_generate_diff_nested():
    file1 = get_fixture_path('file1_nested.json')
    file2 = get_fixture_path('file2_nested.json')
    expected_output = get_fixture_path('res_nested_stylish.txt')

    with open(expected_output) as f:
        expected = f.read().strip()

    assert generate_diff(file1, file2) == expected
    
def test_generate_diff_plain():
    file1 = get_fixture_path('file1_nested.json')
    file2 = get_fixture_path('file2_nested.json')
    expected_output = get_fixture_path('res_nested_plain.txt')

    with open(expected_output) as f:
        expected = f.read().strip()

    assert generate_diff(file1, file2, format='plain') == expected