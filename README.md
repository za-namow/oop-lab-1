Just as a note before I explain. There's a foreign file in the submission of Lab 2 also, that is an image of the first file that was in the github but I made a mistake that caused the history of it to be deleted and replace by current commit, I submitted that as a proof that I have done it but it gone missing and the missing version can be found in the first commit of this repository, My mistake.

1. DataLoader Class
-The DataLoader class is responsible for loading CSV files
-When it’s created, it sets a base path
-Its method load_csv, opens a CSV file, reads it line by line, and converts each row into a dictionary
-Finally, it returns all rows as a list of dictionaries, which makes the data easy to work with in Python.
2. Table Class
-It stores the table’s name and the list of rows
-The method filter(condition) allows you to select specific rows based on a condition (like “all cities in Germany”).
-The method aggregate(func, column) lets you perform calculations on one column

As for how I test the code: trial and error