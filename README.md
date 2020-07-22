Meaning of columns:
col 1: number of simultaneous clients
col 2: full event time
col 3: sd for col 2
col 4: EmTrackMichelId time
col 5: sd for col 4
the second file "results_rscaletest-gke4.txt" has two additional columns:
col 6: inference only time
col 7: sd for col 6

Contents of files:
results_rscaletest-gke1.txt: GKE-1gpu server results with Dynamic Batching turned On
results_rscaletest-gke4.txt: GKE-4gpu server results with Dynamic Batching turned On
results_rscaletest-gke4_nodybat.txt: GKE-4gpu server results with Dynamic Batching turned Off, and max batch size per wire plane set to 256 (avg~=235)
results_rscaletest-gke4_nodybat_bigbat.txt: GKE-4gpu server results with Dynamic Batching turned Off, and max batch size per wire plane set to 16384 (avg~=1720) (
