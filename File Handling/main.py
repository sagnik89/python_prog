
# This opens the file in the python program.
# Syntax of writing the open() function is the that the name of the file should be written as a string along with the extension of the file
file = open("my_files.txt")

# Stores the data in the variable assigned to
content = file.read()

print(content)

# to close the file to save memory
file.close()

# People forget to close the file so they use this key word which does the same thing. 
with open("my_files.txt", mode= "w") as f:
    f.write("This the new text.")
    

