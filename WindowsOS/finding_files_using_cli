Finding Files Using CLI
--------------------------
from: https://www.addictivetips.com/windows-tips/search-for-files-and-folders-from-command-prompt-windows-10/

> <DRIVE_LETTER>:
# entering the desired drive letter followed by a colon will switch to that drive so that it can be searched

> cd "<PATH_TO_FOLDER>"
# this will switch to a particular folder that can then be searched
# if you are not in the drive where the folder is you can switch drives and to the folder by giving the full file path, e.g. cd "D:\Images"
# quotation marks are needed whenever there is whitespace in the file path; it is recommended to always use them

> dir /b/s *.<FILE_EXTENSION>
# search for all files in the current directory that have specified file extension (e.g. .pdf or .docx)
# * = wildcard
# /b = do not include metadata; easier to read
# /s = include subfolders in the search

> dir *<FILE_NAME>*.* /s
# search by file name; wildcards are used in case there is text before and/or after the string being searched for; file extension is also a wildcard

> dir "<NAME_OF_FOLDER>" /AD /b /s
# search within the named folder and return all its subfolders

> dir /s/b /A:D "D:*<PARTIAL_NAME_OF_FOLDER>*"
# searches the entire designated drive (in this case D) for a folder; wildcards are used because only part of the folder's name is known

