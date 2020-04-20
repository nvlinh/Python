file_path = 'text_files/pi_1m.txt'
pi_str = ''
with open(file_path) as file_object:
    for line in file_object:
        pi_str += line.strip()

print(f"Length: {len(pi_str)}")
print(pi_str[:50])

# Python has no inherent limit to how much data you can work with; you  can work
# with as much data as your system’s memory can handle.

# Replace
message = "I'm learning Python."
print(message.replace('Python', 'C'))