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

class RSA:
    def __init__(self, n, p, q):
        self.n = n
        self.p = p
        self.q = q
        self.calculate_keys()

    def public_key_generator(self) -> int:
        fi = (self.p-1)*(self.q-1)
        for e in reversed(range(1, fi)):
            if euclidean_algorithm(fi, e)==1:
                self.e = e

    def private_key_generator(self) -> int:
        for d in range(0, self.n):
            if (self.e*d)%self.n==1:
                self.d = d

    def calculate_keys(self):
        self.public_key_generator()
        self.private_key_generator()

    def encrypt(self, m) -> int: return (m^self.e)%self.n 

    def decrypt(self, c) -> int: return (c^self.d)%self.n

def find_carmichael_numbers(n) -> list: return [ a for a in range(1, n) if fermat_primality__test(n=a) and not Rabin.miller_rabin(n=a) ]

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

    @staticmethod
    def miller_rabin_primality_test(n) -> bool: return Rabin.miller_rabin_primality_test(n=n) if fermat_primality__test(n=n) and fermat_primality__test(n=n) else False

    @staticmethod
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

def baby_step_giant_step_algorithm(module, generator, number):
    import math as math
    # Solve x with number = generator^x (mod module)
    s = math.ceil(math.sqrt(module))
    for bs in  [ ( number*generator^j, j) for j in range(0, s+1) ]:
        for gs in [ ( generator^(s*i), i) for i in range(0, s+1) ]:
            if bs[0] == gs[0]: return gs[1]*bs[0]-bs[1]

class ElicpticCurveArithmetic:

    VECTOR_SUM = lambda x, y: ( x[0]+y[0], x[1]+y[1])
    
    DOUBLE_VECTOR = lambda x: ( x[0]+x[0], x[1]+x[1])

    NEGATIVE_POINT = lambda x: ( x[0]*(-1), x[1]*(-1))

    @staticmethod
    def scalar_multiplication(P: tuple, k: int): return ElicpticCurveArithmetic.VECTOR_SUM( ElicpticCurveArithmetic.scalar_multiplication(P, k-1), P) if k>1 else P

    @staticmethod
    def discrete_logarithm_problem( Q: tuple, P: tuple, number: int):
        for k in range(number): 
            if ElicpticCurveArithmetic.scalar_multiplication(P=P, k=k) == Q: return k

class AffineCaesarCipher:
    
    CIPHER = lambda l, a, b: (a*l + b) % 26

    # Show that for an affine Caesar cipher scheme to be one-to-one or not, does not
    # depend on the choice of b.


    # Determine a necessary and sufficient condition on the value of a for an affine Caesar
    # cipher scheme to be one-to-one.

    # How many one-to-one affine Caesar cipher schemes do there exist.

    @staticmethod
    def decrypt(c, a,b):  return None

    @staticmethod
    def find_key_pair_of_c(c): return None, None

if __name__ == "__main__":
 pass