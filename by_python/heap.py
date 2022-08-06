import math
import random
import time
import numpy as np
import heapq

"""
2022.08.06 - sng_hn.lee - Init
- my heap is not worse than heapq, heapq is about 50000 faster than mine
- why it happened? and How can i make my heap better?
"""


def bubble_sort(input_lst: list):
    """
    2022.08.06 - Init
    """
    for i in range(0, len(input_lst) - 1):
        for j in range(i + 1, len(input_lst)):
            if input_lst[i] > input_lst[j]:
                input_lst[i], input_lst[j] = input_lst[j], input_lst[i]


class Heap:
    """
    2022.08.06 - sng_hn.lee - Init
    default min heap
    """
    def __init__(self):
        self.lst = list()

    def size(self):
        return len(self.lst)

    def depth(self):
        return int(math.log2(len(self.lst))) + 1

    def get_parent_idx(self, idx):
        if idx == 0:
            return None
        else:
            return (idx - 1) // 2

    def get_left_child_idx(self, idx):
        if (idx * 2 + 1) >= len(self.lst):
            return None
        else:
            return idx * 2 + 1

    def get_right_child_idx(self, idx):
        if (idx * 2 + 2) >= len(self.lst):
            return None
        else:
            return idx * 2 + 2

    def swap(self, i, j):
        self.lst[i], self.lst[j] = self.lst[j], self.lst[i]

    def push(self, x):
        self.lst.append(x)
        idx = self.size() - 1

        while True:
            p_idx = self.get_parent_idx(idx)
            if p_idx is None:
                break
            else:
                if self.lst[idx] < self.lst[p_idx]:
                    self.swap(idx, p_idx)
                    idx = p_idx
                else:
                    break

    def pop(self):
        r_value = self.lst[0]
        self.swap(0, self.size() - 1)
        self.lst.pop()
        idx = 0

        while True:
            left_idx = self.get_left_child_idx(idx)
            right_idx = self.get_right_child_idx(idx)

            if left_idx is None:
                break
            else:
                if right_idx is None:
                    # only left exists
                    if self.lst[left_idx] < self.lst[idx]:
                        self.swap(left_idx, idx)
                        idx = left_idx
                    else:
                        break
                else:
                    # both exists
                    if self.lst[left_idx] < self.lst[right_idx]:
                        if self.lst[left_idx] < self.lst[idx]:
                            self.swap(left_idx, idx)
                            idx = left_idx
                        else:
                            break
                    else:
                        if self.lst[right_idx] < self.lst[idx]:
                            self.swap(right_idx, idx)
                            idx = right_idx
                        else:
                            break
        return r_value

    def print(self):
        print("==" * 30)
        print(f"size: {self.size()}")
        print(f"depth: {self.depth()}")
        print(self.lst)


if __name__ == "__main__":
    my_heap = Heap()

    N = 10 ** 4

    target_lst = np.random.randint(0, 1000, N)
    benchmark_heap = list(target_lst.copy())
    heapq.heapify(benchmark_heap)

    for x in target_lst:
        my_heap.push(x)
        heapq.heappush(benchmark_heap, x)

    start_time = time.time()
    sorted_heap_lst_by_me = list()
    while my_heap.size() > 0:
        sorted_heap_lst_by_me.append(my_heap.pop())
    print("== my_heap:")
    print(f'elapsed time: {time.time() - start_time:e}')
    # print(sorted_heap_lst)

    start_time = time.time()
    sorted_heap_lst_by_heapq = list()
    while my_heap.size() > 0:
        sorted_heap_lst_by_heapq.append(heapq.heappop(benchmark_heap))
    print("== heapq :")
    print(f'elapsed time: {time.time() - start_time:e}')

    is_same = True
    for x, y in zip(sorted_heap_lst_by_me, sorted_heap_lst_by_heapq):
        if x != y:
            is_same = False
            break
    print(f'== validation: {is_same}')
