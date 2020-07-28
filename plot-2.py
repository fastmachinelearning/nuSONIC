import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt
import numpy as np

d1=np.loadtxt("data/results_rscaletest-gke4_nodybat.txt")
d4=np.loadtxt("data/results_rscaletest-gke4.txt")

fig=plt.figure()
ax=fig.add_subplot(111)

ax.set_xlim(0,310)
ax.set_ylim(0,60)
ax.grid(True)
ax.errorbar(d1[:,0], d1[:,3], yerr=d1[:,4], fmt='r^--', linewidth=0.8,markersize=7, markeredgecolor='red', fillstyle='none', capsize=3, label = "w/ tRTis on GKE-4gpu, dynamic batching Off")
ax.errorbar(d4[:,0], d4[:,3], yerr=d4[:,4], fmt='bv--', linewidth=0.8,markersize=7, markeredgecolor='blue', fillstyle='none', capsize=3, label = "w/ tRTis on GKE-4gpu, dynamic batching On")
ax.set(title="EmTrkMichelId module proc time vs # jobs (GKE-4gpu)", xlabel="number of simultaneous jobs", ylabel="processing time [seconds]")

#xr=[0.,310.]
#yr=[219.4,219.4]
#ax.plot(xr, yr, color='orange',label = "without tRTis",linestyle='solid',linewidth=2)

plt.legend()
plt.tight_layout()
plt.savefig("plot-2.png")
plt.show()
