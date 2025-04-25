import argparse

members_holoID = [
    "Moona Hoshinova",
    "Ayunda Risu",
    "Airani Iofifteen",
    "Anya Melfissa",
    "Kureiji Ollie",
    "Pavolia Reine",
    "Vestia Zeta",
    "Kobo Kanaeru",
    "Kaela Kovalskia",
]

parser = argparse.ArgumentParser(
    description="Search for a Hololive ID member by name keyword."
)
parser.add_argument(
    "-n", "--name", required=True, help="Enter a name or keyword to search."
)
args = parser.parse_args()


def get_name_by_keyword(keyword, data):
    matched_names = [name for name in data if keyword.lower() in name.lower()]
    return matched_names if matched_names else ["No matching names found."]


print(get_name_by_keyword(args.name, members_holoID))
