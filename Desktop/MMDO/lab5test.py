from pulp import *

def solve(c, a, b):
    problem = LpProblem("tp", LpMinimize)

    rows, cols = len(a), len(b)
    variables = LpVariable.dicts("x", (range(rows), range(cols)), lowBound=0, cat=LpInteger)

    problem += lpSum([variables[i][j] * c[i][j] for i in range(rows) for j in range(cols)])

    for i in range(rows):
        problem += lpSum([variables[i][j] for j in range(cols)]) == a[i]

    for j in range(cols):
        problem += lpSum([variables[i][j] for i in range(rows)]) == b[j]

    problem.solve(PULP_CBC_CMD(msg=0, warmStart=True))
    for v in problem.variables():
        if v.varValue > 0:
            print(v.name, "=", v.varValue)
    return value(problem.objective)
    
a_real = [60, 40, 100, 50]
b_real = [30, 80, 65, 35, 40]
C_real = [
	[8, 12, 4, 9, 10],
	[7, 5, 15, 3, 6],
	[9, 40, 6, 12, 7],
	[5, 30, 2, 6, 4]
	]
print(solve(C_real, a_real, b_real))
