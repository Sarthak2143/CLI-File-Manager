# CLI-File-Manager

A CLI based file manager for .txt files.                
## Features

1. Reading text files
1. Showing text files in a given directories.
1. Deleting text files.
1. Renaming text files.
1. Copying text files.

## Help message

```bash
┌─[Shinero@Voldemort]─[Programming/]
└──╼ ❯❯❯ python3 main.py -h
usage: main.py [-h] [-r file_name] [-s file_name]
               [-c file1 file2] [-d file_name]     
               [--rename old_name new_name]

A CLI based file manager!

options:
  -h, --help            show this help message and
                        exit   
  -r file_name, --read file_name
                        Opens and read the specified
                        file.
  -s file_name, --show file_name
                        Shows all the text files on a
                        specified directory. Type .
                        for current directory.
  -c file1 file2, --copy file1 file2
                        Copies content of file1 to
                        file2. Warning: file2 data
                        will be overwritten.
  -d file_name, --delete file_name
                        Deletes the specified text
                        file.
  --rename old_name new_name
                        Renames the specified text
                        file to a new name.
```

---

## TODO

- [ ] Add write functionality.
- [ ] Delete files in bulk.
- [ ] Move files.
