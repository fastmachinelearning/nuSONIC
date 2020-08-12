import numpy as np

# t_sonic = (1-p)t_cpu + t_gpu[1 + max(0, N_cpu / N_gpu - t_ideal / t_gpu)]
def model(x, dynbat=False, bigbat=False, emtrack=False):
    n_gpu = 4.
    t_cpu = 330.
    p = 0.65
    t_gpu = 2.5 #change to actual value, 2.5 is an approx, down from 2.75
    t_preprocess = 7
    if dynbat: t_gpu = 1.77
    if bigbat: t_gpu = 1.77
    t_transmit = 2.05
    t_travel = 2.6
    if bigbat: t_travel = 0.38
    t_latency = t_transmit + t_travel
    t_ideal = (1-p)*t_cpu + t_gpu + t_latency
    if emtrack: t_cpu = 0
    return (1-p)*t_cpu + t_gpu*(1 + np.maximum(0, x/n_gpu - t_ideal/t_gpu)) + t_latency + t_preprocess
