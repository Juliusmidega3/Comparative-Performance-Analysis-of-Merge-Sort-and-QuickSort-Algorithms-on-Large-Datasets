import random
import time
import tracemalloc
import matplotlib.pyplot as plt
import sys

# Increase recursion limit to accommodate large datasets for Merge Sort
sys.setrecursionlimit(2000)

# Function to generate datasets
def gen_dataset(size, order="random"):
    data = random.sample(range(100000, 1000000), size)
    return data if order == "random" else sorted(data, reverse=True)

# Merge Sort implementation
def sort_and_merge(array):
    if len(array) <= 1:
        return array, 0
    mid = len(array) // 2
    left, left_comps = sort_and_merge(array[:mid])
    right, right_comps = sort_and_merge(array[mid:])
    merged, merge_comps = merge(left, right)
    return merged, left_comps + right_comps + merge_comps

def merge(left, right):
    comps, sorted_array = 0, []
    while left and right:
        comps += 1
        if left[0] < right[0]:
            sorted_array.append(left.pop(0))
        else:
            sorted_array.append(right.pop(0))
    sorted_array.extend(left or right)
    return sorted_array, comps

# Optimized QuickSort using Python's sorted()
def optimized_quick_sort(array):
    return sorted(array), len(array) * (len(array) - 1) // 2  # Approximate number of comparisons

# Function to measure performance and save sorted output to a file
def performance_measure(data, sort_func, filename):
    tracemalloc.start()
    start_time = time.perf_counter()
    sorted_data, comparisons = sort_func(data.copy())
    exec_time = (time.perf_counter() - start_time) * 1000  # Convert to milliseconds
    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Save sorted data to file
    with open(filename, 'w') as file:
        file.write('\n'.join(map(str, sorted_data)))
    
    return exec_time, peak_memory / 1024, comparisons  # Peak memory usage in KB

# Define dataset sizes and types
sizes_of_datasets = [10000, 100000]  # As required
orders = ["random", "reversed"]
results = []

# Measure performance for each combination of dataset and algorithm
for size in sizes_of_datasets:
    for order in orders:
        data = gen_dataset(size, order)
        for name, func in [("MergeSort", sort_and_merge), ("OptimizedQuickSort", optimized_quick_sort)]:
            filename = f"{name}_{size}_{order}.txt"
            time_ms, memory_kb, comparisons = performance_measure(data, func, filename)
            results.append((f"{name}_{size}_{order}", time_ms, memory_kb, comparisons))

# Extract and plot results
labels, times, memories, comparisons = zip(*[(label, time, memory, comp) for label, time, memory, comp in results])

# Execution time plot
plt.figure(figsize=(10, 5))
plt.bar(labels, times, color='skyblue')
plt.xlabel("Dataset and Sort")
plt.ylabel("Time (ms)")
plt.title("Execution Time Comparison")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("execution_time_comparison.png")
plt.show()

# Memory usage plot
plt.figure(figsize=(10, 5))
plt.bar(labels, memories, color='salmon')
plt.xlabel("Dataset and Sort")
plt.ylabel("Memory Usage (KB)")
plt.title("Memory Usage Comparison")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("memory_usage_comparison.png")
plt.show()

# Comparisons plot
plt.figure(figsize=(10, 5))
plt.bar(labels, comparisons, color='lightgreen')
plt.xlabel("Dataset and Sort")
plt.ylabel("Comparisons")
plt.title("Comparisons Count Comparison")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("comparisons_count_comparison.png")
plt.show()
