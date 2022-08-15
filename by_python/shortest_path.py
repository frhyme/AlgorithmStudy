import networkx as nx
import random
import itertools


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


if __name__ == '__main__':
    print(" == Shortest path")
    random.seed(4)

    g = Graph()

    targetG = nx.complete_graph(4)
    targetG = nx.karate_club_graph()

    # print(targetG.nodes)

    for n1, n2 in targetG.edges():
        targetG[n1][n2]['weight'] = random.randint(1, 100)

    if False:
        for n1, n2 in itertools.combinations(targetG.nodes(), 2):
            bench_l = nx.shortest_path_length(targetG, n1, n2, weight='weight')
            print(f'{n1}, {n2} = {bench_l}')
    if True:
        print(dfs(targetG, 0))
        print(bfs(targetG, 0))




