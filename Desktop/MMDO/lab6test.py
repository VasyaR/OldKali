import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming

distance_matrix = np.array(
			[	
			[0, 30, 18, 9, 19],
			[18, 0, 20, 9, 2],
			[15, 19, 0, 15, 17],
			[18, 19, 7, 0, 4],
			[50, 3, 9, 17, 0]
			]
			)
			
path, distance = solve_tsp_dynamic_programming(distance_matrix)

print(path, distance)
