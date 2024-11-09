import math

def is_prime(num):
    """Checks if a number is prime.

    Input:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:

    boolean = is_prime(5)   # returns True
    print(boolean)
    """


    # Function implementation here ...
    output = ""
    max = int(math.sqrt(num))
    a = num - 2


    
    if (a * a)% num == a % num:
        output is True
    else:
        output is False
    
    """

    for x in range(2, max):
        if num % x == 0:
            output is False
        else:
            output is True
    """
    return output


# # # Run code example
print(is_prime(5))   # returns True
