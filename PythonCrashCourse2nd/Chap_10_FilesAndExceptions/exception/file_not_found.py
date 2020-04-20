import logging

file_path = "test.txt"
try:
    with open(file_path) as file_object:
        print(file_object.read())
except FileNotFoundError:
    logging.error(f"Sorry, the file {file_path} not exist.")
