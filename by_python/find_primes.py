import time


def is_prime_benchmark(n: int) -> bool:
    if 1 < n:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    else:
        return False


def is_prime(n: int) -> bool:
    if 1 < n:
        if n % 2 == 0 and n != 2:
            return False
        for i in range(3, int(n ** (0.5) + 1), 2):
            if n % i == 0:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    """
    --------------------------------------------------------------------------------
    == is_prime - benchmark
    == elapsed time: 0.3050079345703125
    --------------------------------------------------------------------------------
    == is_prime - improved
    == elapsed time: 0.006582021713256836
    Set Equivalent:  True
    """
    print('--' * 40)
    end_n = 10 ** 4
    print('== is_prime - benchmark')
    start_time = time.time()
    prime_set_benchmark = set()
    for n in range(2, end_n):
        is_p = is_prime_benchmark(n)
        if is_p:
            prime_set_benchmark.add(n)
    print(f"== elapsed time: {time.time() - start_time}")

    print('--' * 40)
    print('== is_prime - improved')
    start_time = time.time()
    prime_set = set()
    for n in range(2, end_n):
        is_p = is_prime(n)
        if is_p:
            prime_set.add(n)
    print(f"== elapsed time: {time.time() - start_time}")

    print("Set Equivalent: ", prime_set_benchmark == prime_set)
