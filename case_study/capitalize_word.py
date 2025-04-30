def capitalize_each_word(text: str) -> str:
    """
    Capitalizes the first letter of each word in the given text.

    Args:
        text (str): The input text to be capitalized.

    Returns:
        str: The text with each word capitalized.
    """
    return " ".join(word.capitalize() for word in text.split())

if __name__ == "__main__":
    # Example usage
    input_text = "hello world! this is a test."
    capitalized_text = capitalize_each_word(input_text)
    print(capitalized_text)  # Output: "Hello World! This Is A Test."