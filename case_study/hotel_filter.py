import argparse

# List of hotels with star ratings
hotel_list = [
    "Four Seasons*5",
    "Holiday Inn*3",
    "Aston*4",
    "Hyatt*5",
    "Fave Hotel*3",
    "Mulia*5",
    "Swiss-Bel*4",
    "101 Hotel*3",
    "InterContinental*5",
    "Horison*4",
    "RedDoorz Plus*2",
    "POP! Hotel*2",
    "The Ritz-Carlton*5",
    "Amaris Hotel*2",
    "Ibis Budget*2",
    "Grand Hyatt*5",
    "Zest Hotel*3",
    "The Westin*5",
    "Yello Hotel*3",
    "Mercure*4",
    "Novotel*4",
    "Pullman*5",
    "Royal Ambarrukmo*4",
    "The Alana*4",
    "OYO Rooms*1",
]


# Version 1 - Manual parsing (educational purpose)
def filter_hotels_v1(star, data):
    result = []

    for item in data:
        name = ""
        star_str = ""
        found_separator = False

        for char in item:
            if char == "*":
                found_separator = True
                continue
            if not found_separator:
                name += char
            else:
                star_str += char

        if int(star_str) == star:
            result.append(name.strip())

    return result


# Version 2 - Split and loop
def filter_hotels_v2(star, data):
    result = []

    for item in data:
        name, stars = item.split("*")
        if int(stars) == star:
            result.append(name.strip())

    return result


# Version 3 - Pythonic list comprehension
def filter_hotels_v3(star, data):
    return [
        name.strip()
        for name, stars in (i.split("*") for i in data)
        if int(stars) == star
    ]


#  CLI Interface
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter hotels by star rating.")
    parser.add_argument(
        "-s", "--star", type=int, required=True, help="Star rating to filter by (1-5)"
    )
    parser.add_argument(
        "-v",
        "--version",
        type=int,
        choices=[1, 2, 3],
        default=3,
        help="Version to use (1, 2, or 3)",
    )

    args = parser.parse_args()

    if args.version == 1:
        result = filter_hotels_v1(args.star, hotel_list)
    elif args.version == 2:
        result = filter_hotels_v2(args.star, hotel_list)
    else:
        result = filter_hotels_v3(args.star, hotel_list)

    print(f"\n Hotels with {args.star} stars:")
    for name in result:
        print(f" - {name}")
