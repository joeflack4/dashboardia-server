"""Tests."""
from os import path
from docunit import doctest_unittest_runner as docunit


if __name__ == '__main__':
    TEST_DIR = path.dirname(path.realpath(__file__)) + '/'
    docunit(test_dir=TEST_DIR, relative_path_to_root='../',
            package_names=['my_package_name', 'test'])
