import random
from timeit import timeit
from tabulate import tabulate

from merge_sort import merge_sort
from insertion_sort import insertion_sort


sizes = [1000, 5000, 10000]

merge_sort_times = {}
insertion_sort_times = {}
timsort_times = {}


if __name__ == "__main__":
    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]

        merge_time = timeit("merge_sort(arr.copy())", globals=globals(), number=1)
        merge_sort_times[size] = merge_time

        insertion_time = timeit(
            "insertion_sort(arr.copy())", globals=globals(), number=1
        )
        insertion_sort_times[size] = insertion_time

        timsort_time = timeit("sorted(arr.copy())", globals=globals(), number=1)
        timsort_times[size] = timsort_time

    table_data = [
        [
            "Сортування злиттям",
            merge_sort_times[1000],
            merge_sort_times[5000],
            merge_sort_times[10000],
        ],
        [
            "Сортування вставками",
            insertion_sort_times[1000],
            insertion_sort_times[5000],
            insertion_sort_times[10000],
        ],
        [
            "Сортування злиттям",
            timsort_times[1000],
            timsort_times[5000],
            timsort_times[10000],
        ],
    ]

    headers = ["", "Час для 1000 ел.", "Час для 5000 ел.", "Час для 10000 ел."]

    table = tabulate(table_data, headers=headers, tablefmt="grid")

    print(table)
