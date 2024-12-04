import pytest
import os
from unittest.mock import patch
# Import the functions to be tested
from seq import parse_file, main

# Tests for parse_file function
def test_parse_file_with_mixed_data():
    file_name = 'a_seq.txt'
    result = parse_file(file_name)
    expected = {'A': 2, 'C': 5, 'G': 6, 'T': 7, 'Unknown': 7}
    assert result == expected

def test_parse_file_with_good_data():
    file_name = 'b_seq.txt'
    result = parse_file(file_name)
    expected = {'A': 1, 'C': 2, 'G': 3, 'T': 4, 'Unknown': 0}
    assert result == expected

def test_parse_file_empty_file():
    file_name = 'empty_file.txt'
    result = parse_file(file_name)
    expected = {"A": 0, "C": 0, "G": 0, "T": 0, "Unknown": 0}
    assert result == expected

# Tests for main function
# use capsys to simulate command line
def test_main_no_files(capsys):
    with patch("sys.argv", ["script.py"]):
        main()
        captured = capsys.readouterr()
        assert "No files received" in captured.out

def test_main_with_files(capsys):
    file_name1 = 'a_seq.txt'
    file_name2 = 'b_seq.txt'

    with patch("sys.argv", ["script.py", file_name1, file_name2]):
        results = main()
        expected = {
            'a_seq.txt': {'A': 2, 'C': 5, 'G': 6, 'T': 7, 'Unknown': 7},
            'b_seq.txt': {'A': 1, 'C': 2, 'G': 3, 'T': 4, 'Unknown': 0}
        }
        assert results == expected

    # Additional output tests can be implemented if needed
