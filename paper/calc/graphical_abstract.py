"""Graphical abstract for 'A Cross-Polytope Geometry of the Primes'."""
import math, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm"})
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "graphical_abstract.png")

COL = ["#1f5fa8", "#c0392b", "#2e8b57", "#d68910"]
AX = {1: 0, 29: 0, 7: 1, 23: 1, 11: 2, 19: 2, 13: 3, 17: 3}
order = [1, 7, 11, 13, 29, 23, 19, 17]

fig = plt.figure(figsize=(12, 6.2), dpi=180)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 12); ax.set_ylim(0, 6.2); ax.axis("off")

ax.text(6, 5.85, "A Cross-Polytope Geometry of the Primes", ha="center", va="center",
        fontsize=21, weight="bold", color="#1b2a41")
ax.text(6, 5.45, "Orbit minima, exact residue counts and singular series", ha="center",
        va="center", fontsize=13.5, color="#44546a", style="italic")

# ---- panel 1: the 16-cell -------------------------------------------------
cx, cy, R = 1.85, 3.0, 1.35
pos = {a: (cx + R * math.cos(math.pi / 2 - i * math.pi / 4),
           cy + R * math.sin(math.pi / 2 - i * math.pi / 4)) for i, a in enumerate(order)}
for i, a in enumerate(order):
    for b in order[i + 1:]:
        if (a + b) % 30:
            ax.plot(*zip(pos[a], pos[b]), color="#c9d1db", lw=0.7, zorder=1)
for a in (1, 7, 11, 13):
    b = 30 - a
    ax.plot(*zip(pos[a], pos[b]), color=COL[AX[a]], lw=1.8, ls="--", zorder=2)
for a, (x, y) in pos.items():
    ax.add_patch(plt.Circle((x, y), 0.2, color=COL[AX[a]], zorder=3))
    ax.text(x, y, str(a), ha="center", va="center", color="white", fontsize=10.5,
            weight="bold", zorder=4)
ax.text(cx, 1.15, "8 units mod 30, paired $a \\leftrightarrow 30-a$\n= the 4 axes of the 16-cell",
        ha="center", va="center", fontsize=11, color="#1b2a41")
ax.text(cx, 4.85, "1  The 16-cell", ha="center", fontsize=13, weight="bold", color="#1b2a41")

def arrow(x0, x1, y=3.0):
    ax.add_patch(FancyArrowPatch((x0, y), (x1, y), arrowstyle="-|>", mutation_scale=22,
                                 color="#7f8c8d", lw=1.8))

arrow(3.45, 4.0)

# ---- panel 2: four theorems ----------------------------------------------
ax.text(6.0, 4.85, "2  Cascade over every primorial", ha="center", fontsize=13,
        weight="bold", color="#1b2a41")
ax.text(6.0, 4.45, "$M_k = 2\\cdot3\\cdots p_k$, sign flips $G_k\\cong(\\mathbb{Z}/2)^{k-1}$",
        ha="center", fontsize=11.5, color="#1b2a41")
thms = [("Symmetry", "orbits = square classes of $U(M_k)$"),
        ("Completeness", "for $k\\geq 6$: orbit minima $\\leq p_{k+1}^2$ are\nexactly the primes (sharp at $k=5$)"),
        ("Recursion", "$p_{k+1}$ = smallest non-trivial orbit minimum"),
        ("Growth", "orbits grow by the factor $(p_{k+1}-1)/2$")]
y = 3.95
for i, (h, t) in enumerate(thms):
    hgt = 0.82 if i == 1 else 0.6
    ax.add_patch(FancyBboxPatch((4.15, y - hgt), 3.7, hgt - 0.08,
                                boxstyle="round,pad=0.02,rounding_size=0.08",
                                fc=["#eaf1fa", "#fbecea", "#e9f5ee", "#fcf3e4"][i],
                                ec=COL[i], lw=1.2))
    ax.text(4.28, y - 0.2, h, fontsize=11, weight="bold", color=COL[i], va="center")
    ax.text(4.28, y - 0.25 - (0.25 if i == 1 else 0.17), t, fontsize=9.6, color="#1b2a41",
            va="center")
    y -= hgt + 0.02
ax.text(6.0, 0.95, "four structural theorems, fully proved", ha="center", fontsize=11,
        color="#1b2a41")

arrow(8.0, 8.55)

# ---- panel 3: application scheme -----------------------------------------
ax.text(10.2, 4.85, "3  One scheme for the", ha="center", fontsize=13, weight="bold",
        color="#1b2a41")
ax.text(10.2, 4.5, "classical prime problems", ha="center", fontsize=13, weight="bold",
        color="#1b2a41")
steps = ["vertex configuration", "exact count $\\prod_p\\,(p-\\nu(p))$",
         "singular series $\\to$ Hardy\u2013Littlewood", "numerics up to $10^8$"]
y = 4.05
for s in steps:
    ax.add_patch(FancyBboxPatch((8.7, y - 0.42), 3.0, 0.38,
                                boxstyle="round,pad=0.02,rounding_size=0.08",
                                fc="#f4f6f8", ec="#8a99ab", lw=1))
    ax.text(10.2, y - 0.23, s, ha="center", va="center", fontsize=10, color="#1b2a41")
    y -= 0.5
ax.text(10.2, 1.75, "twins \u00b7 Polignac \u00b7 Goldbach \u00b7 Sophie Germain\n"
        "prime $k$-tuples \u00b7 $n^2+1$ \u00b7 progressions \u00b7 Mersenne",
        ha="center", va="center", fontsize=9.8, color="#44546a")
ax.text(10.2, 1.0, "$\\pi_2(10^8) = 440\\,312$  vs.  $2C_2\\,\\mathrm{Li}_2 = 440\\,368$",
        ha="center", va="center", fontsize=11, color="#c0392b")

ax.text(6, 0.35, "Thomas Krause \u00b7 Independent Researcher, L\u00fcbeck \u00b7 ORCID 0009-0004-3867-9941",
        ha="center", fontsize=10, color="#7f8c8d")
fig.savefig(OUT, dpi=180, facecolor="white")
print("saved", OUT)
