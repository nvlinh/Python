# Relative paths
print("Relative paths:")
with open('text_files/linh_note.txt') as file_object:
    contents = file_object.read()
    print(contents)

# Absolute file paths
print("\nAbsolute file paths:")
with open('../writing/linh_test_absolute_path.txt') as file_object:
    contents = file_object.read()
    print(contents)
