import os
import datetime
import pytest
from chatgpt_file_script import rename_files

def test_rename_files(tmpdir):
    # Create a temporary directory for testing
    directory = tmpdir.mkdir("test_files")

    # Create some test files
    file1 = directory.join("file1.txt")
    file1.write("Test file 1")
    file2 = directory.join("file2.txt")
    file2.write("Test file 2")

    # Call the rename_files function
    username = "testuser"
    rename_files(directory, username)

    # Check if the files are renamed correctly
    today_date = datetime.datetime.now().strftime('%m-%d-%Y')
    new_file1 = f"{username}-file1-{today_date}.txt"
    new_file2 = f"{username}-file2-{today_date}.txt"
    assert os.path.exists(os.path.join(directory, new_file1))
    assert os.path.exists(os.path.join(directory, new_file2))
    assert not os.path.exists(os.path.join(directory, "file1.txt"))
    assert not os.path.exists(os.path.join(directory, "file2.txt"))

test_rename_files()