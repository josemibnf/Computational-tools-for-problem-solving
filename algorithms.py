def euclidean_algorithm(x, y) -> int: return euclidean_algorithm(x=y, y=x%y) if x%y!=0 else y

def extended_euclidean_algorithm(x, y, s=1, t=0, S=0, T=1) -> float: return extended_euclidean_algorithm(x=y, y=x%y, s=S, t=T, S=s-x/y*S, T=t-x/y*T ) if x%y!=0 else s*x+t*y

def fermat_little__theorem(n, a=1) -> bool: return (fermat_little__theorem(n=n, a=a+1) if a^(n-1)%n==1 else False ) if a<n else True

def is_not_prime(n):
    return True

def find_carmichael_numbers(n) -> list: return [ a for a in range(1, n) if fermat_little__theorem(n=a) and is_not_prime(a)]



