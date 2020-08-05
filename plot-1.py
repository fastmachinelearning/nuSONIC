import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt
import numpy as np

d1=np.loadtxt("data/results_rscaletest-gke1.txt")
d4=np.loadtxt("data/results_rscaletest-gke4.txt")

fig=plt.figure()
ax=fig.add_subplot(111)

ax.set_xlim(0,310)
ax.set_ylim(0,250)
ax.grid(True)
# another way to fill markers is to set e.g. markerfacecolor='blue'
ax.errorbar(d1[:,0], d1[:,3], yerr=d1[:,4], fmt='ro--', linewidth=0.8,markersize=4, fillstyle='none', markeredgecolor='r', capsize=3, label = "w/ Triton on GKE-1gpu")
ax.errorbar(d4[:,0], d4[:,3], yerr=d4[:,4], fmt='bv--', linewidth=0.8,markersize=4, fillstyle='none', markeredgecolor='blue', capsize=3, label = "w/ Triton on GKE-4gpu")
ax.set(title="EmTrkMichelId module proc time vs # jobs (GKE w/ dynamic batching)", xlabel="number of simultaneous jobs", ylabel="processing time [seconds]")

xr=[0.,310.]
yr=[219.4,219.4]
ax.plot(xr, yr, color='orange',label = "without tRTis",linestyle='solid',linewidth=2)

plt.legend()
plt.tight_layout()
plt.savefig("plot-1.pdf")
plt.savefig("plot-1.png")
plt.show()
