# A Cross-Polytope Geometry of the Primes

**Orbit Minima, Exact Residue Counts, and Singular Series**

Thomas Krause, Independent Researcher, Lübeck, Germany
ORCID [0009-0004-3867-9941](https://orcid.org/0009-0004-3867-9941) · krause-virtuell@web.de

Preprint: [doi:10.20944/preprints202611.0311.v1](https://doi.org/10.20944/preprints202611.0311.v1) (preprints.org, 2026)

This repository contains the LaTeX source, the compiled PDF, all figures and the complete Python code behind every numerical finding of the paper.

## About the paper

The eight reduced residues modulo 30 sit on the eight vertices of the 16-cell, the four-dimensional cross-polytope. Lifting this geometry along the primorial tower M_k = 2·3·5·…·p_k gives four structural theorems:

1. an orbit criterion,
2. a symmetry key lemma,
3. completeness of the orbit minima for k ≥ 6, with sharpness at k = 5,
4. the recursion p_{k+1} = min B_k \ {1}.

These lead to exact residue counts for twins, Goldbach, Polignac and Hardy–Littlewood constellations, and their singular-series limits. Every statement in the paper is marked as proved, numerical or open. See `docs/` for the full description.

## Repository layout

```
paper/
  synthesis_main.tex        single-file LaTeX source (pdfLaTeX / Overleaf)
  synthesis_main.pdf        compiled manuscript, 28 pages
  graphical_abstract.png    graphical abstract
  figures/                  the nine figures (PDF)
  calc/
    numerics_check.py       recomputes every numerical finding [N] with an independent NumPy sieve up to 10^8
    numerics_output.txt     full output of the check script
    reference_code_appendixB.py   reference code of Appendix B (checks the four structural theorems for k = 3..7)
    figs.py                 regenerates all figures into paper/figures/
    graphical_abstract.py   regenerates paper/graphical_abstract.png
docs/
  Description_Cross-Polytope_Geometry_of_the_Primes.md
```

## Reproducing the results

```bash
pip install -r requirements.txt
cd paper/calc
python reference_code_appendixB.py   # structural theorems, k = 3..7
python numerics_check.py             # all numerical findings (about 1 GB RAM)
python figs.py                       # figures
python graphical_abstract.py         # graphical abstract
```

Requirements: Python 3.9+, numpy, sympy, mpmath, matplotlib.

To compile the paper, upload `paper/synthesis_main.tex` together with the `figures/` folder to Overleaf, or run `pdflatex synthesis_main.tex` twice.

## Citation

See `CITATION.cff`, or cite:

> T. Krause, *A Cross-Polytope Geometry of the Primes: Orbit Minima, Exact Residue Counts, and Singular Series*, Preprints (2026), doi:10.20944/preprints202611.0311.v1.

## License

- **Code** (`paper/calc/`, `requirements.txt`): [MIT License](LICENSE).
- **Paper, figures and documentation** (`paper/synthesis_main.tex`, `paper/synthesis_main.pdf`, `paper/figures/`, `paper/graphical_abstract.png`, `docs/`, this README): [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE-CC-BY-4.0.txt), as for the preprint on preprints.org.

© 2026 Thomas Krause
