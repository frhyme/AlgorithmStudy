"""
- string은 각각 birth_date, lifeSpan, deatDate(birthDate + lifeSpan) 을 가진다.
- timestamp 가 증가하면서 deathDate에 도달하면 해당 string은 삭제된다.
- string이 추가될 때, 새로운 string과 consecutive character more 3, they could be friends, then new string's deathDate is going to be assigned to their friends
- get alive strings at timstamp, with specific strLength

2022-08-14 (Sun) - all strNode should be sorted by closest deathDate
- it is better to hashMap by deathDate
2022-08-15 (Mon) - get each node by heap
"""


class StringNode:
    def __init__(self, s: str, birthDate: int, lifeSpan: int):
        self.s = s
        self.birthDate = birthDate
        self.lifeSpan = lifeSpan
        self.deathDate = self.birthDate + self.lifeSpan

    def __repr__(self):
        fs = f"{self.s} - {self.birthDate: 3d} to {self.deathDate: 3d}"
        return fs

    def len(self):
        return len(self.s)


class Heap:
    def __init__(self):
        self.lst = list()
        self.is_min = True
        self.size = 0

    def cmp(self, i, j):
        if self.lst[i].deathDate < self.lst[j].deathDate:
            return -1
        elif self.lst[i].deathDate == self.lst[j].deathDate:
            return 0
        else:
            return 1

    def swap(self, i, j):
        tmp = self.lst[i]
        self.lst[i] = self.lst[j]
        self.lst[j] = tmp

    def get_parent(self, i: int):
        return (i - 1) // 2

    def get_left(self, i: int):
        return (i * 2) + 1

    def get_right(self, i: int):
        return (i * 2) + 2

    def push(self, sn: StringNode):
        self.lst.append(sn)
        self.size += 1

        cursor = self.size - 1
        p_cursor = self.get_parent(cursor)

        while cursor >= 0 and p_cursor >= 0:
            if self.cmp(cursor, p_cursor) == 1:
                self.swap(cursor, p_cursor)
                cursor = p_cursor
                p_cursor = self.get_parent(cursor)
            else:
                break

    def pop(self) -> StringNode:
        # print('== pop')
        r = self.lst[0]

        if self.size == 1:
            self.size -= 1
            return r
        elif self.size == 0:
            return None
        else:
            self.swap(0, self.size - 1)
            self.size -= 1

            cursor = 0
            l_cursor = self.get_left(cursor)
            r_cursor = self.get_right(cursor)

            while cursor < self.size and l_cursor < self.size and r_cursor < self.size:
                # print(cursor, l_cursor, r_cursor)
                if self.cmp(l_cursor, r_cursor) == 1:
                    # left is small
                    if self.cmp(cursor, l_cursor) == -1:
                        break
                    else:
                        self.swap(cursor, l_cursor)
                        cursor = l_cursor
                else:
                    # right is small or equal
                    if self.cmp(cursor, r_cursor) == -1:
                        break
                    else:
                        self.swap(cursor, r_cursor)
                        cursor = r_cursor
                l_cursor = self.get_left(cursor)
                r_cursor = self.get_right(cursor)
            return r

    def top(self) -> StringNode:
        return self.lst[0]

    def print(self):
        for i in range(0, self.size):
            x = self.lst[i]
            print(x, end=" ")
        if self.size > 0:
            print()


def is_consecutive_same(s1: str, s2: str, n: int = 3):
    """
    2022.08.12 - frhyme - Init
    - is this enough efficienl algorithm?
    """
    is_partial_same = False

    for i in range(0, len(s1) - n + 1):
        for j in range(0, len(s2) - n + 1):
            if s1[i] == s2[j]:
                char_same_count = 0
                for k in range(0, n):
                    if s1[i + k] == s2[j + k]:
                        char_same_count += 1
                    else:
                        break
                if char_same_count == n:
                    is_partial_same = True
                    break
                else:
                    continue
            else:
                continue
    return is_partial_same


class HashDict:
    def __init__(self):
        self.hashmap = dict()
        self.fr = Friends()
        self.timestamp = 0

    def hash(self, strNode: StringNode):
        return strNode.len()

    def initialize(self):
        pass

    def push(self, strNode: StringNode):
        k = self.hash(strNode)
        if k not in self.hashmap.keys():
            self.hashmap[k] = Heap()
        self.hashmap[k].push(strNode)
        self.fr.add_friend(strNode)

    def print(self):
        print("== HashDict ============================")
        for k in self.hashmap.keys():
            self.hashmap[k].print()
        self.fr.print()

    def tick(self):
        self.timestamp += 1
        print(f"== tick at timestamp: {self.timestamp}")

        for k in self.hashmap.keys():
            while self.hashmap[k].top().deathDate <= self.timestamp and self.hashmap[k].size > 0:
                sn = self.hashmap[k].pop()
                self.fr.del_friend(sn)


class Friends:
    def __init__(self):
        self.friends_lst = list()

    def add_friend(self, sn1: StringNode):
        friends_idx = -1
        for i, each_set in enumerate(self.friends_lst):
            for sn2 in each_set:
                if is_consecutive_same(sn1.s, sn2.s):
                    friends_idx = i
                    break
            if friends_idx != -1:
                break
        if friends_idx == -1:
            # not yet deciede
            new_set = set()
            new_set.add(sn1)
            self.friends_lst.append(new_set)
        else:
            self.friends_lst[friends_idx].add(sn1)

            friends_idx_lst = list()
            for i in range(friends_idx + 1, len(self.friends_lst)):
                for sn2 in self.friends_lst[i]:
                    if is_consecutive_same(sn1.s, sn2.s):
                        friends_idx_lst.append(i)
                        break
            # update
            for i in friends_idx_lst:
                self.friends_lst[friends_idx].update(self.friends_lst[i])
            # delete each set:
            for i in sorted(friends_idx_lst, reverse=True):
                del self.friends_lst[i]
            # set same deathDate
            for _sn in self.friends_lst[friends_idx]:
                _sn.deathDate = sn1.deathDate

    def find_friends_idx(self, sn: StringNode):
        target_idx = -1
        for i, each_set in enumerate(self.friends_lst):
            if sn in each_set:
                target_idx = i
        return target_idx

    def del_friend(self, sn: StringNode):
        target_idx = -1
        for i, each_set in enumerate(self.friends_lst):
            if sn in each_set:
                target_idx = i
        if target_idx != -1:
            del self.friends_lst[target_idx]
        else:
            pass

    def print(self):
        print("== Friends ========================")
        for each_set in self.friends_lst:
            print(each_set)


if __name__ == "__main__":
    print("== This is main code")

    hd = HashDict()
    # fr = Friends()

    s_lst = ['member', 'barbeque', 'memory', 'barber', 'abcdefg']
    b_lst = [0, 0, 0, 0, 0, 0]
    l_lst = [3, 4, 5, 6, 10]

    for s, b, l in zip(s_lst, b_lst, l_lst):
        sn = StringNode(s, b, l)
        hd.push(sn)
        # hd.print()
        # fr.print()
    hd.tick()
    hd.tick()
    hd.tick()
    hd.tick()
    hd.tick()
    hd.print()
    hd.tick()
    hd.print()

