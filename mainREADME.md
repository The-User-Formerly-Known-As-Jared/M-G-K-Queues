# M-G-K-Queues

An M/G/k queue is a servicing structure in which inputs arrive by a Poisson process (M) - that is with an exponentially distributed interarrival time. Service time is a random variable from some general distribution (G) and there are only k service channels. Thus, k inputs can be serviced at once, if all k service channels are full, arrivals begin to fill up an infinite waiting room.

This code was written to simulate the transient behavior or M/G/k queues, specifically to model genes as queues. For this reason, the inputs and outputs are often referred to as molecules in the commenting and randomly generated times denote arrivals or reactions. And because of this interest in transient behavior, an output threshold R (count of things exiting the queue) is be denoted as a parameter.

For simulation, a specific distribution must be chosen for G. It can be input as a parameter, serv_dist into the main (single_trial) function.

Other parameters can be tinkered with, the mean of the arrivals - alpha, the mean of the service time - tau, the variance  of the service time - sigma.

The algorithm used is a modified version of Delay Gillespie. This is why if there is a reaction time in stack before a generated arrival time, that arrival time gets thrown out and time step is advanced to the next reaction time. A new arrival time will be generated after, and as shown with Delay Gillespie, this does not affect the output distribution.

The original code is written in a functional style, which I think works quite well. However there may be performance improvements to be had by conversion to the use of Simpy package or an OOP paradigm. 

