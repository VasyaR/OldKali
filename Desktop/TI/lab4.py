import math

def my_entropy(probabilities, base=2):
	res = 0
	for i in range(len(probabilities)):
		res += probabilities[i] * math.log(probabilities[i], base)
	return -res
	
def conditional_entropy(q, p_mistake, p_erase):
	
	return  -q * math.log(q, 2) - p_mistake * math.log(p_mistake, 2) - p_erase * math.log(p_erase, 2)

def max_entropy(q, p_mistake, p_erase):
	return -(q + p_mistake) * math.log((q + p_mistake) / 2, 2) - p_erase * math.log(p_erase, 2)

	
y = [0.31, 0.305, 0.385]
r = [0.85, 0.1, 0.05]

mistake = 0.05
erasing = 0.15
correct_symbol = 0.8

table1 = [
	[0.255, 0.015, 0.04],
	[0.03, 0.255, 0.02],
	[0.015, 0.03, 0.34]	
	] 

table2 = [
	[0.85, 0.05, 0.1],
	[0.1, 0.85, 0.05],
	[0.05, 0.1, 0.85]	
	]

res = 0
for i in range (len(table1)):
	for j in range(len(table1[0])):
		res += table1[i][j] * math.log(table2[i][j], 2)
	
res = -res
#Vzaemna informacia	
#print(my_entropy(y, base=2) - my_entropy(r, base=2))
#Propyskna zdatnist`
#print(math.log(3, 2) - my_entropy(r, base=2))
#print(my_entropy(correct_symbol))
#print(math.log(3, 2) - 0.15 - my_entropy(mistake) - my_entropy(correct_symbol))
#print(max_entropy(correct_symbol, mistake, erasing), math.log(3, 2))
print(max_entropy(correct_symbol, mistake, erasing) - conditional_entropy(correct_symbol, mistake, erasing))
