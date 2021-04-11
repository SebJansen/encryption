# decides whether a number is prime or not
from random import randrange


def is_prime(num: int) -> bool:
    i: int = 2

    # uses a while loop for tail call elimination
    while i < num:
        if num % i == 0:
            # `num` is not prime, because `num` === 0 (mod i)
            return False
        # `num` is `not not prime` for now,
        # keep trying exhaustively
        i += 1

    # implicitly, the number is prime
    return True


# generates a random prime number,
# and optionally excludes some for uniqueness
def random_prime(stop=3 ** 4, exclude=()) -> int:
    # exhaustively try to find a prime number
    while True:
        # generate a random number, and try in
        # increments of 2, to skip even numbers
        prime = randrange(start=3, stop=stop, step=2)

        # check if random number is prime
        if is_prime(prime) and prime not in exclude:
            return prime


def calc_n(ip, iq):
    return ip * iq


def calc_k(ip, iq):
    return (ip - 1) * (iq - 1)


def calc_e(p, q, n, k):
    return random_prime(stop=k - 1, exclude=(p, q, n, k))


def calc_d(ie, ik):
    i = 1
    while True:
        # calculate the inverse of e (mod k)
        # and check if it is equivalent to 1
        if i * ie % ik == 1:
            return i
        i += 1
