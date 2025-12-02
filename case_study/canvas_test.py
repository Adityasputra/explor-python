def sum_of_positive(numbers):
    # Tulis kode Anda di sini
    return sum(x for x in numbers if x > 0)

# Test cases
assert sum_of_positive([1, -4, 7, 12]) == 20
assert sum_of_positive([-1, -2, -3]) == 0
assert sum_of_positive([1, 2, 3, 4, 5]) == 15
assert sum_of_positive([]) == 0

print(sum_of_positive([1, -4, 7, 12]))
print(sum_of_positive([]))

def find_vowels(text):
    return sum(1 for char in text if char in "aeiuo")


print(find_vowels("hello"))



def reverse_word(text):
    return " ".join(text.split()[::-1])


print(reverse_word("Hello world"))
print(reverse_word("Hello"))