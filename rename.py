import os
import re

# Directory path where files need to be renamed
directory = "./songs"
# directory = "/Users/churongzhang/Downloads/Movies/BILLIONS"
pattern = r'(\d+)'

def rename_files_with_regex(directory, pattern):
    for filename in os.listdir(directory):
        match = re.search(pattern, filename)
        if ".mp4" not in filename:
            continue
        if match:
            episode_number = match.group(1)  # Get the captured episode number
            new_filename = f"雪中 第{episode_number}集.mp4"
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            
            try:
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {filename} => {new_filename}")
            except Exception as e:
                print(f"Error renaming {filename}: {str(e)}")

# Call the function to rename files in the directory
rename_files_with_regex(directory, pattern)
