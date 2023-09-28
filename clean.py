import os

def delete_files(directory_path):
    try:
        files = os.listdir(directory_path)
        for file in files:
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print("All files deleted...")
    except OSError:
        print("Error occurred...")

directory_path = input("Enter directory to search: ")
delete_files(directory_path)