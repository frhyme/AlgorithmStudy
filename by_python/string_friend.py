"""
- string은 각각 birth_date, lifeSpan, deatDate(birthDate + lifeSpan) 을 가진다.
- timestamp 가 증가하면서 deathDate에 도달하면 해당 string은 삭제된다.
- string이 추가될 때, 새로운 string과 consecutive character more 3, they could be friends, then new string's deathDate is going to be assigned to their friends
- get alive strings at timstamp, with specific strLength
"""


# how to fix these automatically
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

    def hash(self, strNode: StringNode):
        return strNode.len()

    def initialize(self):
        pass

    def push(self, strNode: StringNode):
        k = self.hash(strNode)
        if k not in self.hashmap.keys():
            self.hashmap[k] = list()
        self.hashmap[k].append(strNode)

    def delete(self, strNode: StringNode):
        k = self.hash(strNode)
        self.hashmap[k].remove(StringNode)

    def print(self):
        print("== HashDict ============================")
        for k in self.hashmap.keys():
            if len(self.hashmap[k]) != 0:
                print(f"== key: {k}")
                for s in self.hashmap[k]:
                    print(s)


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

    def print(self):
        print("== Friends ========================")
        for each_set in self.friends_lst:
            print(each_set)

    def del_friend(self, strNode: StringNode):
        pass



if __name__ == "__main__":
    print("== This is main code")

    hd = HashDict()
    fr = Friends()

    s_lst = ['member', 'barbeque', 'memory', 'barber']
    b_lst = [0, 0, 0, 0]
    l_lst = [3, 4, 5, 6]

    for s, b, l in zip(s_lst, b_lst, l_lst):
        sn = StringNode(s, b, l)
        hd.push(sn)
        fr.add_friend(sn)
        hd.print()
        fr.print()









