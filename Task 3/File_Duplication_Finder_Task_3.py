# Objective: Develop a script that identifies and removes duplicate files in a directory based on their content, 
# not just their file names. You will need to use a hashing algorithm, such as SHA256, to compute the hash of the 
# file content and determine if any duplicates exist.

import hashlib
import os
import logging

def compute_sha256(file_path):
    hasher = hashlib.sha256()
    try:
        with open(file_path, "rb") as f: # Open the file in binary mode.
            while True:
                chunk = f.read(4096) # Read files in chunks of 4096 bytes
                hasher.update(chunk) #Update the hash with file content
    except Exception as e:
        logging.error(f"Could not read {file_path} - {e}")
        return None
    
    return hasher.hexdigest() # Return the final hash value as a hexadecimal string

def find_duplicates(directory):
    file_hashes = {} #Dictionary to store the hash --> List of file paths
    duplicates = {}

    for root, _, files in os.walk(directory): #walk through the directory
# os.walk(directory) --> scans through all the files in in the given directory, including subdirectories. Helps us loop through them without manually listing them.
        for file in files:
            file_path = os.path.join(root, file) #Get full file path #Ensure we correctly join directory paths and file names in a cross_platform way.
            file_hash = compute_sha256(file_path) #Compute hash of the file.

            if file_hash in file_hashes:
                file_hashes[file_hash].append(file_path) #add to existing file
            else:
                file_hashes[file_hash] = [file_path] #create new list

        for file_hash, file_list in file_hashes.items():
            if len(file_list) > 1:
                duplicates[file_hash] = file_list

        return duplicates

    # Return only hashes that have more than one file (duplicates)
    # return {h: p for h, p in file_hashes.items() if len(p)>1}

# root gives us the current directory and file is the name of file inside it.

#Example Use:
# Duplicates = find_duplicates("path/to/directory")
# print(Duplicates)

#setup logging for recoding the deleted files
logging.basicConfig(filename="duplicate_files.log", level=logging.INFO, format="%(asctime)s - %(messages)s")
    #Logs deleted files into "duplicate_files.log".
    #Format → Timestamp - Deleted File Path.
    #Helps track which files were deleted for record-keeping.


def manual_deletion(duplicates):
    for file_hash, file_list in duplicates.items():
    #Loops through each group of duplicate files in the dictionary.
    #file_hash → SHA256 hash of the files.
    #file_list → List of duplicate file paths for that hash.
        print(f"\nDuplicate group (SHA256: {file_hash}: )")
        #Prints each duplicate group (grouped by SHA256 hash).
        #Numbering each file (start=1) makes it easier for the user to select files.
        for idx, file in enumerate(file_list, start=1):
            print(f"{idx} {file}")
        
        user_input = input("Which file would you like to delete. Choose the numbers seperated by ',' or type none to skip: ")

        if user_input.lower() == "none":
            continue #Skip deletion for this group.

        try:
            indexes_to_delete = [int(i) - 1 for i in user_input.split(",")]
            
            for i in indexes_to_delete:
                if 0 <= i < len(file_list):
                    file_to_delete = file_list[i]
                    os.remove(file_to_delete) # Delete file.

                    logging.info(f"Deleted: {file_to_delete}")
                    print(f"Deleted: {file_to_delete}")
                
                else:
                    print(f"invalid index: {i+1}")
        
        except ValueError:
            print("Invalid input. Please enter numbers seperated by commas.")

# def log_script_completion(total_duplicates):
#     logging.info(f"Duplicate file scan completed. Total duplicate groups: {total_duplicates}")

def main():
    directory = input("Enter the directory to scan for duplicates: ").strip()

    if not os.path.isdir(directory):
        print("Invalid Directory. Please enter a valid path.")
        logging.error(f"Invalid directory entered: {directory}")
        return
    duplicates = find_duplicates(directory)

    if duplicates:
        print("\nDuplicate files found!")
        logging.info(f"DUplicate scan completed. Total groups found: {len(duplicates)}")
        manual_deletion(duplicates)
    else:
        print("No duplicates found.")
        logging.info("No Duplicate files found.")

if __name__ == "__main__":
    main()