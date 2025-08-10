import random
import time
import matplotlib.pyplot as plt

# ---------- Deterministic QuickSort ----------
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # фіксоване правило — середній елемент
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

# ---------- Randomized QuickSort ----------
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # випадковий вибір pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

# ---------- Вимірювання часу виконання ----------
sizes = [10_000, 50_000, 100_000, 500_000]
det_times = []
rand_times = []

for size in sizes:
    arr = [random.randint(0, 10**6) for _ in range(size)]
    
    # Детермінований QuickSort
    total_time = 0
    for _ in range(5):
        arr_copy = arr.copy()
        start = time.perf_counter()
        deterministic_quick_sort(arr_copy)
        total_time += time.perf_counter() - start
    avg_det = total_time / 5
    det_times.append(avg_det)

    # Рандомізований QuickSort
    total_time = 0
    for _ in range(5):
        arr_copy = arr.copy()
        start = time.perf_counter()
        randomized_quick_sort(arr_copy)
        total_time += time.perf_counter() - start
    avg_rand = total_time / 5
    rand_times.append(avg_rand)

    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {avg_rand:.4f} секунд")
    print(f"   Детермінований QuickSort: {avg_det:.4f} секунд\n")

# ---------- Побудова графіка ----------
plt.plot(sizes, rand_times, label='Рандомізований QuickSort')
plt.plot(sizes, det_times, label='Детермінований QuickSort')
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.title("Порівняння рандомізованого та детермінованого QuickSort")
plt.legend()
plt.show()
