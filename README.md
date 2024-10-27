# Sorting Algorithm Performance Analysis

This project evaluates the performance of two sorting algorithms, **Merge Sort** and **QuickSort**, on large datasets, with a focus on execution time, memory usage, and the number of comparisons. The code generates random and reversed datasets of sizes 10,000 and 100,000 and analyzes each algorithm's efficiency under different conditions.

## Project Structure

- `main.py`: The main Python script that:
  - Generates datasets of different sizes and orders (random and reversed).
  - Implements and tests Merge Sort and an optimized QuickSort.
  - Measures and records execution time, memory usage, and the number of comparisons.
  - Visualizes performance results through bar charts.
- `execution_time_comparison.png`: Bar chart comparing execution times across different datasets and algorithms.
- `memory_usage_comparison.png`: Bar chart comparing memory usage.
- `comparisons_count_comparison.png`: Bar chart showing the number of comparisons made by each algorithm.

## Requirements

- **Python 3.x**
- **Libraries**:
  - `matplotlib` for plotting
  - `tracemalloc` (built-in) for memory tracking
 
# Comparative Performance Analysis of Merge Sort and QuickSort Algorithms on Large Datasets

## How It Works

### Dataset Generation
- Generates two datasets of 10,000 and 100,000 elements each.
- Creates both random and reversed (sorted in descending order) datasets to simulate different real-world data scenarios.

### Sorting Algorithms
- **Merge Sort**: A divide-and-conquer algorithm with consistent performance across data types, implemented from scratch.
- **Optimized QuickSort**: Uses Python's built-in `sorted()` function for optimal performance on large datasets.

### Performance Metrics
- **Execution Time**: Measures sorting duration in milliseconds.
- **Memory Usage**: Tracks peak memory usage during the sorting process.
- **Number of Comparisons**: Counts the number of comparisons made during sorting.

### Visualization
- Generates bar charts for execution time, memory usage, and comparisons, enabling easy performance comparison between algorithms.

## Usage

Run the `main.py` script to generate datasets, execute sorting, and display performance metrics:





