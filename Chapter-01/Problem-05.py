# Importing the os module to interact with the operating system
import os

# Specify the directory path you want to list
# Here, '.' means the current working directory
directory = '.'

# Using os.listdir() function to get all files and folders in the directory
contents = os.listdir(directory)

# Printing the directory contents
print("Contents of the directory:")
for item in contents:
    print(item)   # Print each file or folder name
