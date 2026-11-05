"""
Numerical checks for
  T. Krause, "A Cross-Polytope Geometry of the Primes: Orbit Minima,
  Exact Residue Counts, and Singular Series" (2026).

Recomputes the numerical findings [N] of the paper with an independent
NumPy sieve up to 10^8. Requirements: Python 3.9+, numpy, sympy, mpmath.
Runtime: a few minutes, memory about 1 GB.

Usage:  python numerics_check.py
"""
import math
import time
from math import gcd

import numpy as np
from sympy import prime, primorial
import mpmath as mp

X = 10**8


def sieve(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    s[4::2] = False
    for p in range(3, int(n**0.5) + 1, 2):
        if s[p]:
            s[p * p::2 * p] = False
    return s


def Li_k(x, k):
    """Integral from 2 to x of dt / log(t)^k."""
    return float(mp.quad(lambda t: 1 / mp.log(t) ** k, [2, 10, 1e3, 1e5, x]))


def section(title):
    print("\n" + "=" * 70 + "\n" + title + "\n" + "=" * 70)


def main():
    t0 = time.time()
    isp = sieve(X + 64)
    P = np.flatnonzero(isp[: X + 1])
    print(f"sieve up to {X:.0e}: pi(x) = {len(P)}  ({time.time() - t0:.1f}s)")

    # ---------------------------------------------------------------
    section("Observation 4.11: local minima vs orbit minima, k = 3..8")
    for k in range(3, 9):
        M = int(primorial(k))
        a = np.arange(1, M, dtype=np.int64)
        g = np.gcd(a, M)
        a = a[g == 1]
        # orbit minima: first unit in every square class
        sq = (a * a) % M
        _, first = np.unique(sq, return_index=True)
        n_orbit = len(first)
        # local minima: smaller than all single-flip neighbours
        is_loc = np.ones(len(a), dtype=bool)
        for j in range(2, k + 1):
            p = int(prime(j))
            m = M // p
            # e = -1 mod p, +1 mod M/p  (CRT)
            e = (m * pow(m, -1, p) * (p - 1) + p * pow(p, -1, m)) % M
            is_loc &= a < (e * a) % M
        print(f"k={k}: local minima {is_loc.sum():>7}   orbit minima {n_orbit:>6}")

    # ---------------------------------------------------------------
    section("Observation 6.x: primes in (p_k^2, p_{k+1}^2), k = 2..15")
    out = []
    for k in range(2, 16):
        a, b = int(prime(k)) ** 2, int(prime(k + 1)) ** 2
        out.append(int(isp[a + 1:b].sum()))
    print(out)

    # ---------------------------------------------------------------
    section("Twin edge: renormalised density N_k/phi(M_k) * log p_k / (2 e^-gamma)")
    eg = math.exp(-0.5772156649015329)
    ratio = 1.0
    for k in range(2, 40):
        p = int(prime(k))
        if p >= 3:
            ratio *= (p - 2) / (p - 1)  # N_k({0,2}) / phi(M_k)
        if k in (3, 6, 10, 39):
            print(f"k={k:>2}: {ratio * math.log(p) / (2 * eg):.4f}")
    C2 = 1.0
    for p in P[1:200000]:
        p = float(p)
        C2 *= 1 - 1 / (p - 1) ** 2
    print(f"C2 (truncated product) = {C2:.7f}")

    # ---------------------------------------------------------------
    section("Twin primes pi_2(x) vs 2 C2 Li_2(x)")
    tw = P[isp[P + 2]]
    for e in range(4, 9):
        x = 10**e
        n = int((tw <= x - 2).sum())
        pred = 2 * C2 * Li_k(x, 2)
        print(f"x=1e{e}: pi_2={n:>7}  pred={pred:>9.0f}  ratio={n / pred:.4f}")

    section("Polignac ratios up to 1e8 (pairs p, p+d both prime) / twins")
    n2 = int((tw <= X - 2).sum())
    for d in (6, 30):
        nd = int((P[P <= X - d][isp[P[P <= X - d] + d]]).size)
        print(f"d={d}: {nd} pairs, ratio to twins {nd / n2:.3f}")

    # ---------------------------------------------------------------
    section("Goldbach: mean r(N) for even N in (20000, 40000]")
    L = 40000
    v = isp[: L + 1].astype(np.int64)
    r = np.convolve(v, v)[: L + 1]  # ordered pairs p+q=N
    groups = {"30|N": [], "6|N,30∤N": [], "10|N,30∤N": [], "other": []}
    for N in range(20002, L + 1, 2):
        if N % 30 == 0:
            groups["30|N"].append(r[N])
        elif N % 6 == 0:
            groups["6|N,30∤N"].append(r[N])
        elif N % 10 == 0:
            groups["10|N,30∤N"].append(r[N])
        else:
            groups["other"].append(r[N])
    base = np.mean(groups["other"])
    for kname, vals in groups.items():
        m = np.mean(vals)
        print(f"{kname:>11}: mean r(N) = {m:8.1f}   ratio to 'other' {m / base:.2f}")

    # ---------------------------------------------------------------
    section("Residue classes mod 30 up to 1e8 and consecutive repetitions")
    Q = P[P > 5]
    res = Q % 30
    for c in (1, 7, 11, 13, 17, 19, 23, 29):
        print(f"class {c:>2}: {(res == c).sum()}")
    same = np.mean(res[1:] == res[:-1])
    print(f"proportion of consecutive primes in the same class: {same:.4f}")

    # ---------------------------------------------------------------
    section("Triplets and quadruplets up to 1e8")
    Pq = P[P <= X - 8]
    t1 = int((isp[Pq + 2] & isp[Pq + 6]).sum())
    t2 = int((isp[Pq + 4] & isp[Pq + 6]).sum())
    q4 = int((isp[Pq + 2] & isp[Pq + 6] & isp[Pq + 8]).sum())

    def sing(H, nprimes=200000):
        S = 1.0
        for p in P[:nprimes]:
            p = int(p)
            nu = len({h % p for h in H})
            S *= (1 - nu / p) / (1 - 1 / p) ** len(H)
        return S

    S3, S4 = sing((0, 2, 6)), sing((0, 2, 6, 8))
    print(f"{{0,2,6}}: {t1}   {{0,4,6}}: {t2}   pred {S3 * Li_k(X, 3):.0f}  (S={S3:.4f})")
    print(f"{{0,2,6,8}}: {q4}   pred {S4 * Li_k(X, 4):.0f}  (S={S4:.4f})")

    # ---------------------------------------------------------------
    section("Primes n^2 + 1, n <= x, against (C/2) * int_2^x dt/log t")
    n = np.arange(1, 200001, dtype=np.int64)
    vals = n * n + 1
    from sympy import isprime
    flags = np.array([isprime(int(v)) for v in vals])
    C = 1.0
    for p in P[1:200000]:
        p = int(p)
        chi = 1 if p % 4 == 1 else -1
        C *= 1 - chi / (p - 1)
    for x in (10**3, 10**4, 10**5, 2 * 10**5):
        cnt = int(flags[:x].sum())
        pred = C / 2 * Li_k(x, 1)
        print(f"x={x:>6}: count {cnt:>6}  pred {pred:8.0f}")
    print(f"C = {C:.5f}")

    # ---------------------------------------------------------------
    section("Collatz: starting values whose trajectory maximum is 9232")
    def traj_max(s):
        m = s
        while s != 1:
            s = 3 * s + 1 if s & 1 else s >> 1
            if s > m:
                m = s
        return m
    for Nmax in (10**4, 10**5, 10**6):
        c = sum(1 for s in range(1, Nmax + 1) if traj_max(s) == 9232)
        print(f"N={Nmax:>7}: {c}")

    print(f"\ntotal runtime {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
