def euclidean_algorithm(x, y) -> int: return euclidean_algorithm(x=y, y=x%y) if x%y!=0 else y

def extended_euclidean_algorithm(x, y, s=1, t=0, S=0, T=1) -> float: return extended_euclidean_algorithm(x=y, y=x%y, s=S, t=T, S=s-x/y*S, T=t-x/y*T ) if x%y!=0 else (s, t)

def fermat_primality__test(n, a=1) -> bool: return (fermat_primality__test(n=n, a=a+1) if a^(n-1)%n==1 or a^(n-1)%n==-1 else False ) if a<n else True

def fermat_factory_method(n) -> tuple:
    import math
    k = math.ceil(math.sqrt(n))
    h = k**2-n
    sh = math.sqrt(abs(h))
    while not sh.is_integer():
        k +=1
        h = k**2-n
        sh = math.sqrt(abs(h))
    return k-sh, k+sh

def euler_function(n) -> int: return len([ m for m in range(1, n) if m<n and euclidean_algorithm(n,m)==1 ])

def rsa_public_key_generator(n, p, q) -> int:
    fi = (p-1)*(q-1)
    for e in reversed(range(1, fi)):
        if euclidean_algorithm(fi, e)==1:
            return e

def rsa_private_key_generator(n, e) -> int:
    for d in range(0, n):
        if (e*d)%n==1:
            return d

def find_carmichael_numbers(n) -> list: return [ a for a in range(1, n) if fermat_primality__test(n=a) and not miller_rabin(n=a) ]

def miller_rabin_primality_test(n) -> bool: return miller_rabin_primality_test(n=n) if fermat_primality__test(n=n) and fermat_primality__test(n=n) else False

def miller_rabin(n, k=40):
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

class Rabin:
    def rabin_key_generator(self) -> int:
        import random
        p=11
        q=17
        return p*q, p, q

    def rabin_encryption(self, message) -> int: 
        n = self.rabin_key_generator()[0]
        return int(message)^2%n if int(message) < n else None

    def rabin_decryption(self, crypted, p, q) -> tuple:
        yp, yq = extended_euclidean_algorithm(p, q)
        mq, mp = crypted^((p+1)/4)%p, crypted^((q+1)/4)%q
        return (
            yp*p*mq+yq+q+mp,
            p*q-yp*p*mq+yq+q+mp,
            yp*p*mq-yq*q*mp,
            p*q-yp*p*mq-yq*q*mp
        )

if __name__ == "__main__":
    n = 17947
    e= 3929
    fi = euler_function(n)
    print(  )
