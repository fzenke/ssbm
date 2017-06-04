# SuperSpike benchmark suite

This is v0.1 of the SuperSpike benchmark suite, a collection of benchmarks for
supervised learning in spiking neural networks. It is meant to make supervised
learning techniques in spiking nets more comparable to each other.

Please see this early version of the suite as an invitation to suggest and add
your own benchmarks. Please get in touch.

When using a benchmark from this suite for your work please cite the benchmark name, 
address of this repository and version number/commit.


# Overview 

## Precise timing 

All precise timing benchmarks contain a spike raster file with the input spikes
(input.ras) and the target spike times (target.ras). These files are human
readable two-column formatted. The first column contains the firing time in
seconds and the second column denotes the id of the unit emitting a spike.

* poisson: 100 Poisson input spike trains with 0.5s duration, single target
  output spike train with 5 spikes
* poisson10: 100 Poisson input spike trains with 10s duration, and different
  Poisson target spike trains at different mean firing rates.
* secgen: Sequence generation benchmark. 100 Poisson input spike trains of 1s
  duration, 100 output units firing in sequence
* auryn: 100 Poisson input spike trains with 3.5s duration, 100 output spike
  trains resembling the Auryn logo
* monalisa: 1000 Poisson input spike trains with 33s duration, 500 output spike
  trains resembling Leonardo da Vinci's Mona Lisa
