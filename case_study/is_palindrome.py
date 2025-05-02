def is_palindrome(text: str) -> bool:
    """
    Check if a given string is a palindrome.

    A palindrome is a word, phrase, number, or other sequences of characters
    that reads the same forward and backward (ignoring spaces, punctuation,
    and capitalization).

    Args:
        text (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """

    text = text.lower()

    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    print(is_palindrome("RaceCar"))  # True
    print(is_palindrome("Kasur"))  # False
    print(is_palindrome("Katak"))  # True
    print(is_palindrome("Hello"))  # False
