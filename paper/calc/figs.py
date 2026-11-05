import numpy as np, math, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from itertools import combinations
from collections import Counter
from sympy import primorial, prime, primerange, isprime, divisor_count
from math import gcd
plt.rcParams.update({'font.size':10,'font.family':'serif','mathtext.fontset':'cm','axes.spines.top':False,'axes.spines.right':False})
import os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','figures')+os.sep
AX={1:0,29:0,7:1,23:1,11:2,19:2,13:3,17:3}
COL=['#1f5fa8','#c0392b','#2e8b57','#d68910']
U=[1,7,11,13,17,19,23,29]

# ---------- Fig: matchstick game strip ----------
def move(n):
    if isprime(n): return 'D'
    r=int(math.isqrt(n))
    if r*r==n and isprime(r): return 'E'
    return 'S'
fig,ax=plt.subplots(figsize=(7.2,1.6))
cm={'D':'#c0392b','E':'#d68910','S':'#7f8c8d'}
for n in range(2,41):
    m=move(n); x=(n-2)%20; y=-((n-2)//20)
    ax.add_patch(plt.Rectangle((x,y),0.92,0.85,color=cm[m],alpha=0.9 if m=='D' else 0.55))
    ax.text(x+0.46,y+0.55,str(n),ha='center',va='center',fontsize=8,color='white' if m=='D' else 'black')
    ax.text(x+0.46,y+0.2,m,ha='center',va='center',fontsize=7,color='white' if m=='D' else 'black')
ax.set_xlim(-0.2,20.2); ax.set_ylim(-1.2,1.0); ax.axis('off')
for m,lab in [('D','D: new axis (prime)'),('E','E: echo (prime square)'),('S','S: closes a divisor pair')]:
    ax.plot([],[],'s',color=cm[m],label=lab,ms=8)
ax.legend(loc='upper center',bbox_to_anchor=(0.5,1.45),ncol=3,frameon=False,fontsize=8)
fig.savefig(OUT+'fig_game.pdf',bbox_inches='tight'); plt.close()

# ---------- Fig: HCN staircase ----------
N=10000; d=[0]+[int(divisor_count(n)) for n in range(1,N+1)]
hc=[];best=0
for n in range(1,N+1):
    if d[n]>best: best=d[n]; hc.append(n)
fig,ax=plt.subplots(figsize=(6.2,2.6))
xs=np.arange(1,N+1); ax.scatter(xs,d[1:],s=0.3,color='#bbbbbb')
run=np.maximum.accumulate(d[1:]); ax.step(xs,run,where='post',color='#1f5fa8',lw=1)
ax.scatter(hc,[d[h] for h in hc],color='#c0392b',s=12,zorder=3)
ax.set_xscale('log'); ax.set_xlabel('$n$'); ax.set_ylabel('$d(n)$')
ax.set_title(f'Highly composite numbers up to $10^4$ ({len(hc)} red points)',fontsize=10)
fig.savefig(OUT+'fig_hcn.pdf',bbox_inches='tight'); plt.close()
print('HCN count',len(hc))

# ---------- Fig: 16-cell projection ----------
order=[1,7,11,13,29,23,19,17]  # antipode at +4
pos={a:(math.cos(math.pi/2-i*math.pi/4),math.sin(math.pi/2-i*math.pi/4)) for i,a in enumerate(order)}
def base(ax,title):
    for a,b in combinations(U,2):
        if (a+b)%30: ax.plot(*zip(pos[a],pos[b]),color='#cccccc',lw=0.6,zorder=1)
    ax.set_aspect('equal'); ax.axis('off'); ax.set_title(title,fontsize=9.5)
def verts(ax,hl=None,colfun=None):
    for a in U:
        c=colfun(a) if colfun else COL[AX[a]]
        ax.scatter(*pos[a],s=330,color=c,zorder=3,edgecolor='k',lw=0.5)
        ax.text(*pos[a],str(a),ha='center',va='center',color='white',fontsize=9,zorder=4,fontweight='bold')
fig,axs=plt.subplots(1,3,figsize=(7.6,2.9))
ax=axs[0]; base(ax,'(a) vertices, edges and axes')
for i in range(4):
    a=order[i]; b=order[i+4]; ax.plot(*zip(pos[a],pos[b]),color=COL[AX[a]],lw=1.8,ls='--',zorder=2)
verts(ax)
ax=axs[1]; base(ax,'(b) two great squares $T_1$, $T_2$')
for T,c in [([1,11,29,19],'#1f5fa8'),([7,13,23,17],'#c0392b')]:
    pts=[pos[a] for a in T]+[pos[T[0]]]; ax.plot(*zip(*pts),color=c,lw=2,zorder=2)
verts(ax,colfun=lambda a:'#1f5fa8' if a in (1,11,19,29) else '#c0392b')
ax=axs[2]; base(ax,'(c) the cell $\\{1,7,11,17\\}$ ($n^2+1$)')
cell=[1,7,11,17]
for a,b in combinations(cell,2): ax.plot(*zip(pos[a],pos[b]),color='#2e8b57',lw=2,zorder=2)
verts(ax,colfun=lambda a:'#2e8b57' if a in cell else '#999999')
fig.savefig(OUT+'fig_16cell.pdf',bbox_inches='tight'); plt.close()

# ---------- Fig: sum histograms ----------
anti=lambda a,b:(a+b)%30==0
E=[e for e in combinations(U,2) if not anti(*e)]
F=[f for f in combinations(U,3) if not any(anti(a,b) for a,b in combinations(f,2))]
C=[c for c in combinations(U,4) if not any(anti(a,b) for a,b in combinations(c,2))]
fig,axs=plt.subplots(1,3,figsize=(7.6,2.3),sharey=True)
for ax,data,lab,rng in [(axs[0],[sum(e)%30 for e in E],'24 edges: $a+b$ mod 30',range(0,30,2)),
                        (axs[1],[sum(f)%30 for f in F],'32 facets: $a+b+c$ mod 30',range(1,30,2)),
                        (axs[2],[(sum(c)-1)%30+1 for c in C],'16 cells: sum in $\\{2,\\dots,30\\}$',range(2,31,2))]:
    cnt=Counter(data); ax.bar(list(rng),[cnt.get(r,0) for r in rng],width=1.5,color='#1f5fa8')
    ax.set_title(lab,fontsize=9); ax.set_xticks(list(rng)[::2]); ax.tick_params(labelsize=7)
axs[0].set_ylabel('multiplicity')
fig.savefig(OUT+'fig_sums.pdf',bbox_inches='tight'); plt.close()

# ---------- Fig: cascade ----------
ks=list(range(2,11)); phi=[]; B=[]
for k in ks:
    f=1
    for i in range(1,k+1): f*=prime(i)-1
    phi.append(f); B.append(f//2**(k-1))
fig,ax=plt.subplots(figsize=(5.6,2.8))
ax.semilogy(ks,phi,'o-',color='#1f5fa8',label='vertices $\\varphi(M_k)$')
ax.semilogy(ks,[f//2 for f in phi],'s-',color='#2e8b57',label='axes $\\varphi(M_k)/2$ = dimension')
ax.semilogy(ks,B,'^-',color='#c0392b',label='orbits $|B_k|=\\varphi(M_k)/2^{k-1}$')
for k,b in zip(ks,B): ax.annotate(str(b),(k,b),textcoords='offset points',xytext=(6,-10),fontsize=7,color='#c0392b')
ax.set_xlabel('stage $k$  ($M_k=2\\cdot3\\cdots p_k$)'); ax.legend(fontsize=8,frameon=False)
fig.savefig(OUT+'fig_cascade.pdf',bbox_inches='tight'); plt.close()

# ---------- Fig: orbit as Q3 (k=4) ----------
M=210; y=11; orb=sorted(z for z in range(1,M) if gcd(z,M)==1 and (z*z-y*y)%M==0)
print('orbit of 11 mod 210',orb)
def sig(z): return tuple(0 if z%p==y%p else 1 for p in (3,5,7))
pts={z:sig(z) for z in orb}
proj=lambda s:(s[0]*1.0+s[2]*0.45, s[1]*1.0+s[2]*0.35)
fig,ax=plt.subplots(figsize=(3.6,3.0))
for a,b in combinations(orb,2):
    if sum(x!=w for x,w in zip(pts[a],pts[b]))==1:
        ax.plot(*zip(proj(pts[a]),proj(pts[b])),color='#888888',lw=1)
for z in orb:
    c='#c0392b' if z==min(orb) else '#1f5fa8'
    ax.scatter(*proj(pts[z]),s=420,color=c,zorder=3,edgecolor='k',lw=0.5)
    ax.text(*proj(pts[z]),str(z),ha='center',va='center',color='white',fontsize=8,fontweight='bold',zorder=4)
ax.set_aspect('equal'); ax.axis('off')
ax.set_title('orbit of 11 at $k=4$ ($M_4=210$)\nedges = single sign flips mod 3, 5, 7',fontsize=9)
fig.savefig(OUT+'fig_orbitcube.pdf',bbox_inches='tight'); plt.close()

# ---------- Fig: threshold ----------
def Bk(k):
    M=int(primorial(k)); best={}
    for z in range(1,M):
        if gcd(z,M)==1:
            s=z*z%M
            if s not in best: best[s]=z
    return M,sorted(best.values())
fig,axs=plt.subplots(2,1,figsize=(7.2,3.2))
for ax,k in zip(axs,(5,6)):
    M,B=Bk(k); pk=prime(k); hi=pk*pk if k==6 else 130
    if k==6: hi=370
    prs=list(primerange(pk+1,hi+1)); Bs=set(B)
    for q in prs:
        ok=q in Bs
        ax.plot([q,q],[0,1],color='#2e8b57' if ok else '#c0392b',lw=1.4)
    for b in B:
        if pk<b<=hi and not isprime(b): ax.plot([b,b],[0,1],color='#d68910',lw=1.6)
    ax.axvline(2*M**0.5,color='k',ls=':',lw=1)
    ax.text(2*M**0.5,1.08,'$2\\sqrt{M_%d}$'%k,ha='center',fontsize=8)
    ax.set_yticks([]); ax.set_xlim(pk,hi); ax.set_ylim(0,1.35)
    ax.set_title(f'$k={k}$, $M_{k}={M}$: primes in $({pk},{hi}]$', fontsize=8.5,loc='left')
axs[1].set_xlabel('$n$  (green: prime and orbit minimum; red: prime but not an orbit minimum; orange: composite orbit minimum)',fontsize=8)
fig.tight_layout(); fig.savefig(OUT+'fig_threshold.pdf',bbox_inches='tight'); plt.close()

# ---------- Fig: twin edge density ----------
g=0.5772156649; C2=0.6601618158
ks=list(range(3,40)); vals=[]
for k in ks:
    d=1.0
    for p in primerange(3,prime(k)+1): d*=(p-2)/(p-1)
    vals.append(d*math.log(prime(k))/(2*math.exp(-g)))
fig,ax=plt.subplots(figsize=(5.6,2.5))
ax.plot(ks,vals,'o-',ms=3,color='#1f5fa8'); ax.axhline(C2,color='#c0392b',ls='--',lw=1)
ax.text(ks[-1],C2+0.004,'$C_2=0.66016\\ldots$',ha='right',color='#c0392b',fontsize=9)
ax.set_xlabel('stage $k$'); ax.set_ylabel('$\\delta_k\\,\\log p_k/(2e^{-\\gamma})$')
fig.savefig(OUT+'fig_twin.pdf',bbox_inches='tight'); plt.close()
print('twin renorm k=3,6,10,20,39',[round(vals[ks.index(k)],4) for k in (3,6,10,20,39)])

# ---------- Fig: Goldbach comet ----------
_L=40000; _v=np.zeros(_L+1,dtype=np.int64)
for _p in primerange(2,_L+1): _v[_p]=1
_r=np.convolve(_v,_v)[:_L+1]          # ordered pairs p+q=N
Ns=np.arange(4,_L+1,2); r=_r[Ns]
cls=np.where(Ns%30==0,0,np.where(Ns%6==0,1,np.where(Ns%10==0,2,3)))
lab=['$30\\mid N$: 4 axes (factor 8)','$6\\mid N$: 3 edges (factor 6)','$10\\mid N$: 2 edges (factor 4)','otherwise: 1 edge + diagonal (factor 3)']
cc=['#c0392b','#d68910','#2e8b57','#1f5fa8']
fig,ax=plt.subplots(figsize=(6.4,3.2))
for c in (3,2,1,0):
    m=cls==c; ax.scatter(Ns[m],r[m],s=0.6,color=cc[c],label=lab[c],rasterized=True)
ax.set_xlabel('even $N$'); ax.set_ylabel('$r(N)$ (ordered prime pairs)')
ax.legend(markerscale=10,fontsize=7.5,frameon=False,loc='upper left')
fig.savefig(OUT+'fig_goldbach.pdf',bbox_inches='tight',dpi=200); plt.close()
print('done')
