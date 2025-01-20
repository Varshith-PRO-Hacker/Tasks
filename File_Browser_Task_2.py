# Objective: Develop a program that enables interactive browsing of file content, displaying one line at a time with user-defined controls.
import sys

class SkipThisFile(Exception):
    """Custom exception to skip the current file."""
    pass

def main():
    try:
        with open("File1.txt", "r") as file:
            lines = file.readlines() #reads all the lines in the file

            for line in lines:
                print(line.strip()) # in each line the unwanted spaces and empty lines are removed and printed
                Input = input("Press Enter for next line, 'n' + Enter to skip file: ")
                if Input == "n":
                    return SkipThisFile
    
    except SkipThisFile:
        second()
        return # acts as a stop function preventing python from going back and reopening File1 and continuing it.


def second():
    try:
        with open("File2.txt", "r") as file1:
            lines = file1.readlines()
    
        for line in lines:
            print(line.strip())
            Input = input("Press Enter for next line, 'n' + Enter to skip file: ")
            if Input == "n":
                return SkipThisFile
    
    except SkipThisFile:
        print("Skipping this file ... Work in Progress ...")

main()

print("End of Files")
sys.exit()