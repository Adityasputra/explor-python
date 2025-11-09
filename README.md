# explor-python 🐍

Repository pembelajaran Python dengan berbagai contoh program dasar hingga studi kasus. Proyek ini berisi materi lengkap untuk memahami fundamental Python dan penerapannya dalam berbagai situasi.

## 📚 Struktur Repository

### 🎯 Basic Python (`basic/`)

Folder ini berisi 11 modul pembelajaran dasar Python yang terstruktur:

1. **[01_variables_basics.py](basic/01_variables_basics.py)** - Pengenalan variabel, assignment, dan tipe data dasar
2. **[02_user_input_basics.py](basic/02_user_input_basics.py)** - Cara menerima input dari user
3. **[03_python_data_types.py](basic/03_python_data_types.py)** - Tipe data Python (int, float, string, boolean, dll)
4. **[04_string_manipulation.py](basic/04_string_manipulation.py)** - Manipulasi dan operasi string
5. **[05_python_operators.py](basic/05_python_operators.py)** - Operator aritmatika, perbandingan, dan logika
6. **[06_control_flow.py](basic/06_control_flow.py)** - Percabangan (if-elif-else)
7. **[07_loops.py](basic/07_loops.py)** - Perulangan (for, while)
8. **[08_builtin_data_structures.py](basic/08_builtin_data_structures.py)** - List, tuple, dictionary, dan set
9. **[09_functions_in_python.py](basic/09_functions_in_python.py)** - Fungsi, parameter, dan return value
10. **[10_exception_handling.py](basic/10_exception_handling.py)** - Penanganan error dengan try-except
11. **[11_file_handling.py](basic/11_file_handling.py)** - Membaca dan menulis file
12. **[hello_world_program.py](basic/hello_world_program.py)** - Program Python pertama

### 💡 Case Study (`case_study/`)

Folder ini berisi berbagai studi kasus penerapan Python:

- **[capitalize_word.py](case_study/capitalize_word.py)** - Mengkapitalisasi setiap kata dalam string
- **[find_duplicates.py](case_study/find_duplicates.py)** - Menemukan duplikasi dalam list
- **[holoid_search.py](case_study/holoid_search.py)** - Pencarian data HoloID
- **[hotel_filter.py](case_study/hotel_filter.py)** - Filter data hotel
- **[is_palindrome.py](case_study/is_palindrome.py)** - Mengecek apakah string adalah palindrome
- **[most_frequent_char.py](case_study/most_frequent_char.py)** - Mencari karakter yang paling sering muncul
- **[not_repeat_string.py](case_study/not_repeat_string.py)** - Mencari karakter yang tidak berulang

### 🔧 Utility Scripts (Root Level)

Program-program utilitas sederhana:

- **[convert_kilometers_to_miles.py]( convert_kilometers_to_miles.py)** - Konversi kilometer ke mil
- **[convert_celsius_to_fahrenheit.py](convert_celsius_to_fahrenheit.py)** - Konversi Celsius ke Fahrenheit
- **[arithmetical_operations.py](arithmetical_operations.py)** - Operasi aritmatika dasar
- **[display_calender.py](display_calender.py)** - Menampilkan kalender
- **[generate_random_number.py](generate_random_number.py)** - Generate angka random

## 🚀 Cara Menggunakan

### Prerequisites

- Python 3.x terinstall di sistem
- Text editor atau IDE (VS Code, PyCharm, dll)

### Menjalankan Program

1. **Clone repository ini:**
   ```bash
   git clone <repository-url>
   cd explor-python
   ```

2. **Menjalankan file individual:**
   ```bash
   python basic/01_variables_basics.py
   python case_study/is_palindrome.py
   python convert_celsius_to_fahrenheit.py
   ```

3. **Untuk program yang memerlukan input:**
   ```bash
   python arithmetical_operations.py
   # Ikuti prompt untuk memasukkan angka
   ```

## 📖 Urutan Pembelajaran yang Disarankan

Untuk pemula, ikuti urutan ini:

1. Mulai dari `basic/hello_world_program.py`
2. Lanjutkan dengan file di folder `basic/` secara berurutan (01-11)
3. Setelah memahami dasar, eksplorasi `case_study/` untuk melihat penerapan nyata
4. Coba modifikasi utility scripts di root level sebagai latihan

## 💻 Contoh Penggunaan

### Basic Example
```python
# 01_variables_basics.py
name = "adits"
age = 20
print(f"Hello, my name is {name} and I'm {age} years old")
```

### Case Study Example
```python
# is_palindrome.py
from case_study.is_palindrome import is_palindrome

print(is_palindrome("RaceCar"))  # True
print(is_palindrome("Kasur"))    # False
print(is_palindrome("Katak"))    # True
```

## 🤝 Kontribusi

Jika ingin menambahkan materi atau memperbaiki code:
1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/new-topic`)
3. Commit perubahan (`git commit -m 'Add new topic'`)
4. Push ke branch (`git push origin feature/new-topic`)
5. Buat Pull Request

## 📝 Catatan

- Setiap file memiliki dokumentasi dan komentar yang jelas
- Program dirancang untuk pembelajaran bertahap
- Silakan eksplorasi dan modifikasi sesuai kebutuhan

## 📧 Kontak

Jika ada pertanyaan atau saran, silakan buat issue di repository ini.

---
**Happy Learning! 🎓**
