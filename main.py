from lib import random_prime, calc_d, calc_k, calc_n, calc_e

p = random_prime()
q = random_prime(exclude=(p,))
n = calc_n(p, q)
k = calc_k(p, q)
e = calc_e(p, q, n, k)
d = calc_d(e, k)

print(f'p: {p}, q: {q}, n: {n}, k: {k}, e: {e}, d: {d}')
plain_message: int = int(input('message to encrypt? '))
encrypted_message = plain_message ** e % n
print(f'encrypted message: {encrypted_message}')
decrypted_message = encrypted_message ** d % n
print(f'decrypted message: {decrypted_message}')
