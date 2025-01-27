# Objective: Develop a script that identifies and removes duplicate files in a directory based on their content, 
# not just their file names. You will need to use a hashing algorithm, such as SHA256, to compute the hash of the 
# file content and determine if any duplicates exist.

import hashlib

def compute_sha256(file_path):
    hasher = hashlib.sha256()

    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            hasher.update(chunk)
    
    return hasher.hexidigest()