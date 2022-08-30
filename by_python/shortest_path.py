import networkx as nx
import random
import itertools
import time

"""
TO DO LIST:
2022.08.23 - frhyme
- shortest path by Heap should be faster than shortest path basic.
But, in my python code the method with Heap is much slower than basic method.
"""


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = dict()

    def add_node(self, nid: int):
        self.nodes.add(nid)

    def add_edge(self, n1, n2, weight=1, recursive=True):
        self.nodes.add(n1)
        self.nodes.add(n2)

        if n1 not in self.edges:
            self.edges[n1] = dict()
        self.edges[n1][n2] = weight

        if recursive:
            self.add_edge(n2, n1, weight, False)

    def print(self):
        print('== node')
        print(self.nodes, sep=', ')
        print('== edge')
        for n1 in self.edges.keys():
            for n2 in self.edges[n1].keys():
                w = self.edges[n1][n2]
                print(f'({n1}, {n2}, {w})')

    def update_shortest_path(self, n1, n2):
        """
        n1: from nid
        n2: to nid
        """
        INF = 10 ** 10
        visited = set()
        shrt_ps = dict()
        for nid in self.nodes:
            shrt_ps[nid] = INF

        shrt_ps[0] = 0

    def dfs(self, nid) -> list:
        r_lst = list()
        stack = list()
        visited = set()

        stack.add(nid)
        visited.add(n1)

        while len(stack) >= 0:
            n1 = stack.pop()
            print(n1)
            r_lst.append(n1)

            for nbr in self.edges[n1]:
                if nbr not in visited:
                    stack.append(nbr)
                    visited.add(nbr)

    def bfs(self, nid) -> list:
        pass


def dfs(g: nx.Graph, nid) -> list:
    r_lst = list()
    stack = list()
    visited = set()

    stack.append(nid)
    visited.add(nid)

    while len(stack) > 0:
        n1 = stack.pop()
        r_lst.append(n1)

        for nbr in nx.neighbors(g, n1):
            if nbr not in visited:
                stack.append(nbr)
                visited.add(nbr)
    return r_lst


def bfs(g: nx.Graph, nid) -> list:
    r_lst = list()
    queue = list()
    visited = set()

    queue.append(nid)
    visited.add(nid)

    while len(queue) > 0:
        n1 = queue.pop(0)
        r_lst.append(n1)

        for nbr in nx.neighbors(g, n1):
            if nbr not in visited:
                queue.append(nbr)
                visited.add(nbr)
    return r_lst


def shortest_path_basic(g: nx.Graph, from_n, to_n) -> dict:
    def get_smallest_node(dest: dict, visited: dict):
        min_idx = -1
        for k, v in dest.items():
            if not visited[k]:
                if min_idx == -1:
                    min_idx = k
                else:
                    if dest[k] <= dest[min_idx]:
                        min_idx = k
        return min_idx

    INF = 10 ** 10
    dest = dict()
    visited = {nid: False for nid in g.nodes()}

    for nid in g.nodes():
        dest[nid] = INF
    dest[from_n] = 0
    # visited[from_n] = True

    for _ in range(0, len(visited)):
        now = get_smallest_node(dest, visited)
        visited[now] = True

        for nbr in nx.neighbors(g, now):
            calc_v = dest[now] + g[now][nbr]['weight']
            if dest[nbr] >= calc_v:
                dest[nbr] = calc_v
    return dest[to_n]


class Heap:
    def __init__(self):
        self.lst = list()
        self.size = 0

    def print(self):
        print('== heap')
        for i in range(0, self.size):
            print(self.lst[i], end=' ')
        print()

    def parent_idx(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return i * 2 + 1

    def right_child(self, i):
        return i * 2 + 2

    def cmp(self, i, j):
        if self.lst[i][0] < self.lst[j][0]:
            return -1
        elif self.lst[i][0] == self.lst[j][0]:
            return 0
        else:
            return 1

    def swap(self, i, j):
        tmp = self.lst[i]
        self.lst[i] = self.lst[j]
        self.lst[j] = tmp

    def push(self, x):
        # 2022.08.18 - frhyme - do not use append method when you implement heap
        # the actual size of heap and the allocated size of the lst might be different
        # Therefore, the last element which was indicated by the hash.size might be different withe the last element which was appended recently
        if len(self.lst) > self.size:
            self.lst[self.size] = x
        else:
            self.lst.append(x)
        self.size += 1

        cursor = self.size - 1
        p_cursor = self.parent_idx(cursor)

        while cursor >= 0 and p_cursor >= 0:
            if self.cmp(cursor, p_cursor) == -1:
                # cursor is smaller than p_cursor
                self.swap(cursor, p_cursor)
                cursor = p_cursor
                p_cursor = self.parent_idx(cursor)
            else:
                break

    def pop(self):
        if self.size == 0:
            return None
        else:
            r_v = self.lst[0]
            self.swap(0, self.size - 1)
            self.size -= 1

            cursor = 0

            while cursor < self.size:
                left = self.left_child(cursor)
                right = self.right_child(cursor)

                if left < self.size:
                    if right < self.size:
                        # both exists
                        if self.cmp(left, right) == -1:
                            # left smaller
                            if self.cmp(cursor, left) == 1:
                                self.swap(cursor, left)
                                cursor = left
                            else:
                                break
                        else:
                            # right smaller
                            if self.cmp(cursor, right) == 1:
                                self.swap(cursor, right)
                                cursor = right
                            else:
                                break
                    else:
                        # only left exist
                        if self.cmp(cursor, left) == 1:
                            self.swap(cursor, left)
                            cursor = left
                        else:
                            break
                else:
                    # both not exist
                    break
            return r_v

    def top(self):
        return self.lst[0]
# Heap Definition done =================


def shortest_path_advanced(g: nx.Graph, from_n, to_n) -> dict:
    # print("== shortest_path_advanced")
    # Function Definition done ==============

    hp = Heap()

    INF = 10 ** 10
    dest = dict()
    visited = {nid: False for nid in g.nodes()}

    for nid in g.nodes():
        dest[nid] = INF
    dest[from_n] = 0
    # visited[from_n] = True
    hp.push((dest[from_n], from_n))

    while hp.size > 0:
        l, now = hp.pop()
        # print(f"pop: {l}, {now}")

        if visited[now]:
            continue
        else:
            visited[now] = True

        for nbr in nx.neighbors(g, now):
            calc_v = dest[now] + g[now][nbr]['weight']
            # print(f"nbr: {nbr}, {calc_v}")
            if dest[nbr] > calc_v:
                dest[nbr] = calc_v
                hp.push((calc_v, nbr))

    return dest[to_n]


if __name__ == '__main__':
    print("== Shortest path")
    random.seed(4)

    # g = Graph()

    targetG = nx.complete_graph(20)
    targetG = nx.karate_club_graph()

    for n1, n2 in targetG.edges():
        targetG[n1][n2]['weight'] = random.randint(1, 100)

    if True:
        benchmark_duration = 0.0
        my_code_duration = 0.0
        my_adv_code_duration = 0.0
        # print('== benchmark')
        for n1, n2 in itertools.combinations(targetG.nodes(), 2):
            start_time = time.time()
            bench_l = nx.shortest_path_length(targetG, n1, n2, weight='weight')
            benchmark_duration += time.time() - start_time

            start_time = time.time()
            my_l = shortest_path_basic(targetG, n1, n2)
            my_code_duration += time.time() - start_time
            # print(f'custom: {n1}, {n2} = {my_l}')
            assert bench_l == my_l

            # print("- adv")
            start_time = time.time()
            my_l = shortest_path_advanced(targetG, n1, n2)
            my_adv_code_duration += time.time() - start_time
            assert bench_l == my_l

        print(f'- benchmark     duration: {benchmark_duration: .5f}')
        print(f'- my basic code duration: {my_code_duration: .5f}')
        print(f'- my adv code   duration: {my_adv_code_duration: .5f}')

    print('== complete')

    if False:
        print(dfs(targetG, 0))
        print(bfs(targetG, 0))
