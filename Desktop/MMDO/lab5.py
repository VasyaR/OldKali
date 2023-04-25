import math
from copy import copy, deepcopy

def everything_is_pair(templist):
	for i in range(len(templist)):
		if templist[i] % 2 != 0:
			return False
	return True
	

def my_dfs(myC, visited, curr_i, curr_j, vertical, start, needed_i, needed_j, paritychecker_i, paritychecker_j):
	visited.append([curr_i, curr_j])
	paritychecker_i[curr_i] += 1
	paritychecker_j[curr_j] += 1
	"""
	print(curr_i, curr_j)
	if curr_i == 0 and curr_j == 1:
		print(paritychecker_i)
		print(paritychecker_j)
	"""
	if start == "green":
		for i in range(len(myC)):
			if myC[i][curr_j][0] != -1:
				in_cycle = my_dfs(myC, visited, i, curr_j, False, "yellow", needed_i, needed_j, paritychecker_i, paritychecker_j)
				if in_cycle:
					return True
		for j in range(len(myC[0])):
			if myC[curr_i][j][0] != -1:
				in_cycle = my_dfs(myC, visited, curr_i, j, True, "yellow", needed_i, needed_j, paritychecker_i, paritychecker_j)
				if in_cycle:
					return True
		return False
	
	if start == "yellow":
		if vertical:
			for i in range(len(myC)):
				if myC[i][curr_j][0] != -1 and [i, curr_j] not in visited:
					in_cycle = my_dfs(myC, visited, i, curr_j, False, "red", needed_i, needed_j, paritychecker_i, paritychecker_j)
					if in_cycle:
						return True
			visited.remove([curr_i, curr_j])
			paritychecker_i[curr_i] -= 1
			paritychecker_j[curr_j] -= 1
			return False
		else:
			for j in range(len(myC[0])):
				if myC[curr_i][j][0] != -1 and [curr_i, j] not in visited:
					in_cycle = my_dfs(myC, visited, curr_i, j, True, "red", needed_i, needed_j, paritychecker_i, paritychecker_j)
					if in_cycle:
						return True
			visited.remove([curr_i, curr_j])
			paritychecker_i[curr_i] -= 1
			paritychecker_j[curr_j] -= 1
			return False
			
	if start == "red":
		if curr_i == needed_i or curr_j == needed_j:
			if everything_is_pair(paritychecker_i) and everything_is_pair(paritychecker_j):
				#print("I`m here")
				return True
		if vertical:
			for i in range(len(myC)):
				if myC[i][curr_j][0] != -1 and [i, curr_j] not in visited:
					in_cycle = my_dfs(myC, visited, i, curr_j, False, "red", needed_i, needed_j, paritychecker_i, paritychecker_j)
					if in_cycle:
						return True
			visited.remove([curr_i, curr_j])
			paritychecker_i[curr_i] -= 1
			paritychecker_j[curr_j] -= 1
			return False
		else:
			for j in range(len(myC[0])):
				if myC[curr_i][j][0] != -1 and [curr_i, j] not in visited:
					in_cycle = my_dfs(myC, visited, curr_i, j, True, "red", needed_i, needed_j, paritychecker_i, paritychecker_j)
					if in_cycle:
						return True
			visited.remove([curr_i, curr_j])
			paritychecker_i[curr_i] -= 1
			paritychecker_j[curr_j] -= 1
			return False
		
	print("My_dfs last raw")
	return False
					 

