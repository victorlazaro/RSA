
def extended_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def mod_exp(g, s, p):
    # g^s%p
    number = 1
    while s:
        if s & 1:
            number = number * g % p
        s >>= 1
        g = g * g % p
    return number


def main():
    # g = 5
    # s = generate_large_prime(500)
    # p = generate_large_prime(500)
    # moded = mod_exp(g, s, p)

    # print('s = {}\np = {}\nmoded = {}'.format(s, p, moded))
    extended_gcd(240, 46)

if __name__ == "__main__":
    main()
