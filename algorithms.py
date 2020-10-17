def euclidean_algorithm(x, y) -> int: return euclidean_algorithm(x=y, y=x%y) if x%y!=0 else y

def extended_euclidean_algorithm(x, y, s=1, t=0, S=0, T=1) -> float: return extended_euclidean_algorithm(x=y, y=x%y, s=S, t=T, S=s-x/y*S, T=t-x/y*T ) if x%y!=0 else s*x+t*y

def fermat_primality__test(n, a=1) -> bool: return (fermat_primality__test(n=n, a=a+1) if a^(n-1)%n==1 or a^(n-1)%n==-1 else False ) if a<n else True

def is_prime(n): return False

def find_carmichael_numbers(n) -> list: return [ a for a in range(1, n) if fermat_primality__test(n=a) and not is_prime(a) ]

def miller_rabin_primality_test(n) -> bool: return miller_rabin_primality_test(n=n) if fermat_primality__test(n=n) and other(n=n) else False

def miller_rabin(n, k):
    import random

    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True