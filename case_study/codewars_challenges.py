"""
CODEWARS STYLE CHALLENGES - PEMULA HINGGA MENENGAH
===================================================
10 soal Python dengan tingkat kesulitan bertingkat
"""

# ============================================================================
# CHALLENGE 1: Sum of Positive (Pemula)
# ============================================================================
"""
Diberikan sebuah array bilangan bulat, kembalikan jumlah dari semua bilangan positif.

Contoh:
[1, -4, 7, 12] => 1 + 7 + 12 = 20
[-1, -2, -3] => 0
[1, 2, 3, 4, 5] => 15

Note: Jika tidak ada bilangan positif, return 0
"""

def sum_of_positive(numbers):
    # Tulis kode Anda di sini
    return sum(x for x in numbers if x > 0)

# Test cases
assert sum_of_positive([1, -4, 7, 12]) == 20
assert sum_of_positive([-1, -2, -3]) == 0
assert sum_of_positive([1, 2, 3, 4, 5]) == 15
assert sum_of_positive([]) == 0


# ============================================================================
# CHALLENGE 2: Count Vowels (Pemula)
# ============================================================================
"""
Hitung jumlah huruf vokal (a, e, i, o, u) dalam sebuah string.

Contoh:
"hello" => 2
"python" => 1
"aeiou" => 5

Note: Case insensitive (huruf besar/kecil dihitung sama)
"""

def count_vowels(text):
    # Tulis kode Anda di sini
    # vowels = ["a", "e", "i", "o", "u"]
    # found = 0
    
    # for char in text:
    #     for i in vowels:
    #         if char.lower() == i.lower():
    #             found += 1
                
    # return found
    return sum(1 for char in text if char in "aeiou")

# Test cases
assert count_vowels("hello") == 2
assert count_vowels("python") == 1
assert count_vowels("aeiou") == 5
assert count_vowels("AEIOU") == 5
assert count_vowels("xyz") == 0


# ============================================================================
# CHALLENGE 3: Reverse Words (Pemula-Menengah)
# ============================================================================
"""
Balikkan urutan kata dalam sebuah string, tapi jaga spasi di antara kata.

Contoh:
"Hello World" => "World Hello"
"a b c d" => "d c b a"
"one" => "one"

Note: Kata dipisahkan oleh spasi tunggal
"""

def reverse_words(text):
    # Tulis kode Anda di sini
    return " ".join(text.split()[::-1])

# Test cases
assert reverse_words("Hello World") == "World Hello"
assert reverse_words("a b c d") == "d c b a"
assert reverse_words("one") == "one"
assert reverse_words("") == ""


# ============================================================================
# CHALLENGE 4: Find the Odd Int (Menengah)
# ============================================================================
"""
Diberikan array bilangan bulat, temukan bilangan yang muncul dengan jumlah GANJIL.

Contoh:
[1, 1, 2] => 2 (karena 2 muncul 1 kali, 1 muncul 2 kali)
[1, 1, 1, 2, 2] => 1 (karena 1 muncul 3 kali, 2 muncul 2 kali)
[5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10] => 1

Note: Selalu ada SATU bilangan yang muncul jumlah ganjil
"""

def find_odd_occurrence(numbers):
    # Tulis kode Anda di sini
    pass

# Test cases
assert find_odd_occurrence([1, 1, 2]) == 2
assert find_odd_occurrence([1, 1, 1, 2, 2]) == 1
assert find_odd_occurrence([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]) == 1


# ============================================================================
# CHALLENGE 5: Longest Word (Pemula-Menengah)
# ============================================================================
"""
Temukan kata terpanjang dalam sebuah kalimat. Jika ada beberapa kata dengan 
panjang yang sama, return yang pertama ditemukan.

Contoh:
"The quick brown fox" => "quick"
"Hello world" => "Hello"
"a bb ccc" => "ccc"

Note: Kata dipisahkan oleh spasi
"""

def longest_word(sentence):
    # Tulis kode Anda di sini
    pass

# Test cases
assert longest_word("The quick brown fox") == "quick"
assert longest_word("Hello world") == "Hello"
assert longest_word("a bb ccc") == "ccc"


# ============================================================================
# CHALLENGE 6: FizzBuzz Array (Pemula-Menengah)
# ============================================================================
"""
Buat array dari 1 sampai n dengan aturan FizzBuzz:
- Jika angka habis dibagi 3, ganti dengan "Fizz"
- Jika angka habis dibagi 5, ganti dengan "Buzz"
- Jika angka habis dibagi 3 DAN 5, ganti dengan "FizzBuzz"
- Jika tidak, gunakan angka itu sendiri (sebagai string)

Contoh:
fizz_buzz(15) => ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", 
                  "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
"""

def fizz_buzz(n):
    # Tulis kode Anda di sini
    result = []
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(num))
    
    return result

# Test cases
result = fizz_buzz(15)
assert result[0] == "1"
assert result[2] == "Fizz"
assert result[4] == "Buzz"
assert result[14] == "FizzBuzz"


