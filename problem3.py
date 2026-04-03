import os

# Specify directory path (current directory if empty)
path = "/New folder"

# Get list of files and folders
contents = os.listdir(path)

print("Contents of directory:")
for item in contents:
    print(item)