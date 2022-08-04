# How to use csv_parser:
Add CSV file to project root (next to the csv_parser.py file)
On line 11, change the name of the default file to the name of the csv file to be parsed:
```
with open("<enter-csv-file-name-here>.csv", 'r') as infile:
```
## Running csv_parser.py
MacOS comes with Python pre-installed but with version 2.7. More info: https://www.freecodecamp.org/news/python-version-on-mac-update/
### via VSCode
Click the arrow button on the top-right corner of the csv_parser.py file tab to run the file. The parsed csv file should appear on the project root alongside the csv_parser.py and your original csv file.
### via Terminal
Navigate to the root directory where csv_parser.py is located, and run:
```
Python3 csv_parser.py
```
The parsed csv file should appear on the project root alongside the csv_parser.py and your original csv file.

