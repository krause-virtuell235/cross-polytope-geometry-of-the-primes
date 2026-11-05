# A Cross-Polytope Geometry of the Primes: Orbit Minima, Exact Residue Counts, and Singular Series

**Author:** Thomas Krause, Independent Researcher, Lübeck, Germany (ORCID 0009-0004-3867-9941)
**Suggested subject:** Computer Science and Mathematics → Algebra and Number Theory
**Keywords:** cross-polytope; 16-cell; primorial; unit group; sign-flip action; orbit minima; singular series; Hardy–Littlewood; Goldbach; prime k-tuples

---

## Short description (about 100 words)

Every prime above 5 falls into one of eight residue classes modulo 30. Pairing each class with its mirror image turns these eight classes into the vertices of the 16-cell, the four-dimensional cross-polytope. Repeating the construction at every primorial 210, 2310, … gives a whole cascade of cross-polytopes. The paper proves four structural theorems for this cascade, including a sharp completeness theorem: from modulus 30030 on, the orbit minima in a precise window are exactly the primes. It then uses one uniform scheme to compute the exact local factors of the classical prime problems.

---

## Full description

**What the paper is.** This is a self-contained synthesis of a series of studies on the geometry of the primes. It is written for two audiences at once. Every section opens with an "In plain words" box that explains the idea without formulas, and the technical text gives complete definitions, theorems and proofs. Each statement carries a status mark: proved, exact geometric reformulation, numerical, heuristic or open. Readers can therefore always see what has been shown and what has only been observed.

**The idea behind the approach.** The starting point is a simple observation.

- Removing the multiples of 2, 3 and 5 leaves eight residues modulo 30: 1, 7, 11, 13, 17, 19, 23, 29.
- The mirror map a ↦ 30 − a pairs them into four axes.
- Four axes with two ends each are exactly the eight vertices of the 16-cell.

The paper takes this seriously and carries it to every primorial M_k = 2·3·5·…·p_k. The units modulo M_k become the vertices of a cross-polytope. A natural group of sign flips acts on them: one switch per odd prime, which changes the sign of a residue modulo that prime alone. The smallest member of each orbit, its orbit minimum, becomes the central object. In this way questions about primes become questions about vertices, edges, cells and symmetries of a well-understood geometric object.

**What it proves.** Four structural theorems organise the cascade.

1. **Symmetry.** The orbits are exactly the square classes of the unit group, and the sign-flip group is its 2-torsion.
2. **Completeness.** For every k ≥ 6, the orbit minima up to p_{k+1}² are precisely the primes in that range together with p_{k+1}² itself. The threshold is sharp: at modulus 2310 the primes 97, 101, 103 and 107 fail, and the paper shows exactly why. The proof rests on one short divisibility lemma, 4M_k | n² − z².
3. **Recursion.** The next prime is always the smallest non-trivial orbit minimum, so the cascade "knows" its next step.
4. **Growth.** The number of orbits grows by the exact factor (p_{k+1} − 1)/2 per level.

The same structure is checked in four mathematical languages: hypercube graphs, an averaging operator with an explicit binomial spectrum, Legendre symbols, and the growth law.

**What it delivers.** One six-step scheme treats the classical problems on the same footing:

- twin primes and Polignac pairs,
- Goldbach and Lemoine,
- Sophie Germain primes and Cunningham chains,
- Hardy–Littlewood constellations,
- primes of the form n² + 1,
- arithmetic progressions,
- exponential families such as Mersenne primes and repunits,
- the Collatz iteration as a control case.

For each problem the geometry yields:

- the admissible vertex configurations,
- an exact Chinese-remainder count of these configurations,
- a truncated singular series that converges to the classical Hardy–Littlewood constant.

These are set side by side with the conditional asymptotic, the strongest known unconditional result, and numerical checks up to 10⁸.

Many classical facts become visible as geometry:

- The local Goldbach factor at 30 is a count of axes, edges and diagonals of the 16-cell.
- All primes of the form n² + 1 beyond 5 lie on a single tetrahedral cell.
- Long Cunningham chains and long prime progressions sit on a single vertex.
- The Goldbach comet splits into bands in the ratio 3 : 4 : 6 : 8, exactly as the edge structure predicts.

**Why it is useful.** The paper gives a single, transparent and fully proved framework that computes all local information about prime patterns exactly and uniformly, at every level of the cascade. It makes the classical constants geometrically intuitive. It also locates precisely the one step that requires analytic input: showing that admissible configurations are actually occupied by primes infinitely often, which the paper calls the lifting problem. A table records, for each configuration, where this step is solved classically (Dirichlet, Green–Tao, Maynard–Polymath, Helfgott) and where it remains open. This makes the cascade a clear map of the subject, a teaching tool, and a precise starting point for further work.

**Supplementary material.** The reference code in Appendix B reproduces the finite verifications and orbit computations. A supplementary Python script recomputes every numerical finding of the paper with an independent sieve up to 10⁸ in under a minute; a second script regenerates all figures.
