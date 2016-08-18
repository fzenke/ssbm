# SLSNB Poisson to Poisson benchmark

The Poisson to Poisson benchmark is part of the supervised learning in spiking
networks benchmark (SLSNB) suite. The task is to learn a Poisson output spike
train from a number of fixed Poisson input spike trains.  The present directory
contains one input dataset consisting of 1000 Poisson spike trains at 5Hz and
duration 10s. And multiple single cell target outputs at increasing
frequencies.  Spikes are given in the human readible event based RAS format.
All spikes are aligned to a 0.1ms grid.
