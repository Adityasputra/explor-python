def not_repeat(string):
    counts = {}
    for char in string:
        lower_char = char.lower()
        if lower_char in counts:
            counts[lower_char] += 1
        else:
            counts[lower_char] = 1

    for char in string:
        if counts[char.lower()] == 1:
            return char

    return "None"

# Test cases
print(not_repeat("nescafe"))   # n
print(not_repeat("torAbika"))  # t
print(not_repeat("kUroky"))    # U
print(not_repeat("Pesawat"))   # P
print(not_repeat("taaT"))      # None
