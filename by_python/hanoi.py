import time

"""
2022.08.07 - frhyme - Init
sub hanoi problem
- start in the middle of the procedure how could it be solved?
"""


def hanoi(n=3, from_p=0, by_p=1, to_p=2):
    """
    2022.08.07 - sng_hn.lee - Init
    """
    if n >= 1:
        hanoi(n - 1, from_p, to_p, by_p)
        print(f"disk {n: 2d} - move from pillar {from_p} to pillar {to_p}")
        hanoi(n - 1, by_p, from_p, to_p)


if __name__ == '__main__':
    print("== This is for hanoi method")
    hanoi(n=5)
