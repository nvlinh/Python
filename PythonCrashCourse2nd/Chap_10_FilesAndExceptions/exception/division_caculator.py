print("Give me two number, I'll divide them.")
print("\nAny time, press 'q' to exit.")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        divide_number = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide a number is zero.")
    except ValueError:
        print("Please input a number.")
    else:
        print(divide_number)
