def test_function(name):
    """
    Test the input name.

    This function checks if the input name is empty or not.

    Parameters:
    name (str): The name to be tested.

    Returns:
    str or int: If the name is empty, returns "The name is empty". 
                If the name is not empty, returns 1.
    """
    if name == "":
        return "The name is empty"
    else:
        return 1

# this is how a docstring is output into the terminal
print(test_function.__doc__)