"""
This module is used for getting and validating user data for the Future Value Program
"""

def get_float(prompt: str, high: int, low: int) -> float:
    """
    This function accepts a string to be used for a prompt for getting user input, 
    converts the recieved value to a float and checks to make sure its a valid entry within 
    the range of high and low  

    Args:
        prompt (str): The string that will be used to prompt the user for input
        high (int): The max value of the range for the user entry
        low (int): The minimum value of the range for the user entry (cannot be equal to)

    Returns:
        float: the converted/validated float that was input by the user
    """

    while True:
        num = float(input(prompt))

        if num > low and num <= high:
            break
        else:
            print(f"Entry must be greater than {low} and less than or equal to {high}")

    return num


def get_int(prompt: str, high: int, low: int) -> int:
    """Gets user input using the prompt string provided, converts it to an int, 
        and validates that it lies within the range of high and low

    Args:
        prompt (str): The string that will be used to prompt the user for input
        high (int): The max value of the range for the user entry
        low (int): The minimum value of the range for the user entry (cannot be equal to)

    Returns:
        int: validated user entry to be returned
    """

    while True:
        num = int(input(prompt))

        if num > low and num <= high:
            break
        else:
            print(f"Entry must be greater than {low} and less than or equal to {high}")

    return num 