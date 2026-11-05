# Reference code from Appendix B of the paper (verbatim).
from sympy import primorial, prime, isprime, primerange
from math import gcd
from itertools import combinations

def orbit_minima(k):
    """B_k: smallest representative of every square class of U(M_k)."""
    M = int(primorial(k)); best = {}
    for y in range(1, M):
        if gcd(y, M) == 1:
            s = y * y % M
            if s not in best:      # y increases, so the first hit is the minimum
                best[s] = y
    return M, sorted(best.values())

def check(k):
    M, B = orbit_minima(k); pk, pn = prime(k), prime(k + 1)
    phi = 1
    for i in range(1, k + 1): phi *= prime(i) - 1
    low  = [b for b in B if 1 < b <= pn * pn]
    pred = list(primerange(pk + 1, pn * pn)) + [pn * pn]
    comp = [b for b in B if b > 1 and not isprime(b)]
    return dict(k=k, orbits=len(B), formula=phi // 2**(k - 1),
                completeness=(low == pred), smallest_composite=min(comp) if comp else None,
                p_next=min(b for b in B if b > 1))

def local_minima(k):
    """Units smaller than all single-flip neighbours sigma_j(a)."""
    M = int(primorial(k)); E = []
    for j in range(2, k + 1):
        p = prime(j); m = M // p
        E.append(next(e for e in range(1, M) if e % p == p - 1 and e % m == 1 % m))
    return sum(1 for a in range(1, M) if gcd(a, M) == 1
               and all(a < e * a % M for e in E))

def incidences():
    U = [a for a in range(1, 30) if gcd(a, 30) == 1]
    face = lambda S: all((a + b) % 30 for a, b in combinations(S, 2))
    edges = [S for S in combinations(U, 2) if face(S)]
    facets = [S for S in combinations(U, 3) if face(S)]
    cells = [S for S in combinations(U, 4) if face(S)]
    return len(edges), len(facets), len(cells)   # (24, 32, 16)

if __name__ == "__main__":
    for k in range(3, 8):
        print(check(k), local_minima(k) if k <= 6 else "")
    print(incidences())
