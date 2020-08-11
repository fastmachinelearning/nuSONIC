import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from model import model

d4a=np.loadtxt("data/results_rscaletest-gke4_bigbat.txt")
d4b=np.loadtxt("data/results_rscaletest-gke4_nodybat_bigbat.txt")

# EmTrackMichelIS Time
fig=plt.figure()
ax=fig.add_subplot(111)

ax.set_xlim(0,410)
ax.set_ylim(0,250)
ax.grid(True)
ax.errorbar(d4b[:,0], d4b[:,3], yerr=d4b[:,4]/np.sqrt(d4b[:,0]), fmt='bD--', linewidth=0.8,markersize=5.5, markeredgecolor='b', fillstyle='none', capsize=3, label = "w/ Triton on GKE-4gpu, dyn bat Off, avg bat sz = 1720")
ax.errorbar(d4a[:,0], d4a[:,3], yerr=d4a[:,4]/np.sqrt(d4a[:,0]), fmt='rv--', linewidth=0.8,markersize=7, markeredgecolor='r', fillstyle='none', capsize=3, label = "w/ Triton on GKE-4gpu, dyn bat On, avg bat sz = 1720")
ax.set(title="EmTrkMichelId module proc time vs # jobs (GKE-4gpu)", xlabel="number of simultaneous jobs", ylabel="processing time [seconds]")

xm = np.arange(0.,410.)
ym = model(xm,False,True, True)
ax.plot(xm, ym, color='purple',label = "model (big batch)",linestyle='dotted',linewidth=2)

xm = np.arange(0.,410.)
ym = model(xm,True,True, True)
ax.plot(xm, ym, color='cyan',label = "model (dynamic batching, big batch)",linestyle='dotted',linewidth=2)

xr=[0.,410.]
yr=[220,220]
ax.plot(xr, yr, color='orange',label = "CPU-only (w/o Triton)",linestyle='solid',linewidth=2)

ax.legend()
fig.tight_layout()
fig.savefig("plot-5a_EmTrackMichelID.pdf")
fig.savefig("plot-5a_EmTrackMichelID.png")
fig.show()

# Full Event Time
fig2=plt.figure()
ax2=fig2.add_subplot(111)

ax2.set_xlim(0,410)
ax2.set_ylim(0,350)
ax2.grid(True)
ax2.errorbar(d4b[:,0], d4b[:,1], yerr=d4b[:,2]/np.sqrt(d4b[:,0]), fmt='bD--', linewidth=0.8,markersize=5.5, markeredgecolor='b', fillstyle='none', capsize=3, label = "w/ Triton on GKE-4gpu, dyn bat Off, avg bat sz = 1720")
ax2.errorbar(d4a[:,0], d4a[:,1], yerr=d4a[:,2]/np.sqrt(d4a[:,0]), fmt='rv--', linewidth=0.8,markersize=7, markeredgecolor='r', fillstyle='none', capsize=3, label = "w/ Triton on GKE-4gpu, dyn bat On, avg bat sz = 1720")
ax2.set(title="Full Event proc time vs # jobs (GKE-4gpu)", xlabel="number of simultaneous jobs", ylabel="processing time [seconds]")

xm = np.arange(0.,410.)
ym = model(xm,False,True)
ax2.plot(xm, ym, color='purple',label = "model (big batch)",linestyle='dotted',linewidth=2)

xm = np.arange(0.,410.)
ym = model(xm,True,True)
ax2.plot(xm, ym, color='cyan',label = "model (dynamic batching, big batch)",linestyle='dotted',linewidth=2)

xr=[0.,410.]
yr=[330,330]
ax2.plot(xr, yr, color='orange',label = "CPU-only (w/o Triton)",linestyle='solid',linewidth=2)

ax2.legend()
fig2.tight_layout()
fig2.savefig("plot-5a_FullEvent.pdf")
fig2.savefig("plot-5a_FullEvent.png")
fig2.show()
