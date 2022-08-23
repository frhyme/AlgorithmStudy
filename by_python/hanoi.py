import time

"""
2022.08.07 - frhyme - Init
- How can i make this with call stack
- sub hanoi problem
start in the middle of the procedure how could it be solved?
2022.08.08 - frhyme
- to make this as non recursive code is too difficult to solve, check follow link to implement it1
https://en.wikipedia.org/wiki/Tower_of_Hanoi
"""


def init_hanoi(n=3) -> list:
    r_lst = list()
    r_lst.append([i for i in range(n, 0, -1)])
    for i in range(0, n - 1):
        r_lst.append([])
    return r_lst


def print_hanoi(hanoi) -> None:
    for each_pillar in hanoi:
        print(each_pillar)


def hanoi_recursion(hanoi, n=3, from_p=0, by_p=1, to_p=2):
    if n >= 1:
        hanoi_recursion(hanoi, n - 1, from_p, to_p, by_p)
        hanoi[to_p].append(hanoi[from_p].pop())

        print(f"disk {n: 2d} - move from pillar {from_p} to pillar {to_p}")
        print_hanoi(hanoi)

        hanoi_recursion(hanoi, n - 1, by_p, from_p, to_p)


def hanoi_stack(n=3, from_p=0, by_p=1, to_p=2):
    """
    2022.08.07 - sng_hn.lee - Init
    - a little hard to implement
    2022.08.08 - sng_hn.lee - queue may be useful
    """
    hanoi_call_stack1 = list()
    hanoi_call_stack2 = list()

    hanoi_call_stack1.append((n, from_p, by_p, to_p))

    while len(hanoi_call_stack1) > 0:
        n, from_p, by_p, to_p = hanoi_call_stack1[-1]
        if n > 1:
            hanoi_call_stack1.append((n - 1, from_p, to_p, by_p))
        else:
            n, from_p, by_p, to_p = hanoi_call_stack1.pop()
            print(f"disk {n: 2d} - move from pillar {from_p} to pillar {to_p}")
            break


if __name__ == '__main__':
    N = 3
    print('--' * 30)
    print("== hanoi method by recursion")
    hanoi = init_hanoi(n=N)
    print_hanoi(hanoi)
    hanoi_recursion(hanoi)
    print('--' * 30)

    print("== hanoi method by call stack")
    hanoi = init_hanoi(n=N)
    hanoi_stack(n=N)
    print('--' * 30)
