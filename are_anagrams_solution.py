def are_anagrams(str1, str2):
    """
    This function checks if two strings are anagrams of each other.

    Parameters:
    ----------
    str1 : str
        The first string to be compared.
    str2 : str
        The second string to be compared.

    Returns:
    -------
    bool:
        Returns True if the two strings are anagrams, otherwise False.

    Example:
    --------
    are_anagrams("listen", "silent")  # Output: True
    are_anagrams("hello", "world")    # Output: False
    """

    # Normalise the strings by converting them to lowercase and sorting the characters
    str1 = sorted(str1)
    str2 = sorted(str2)

    # Compare the sorted strings
    return str1 == str2

# # Example usage
# print(are_anagrams("listen", "silent"))  # Expected output: True
# print(are_anagrams("hello", "world"))    # Expected output: False