# ============================================================================
# CHALLENGE 7: Is Valid Parentheses (Menengah)
# ============================================================================
"""
Tentukan apakah string yang berisi karakter '(', ')', '{', '}', '[', ']' valid.

String valid jika:
1. Setiap kurung buka harus ditutup dengan kurung tutup yang sesuai
2. Kurung buka harus ditutup dalam urutan yang benar

Contoh:
"()" => True
"()[]{}" => True
"(]" => False
"([)]" => False
"({[]})" => True
"""

def is_valid_parentheses(s):
    # Tulis kode Anda di sini
    stack = []
    mapping = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if len(stack) == 0:
                return False
            if stack[-1] != mapping[char]:
                return False
            else:
                stack.pop()
            
    return len(stack) == 0

# Test cases
assert is_valid_parentheses("()") == True
assert is_valid_parentheses("()[]{}") == True
assert is_valid_parentheses("(]") == False
assert is_valid_parentheses("([)]") == False
assert is_valid_parentheses("({[]})") == True


# ============================================================================
# CHALLENGE 8: Digital Root (Menengah)
# ============================================================================
"""
Hitung digital root dari sebuah bilangan positif. Digital root diperoleh dengan
menjumlahkan semua digit, lalu menjumlahkan digit dari hasil tersebut, 
dan terus hingga mendapat satu digit.

Contoh:
16 => 1 + 6 = 7
942 => 9 + 4 + 2 = 15 => 1 + 5 = 6
132189 => 1+3+2+1+8+9 = 24 => 2+4 = 6
493193 => 4+9+3+1+9+3 = 29 => 2+9 = 11 => 1+1 = 2
"""

def digital_root(n):
    # Tulis kode Anda di sini
    pass

# Test cases
assert digital_root(16) == 7
assert digital_root(942) == 6
assert digital_root(132189) == 6
assert digital_root(493193) == 2


# ============================================================================
# CHALLENGE 9: Persistent Bugger (Menengah)
# ============================================================================
"""
Hitung berapa kali Anda harus mengalikan digit-digit dari sebuah bilangan 
sampai Anda mendapat satu digit.

Contoh:
39 => 3 * 9 = 27 => 2 * 7 = 14 => 1 * 4 = 4 (3 iterasi)
999 => 9 * 9 * 9 = 729 => 7 * 2 * 9 = 126 => 1 * 2 * 6 = 12 => 1 * 2 = 2 (4 iterasi)
4 => 0 iterasi (sudah satu digit)
"""

def persistence(n):
    # Tulis kode Anda di sini
    pass

# Test cases
assert persistence(39) == 3
assert persistence(4) == 0
assert persistence(25) == 2
assert persistence(999) == 4


# ============================================================================
# CHALLENGE 10: Snail Sort (Menengah)
# ============================================================================
"""
Diberikan matrix n x n, kembalikan elemen-elemen dalam urutan spiral clockwise.

Contoh:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
 
=> [1, 2, 3, 6, 9, 8, 7, 4, 5]

Penjelasan: Mulai dari pojok kiri atas, gerak ke kanan, lalu ke bawah, 
lalu ke kiri, lalu ke atas, dan terus spiral ke dalam.
"""

def snail_sort(matrix):
    # Tulis kode Anda di sini
    pass

# Test cases
assert snail_sort([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert snail_sort([[1, 2], [3, 4]]) == [1, 2, 4, 3]
assert snail_sort([[1]]) == [1]


# ============================================================================
# SOLUSI (UNCOMMENT UNTUK MELIHAT JAWABAN)
# ============================================================================

"""
# SOLUSI 1
def sum_of_positive(numbers):
    return sum(num for num in numbers if num > 0)

# SOLUSI 2
def count_vowels(text):
    return sum(1 for char in text.lower() if char in 'aeiou')

# SOLUSI 3
def reverse_words(text):
    return ' '.join(text.split()[::-1])

# SOLUSI 4
def find_odd_occurrence(numbers):
    from collections import Counter
    count = Counter(numbers)
    for num, freq in count.items():
        if freq % 2 == 1:
            return num

# SOLUSI 5
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len) if words else ""

# SOLUSI 6
def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# SOLUSI 7
def is_valid_parentheses(s):
    stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if not stack or pairs[stack.pop()] != char:
                return False
    return len(stack) == 0

# SOLUSI 8
def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# SOLUSI 9
def persistence(n):
    count = 0
    while n >= 10:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
        count += 1
    return count

# SOLUSI 10
def snail_sort(matrix):
    if not matrix or not matrix[0]:
        return []
    
    result = []
    while matrix:
        # Ambil baris pertama
        result.extend(matrix.pop(0))
        
        if matrix and matrix[0]:
            # Ambil kolom terakhir
            for row in matrix:
                result.append(row.pop())
        
        if matrix:
            # Ambil baris terakhir (terbalik)
            result.extend(matrix.pop()[::-1])
        
        if matrix and matrix[0]:
            # Ambil kolom pertama (dari bawah ke atas)
            for row in matrix[::-1]:
                result.append(row.pop(0))
    
    return result
"""

print("✅ File challenge berhasil dibuat!")
print("📝 Kerjakan setiap challenge dan uncomment solusi untuk melihat jawaban.")
print("\nUntuk menjalankan test: python codewars_challenges.py")
