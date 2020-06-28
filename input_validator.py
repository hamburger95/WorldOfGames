# check that user input is valid
def input_validator(usr_input, max_value):
    try:
        if int(usr_input) in range(1, max_value + 1):
            return True
            # print("Good Input")
        elif usr_input not in range(1, max_value + 1):
            print("Input out of range, input must be a number between 1 to " + str(max_value) + ". Input: ", usr_input)
            return False
    except ValueError:
        try:
            if type(float(usr_input)) is float:
                print("Input is a float number. input must be an integer number between 1 to " + str(max_value) + ". Input: ", usr_input)
                return False
        except ValueError:
            print("input is not a number. It's a string. input must be an integer number between 1 to " + str(max_value) + ". Input: ", usr_input)
            return False
