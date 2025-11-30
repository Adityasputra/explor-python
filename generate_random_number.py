"""Generate random numbers with various options."""

import random


def generate_random_integer(start=1, end=10):
    """
    Generate a random integer within a range.
    
    Args:
        start (int): Start of range (default: 1).
        end (int): End of range (default: 10).
        
    Returns:
        int: Random integer between start and end (inclusive).
    """
    return random.randint(start, end)


def generate_random_float(start=0.0, end=1.0):
    """
    Generate a random float within a range.
    
    Args:
        start (float): Start of range (default: 0.0).
        end (float): End of range (default: 1.0).
        
    Returns:
        float: Random float between start and end.
    """
    return random.uniform(start, end)


def generate_random_choice(items):
    """
    Choose a random item from a list.
    
    Args:
        items (list): List of items to choose from.
        
    Returns:
        Any: Random item from the list.
    """
    return random.choice(items)


def main():
    """Main function to demonstrate random number generation."""
    print("=== Random Number Generator ===\n")
    
    # Generate random integer
    print("1. Random Integer (1-10):")
    print(f"   Result: {generate_random_integer()}\n")
    
    # Generate random integer with custom range
    print("2. Random Integer (1-100):")
    print(f"   Result: {generate_random_integer(1, 100)}\n")
    
    # Generate random float
    print("3. Random Float (0.0-1.0):")
    print(f"   Result: {generate_random_float():.4f}\n")
    
    # Generate random float with custom range
    print("4. Random Float (10.0-50.0):")
    print(f"   Result: {generate_random_float(10.0, 50.0):.2f}\n")
    
    # Random choice from list
    colors = ["Red", "Green", "Blue", "Yellow", "Purple"]
    print("5. Random Choice from list:")
    print(f"   Colors: {colors}")
    print(f"   Result: {generate_random_choice(colors)}\n")


if __name__ == "__main__":
    main()