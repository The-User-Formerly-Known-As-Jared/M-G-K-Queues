import heapq as hq
import random as rd


def single_trial(serv_dist_ , k_, alpha_, tau_, sigma_, R_):
	
	
	x = 0 							# in system, waiting to be serviced
	y = 0 							# in system, currently being serviced
	
	current_time = 0 
	next_arrival = 0
	output = 0 
	
	INFTY = float("inf")			#denote largest value in stack - for testing first case
	q = [] 							#initializes stack											
	hq.heappush(q, INFTY)			#puts INFTY in stack
	
	
	threshold_reached = False 		#kills process after output threshold is reached
	
	while threshold_reached == False:
		
		next_arrival = current_time + rd.expovariate(alpha_)			#generates next arrival time
		
		
		if q[0] <= next_arrival:										#if there is a reaction in stack before next arrival
			
			current_time = q[0]												#advance time to THAT reaction, a reaction will now take place
			
			if x == 0:														#if there are NO molecules waiting to be serviced
				y -= 1															#decrease y
				hq.heappop(q)													#take current time out of stack
			
			else:															#if there ARE molecules waiting to be serviced
				x -= 1															#decrease X (y exits Y, x moves to Y,)
				rand_service = current_time + serv_dist_(tau_, sigma_)		#generate new service time for the "transferred" molecule
				hq.heapreplace(q, rand_service)									#replace current time in stack with new service time
			
			#print "time is",current_time,"x =",x,"y =",y,"output =",output,"\n"
			
			output += 1														#in either case, increase output
			
		else:															#if there is NO reaction in stack before next arrival
			current_time = next_arrival										#advance time
			
			if y == k_:														#if service channels are full
				x += 1															#increase x
			else:															#if service channels are available
				y += 1															#increase y
				rand_service = current_time + serv_dist_(tau_, sigma_)		#generate new service time 
				hq.heappush(q, current_time + rand_service)						#put new service time into stack
				
		if output == R_:
			threshold_reached = True									
			
	return current_time
	

