
def validate_custom(input_1, input_2):
    try:
        int(input_1.get())
    except ValueError:
        print(ValueError("Width is not int"))
    try:
        int(input_2.get())
    except ValueError:
        print(ValueError("Height is not int"))

