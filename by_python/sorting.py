import time
import numpy as np

"""
2022.08.06 - sng_hn.lee
- fastest sort(quick sort) still 10 time slower then default sort
why it happenend? because default python sorting algorithm is Tim Sort which means hybrid method of both insertion and merge sort
https://en.wikipedia.org/wiki/Timsort
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


def binary_insertion_sort(xs: list):
    """
    2022.08.5
    """
    def binary_search(lst: list, n_open: int, pivot: int) -> int:
        """
        2022.08.30 - frhyme - Init
        """
        left, right = 0, n_open
        cursor = (left + right) // 2

        while left >= 0 and right >= 0 and cursor >= 0:
            if lst[cursor] < pivot:
                # to the right
                left = cursor + 1
                cursor = (left + right) // 2
            elif lst[cursor] > pivot:
                # to the left
                right = cursor - 1
                cursor = (left + right) // 2

            if cursor == left or cursor == right:
                return cursor
    # Function Definition Done ========================
    lst = [1, 2, 3, 8]

    for x in range(1, 10):
        b_idx = binary_search(lst, len(lst), x)
        # print(f"b_idx of {x}: {b_idx}")
        lst.insert(b_idx, x)
    print(lst)

    # test
    for i in range(1, len(xs)):
        b_idx = binary_search(xs, i - 1, xs[i])

        tmp = xs[i]
        print(f"xs: {xs}")
        print(f"x: {xs[i]}, i: {i}, b_idx: {b_idx}")
        for j in range(i, b_idx - 1, -1):
            if j == 0:
                break
            xs[j] = xs[j - 1]
            print(f"j: {j}")
        xs[b_idx] = tmp
        print(f"xs: {xs}")
        print(f'== {i} ============================')


def merge_sort(lst):
    def merge(lst, left_idx, pivot_idx, right_idx):
        left_lst = lst[left_idx:pivot_idx]
        right_lst = lst[pivot_idx:right_idx]
        # print('left_lst:', left_lst)
        # print('right_lst: ', right_lst)

        combined_lst = list()

        while len(left_lst) != 0 and len(right_lst) != 0:
            if left_lst[0] < right_lst[0]:
                x = left_lst.pop(0)
                combined_lst.append(x)
            else:
                x = right_lst.pop(0)
                combined_lst.append(x)
        combined_lst += left_lst
        combined_lst += right_lst

        for i in range(left_idx, right_idx):
            lst[i] = combined_lst.pop(0)

    merge_sort_call_stack = list()
    merge_call_stack = list()

    merge_sort_call_stack.append((0, len(lst)))

    while len(merge_sort_call_stack) != 0:
        left_idx, right_idx = merge_sort_call_stack.pop()
        # print(left_idx, right_idx)
        if (right_idx - left_idx) > 1:
            pivot_idx = (left_idx + right_idx) // 2
            merge_sort_call_stack.append((left_idx, pivot_idx))
            merge_sort_call_stack.append((pivot_idx, right_idx))
        merge_call_stack.append((left_idx, pivot_idx, right_idx))

    while len(merge_call_stack) != 0:
        left_idx, pivot_idx, right_idx = merge_call_stack.pop()
        # print(left_idx, pivot_idx, right_idx)
        # print("Before: ", lst)
        merge(lst, left_idx, pivot_idx, right_idx)


def quick_sort(lst):
    def sub_quick_sort(lst, left_idx, right_idx):
        if (right_idx - left_idx) > 1:
            # print(left_idx, right_idx)
            p_idx = right_idx - 1
            p_value = lst[p_idx]
            i = left_idx
            j = p_idx - 1

            while True:
                while True:
                    if lst[i] < p_value and i < (right_idx - 1):
                        i = i + 1
                    else:
                        break
                while True:
                    if p_value < lst[j] and 0 <= j:
                        j = j - 1
                    else:
                        break
                # print(left_idx, right_idx)
                # print(f"i: {i}, j: {j}")
                if i < j:
                    swap(lst, i, j)
                    i = i + 1
                    j = j - 1
                else:
                    swap(lst, p_idx, i)
                    break

            sub_quick_sort(lst, left_idx, i)
            sub_quick_sort(lst, i + 1, right_idx)
    # Function Definition Done
    sub_quick_sort(lst, 0, len(lst))


def tim_sort(lst):
    """
    2022.08.07 - frhyme - Init
    https://en.wikipedia.org/wiki/Timsort
    https://d2.naver.com/helloworld/0315536
    """
    pass


def sorting_by(lst, sort_func):
    start_time = time.time()
    sort_func(lst)
    elapsed_time = time.time() - start_time
    print(f"elapsed_time: {elapsed_time: 5.3e} seconds")


if __name__ == '__main__':
    """
    == sorting
    [438, 713, 576, 101, 961, 553, 79, 366, 706, 980]
    == basic sort
    elapsed_time:  2.522e-04 seconds
    == bubble_sort
    elapsed_time:  6.274e-02 seconds
    == selection_sort
    elapsed_time:  3.727e-02 seconds
    == insertion_sort
    elapsed_time:  1.260e-02 seconds
    == merge_sort
    elapsed_time:  7.181e-03 seconds
    == quick_sort
    elapsed_time:  2.312e-03 seconds
    """
    print('== sorting ')
    np.random.seed(10)

    N = 10 ** 1
    lst = np.random.randint(0, 1000, N)
    lst = list(lst)
    print(lst[:10])

    print("== python basic sort")
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
    sorting_by(lst_copy, merge_sort)

    for x, y in zip(benchmark_lst, lst_copy):
        if x != y:
            print("== False result")
            break

    print("== quick_sort")
    lst_copy = lst.copy()
    sorting_by(lst_copy, quick_sort)
    # print(lst_copy)

    for x, y in zip(lst_copy, benchmark_lst):
        if x != y:
            print("== False")
            break

    print("== binary insertion sort")
    lst_copy = lst.copy()
    print(lst_copy)
    sorting_by(lst_copy, binary_insertion_sort)

    print(lst_copy)
    for x, y in zip(lst_copy, benchmark_lst):
        if x != y:
            print("== False")
            break
