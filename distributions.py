import random as rd
import math

# Generates Bernoulli service time with mean tau and variance sigma
def coin_flip(tau_, sigma_):
	flip = rd.randint(1,2)
	
	if flip == 1:
		return tau_ - sigma_
	else:
		return tau_ + sigma_
		
#Generates uniform service time with mean tau and variance sigma

def uni(tau_, sigma_):
	number = rd.uniform(tau_ - sigma_, tau_ + sigma_)
	return number
