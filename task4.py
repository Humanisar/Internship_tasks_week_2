user_input = input("Enter something: ")

try:
    int_value = int(user_input)
    print("You entered an integer.")
    print("Type is:", type(int_value))

# If not integer, try to convert to float
except ValueError:
    try:
        float_value = float(user_input)
        print("You entered a float (decimal number).")
        print("Type is:", type(float_value))

    # If not float, then it's a string
    except ValueError:
        print("You entered text (string).")
        print("Type is:", type(user_input))