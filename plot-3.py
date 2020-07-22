import matplotlib.pyplot as plt
import numpy as np

d4a=np.loadtxt("data/results_rscaletest-gke4_nodybat.txt")
d4b=np.loadtxt("data/results_rscaletest-gke4_nodybat_bigbat.txt")

fig=plt.figure()
ax=fig.add_subplot(111)

ax.set_xlim(0,310)
ax.set_ylim(0,60)
ax.grid(True)
ax.errorbar(d4a[:,0], d4a[:,3], yerr=d4a[:,4], fmt='r^--', linewidth=0.8,markersize=7, markeredgecolor='red', fillstyle='none', capsize=3, label = "w/ tRTis on GKE-4gpu, avg batch size = 235")
ax.errorbar(d4b[:,0], d4b[:,3], yerr=d4b[:,4], fmt='bD--', linewidth=0.8,markersize=5.5, markeredgecolor='blue', fillstyle='none', capsize=3, label = "w/ tRTis on GKE-4gpu, avg batch size = 1720")
ax.set(title="EmTrkMichelId module proc time vs # jobs (GKE-4gpu, no dynamic batching)", xlabel="number of simultaneous jobs", ylabel="processing time [seconds]")

#xr=[0.,310.]
#yr=[219.4,219.4]
#ax.plot(xr, yr, color='orange',label = "without tRTis",linestyle='solid',linewidth=2)

plt.legend()
plt.tight_layout()
plt.savefig("plot-3.png")
plt.show()
