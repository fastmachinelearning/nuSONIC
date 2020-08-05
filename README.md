Meaning of columns:
* col 1: number of simultaneous clients
* col 2: full event time
* col 3: sd for col 2
* col 4: EmTrackMichelId time
* col 5: sd for col 4

the second file "results_rscaletest-gke4.txt" has two additional columns:
* col 6: inference only time
* col 7: sd for col 6

Contents of files:
* results_rscaletest-gke1.txt: GKE-1gpu server results with Dynamic Batching turned On
* results_rscaletest-gke4.txt: GKE-4gpu server results with Dynamic Batching turned On
* results_rscaletest-gke4_bigbat.txt: GKE-4gpu server results with Dynamic Batching turned On, and max batch size per wire plane set to 16384 (avg~=1720)
* results_rscaletest-gke4_nodybat.txt: GKE-4gpu server results with Dynamic Batching turned Off, and max batch size per wire plane set to 256 (avg~=235)
* results_rscaletest-gke4_nodybat_bigbat.txt: GKE-4gpu server results with Dynamic Batching turned Off, and max batch size per wire plane set to 16384 (avg~=1720)

Plots:
* plot1: dynamic batching On: [gke-1gpu] vs [gke-4gpu]
* plot1b: full event time, dyn batch on vs off (with model for dyn batch off)
* plot1c: full event time, dyn batch on vs off (with models for dyn batch on vs off)
* plot2: gke-4gpu: [dynamic batching On] vs [dynamic batching Off]
* plot3: gke-4gpu, dynamic batching Off: [small batch size] vs [big batch size]
* plot4: gke-4gpu: [dynamic batch On, small batch size] vs [dynamic batching Off, big batch size]
* plot5a: gke-4gpu: [dynamic batch On, big batch size] vs [dynamic batching Off, big batch size]
* plot5b: gke-4gpu: [dynamic batch On, big batch size] vs [dynamic batching On, small batch size]
* plot5c: gke-4gpu: [dynamic batch On, small batch size] vs [dynamic batching Off, small batch size]

Plot scrips 2-5c generates a plot file for [EmTrackMichelId time vs number of simultaneous jobs] and [full event time vs number of simultaneous jobs] for each comparison