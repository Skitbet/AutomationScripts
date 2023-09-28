import os;
import hashlib;
from collections import defaultdict;

def find_duplicate_files(directory):
    hash_table = defaultdict(list)

    for folderName, subFolders, fileNames in os.walk(directory):
        for filename in fileNames:
            filepath = os.path.join(folderName, filename)
            #calc the md5 hash of file
            file_hash = hash_file(filepath)
            #add file path to table with hash as key
            hash_table[file_hash].append(filepath)
    
    #filter out duplicate hashes
    duplicates = {hash: files for hash, files in hash_table.items() if len(files) > 1}

    return duplicates

def hash_file(filepath):
    # calc md5 hash of file
    hasher = hashlib.md5()
    with open(filepath, 'rb') as file: 
        while True:
            data = file.read(8192) # read file in 8KB 
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