import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Linear Search
def linear_search(books, target):
    for index, book in enumerate(books):
        if book == target:
            return index
    return -1

# Binary Search
def binary_search(books, target):
    low, high = 0, len(books) - 1
    while low <= high:
        mid = (low + high) // 2
        if books[mid] == target:
            return mid
        elif books[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Grafik untuk menyimpan data
n_values = []
linear_times = []
binary_times = []

# Fungsi untuk memperbarui grafik
def update_graph():
    plt.figure(figsize=(8, 6))
    plt.plot(n_values, linear_times, label='Linear Search', marker='o', linestyle='-')
    plt.plot(n_values, binary_times, label='Binary Search', marker='o', linestyle='-')
    plt.title('Performance Comparison: Linear vs Binary Search')
    plt.xlabel('Dataset Size (Number of Books)')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.draw()  # Gambar grafik
    plt.pause(0.01)  # Berikan jeda agar grafik diperbarui tanpa memblokir eksekusi


# Fungsi untuk mencetak tabel waktu eksekusi
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["Dataset Size", "Linear Time (s)", "Binary Time (s)"]
    min_len = min(len(n_values), len(linear_times), len(binary_times))
    for i in range(min_len):
        table.add_row([n_values[i], linear_times[i], binary_times[i]])
    print(table)

# Program utama
while True:
    try:
        dataset_size = int(input("Masukkan ukuran dataset (atau ketik -1 untuk keluar): "))
        if dataset_size == -1:
            print("Program selesai. Terima kasih!")
            break
        if dataset_size <= 0:
            print("Masukkan ukuran dataset yang positif!")
            continue

        n_values.append(dataset_size)

        # Generate dataset dan target
        books = [f"Buku-{i}" for i in range(1, dataset_size + 1)]  # Dataset buku
        target = f"Buku-{dataset_size}"  # Target pencarian

        # Ukur waktu eksekusi Linear Search
        start_time = time.time()
        linear_search(books, target)
        linear_times.append(time.time() - start_time)

        # Ukur waktu eksekusi Binary Search
        books.sort()  # Binary Search membutuhkan dataset terurut
        start_time = time.time()
        binary_search(books, target)
        binary_times.append(time.time() - start_time)

        # Cetak tabel waktu eksekusi
        print_execution_table()

        # Perbarui grafik
        update_graph()

    except ValueError:
        print("Masukkan ukuran dataset yang valid!")
