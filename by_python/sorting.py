import time
import numpy as np


"""
2022.08.06 - sng_hn.lee
"""


def swap(lst: list, i: int, j: int) -> None:
    lst[i], lst[j] = lst[j], lst[i]


def bubble_sort(lst):
    for i in range(0, len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                swap(lst, i, j)


def selection_sort(lst):
    for i in range(0, len(lst) - 1):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        swap(lst, min_idx, i)


def insertion_sort(lst):
    for i in range(1, len(lst)):
        if lst[i - 1] < lst[i]:
            continue
        else:
            for j in range(0, i):
                if lst[j] > lst[i]:
                    swap(lst, i, j)


def merge_sort(lst):
    def merge(lst, left_idx, right_idx):
        i = left_idx
        j = right_idx - 1

        while i < j:
            if lst[i] > lst[j]:
                swap(lst, i, j)
                i += 1
                j -= 1
            else:
                i += 1

    merge_sort_call_stack = list()
    merge_call_stack = list()

    merge_sort_call_stack.append((0, len(lst)))

    while len(merge_sort_call_stack) != 0:
        left_idx, right_idx = merge_sort_call_stack.pop()
        if (right_idx - left_idx) > 1:
            pivot_idx = (left_idx + right_idx) // 2
            merge_sort_call_stack.append((left_idx, pivot_idx))
            merge_sort_call_stack.append((pivot_idx, right_idx))
        merge_call_stack.append((left_idx, right_idx))

    while len(merge_call_stack) != 0:
        left_idx, right_idx = merge_call_stack.pop()
        merge(lst, left_idx, right_idx)


def sorting_by(lst, sort_func):
    start_time = time.time()
    sort_func(lst)
    elapsed_time = time.time() - start_time
    print(f"elapsed_time: {elapsed_time: 5.3e} seconds")


if __name__ == '__main__':
    print('== sorting ')
    N = 10 ** 3
    lst = np.random.randint(0, 1000, N)
    print(lst[:10])

    print("== basic sort")
    benchmark_lst = lst.copy()
    sorting_by(benchmark_lst, lambda x: x.sort())

    print("== bubble_sort")
    lst_copy = lst.copy()
    sorting_by(lst_copy, bubble_sort)
    # print(lst_copy)

    print("== selection_sort")
    lst_copy = lst.copy()
    sorting_by(lst_copy, selection_sort)
    # print(lst_copy)

    print("== insertion_sort")
    lst_copy = lst.copy()
    lst_copy.sort()
    sorting_by(lst_copy, insertion_sort)
    # print(lst_copy)
    # print(lst_copy)

    print("== merge_sort")
    lst_copy = lst.copy()
    lst_copy.sort()
    sorting_by(lst_copy, merge_sort)
    # print(lst_copy)

    for x, y in zip(benchmark_lst, lst_copy):
        if x != y:
            print("== False result")
            break




