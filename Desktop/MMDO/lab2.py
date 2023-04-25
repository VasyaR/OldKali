from scipy.optimize import linprog

c = [-2, -3]
a = [[2, 3], [3, 1], [-2, 5], [-1, 0], [0, -1]]
b = [17, 15, 15, 0, 0]

res = linprog(c, A_ub=a, b_ub=b)#, bounds=[x1_bounds, x2_bounds])
#print(f"res = {res}")
print('Optimal value:', round(res.fun*-1, ndigits=2),
      '\nx values:', res.x,
      '\nStatus:', res.message)
