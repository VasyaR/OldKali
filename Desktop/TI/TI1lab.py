import math
import random
from scipy.stats import entropy
def my_entropy(probabilities, base=2):
	res = 0
	for i in range(len(probabilities)):
		res += probabilities[i] * math.log(probabilities[i], base)
	return -res
	
length = random.randint(10, 20)
elems = []
for i in range(length):
	temp = random.randint(0,10)
	elems.append(temp)
	elems.sort()
	
print("Elems:", end=" ")
print(elems)
probabilities = []
checker = 1
for i in range(length):
	checker -= 1
	if checker > 0:
		continue
	probability = elems.count(elems[i])/length
	probabilities.append(probability)
	print(elems[i], end=' probability: ')
	print(probability)
	checker = elems.count(elems[i])
	

#probabilities = [0.09, 0.12, 0.09, 0.12, 0.09, 0.07, 0.13, 0.11, 0.07, 0.11]	
print("My entrophy:", end=" ")
print(my_entropy(probabilities))
print("Correct entrophy:", end=" ")
print(entropy(probabilities, base=2))
