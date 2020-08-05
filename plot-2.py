import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt
import numpy as np

d1=np.loadtxt("data/results_rscaletest-gke4_nodybat.txt")
d4=np.loadtxt("data/results_rscaletest-gke4.txt")

# EmTrackMichelID Time
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

ax.legend()
fig.tight_layout()
fig.savefig("plot-2_EMTrackMichelID.png")
fig.show()

# Full Event Time
fig2=plt.figure()
ax2=fig2.add_subplot(111)

ax2.set_xlim(0,310)
ax2.set_ylim(0,250)
ax2.grid(True)
ax2.errorbar(d1[:,0], d1[:,1], yerr=d1[:,2], fmt='r^--', linewidth=0.8,markersize=7, markeredgecolor='red', fillstyle='none', capsize=3, label = "w/ tRTis on GKE-4gpu, dynamic batching Off")
ax2.errorbar(d4[:,0], d4[:,1], yerr=d4[:,2], fmt='bv--', linewidth=0.8,markersize=7, markeredgecolor='blue', fillstyle='none', capsize=3, label = "w/ tRTis on GKE-4gpu, dynamic batching On")
ax2.set(title="Full Event proc time vs # jobs (GKE-4gpu)", xlabel="number of simultaneous jobs", ylabel="processing time [seconds]")

ax2.legend()
fig2.tight_layout()
fig2.savefig("plot-2_FullEvent.png")
fig2.show()