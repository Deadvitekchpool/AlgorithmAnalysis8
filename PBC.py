import random
import time
from matplotlib import pyplot as plt
import math

def complexity(alg, n):
	if alg == 'n':
		return n
	elif alg == 'n^2':
		return n**2
	elif alg == 'log':
		return n * math.log(n, 10)
	elif alg == 'n^3':
		return n**3

def RandomSample(m, n):
	if m == 0:
		S = []
		return S
	else:
		S = RandomSample(m - 1, n - 1)
		i = random.randrange(1, n)
		# print(S)
		if i in S:
			S.append(n)
		else:
			S.append(i)
		return S
	# B = [None] * n
	# offset = random.randrange(1, n)
	# for i in range(n):
	# 	dest = i + offset
	# 	if dest >= n:
	# 		dest -= n
	# 	B[dest] = A[i]
	# return B

times = []
for i in range(1, 2001):
	temp_time = 0
	for j in range(5):
		# A = [x for x in range(10)]
		r1 = random.randrange(1, 100)
		r2 = random.randrange(150, 2001)
		# S = []
		t = time.time()
		RandomSample(r1, r2)
		temp_time += time.time() - t
	times.append(temp_time / 5)

k = 1900
theoretical_step_time = times[k] / complexity('n', k)
theoretical_values = [theoretical_step_time * n for n in range(1, 2001)]

plt.title('Random Sample')
plt.scatter(range(1, 2001), times, marker='+', label='real', alpha=.3)
plt.plot(range(1, 2001), theoretical_values, "r", label="O(n)")
plt.legend()
plt.show()
