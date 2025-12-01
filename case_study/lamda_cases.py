import json

transactions = [
    {"product": "Laptop", "category": "Electronics", "price": 15000000, "qty": 1},
    {"product": "Mouse", "category": "Electronics", "price": 150000, "qty": 2},
    {"product": "Chair", "category": "Furniture", "price": 750000, "qty": 1},
    {"product": "Desk", "category": "Furniture", "price": 2000000, "qty": 1},
    {"product": "Monitor", "category": "Electronics", "price": 3000000, "qty": 2},
]


# Studi Kasus 1 — Hitung Total Harga per Transaksi
total = list(
    map(lambda t: t["price"] * t["qty"], transactions)
)

print(total)

# Studi Kasus 2 — Filter Transaksi Elektronik di atas 1 juta
filtered = list(
    filter(lambda t: t["category"] == "Electronics" and t["price"] * t["qty"] > 1_000_000, transactions)
)

print(json.dumps(filtered, indent=2))

# Studi Kasus 3 — Urutkan Transaksi Berdasarkan Total Harga
sorted_transactions = sorted(
    transactions,
    key=lambda t: t["price"] * t["qty"],
    reverse=True
)

for t in sorted_transactions:
    print(t["product"], t["price"] * t["qty"])
    

# Task
# Task 1: Buat list baru berisi nama produk saja.
products_list = list(
    map(lambda p: p["product"], transactions)
)

print(products_list)

# Task 2: Ambil transaksi Furniture yang total harganya di atas 1 juta.
filtered_furniture = list(
    filter(lambda t: t["category"] == "Furniture" and t["price"] * t["qty"] > 1_000_000, transactions)
)

print(json.dumps(filtered_furniture, indent=2))

# Task 3: Hitung total pendapatan toko dari semua transaksi.
total_transaction = list(
    map(lambda t: t["price"] * t["qty"], transactions)
)

print(sum(total_transaction))

# Task 4 : Buat data baru dengan struktur
{
    "product": "Laptop",
    "total": 15000000
}

new_data = dict(
    map(lambda t: {"product" : t["product"], "total": t["price"] * t["qty"]}, transactions)
)

print(json.dumps(new_data, indent=2))


# ============================================================================
# VERSI PYTHONIC & READABLE (TETAP MENGGUNAKAN LAMBDA)
# ============================================================================

print("\n" + "="*80)
print("VERSI LEBIH PYTHONIC & READABLE (DENGAN LAMBDA)")
print("="*80 + "\n")

# Helper lambda functions yang dapat digunakan kembali
calculate_total = lambda t: t["price"] * t["qty"]
is_electronics = lambda t: t["category"] == "Electronics"
is_furniture = lambda t: t["category"] == "Furniture"
is_over_1m = lambda t: calculate_total(t) > 1_000_000

# Studi Kasus 1 — Hitung Total Harga per Transaksi
# Menggunakan map() dengan lambda, tapi dengan nama variabel yang deskriptif
total_prices = list(map(calculate_total, transactions))

print("📊 Total harga per transaksi:")
print(total_prices)
print()

# Studi Kasus 2 — Filter Transaksi Elektronik di atas 1 juta
# Memecah kondisi kompleks menjadi lambda yang lebih readable
is_electronics_over_1m = lambda t: is_electronics(t) and is_over_1m(t)
electronics_over_1m = list(filter(is_electronics_over_1m, transactions))

print("💻 Transaksi Elektronik di atas 1 juta:")
print(json.dumps(electronics_over_1m, indent=2))
print()

# Studi Kasus 3 — Urutkan Transaksi Berdasarkan Total Harga
# Menggunakan lambda sebagai key function dengan nama yang jelas
sorted_by_total = sorted(transactions, key=calculate_total, reverse=True)

print("📈 Transaksi diurutkan berdasarkan total harga:")
for transaction in sorted_by_total:
    total = calculate_total(transaction)
    print(f"  {transaction['product']:<15} Rp {total:>12,}")
print()

# Task 1: Buat list baru berisi nama produk saja
# Lambda function yang sederhana dan fokus
get_product_name = lambda t: t["product"]
product_names = list(map(get_product_name, transactions))

print("📦 Daftar produk:")
print(product_names)
print()

# Task 2: Ambil transaksi Furniture yang total harganya di atas 1 juta
# Kombinasi lambda functions untuk kondisi yang jelas
is_furniture_over_1m = lambda t: is_furniture(t) and is_over_1m(t)
furniture_over_1m = list(filter(is_furniture_over_1m, transactions))

print("🪑 Transaksi Furniture di atas 1 juta:")
print(json.dumps(furniture_over_1m, indent=2))
print()

# Task 3: Hitung total pendapatan toko dari semua transaksi
# Menggunakan map() + sum() untuk menghitung total
total_revenue = sum(map(calculate_total, transactions))

print(f"💰 Total pendapatan toko: Rp {total_revenue:,}")
print()

# Task 4: Buat data baru dengan struktur {"product": "...", "total": ...}
# Lambda function yang membuat struktur baru dengan jelas
create_summary = lambda t: {
    "product": t["product"],
    "total": calculate_total(t)
}
simplified_data = list(map(create_summary, transactions))

print("📋 Data dengan struktur sederhana:")
print(json.dumps(simplified_data, indent=2, ensure_ascii=False))
print()

# BONUS: Tampilkan produk dengan harga tertinggi
# Menggunakan max() dengan lambda key
most_expensive = max(transactions, key=calculate_total)
print(f"🏆 Produk dengan total tertinggi: {most_expensive['product']} - Rp {calculate_total(most_expensive):,}")
print()

# BONUS: Grouping berdasarkan kategori menggunakan lambda
print("📊 Total penjualan per kategori:")
from itertools import groupby

# Sort dulu berdasarkan kategori agar groupby bekerja
sorted_by_category = sorted(transactions, key=lambda t: t["category"])

# Group dan hitung total per kategori
for category, items in groupby(sorted_by_category, key=lambda t: t["category"]):
    items_list = list(items)
    category_total = sum(map(calculate_total, items_list))
    item_count = sum(map(lambda t: t["qty"], items_list))
    print(f"  {category:<15} | Items: {item_count:>3} | Total: Rp {category_total:>12,}")