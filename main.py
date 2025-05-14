# credit to Jiten Dhandha

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# plt.rcParams['text.usetex'] = True
from misc_funcs import plot_formatting
plot_formatting()

data = np.genfromtxt('data.dat')

z = data[:,0]
TM = data[:,2]
TR = data[:,3]
TS = data[:,4]
dTb = data[:,5]
dTb[z<12] = dTb[z<12] * 1/(1+((12-z[z<12])/5)**10)

fig = plt.figure(figsize=(16, 10))


def plot_regions(tax):
    tax.axvline(x=90-1, color='black', linestyle='--', linewidth=0.5)
    tax.axvline(x=29.5-1, color='black', linestyle='--', linewidth=0.5)
    tax.axvline(x=21.2-1, color='black', linestyle='--', linewidth=0.5)
    tax.axvline(x=13-1, color='black', linestyle='--', linewidth=0.5)

    tax.axvspan(90-1, 1000-1, color='violet', alpha=0.25)
    tax.axvspan(29.5-1, 90-1, color='blue', alpha=0.25)
    tax.axvspan(21.2-1, 29.5-1, color='green', alpha=0.25)
    tax.axvspan(21.2-1, 13-1, color='orange', alpha=0.25)
    tax.axvspan(13-1, 0, color='red', alpha=0.25)


ax = fig.add_subplot(211)

ax.plot(z, TM, color='black', ls='-.', label=r'$T_K$ (gas temperature)')
ax.plot(z, TR, color='black', ls='--', label=r'$T_{CMB}$')
ax.plot(z, TS, color='black', ls='-', label=r'$T_s$')

plot_regions(ax)

TEXTY = 2 * 1e4
ax.text(x=133-1, y=TEXTY, s=r'$Collisions$', fontsize=24, ha='center')
ax.text(x=53-1, y=TEXTY, s=r'$CMB$', fontsize=24, ha='center')
ax.text(x=25-1, y=TEXTY, s=r'$Ly\alpha$', fontsize=24, ha='center')
ax.text(x=16.5-1, y=TEXTY, s=r'$X\mathrm{-}rays$', fontsize=24, ha='center')
ax.text(x=8, y=TEXTY, s=r'$UV~reionization$', fontsize=24, ha='center')

ax.set_xlim(5, 200)
ax.set_ylim(1, 5 * 1e4)
ax.set_xscale('log')
ax.set_yscale('log')
ax.legend(fontsize=20, frameon=False, loc='lower left')
ax.invert_xaxis()

ax.tick_params(axis='both', which='both', labelsize=17)
ax.tick_params(labelbottom=False)

ax.set_ylabel(r'$\mathrm{Temperature}$ / K', fontsize=24)

ax2 = fig.add_subplot(212, sharex=ax)
ax2.plot(z, dTb, color='black')
ax2.axhline(y=0, color='black', linestyle='--')

plot_regions(ax2)

# TEXTY = -111
# ax2.text(x=100,y=TEXTY,s=r'$\mathbf{Collisions}$',fontsize=24)
# ax2.text(x=27.8,y=TEXTY,s=r'$\mathbf{Ly}\alpha$',fontsize=24)
# ax2.text(x=20.5,y=TEXTY,s=r'$\mathbf{X}\mathrm{-}\mathbf{rays}$',fontsize=24)
# ax2.text(x=12.5,y=TEXTY,s=r'$\mathbf{UV~reionization}$',fontsize=24)

ax2.text(x=90-1, y=-50, s=r'$\mathrm{Dark~Ages}$', fontsize=20, ha='center')
ax2.text(x=30-1, y=14, s=r'$\mathrm{First~galaxies~form}$', fontsize=20, ha='center')
ax2.text(x=30-1, y=4, s=r'$\mathrm{(Cosmic~Dawn)}$', fontsize=20, ha='center')
ax2.text(x=21-1, y=-108, s=r'$\mathrm{Heating~begins}$', fontsize=20, ha='center')
ax2.text(x=13-1, y=21, s=r'$\mathrm{Reionization~begins}$', fontsize=20, ha='center')
ax2.text(x=7, y=-9, s=r'$\mathrm{Reionization~ends}$', fontsize=20, ha='center')

arr = [200, 150, 100, 80, 40, 20, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]
ax2.set_xticks(arr)
arr2 = [200, 150, 100, 80, 40, 20, 15, '', '', 12, '', 10, 9, 8, 7, 6, 5]
arr2str = []
for x in arr2:
    if x == '':
        arr2str.append(x)
    else:
        arr2str.append(rf'${x}$')
ax2.set_xticklabels(arr2str)
ax2.tick_params(axis='both', which='both', labelsize=17)

ax2.set_ylabel(r'$\overline{T}_{21}$ / mK', fontsize=24)
ax2.set_xlabel(r'$z$', fontsize=24)

ax2.set_ylim(-115, 30)

fig.tight_layout()
fig.savefig('Example21cm.png')