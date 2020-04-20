# Writing to an empty file
file_path = 'flies_text/programming.txt'
with open(file_path, 'w') as file_object:
    file_object.write("I love Python")

# The second argument, 'w',
# tells Python that we want to open the file in write mode. You can open a file
# 192 Chapter 10
# in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows
# you to read and write to the file ('r+'). If you omit the mode argument,
# Python opens the file in read-only mode by default.
# The open() function automatically creates the file you’re writing to if
# it doesn’t already exist. However, be careful opening a file in write mode
# ('w') because if the file does exist, Python will erase the contents of the
# file before returning the file object.

with open(file_path) as file_object:
    print(file_object.read())

with open(file_path, 'a') as file_object:
    file_object.write("\nI love C")

with open(file_path) as file_object:
    print(file_object.read())

# Create new file and wirte data to it
file_path = 'flies_text/new_file.txt'
with open(file_path, 'x') as file_object:  # error when file is exist
    file_object.write("This is new file")