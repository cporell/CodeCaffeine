'''
Acme corporation conducts 5K run each year where they have a strange tradition. The winners of this race are the second and
seventh fastest runners. Given a list of 10000 runners, find the 2nd and 7th fastest runners.
'''

import numpy as np
import heapq


# generating runners_time using gaussian distribution with mean 30 minutes and standard deviation of 3 min.
mean, std = 30, 3
runners_time = np.random.normal(mean, std, 10000)


def find_2nd_fastest_runner(runners_time):
	fastest_runner = 2^63-1
	second_fastest_runner = 2^63-1
	i = 0
    #your code here. try to do in one pass of for loop.
	while i < len(runners_time):
		if runners_time[i] < second_fastest_runner:
			if runners_time[i] <= fastest_runner:
				second_fastest_runner = fastest_runner
				fastest_runner = runners_time[i]
			else:
				second_fastest_runner = runners_time[i]
		i += 1
	return second_fastest_runner


def find_7th_fastest_runner(runners_time):
	seventh_fastest_runner = 60

	list_runners_time = runners_time.tolist()
	heapq.heapify(list_runners_time)
	seventh_fastest_runner = heapq.nsmallest(7, list_runners_time)[6]
	
	return seventh_fastest_runner

if (sorted(runners_time)[1] == find_2nd_fastest_runner(runners_time)):
    print "Second fastest runner is ", find_2nd_fastest_runner(runners_time)

if (sorted(runners_time)[6] == find_7th_fastest_runner(runners_time)):
    print "Seventh fastest runner is ", find_7th_fastest_runner(runners_time)

