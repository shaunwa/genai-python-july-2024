import os
import sys
from datetime import datetime

def rename_files(directory, username):
    # Get today's date in MM-DD-YYYY format
    today_date = datetime.now().strftime('%m-%d-%Y')
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1]
        # Construct the new file name
        new_filename = f"{username}-{os.path.splitext(filename)[0]}-{today_date}{file_extension}"
        # Get the full paths for the old and new file names
        old_file_path = os.path.join(directory, filename)
        new_file_path = os.path.join(directory, new_filename)
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed '{old_file_path}' to '{new_file_path}'")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory> <username>")
    else:
        directory = sys.argv[1]
        username = sys.argv[2]
        rename_files(directory, username)