import math

def my_entropy(probabilities, base=2):
	res = 0
	for i in range(len(probabilities)):
		res += probabilities[i] * math.log(probabilities[i], base)
	return -res

"""	
print("Haffman kod for task A, cheking for Kraftman inequality:", end=" ")


res1 = 6 * pow(2, -3) + 4 * pow(2, -4)

print(res1, end=" ")
if res1 <= 1:
	print("success")
else:
	print("failed")
	
print("Shennon-Fano_elias kod for task A, cheking for Kraftman inequality:", end=" ")

res2 = pow(2, -4) + 9 * pow(2, -5)

print(res2, end=" ")
if res2 <= 1:
	print("success")
else:
	print("failed")
	
print("Haffman kod for task B, cheking for Kraftman inequality:", end=" ")

res3 = 5 * pow(2, -3) + 6 * pow(2, -4)

print(res3, end=" ")
if res3 <= 1:
	print("success")
else:
	print("failed")
	
print("Shennon-Fano-Elias kod for task A, cheking for Kraftman inequality:", end=" ")

res4 = 3 * pow(2, -5) + 3 * pow(2, -4) + 5 * pow(2, -6)

print(res4, end=" ")
if res4 <= 1:
	print("success")
else:
	print("failed")
"""

print("Etropy for task A", end=" ")

list1 = [0.09, 0.12, 0.09, 0.12, 0.09, 0.07, 0.13, 0.11, 0.07, 0.11]
entropy1 = my_entropy(list1)
print(entropy1)

print("Expected length for Haffman code for Task A:", end=" ")

exp1 = 4*0.09 + 3*0.12 + 4*0.09 + 3*0.12 + 3*0.09 + 4*0.07 + 3*0.13 + 3*0.11 + 4*0.07 + 3*0.11
print(exp1)

print("Expected length for Shannon-Fano-Elias code for Task A:", end=" ")
exp2 = 4*0.13 + 5*3*0.09 + 5*2*0.12 + 5*2*0.11 + 5*2*0.07
print(exp2)

print("Etropy for task B", end=" ")

list2 = [0.048, 0.048, 0.143, 0.19, 0.048, 0.143, 0.095, 0.095, 0.095, 0.048, 0.047]
entropy2 = my_entropy(list2)
print(entropy2)

print("Expected length for Haffman code for Task B:", end=" ")

exp3 = 3*0.19 + 3*2*0.143 + 3*2*0.095 + 4*0.095 + 4*4*0.048 + 4*0.047
print(exp3)

print("Expected length for Shannon-Fano-Elias code for Task B:", end=" ")
exp4 = 4*0.19 + 4*2*0.143 + 5*3*0.095 + 6*4*0.048 + 6*0.047
print(exp4)
