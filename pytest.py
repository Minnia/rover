from offtomars import RoverExam
# Make sure that the user inputs valid data


def validate_nums(x, y):
    try:
        if int(x) >= 0 and int(y) >= 0:
            return True
    except ValueError as err:
        ("Only numerical values please!")


def validate_rover(x, y, direction):
    try:
        if validate_nums(x, y) and direction in directions:
            return True
    except ValueError as err:
        ("Incorrect Rover values, please try again")
