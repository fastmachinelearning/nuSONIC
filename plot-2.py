import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from model import model

d1=np.loadtxt("data/results_rscaletest-gke4_nodybat.txt")
d4=np.loadtxt("data/results_rscaletest-gke4.txt")

# EmTrackMichelID Time
fig=plt.figure()
ax=fig.add_subplot(111)

ax.set_xlim(0,500)
ax.set_ylim(0,250)
ax.grid(True)
ax.errorbar(d1[:,0], d1[:,3], yerr=d1[:,4]/np.sqrt(d1[:,0]), fmt='r^--', linewidth=0.8,markersize=7, markeredgecolor='red', fillstyle='none', capsize=3, label = "w/ Triton on GKE-4gpu, dyn bat Off, avg bat sz = 235")
ax.errorbar(d4[:,0], d4[:,3], yerr=d4[:,4]/np.sqrt(d4[:,0]), fmt='bv--', linewidth=0.8,markersize=7, markeredgecolor='blue', fillstyle='none', capsize=3, label = "w/ Triton on GKE-4gpu, dyn bat On, avg bat sz = 235")
ax.set(title="EmTrkMichelId module proc time vs # jobs (GKE-4gpu)", xlabel="number of simultaneous jobs", ylabel="processing time [seconds]")

#xr=[0.,310.]
#yr=[219.4,219.4]
#ax.plot(xr, yr, color='orange',label = "without Triton",linestyle='solid',linewidth=2)
xm = np.arange(0.,500.)
ym = model(xm,False,False,True)
ax.plot(xm, ym, color='purple',label = "model (small batch)",linestyle='dotted',linewidth=2)

xm = np.arange(0.,500.)
ym = model(xm,True,False,True)
ax.plot(xm, ym, color='cyan',label = "model (dynamic batching, small batch)",linestyle='dotted',linewidth=2)

xr=[0.,500.]
yr=[220,220]
ax.plot(xr, yr, color='orange',label = "CPU-only (w/o Triton)",linestyle='solid',linewidth=2)


ax.legend()
fig.tight_layout()
fig.savefig("plot-2_EMTrackMichelID.pdf")
fig.savefig("plot-2_EMTrackMichelID.png")
fig.show()

# Full Event Time
fig2=plt.figure()
ax2=fig2.add_subplot(111)

ax2.set_xlim(0,500)
ax2.set_ylim(0,350)
ax2.grid(True)
ax2.errorbar(d1[:,0], d1[:,1], yerr=d1[:,2]/np.sqrt(d1[:,0]), fmt='r^--', linewidth=0.8,markersize=7, markeredgecolor='red', fillstyle='none', capsize=3, label = "w/ Triton on GKE-4gpu, dyn bat Off, avg bat sz = 235")
ax2.errorbar(d4[:,0], d4[:,1], yerr=d4[:,2]/np.sqrt(d4[:,0]), fmt='bv--', linewidth=0.8,markersize=7, markeredgecolor='blue', fillstyle='none', capsize=3, label = "w/ Triton on GKE-4gpu, dyn bat On, avg bat sz = 235")
ax2.set(title="Full Event proc time vs # jobs (GKE-4gpu)", xlabel="number of simultaneous jobs", ylabel="processing time [seconds]")

xm = np.arange(0.,500.)
ym = model(xm)
ax2.plot(xm, ym, color='purple',label = "model",linestyle='dotted',linewidth=2)

xm = np.arange(0.,500.)
ym = model(xm,True)
ax2.plot(xm, ym, color='cyan',label = "model (dynamic batching)",linestyle='dotted',linewidth=2)

xr=[0.,500.]
yr=[330,330]
ax2.plot(xr, yr, color='orange',label = "CPU-only (w/o Triton)",linestyle='solid',linewidth=2)

ax2.legend()
fig2.tight_layout()
fig2.savefig("plot-2_FullEvent.pdf")
fig2.savefig("plot-2_FullEvent.png")
fig2.show()