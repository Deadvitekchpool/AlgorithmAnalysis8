from numpy import random
import random as r
import networkx as nx
from matplotlib import pyplot as plt
import time
from igraph import *
import string
import math

def complexity(alg, n):
	if alg == 'n':
		return n
	elif alg == 'n^2':
		return n**2
	elif alg == 'log':
		return math.log(n, 10)
	elif alg == 'n^3':
		return n**3
	elif alg == 'root':
		return n**0.5

chars = string.ascii_lowercase

times = []
for i in range(1, 2001):
	temp_time = 0
	for k in range(5):
		G = nx.DiGraph()
		for j in range(i + 1):
			s = set()
			while len(s) != 2:
				s.add(r.choice(chars))
			G.add_edge(*s, capacity=float(random.randint(1,6)))
		edges = list(G.edges)
		t = time.time()
		flow_value, flow_dict = nx.maximum_flow(G, *edges[random.randint(0, len(G.edges))])
		temp_time += time.time() - t
	times.append(temp_time / 5)

k = 1900
theoretical_step_time = times[k] / complexity('log', k)
theoretical_log_values = [theoretical_step_time * math.log(n, 10) for n in range(1, 2001)]

plt.title('Maximum Flow')
plt.scatter(range(1, 2001), times, marker='+', label='real', alpha=.3)
plt.plot(range(1, 2001), theoretical_log_values, "r", label="O(logn)")
plt.legend()
plt.show()