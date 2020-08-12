import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from model import model

d4a=np.loadtxt("data/results_rscaletest-gke4_bigbat.txt")

# EMTrackMichelID Time
fig=plt.figure()
ax=fig.add_subplot(111)

ax.set_xlim(0,410)
ax.set_ylim(0,100)
ax.grid(True)
ax.errorbar(d4a[:,0], d4a[:,3], yerr=d4a[:,4]/np.sqrt(d4a[:,0]), fmt='rv--', linewidth=0.8,markersize=7, markeredgecolor='r', fillstyle='none', capsize=3, label = "EmTrkMichelId Time")
ax.errorbar(d4a[:,0], d4a[:,7], yerr=d4a[:,8]/np.sqrt(d4a[:,0]), fmt='bD--', linewidth=0.8,markersize=5.5, markeredgecolor='b', fillstyle='none', capsize=3, label = "Inference Time") #What are cols 5/6? They aren't inf time, assuming (and seems like) 7/8 are
ax.plot(d4a[:,0], (d4a[:,3]-d4a[:,7]), 'gD--', linewidth=0.8,markersize=5.5, markeredgecolor='g', fillstyle='none', label = "Preprocessing Time")

ax.set(title="EmTrkMichelId time vs # jobs (GKE-4gpu, dyn bat, avg bat sz = 1700)", xlabel="number of simultaneous jobs", ylabel="processing time [seconds]")

#xm = np.arange(0.,410.)
#ym = model(xm,True, False, True)
#ax.plot(xm, ym, color='cyan',label = "model (dynamic batching, small batch)",linestyle='dotted',linewidth=2)

ax.legend()
fig.tight_layout()
fig.savefig("plot-6b_EMTrackMichelID.pdf")
fig.savefig("plot-6b_EMTrackMichelID.png")
fig.show()

