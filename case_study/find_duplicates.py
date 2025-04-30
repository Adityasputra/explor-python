from collections import Counter
import argparse

girlgroups = [
    "Blackpink",
    "Twice",
    "Twice",
    "Blackpink",
    "New Jeans",
    "ITZY",
    "New Jeans",
    "Red Velvet",
    "ITZY",
]


def validate_double_name_v1(data):
    """
    Find duplicate names using manual list tracking.

    Args:
        data (list): List of group names.

    Returns:
        list: List of duplicate names.
    """
    seen = []
    duplicates = []

    for name in data:
        if name in seen:
            if name not in duplicates:
                duplicates.append(name)
        else:
            seen.append(name)

    return duplicates


def validate_double_name_v2(data):
    """
    Find duplicate names by counting occurrences.

    Args:
        data (list): List of group names.

    Returns:
        list: List of duplicate names.
    """
    duplicates = []

    for name in data:
        if data.count(name) > 1 and name not in duplicates:
            duplicates.append(name)

    return duplicates


def validate_double_name_v3(data):
    """
    Find duplicate names using collections.Counter.

    Args:
        data (list): List of group names.

    Returns:
        list: List of duplicate names.
    """
    counter = Counter(data)
    return [name for name, count in counter.items() if count > 1]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find and list duplicate group names.")
    parser.add_argument(
        "-v",
        "--version",
        type=int,
        choices=[1, 2, 3],
        required=True,
        help="Select the version of the method to use (1, 2, or 3).",
    )

    args = parser.parse_args()

    if args.version == 1:
        result = validate_double_name_v1(girlgroups)
    elif args.version == 2:
        result = validate_double_name_v2(girlgroups)
    else:
        result = validate_double_name_v3(girlgroups)

    print("\nGroups with duplicate names:")
    for name in result:
        print(f" - {name}")
