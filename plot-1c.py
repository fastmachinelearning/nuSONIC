import matplotlib as mpl
mpl.use('agg')
import numpy as np
import matplotlib.pyplot as plt

d4a=np.loadtxt("data/results_rscaletest-gke4_nodybat.txt")
d4b=np.loadtxt("data/results_rscaletest-gke4.txt")

fig=plt.figure()
ax=fig.add_subplot(111)

ax.set_xlim(0,310)
ax.set_ylim(0,350)
ax.grid(True)
ax.errorbar(d4a[:,0], d4a[:,1], yerr=d4a[:,2]/np.sqrt(d4a[:,0]), fmt='r^--', linewidth=0.8,markersize=7, markeredgecolor='red', fillstyle='none', capsize=3, label = "w/ Triton (GKE, 4 GPU), avg batch size = 235")
ax.errorbar(d4b[:,0], d4b[:,1], yerr=d4b[:,2]/np.sqrt(d4b[:,0]), fmt='bD--', linewidth=0.8,markersize=5.5, markeredgecolor='blue', fillstyle='none', capsize=3, label = "w/ Triton (GKE, 4 GPU), dynamic batching (avg = 1720)")
ax.set(title="Full ProtoDUNE event time vs # jobs (GKE, 4 GPU)", xlabel="number of simultaneous jobs", ylabel="processing time [seconds]")

xr=[0.,310.]
yr=[330,330]
ax.plot(xr, yr, color='orange',label = "CPU-only (w/o Triton)",linestyle='solid',linewidth=2)

# t_sonic = (1-p)t_cpu + t_gpu[1 + max(0, N_cpu / N_gpu - t_ideal / t_gpu)]
def model(x, dynbat=False, bigbat=False):
    n_gpu = 4.
    t_cpu = 330.
    p = 0.65
    t_gpu = 2.75
    if dynbat: t_gpu = 1.77
    t_transmit = 2.05
    t_travel = 2.6
    if bigbat: t_travel = 0.38
    t_latency = t_transmit + t_travel
    t_ideal = (1-p)*t_cpu + t_gpu + t_latency
    return (1-p)*t_cpu + t_gpu*(1 + np.maximum(0, x/n_gpu - t_ideal/t_gpu)) + t_latency
xm = np.arange(0.,310.)
ym = model(xm)
ax.plot(xm, ym, color='purple',label = "model",linestyle='dotted',linewidth=2)

xm = np.arange(0.,310.)
ym = model(xm,True)
ax.plot(xm, ym, color='cyan',label = "model (dynamic batching)",linestyle='dotted',linewidth=2)


plt.legend(loc='best')
plt.tight_layout()
plt.savefig("plot-1c.png")
plt.savefig("plot-1c.pdf",**{"bbox_inches":"tight"})
plt.show()
