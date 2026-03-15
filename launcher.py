"""
Write a program called "path.py" that has 3 functions : 
dirname(path)
basename(path)
extname(path)
            All these 3 functions take a Unix absolute path as input

            Make sure the function behaves as mentioned below :

            >>> location = "/home/apple/Downloads/story.txt"
            >>> 
            >>> dirname(location)              # returns directory name
            /home/apple/Downloads
            >>> 
            >>> basename(location)          # returns filename
            story.txt
            >>> 
            >>> extname(location)              # returns file extension
            txt
            >>> 



           Write another program called "launcher.py"
This program uses the functions present in "path.py"
to find and execute the application to be used to open the given file
based on the extension of the file.
Expected behaviour :
prompt$ launcher.py story.txt         # Should execute "notepad.exe story.txt"
prompt$ launcher.py master.py      # Should execute "python -m idlelib master.py"
"""


import sys
import os
import path

file = sys.argv[1]

extension = path.extname(file)

if extension == "txt":
    os.system(f'notepad.exe "{file}"')

elif extension == "py":
    os.system(f'python -m idlelib.idle "{file}"')

else:
    print("unsupported file type")





