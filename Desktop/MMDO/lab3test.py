from scipy.optimize import linprog

c = [-3, -3]
A = [
	[1, 2],
	[-3, -1],
	[-1, -5],
	[1, 0],
	[0, 1]
	]
b = [4, -4, -4, 3, 3]
res = linprog(c, A, b, method='simplex')
print(res)
