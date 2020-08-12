import matplotlib as mpl
mpl.use('agg')
import numpy as np
import matplotlib.pyplot as plt
from model import model

d4a=np.loadtxt("data/results_rscaletest-gke4_nodybat.txt")
d4b=np.loadtxt("data/results_rscaletest-gke4.txt")

fig=plt.figure()
ax=fig.add_subplot(111)

ax.set_xlim(0,500)
ax.set_ylim(0,350)
ax.grid(True)
ax.errorbar(d4a[:,0], d4a[:,1], yerr=d4a[:,2]/np.sqrt(d4a[:,0]), fmt='r^--', linewidth=0.8,markersize=7, markeredgecolor='red', fillstyle='none', capsize=3, label = "w/ Triton (GKE, 4 GPU), avg batch size = 235")
ax.errorbar(d4b[:,0], d4b[:,1], yerr=d4b[:,2]/np.sqrt(d4b[:,0]), fmt='bD--', linewidth=0.8,markersize=5.5, markeredgecolor='blue', fillstyle='none', capsize=3, label = "w/ Triton (GKE, 4 GPU), dynamic batching size = 235")
ax.set(title="Full ProtoDUNE event time vs # jobs (GKE, 4 GPU)", xlabel="number of simultaneous jobs", ylabel="processing time [seconds]")

xr=[0.,500.]
yr=[330,330]
ax.plot(xr, yr, color='orange',label = "CPU-only (w/o Triton)",linestyle='solid',linewidth=2)


xm = np.arange(0.,500.)
ym = model(xm)
ax.plot(xm, ym, color='purple',label = "model (small batch",linestyle='dotted',linewidth=2)

xm = np.arange(0.,500.)
ym = model(xm,True)
ax.plot(xm, ym, color='cyan',label = "model (dynamic batching)",linestyle='dotted',linewidth=2)


plt.legend(loc='best')
plt.tight_layout()
plt.savefig("plot-1c.png")
plt.savefig("plot-1c.pdf",**{"bbox_inches":"tight"})
plt.show()
