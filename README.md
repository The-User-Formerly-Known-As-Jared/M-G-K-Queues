# M-G-K-Queues
M-G-k Simulation under different paradigms.

An M/G/k queue is a servicing structure in which inputs arrive by a Poisson process (M) - that is with an exponentially distributed interarrival time. Service time is a random variable from some general distribution (G) and there are only k service channels. Thus, k inputs can be serviced at once, if all k service channels are full, arrivals begin to fill up an infinite waiting room.

For simulation, a specific distribution must be chosen for G. It can be input as a parameter, serv_dist into the main (single_trial) function.

This code was written to simulate the transient behavior or M/G/k queues, specifically to model genes as queues for a summer project at University of Houston. For this reason, the inputs and outputs are often referred to as molecules in the commenting. And because of this interest in transient behavior, an output threshold R must be denoted as a parameter.

Other parameters can be tinkered with, the mean of the arrivals - alpha, the mean of the service time - tau, the variance  of the service time - sigma.

The original code is written in a functional style, which I think works quite well. However there may be performance improvements to be had by conversion to the use of Simpy package or an OOP paradigm. 

