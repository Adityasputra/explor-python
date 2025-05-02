def mostFrequentChar(text: str) -> str:
    """
    Function to find the most frequent character in a string.
    If there are multiple characters with the same frequency,
    the first one encountered in the string is returned.

    Args:
    text (str): The input string.
    Returns:
    str: The most frequent character in the string.
    """

    max_count = 0
    result = ""

    for i in range(len(text)):
        count = 0
        for j in range(len(text)):
            if text[i].lower() == text[j].lower():
                count += 1

        if count > max_count:
            max_count = count
            result = text[i]

    return result


if __name__ == "__main__":
    print(mostFrequentChar("Hello World!"))
    print(mostFrequentChar("Python Programming"))
    print(mostFrequentChar("Case Study"))
    print(mostFrequentChar("Most Frequent Character"))
