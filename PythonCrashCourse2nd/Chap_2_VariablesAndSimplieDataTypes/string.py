'This is a string.'
"This is also a string."

# 1. Changing case in a String with Methods
name = 'lower case'
print(name.title())

name = "Lower Case"
print(name.upper())
print(name.lower())

# 2. Using variables in Strings
firstName = 'Linh'
lastName = 'Nguyen Van'
fullName = f'{firstName} {lastName}' # f is function format
message = f'Hello, {fullName.upper()}'
print(message)

# 3. Adding whitespace to Strings with Tabs or Newlines
print('\tPython')
print('Linh learning: \n\t-Python \n\t-Javascript')

# 4. Stripping Whitespace

stripping = ' left'
print(stripping)
print(stripping.lstrip());
stripping = 'right '
print(stripping.rstrip())
stripping = ' both left and right '
print(stripping.strip())
print(stripping)

# 5. Avoid syntax errors with Strings.
# message = 'It's String' => error 
# message = "It's String" => ok
