import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt
import numpy as np

d4a=np.loadtxt("data/results_rscaletest-gke4_bigbat.txt")
d4b=np.loadtxt("data/results_rscaletest-gke4_nodybat_bigbat.txt")

fig=plt.figure()
ax=fig.add_subplot(111)

ax.set_xlim(0,410)
ax.set_ylim(0,100)
ax.grid(True)
ax.errorbar(d4b[:,0], d4b[:,3], yerr=d4b[:,4], fmt='bD--', linewidth=0.8,markersize=5.5, markeredgecolor='b', fillstyle='none', capsize=3, label = "w/ tRTis on GKE-4gpu, dyn bat Off, avg bat sz = 1720")
ax.errorbar(d4a[:,0], d4a[:,3], yerr=d4a[:,4], fmt='rv--', linewidth=0.8,markersize=7, markeredgecolor='r', fillstyle='none', capsize=3, label = "w/ tRTis on GKE-4gpu, dyn bat On, avg bat sz = 1720")
ax.set(title="EmTrkMichelId module proc time vs # jobs (GKE-4gpu)", xlabel="number of simultaneous jobs", ylabel="processing time [seconds]")

#xr=[0.,310.]
#yr=[219.4,219.4]
#ax.plot(xr, yr, color='orange',label = "without tRTis",linestyle='solid',linewidth=2)

plt.legend()
plt.tight_layout()
plt.savefig("plot-5a.png")
plt.show()
