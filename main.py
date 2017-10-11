from prime_generator import generate_large_prime

def extended_gcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


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

    e = 65537

    while True:
        p = generate_large_prime(512)
        q = generate_large_prime(512)
        gcd, x, y = extended_gcd((p-1)*(q-1), e)
        if gcd == 1:
            break
    print("gcd: ", gcd)
    print("x: ", x)
    print("y: ", y)
    print("p: ", p)
    print("q: ", q)
    print("p*q: ", p*q)


if __name__ == "__main__":
    main()