def potencials_with_northwestcorner(a, b, C):
	a_copy = deepcopy(a)
	b_copy = deepcopy(b)
	myC = []
	#myC elem = value + cyclemarlk
	for i in range(len(C)):
		myC.append([])
		for j in range(len(C[0])):
			myC[i].append([-1, 0])	

	#Northwestcorner method
	#degenerate = vurodzhenuy
	itemp1 = 0
	jtemp1 = 0
	degenerate = 0
	iteramount1 = 0
	while(degenerate < len(a) + len(b) - 1):
		#print("I " + str(itemp1) + " J " + str(jtemp1) + " a " + str(a_copy[itemp1]) + " b " + str(b_copy[jtemp1]))
		if(a_copy[itemp1] == b_copy[jtemp1]):
			degenerate += 2
			myC[itemp1][jtemp1][0] = a_copy[itemp1]
			a_copy[itemp1] = 0
			b_copy[jtemp1] = 0
			if itemp1 != len(a) - 1:
				myC[itemp1 + 1][jtemp1][0] = 0
			else:
				if jtemp1 != len(b) - 1:
					myC[itemp1][jtemp1 + 1][0] = 0
			itemp1 += 1
			jtemp1 += 1
			continue
			
		if(a_copy[itemp1] < b_copy[jtemp1]):
			degenerate += 1
			myC[itemp1][jtemp1][0] = a_copy[itemp1]
			b_copy[jtemp1] -= a_copy[itemp1]
			a_copy[itemp1] = 0
			itemp1 += 1
			continue
			
		if(a_copy[itemp1] > b_copy[jtemp1]):
			degenerate += 1
			myC[itemp1][jtemp1][0] = b_copy[jtemp1]
			a_copy[itemp1] -= b_copy[jtemp1]
			b_copy[jtemp1] = 0
			jtemp1 += 1
			
		if iteramount1 >= 1000:
			print("northwestcorner a lot of iterations")
			return -1
			
	print("Base plan:")
	for i in range(len(C)):
		for j in range(len(C[0])):
			print(myC[i][j][0], end=" ")
		print("")
	
	#potencials
	iteramount = 0
	while(True):
		a_potencials = [0]
		b_potencials = []
		for i in range(len(a) - 1):
			a_potencials.append(-999999)
		for i in range(len(b)):
			b_potencials.append(-999999)
		
		#print myC
		"""
		print("Main table:")
		for i in range(len(C)):
			for j in range(len(C[0])):
				print(myC[i][j][0], end=" ")
			print("")
		"""
		base_plan_potencials_amount = 0
		while(base_plan_potencials_amount < len(a) + len(b) - 1):
			for i in range(len(C)):
				for j in range(len(C[0])):
					if myC[i][j][0] != -1:
						if b_potencials[j] != -999999 and a_potencials[i] == -999999:
							a_potencials[i] = C[i][j] - b_potencials[j]
							base_plan_potencials_amount += 1
						if a_potencials[i] != -999999 and b_potencials[j] == -999999:
							b_potencials[j] = C[i][j] - a_potencials[i]
							base_plan_potencials_amount += 1
		
		#print baseplan potencials	
		"""
		print("baseplan potencials")			
		for i in range(len(a_potencials)):
			print(a_potencials[i], end=" ")
		print("")
		for i in range(len(b_potencials)):
			print(b_potencials[i], end=" ")
		print("")
		#break
		"""
		optimized = True
		maxpotencial_i = -5
		maxpotencial_j = -5
		maxpotencial = -999999
		C_potencials = []
		for i in range(len(C)):
			C_potencials.append([])
			for j in range(len(C[0])):
				temp_potencial = a_potencials[i] + b_potencials[j] - C[i][j]
				C_potencials[i].append(temp_potencial)
				if temp_potencial > 0:
					optimized = False
					if temp_potencial > maxpotencial:
						maxpotencial = temp_potencial
						maxpotencial_i = i
						maxpotencial_j = j
					
		#print all potencials
		"""
		print("all potencials")
		for i in range(len(C)):
			for j in range(len(C[0])):
				print(C_potencials[i][j], end=" ")
			print("")
		#break
		"""
		
		if optimized:
			result = 0
			
			print("Main table:")
			for i in range(len(C)):
				for j in range(len(C[0])):
					print(myC[i][j][0], end=" ")
				print("")
			
			for i in range(len(myC)):
				for j in range(len(myC[0])):
					if myC[i][j][0] != -1:
						result += myC[i][j][0] * C[i][j]
			print("Result = " + str(result))
			return 1
		
		else:
			paritychecker_i = []
			paritychecker_j = []
			for i in range(len(a)):
				paritychecker_i.append(0)
			for i in range(len(b)):
				paritychecker_j.append(0)
				
			#green = first iteration, yellow = second iteration
			start = "green"
			visited = []
			no_error = my_dfs(myC, visited, maxpotencial_i, maxpotencial_j, True, start, maxpotencial_i, maxpotencial_j, paritychecker_i, paritychecker_j)
			#print(visited)
			
			if not no_error:
				
				print("No cycles found", iteramount)
				return -1
			
			lowest_value_in_cycle = 999999
			
			for i in range(len(visited)):
				if i % 2 == 0:
					myC[visited[i][0]][visited[i][1]][1] = 1
					if i == 0:
						myC[visited[i][0]][visited[i][1]][0] = 0
						
				else:
					myC[visited[i][0]][visited[i][1]][1] = -1
					if myC[visited[i][0]][visited[i][1]][0] < lowest_value_in_cycle:
						lowest_value_in_cycle = myC[visited[i][0]][visited[i][1]][0]
				
			already_erased = False		
			for i in range(len(visited)):
				if myC[visited[i][0]][visited[i][1]][1] == 1:
					myC[visited[i][0]][visited[i][1]][0] += lowest_value_in_cycle
					myC[visited[i][0]][visited[i][1]][1] = 0
				else:
					if myC[visited[i][0]][visited[i][1]][0] == lowest_value_in_cycle:
						if already_erased:
							myC[visited[i][0]][visited[i][1]][0] = 0
							myC[visited[i][0]][visited[i][1]][1] = 0
						else:
							myC[visited[i][0]][visited[i][1]][0] = -1
							myC[visited[i][0]][visited[i][1]][1] = 0
							already_erased = True
					else:
						myC[visited[i][0]][visited[i][1]][0] -= lowest_value_in_cycle	
						myC[visited[i][0]][visited[i][1]][1] = 0	
			
		
		iteramount += 1
		if iteramount >= 50:
			print("Endless iterations")
			return -1
					
	print("Something unexpected happened")	
	return -1



a_real = [60, 40, 100, 50]
b_real = [30, 80, 65, 35, 40]
C_real = [
	[8, 12, 4, 9, 10],
	[7, 5, 15, 3, 6],
	[9, 40, 6, 12, 7],
	[5, 30, 2, 6, 4]
	]
	
potencials_with_northwestcorner(a_real, b_real, C_real)


"""
a_real = [100, 150, 200, 100]
b_real = [120, 200, 100, 30, 100]
C_real = [
	[7, 5, 6, 9, 5],
	[4, 5, 8, 8, 10],
	[3, 2, 5, 4, 4],
	[9, 11, 10, 8, 11]
	]
potencials_with_northwestcorner(a_real, b_real, C_real)
"""
"""
a_real = [30, 20, 40, 50]
b_real = [35, 20, 55, 30]
C_real = [
	[2, 4, 1, 3],
	[5, 6, 5, 4],
	[3, 7, 9, 5],
	[1, 2, 2, 7]
	]
potencials_with_northwestcorner(a_real, b_real, C_real)
"""
