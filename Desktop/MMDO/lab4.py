import math
from copy import copy, deepcopy

def simplex_with_dv(c, A, b, maximize=True):
	A_temp = deepcopy(A)
	if not maximize:
		for i in range(len(c)):
			c[i] = -1 * c[i]
			
	basis_c = []
	ignor_list = []

	for j in range(len(A[0])):
		for i in range(len(A)):
			if A[i][j] == 1:
				summ = 0
				for k in range(len(A)):
					if k != i:
						if A[k][j] != 0:
							summ += 100
				if summ == 0:
					temp_basis_elem = [j, c[j]]
					basis_c.append(temp_basis_elem)	
			
	
	stop = 0			
	while(True):
		m1_raw = []
		minus_in_plan = False
		lowest_plan_elem = 0
		lowest_plan_elem_index = -5
		for j in range(len(A[0])):
			summ = 0
			Mcounter = 0
			for i in range(len(A)):
				if b[i] < 0:
					minus_in_plan = True
					if abs(b[i]) > lowest_plan_elem:
						lowest_plan_elem = b[i]
						lowest_plan_elem_index = i
				else:
					summ += basis_c[i][1] * A[i][j]
				
			m1_raw.append(summ - c[j])
			
		minelem = 99999999
		m1_raw_minelemindex = -5
		
		if minus_in_plan:
				
			smallest_expected_plan = 999999
			leadelement_index = [lowest_plan_elem_index, 0]
			for j in range(len(A[0])):
				if A[lowest_plan_elem_index][j] < 0 and abs(m1_raw[j]/A[lowest_plan_elem_index][j]) < smallest_expected_plan:
					smallest_expected_plan = abs(m1_raw[j]/A[lowest_plan_elem_index][j])
					leadelement_index[1] = j
					
			if smallest_expected_plan == 999999:
				print("no solution, endless range of permissible values in dv")
				return -1
				
			else:				
				for i in range(len(b)):
					if i != leadelement_index[0]:
						b[i] = (b[i] * A[leadelement_index[0]][leadelement_index[1]] - b[leadelement_index[0]] * A[i][leadelement_index[1]]) / A[leadelement_index[0]][leadelement_index[1]]
						
				for j in range(len(A[0])):
					for i in range(len(A)):
						if i != leadelement_index[0]:
							#print("indexes: ", leadelement_index[0], " ", leadelement_index[1])
							A_temp[i][j] = (A[i][j] * A[leadelement_index[0]][leadelement_index[1]] - A[leadelement_index[0]][j] * A[i][leadelement_index[1]]) / A[leadelement_index[0]][leadelement_index[1]]
								#print("test:", A[i][j], " ", A[leadelement_index[0]][leadelement_index[1]], " ", A[leadelement_index[0]][j], " ", A[i][leadelement_index[1]])
				
				b[leadelement_index[0]] = b[leadelement_index[0]] / A[leadelement_index[0]][leadelement_index[1]]
				
				#print("Leadraw: ")
				for j in range(len(A[0])):
					if j != leadelement_index[1]:
						A_temp[leadelement_index[0]][j] = A[leadelement_index[0]][j] / A[leadelement_index[0]][leadelement_index[1]]
					
					
				for i in range(len(A)):
					if i != leadelement_index[0]:
						A_temp[i][leadelement_index[1]] = 0
						
				A_temp[leadelement_index[0]][leadelement_index[1]] = 1
				A = deepcopy(A_temp)
				basis_c[leadelement_index[0]][0] = leadelement_index[1]
				basis_c[leadelement_index[0]][1] = c[leadelement_index[1]]
					
					
		else:
			m1_is_optimal = True
			
			#print("!!!!!!!!!!!!!!!!!!!m1_raw:")
			#for i in range(len(m1_raw)):
			#	print(m1_raw[i],end=" ")
			
			for j in range(len(A[0])):
				if m1_raw[j] < 0:
					m1_is_optimal = False
					if m1_raw[j] < minelem:
						minelem = m1_raw[j]
						m1_raw_minelemindex = j
			
			if m1_is_optimal:
				"""
				print("m1raw:")
				for i in range(len(m1_raw)):
					print(m1_raw[i], end=" ")
				print("")
				"""	
				res = 0
				print("Answer: ")
				for i in range(len(basis_c)):
					res += basis_c[i][1] * b[i]
					print("X", basis_c[i][0], " = ", b[i], end=" ")
					
				print(" ")
				
				if not maximize:
					print("function minimun: ", -res)
					
				else:
					print("function maximum: ", res)
					
				return 1			
				
			else:
								
				smallest_expected_plan = 999999
				leadelement_index = [0, 0]
				
				for i in range(len(A)):
					if A[i][m1_raw_minelemindex] > 0 and b[i]/A[i][m1_raw_minelemindex] < smallest_expected_plan:
						smallest_expected_plan = b[i]/A[i][m1_raw_minelemindex]
						leadelement_index[0] = i
						leadelement_index[1] = m1_raw_minelemindex
						
				if smallest_expected_plan == 999999:
						"""
						print("Stop: ", stop)
						for i in range(len(A)):
							for j in range(len(A[0])):
								print(A[i][j], " ", end=" ")
							print(" ")
						print("Indexes: ", leadelement_index[0], " ", leadelement_index[1])
						print("")
						print("b vector: ")
						for i in range(len(b)):
							print(b[i])
						print("")
						print("m1raw:")
						for i in range(len(m1_raw)):
							print(m1_raw[i], end=" ")
						print("")
						print("m2raw:")
						for i in range(len(m2_raw)):
							print(m2_raw[i], end=" ")
						print("")
						print("Ignor list: ")
						for i in range(len(ignor_list)):
							print(ignor_list[i], end=" ")
						print("")
						print("Basis: ")
						for i in range(len(basis_c)):
							print(basis_c[i][0], basis_c[i][1], end=" ")
						print("")	
						"""	
						print("no solution, endless range of permissible values for m1")
						return -1
						
						
				else:
					
					for i in range(len(b)):
						if i != leadelement_index[0]:
							b[i] = (b[i] * A[leadelement_index[0]][leadelement_index[1]] - b[leadelement_index[0]] * A[i][leadelement_index[1]]) / A[leadelement_index[0]][leadelement_index[1]]
							
					for j in range(len(A[0])):
						if j != leadelement_index[1]:
							for i in range(len(A)):
								if i != leadelement_index[0]:
									A_temp[i][j] = (A[i][j] * A[leadelement_index[0]][leadelement_index[1]] - A[leadelement_index[0]][j] * A[i][leadelement_index[1]]) / A[leadelement_index[0]][leadelement_index[1]]
					
					b[leadelement_index[0]] = b[leadelement_index[0]] / A[leadelement_index[0]][leadelement_index[1]]
					
					for j in range(len(A[0])):
						if j != leadelement_index[1]:
							A_temp[leadelement_index[0]][j] = A[leadelement_index[0]][j] / A[leadelement_index[0]][leadelement_index[1]]
						
					for i in range(len(A)):
						if i != leadelement_index[0]:
							A_temp[i][leadelement_index[1]] = 0
					
					A_temp[leadelement_index[0]][leadelement_index[1]] = 1
					A = deepcopy(A_temp)
					basis_c[leadelement_index[0]][0] = leadelement_index[1]
					basis_c[leadelement_index[0]][1] = c[leadelement_index[1]]
		
		"""
		for i in range(len(A)):
			for j in range(len(A[0])):
				print(A[i][j], " ", end=" ")
			print(" ")
		"""
		"""
		print("Indexes: ", leadelement_index[0], " ", leadelement_index[1])
		print("")
		
		
		print("Basis: ")
		for i in range(len(basis_c)):	
			print(basis_c[i][0], basis_c[i][1], end=" ")
		print("")	
		"""
		stop += 1
		if stop == 50:
			#print("ignor_list:")
			#for i in range(len(ignor_list)):
			#	print(ignor_list[i], " ")
			#print("")
			print("endless iterations")
			return -1




c = [3, 3, 0, 0, 0, 0, 0]

A = [	
	[1, 2, 1, 0, 0, 0, 0],
	[-3, -1, 0, 1, 0, 0, 0],
	[-1, -5, 0, 0, 1, 0, 0],
	[1, 0, 0, 0, 0, 1, 0],
	[0, 1, 0, 0, 0, 0, 1]
	]
	
b_real = [4, -4, -4, 3, 3]
simplex_with_dv(c, A, b_real)

"""
c = [4, -4, -4, 3, 3, 0, 0]

A = [
	[-1, 3, 1, -1, 0, 1, 0],
	[-1, 1, 5, 0, -1, 0, 1]
	]
	
b_real = [-3, -3]
simplex_with_dv(c, A, b_real, maximize=False)
"""
