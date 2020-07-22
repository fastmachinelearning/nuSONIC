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
def model(x):
    n_gpu = 4.
    t_cpu = 330.
    p = 0.67
    t_gpu = 2.5
    t_ideal = (1-p)*t_cpu + t_gpu
    return (1-p)*t_cpu + t_gpu*(1 + np.maximum(0, x/n_gpu - t_ideal/t_gpu))
xm = np.arange(0.,310.)
ym = model(xm)
ax.plot(xm, ym, color='purple',label = "model",linestyle='dotted',linewidth=2)

plt.legend(loc='best')
plt.tight_layout()
plt.savefig("plot.png")
plt.show()
