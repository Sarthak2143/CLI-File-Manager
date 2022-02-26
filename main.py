### IMPORTS ###

import os
import argparse
import sys

### ERROR MESSAGES ###

INVALID_FILE_TYPE = "Error: Invalid file format. %s must be a .txt file!"
INVALID_PATH = "Error: Invalid path specified. %s doesn't exist!"

### HELPER FUNCTIONS ###

## -- Checking validation -- ##

def validate_file(file_name):
    """
    validate file name and path
    """
    if not valid_path(file_name):
        print(INVALID_PATH%(file_name))
        sys.exit()

    elif not valid_filetype(file_name):
        print(INVALID_FILE_TYPE%(file_name))
        sys.exit()
    return

def valid_filetype(file_name):
    return file_name.endswith(".txt")

def valid_path(path):
    return os.path.exists(path)

## -- Functions for manager -- ##

def read(args):
    """
    reads a file
    """

    #get file name and path
    file_name = args.read[0]
    
    #validate file path
    validate_file(file_name)

    #read and print file as content

    with open(file_name, "r") as f:
        print(f.read())

def show(args):
    """
    show files
    """

    #get path to directory
    dir_path = args.show[0]

    #validate path
    if not valid_path(dir_path):
        print("Error: No such directory found.")
        sys.exit()

    #get .txt files in directory
    files = [f for f in os.listdir(dir_path) if valid_filetype(f)]
    print(f"{len(files)} text files found.")
    print('\n'.join(f for f in files))

def delete(args):
    """
    deletes a file
    """

    #get the file name/path
    file_name = args.delete[0]

    #validate filename/path
    validate_file(file_name)

    #delete the file
    os.remove(file_name)
    print(f"Successfully deleted {file_name}.")

def copy(args):
    """
    copies a file
    """
    #file to be copied
    file1 = args.copy[0]
    
    #file to be copied upon
    file2 = args.copy[1]
    
    # validate the file to be copied
    validate_file(file1)

    # validate the type of file 2
    if not valid_filetype(file2):
        print(INVALID_FILE_TYPE%(file_name))
        sys.exit()

    # copy file1 to file2
    with open(file1, 'r') as f1:
        with open(file2, 'w') as f2:
            f2.write(f1.read())
    print(f"Successfully copied {file1} to {file2}.")

def rename(args):
    """
    renames a file
    """

    # old file name
    old_filename = args.rename[0]
    # new file name
    new_filename = args.rename[1]

    # validate the file to be renamed
    validate_file(old_filename)

    # validate the type of new file name
    if not valid_filetype(new_filename):
        print(INVALID_FILE_TYPE%(file_name))
        sys.exit()

    # renaming
    os.rename(old_filename, new_filename)
    print(f"Successfully renamed {old_filename} to {new_filename}.")

### Creating the parser ###

def main():
    #create a parser object
    parser = argparse.ArgumentParser(description = "A CLI based file manager!")

    parser.add_argument(
            "-r",
            "--read",
            type = str,
            nargs = 1,
            metavar = "file_name",
            default = None,
            help = "Opens and read the specified file."
            )

    parser.add_argument(
            "-s",
            "--show",
            type = str,
            nargs = 1,
            metavar = 'file_name',
            default = None,
            help = 'Shows all the text files on a specified directory. \nType . for current directory.'
            )


    parser.add_argument(
            "-c",
            "--copy",
            type = str,
            nargs = 2,
            metavar = ("file1", "file2"),
            default = None,
            help = "Copies content of file1 to file2.\nWarning: file2 data will be overwritten."
            )

    parser.add_argument(
            "-d",
            "--delete",
            type = str,
            nargs = 1,
            metavar = "file_name",
            default = None,
            help = "Deletes the specified text file."
            )

    parser.add_argument(
            "--rename",
            type = str,
            nargs = 2,
            metavar = ("old_name", "new_name"),
            default = None,
            help = "Renames the specified text file to a new name."
            )

    # parse the args from standard input
    args = parser.parse_args()

    #calling functions dependant on types
    if args.read != None:
        read(args)
    elif args.show != None:
        show(args)
    elif args.delete !=None:
        delete(args)
    elif args.copy != None:
        copy(args)
    elif args.rename != None:
        rename(args)

### End of script ###

if __name__ == "__main__":
    #calling the main function
    main()

## --- THE END --- ##
