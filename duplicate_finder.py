import os
import hashlib
from collections import defaultdict

def find_duplicate_files(directory):
    print(f"Searching for duplicates in {directory}")
    hash_table = defaultdict(list)

    for folderName, subFolders, fileNames in os.walk(directory):
        for filename in fileNames:
            filepath = os.path.join(folderName, filename)
            print(f"Processing file: {filepath}")
            file_hash = hash_file(filepath)
            hash_table[file_hash].append(filepath)
    
    duplicates = {hash: files for hash, files in hash_table.items() if len(files) > 1}

    return duplicates

def hash_file(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as file:
        while True:
            data = file.read(65536)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

directory_to_search = input("Enter directory to search: ")
duplicated_files = find_duplicate_files(directory_to_search)

if duplicated_files:
    print("Found duplicates")
    for hash_value, file_list in duplicated_files.items():
        print(f"Hash: {hash_value}")
        for file in file_list:
            print(f"- {file}")
else:
    print("No duplicates found.")
    
print("Script completed.")
