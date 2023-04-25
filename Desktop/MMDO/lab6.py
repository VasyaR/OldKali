import numpy as np
import math
from copy import copy, deepcopy
M = 999999

class Node:
	def __init__(self, is_a_leaf=False, is_visited=False, coords=[-M,-M], lowerbound=0, parent=None, matrix=[[]], active_raw_indexes=[], active_column_indexes=[]):
		self.is_a_leaf = is_a_leaf
		self.is_visited = is_visited
		self.coords = coords
		self.lowerbound = lowerbound
		self.parent = parent
		self.matrix = matrix
		self.active_raw_indexes = active_raw_indexes
		self.active_column_indexes = active_column_indexes
		
def count_lowerbound(node):
	func_node = deepcopy(node)	
	summ_of_constants = 0
	for i in func_node.active_raw_indexes:
		min_raw_elem = M
		for j in func_node.active_column_indexes:
			if func_node.matrix[i][j] < min_raw_elem:
				min_raw_elem = func_node.matrix[i][j]
		
		summ_of_constants += min_raw_elem
		
	for j in func_node.active_column_indexes:
		min_column_elem = M
		for i in func_node.active_raw_indexes:
			if func_node.matrix[i][j] < min_column_elem:
				min_column_elem = func_node.matrix[i][j]
		
		summ_of_constants += min_column_elem
		
	return func_node.lowerbound + summ_of_constants
	
		
def iteration_with_zero(node):
	func_node = deepcopy(node)
	coords = [-M, -M]
	highest_zero_mark = -M
	for i in func_node.active_raw_indexes:
		for j in func_node.active_column_indexes:
			min_raw_elem = M
			min_column_elem = M
			if func_node.matrix[i][j] == 0:
				for k in func_node.active_raw_indexes:
					if k != i:
						if func_node.matrix[k][j] < min_raw_elem:
							min_raw_elem = func_node.matrix[k][j]
							
				for z in func_node.active_column_indexes:
					if z != j:
						if func_node.matrix[i][z] < min_column_elem:
							min_column_elem = func_node.matrix[i][z]
							
				if min_raw_elem + min_column_elem > highest_zero_mark:
					highest_zero_mark = min_raw_elem + min_column_elem
					coords = [i, j]
					
	return coords
				

def reduction(node):
	func_node = deepcopy(node)
	summ_of_constants = 0
	min_raw_elems = {}
	min_column_elems = {}
	
	for i in func_node.active_raw_indexes:
		min_raw_elem = M
		for j in func_node.active_column_indexes:
			if func_node.matrix[i][j] < min_raw_elem:
				min_raw_elem = func_node.matrix[i][j]
		
		summ_of_constants += min_raw_elem
		#min_raw_elems.append(min_raw_elem)
		min_raw_elems[i] = min_raw_elem
		
	for i in func_node.active_raw_indexes:
		for j in func_node.active_column_indexes:
			if func_node.matrix[i][j] != M:
				func_node.matrix[i][j] -= min_raw_elems[i]
		
	for j in func_node.active_column_indexes:
		min_column_elem = M
		for i in func_node.active_raw_indexes:
			if func_node.matrix[i][j] < min_column_elem:
				min_column_elem = func_node.matrix[i][j]
		
		summ_of_constants += min_column_elem
		#min_column_elems.append(min_column_elem)
		min_column_elems[j] = min_column_elem
		
	for j in func_node.active_column_indexes:
		for i in func_node.active_raw_indexes:
			if func_node.matrix[i][j] != M:
				func_node.matrix[i][j] -= min_column_elems[j]
				
	if func_node.lowerbound == 0:
		func_node.lowerbound = summ_of_constants
		
	return func_node

	
#test
start_matrix = [
		[M, 5, 13, 3, 2],
               [4, M, 18, 8, 2],
               [8, 14, M, 18, 10],
               [2, 17, 16, M, 10],
               [2, 14, 14, 12, M]
		]	
"""
#My_Variant
start_matrix = [
		[M, 30, 18, 9, 19],
		[18, M, 20, 9, 2],
		[15, 19, M, 15, 17],
		[18, 19, 7, M, 4],
		[50, 3, 9, 17, M]
		]
"""
"""
#Youtube
start_matrix = [
		[M, 20, 18, 12, 8],
		[5, M, 14, 7, 11],
		[12, 18, M, 6, 11],
		[11, 17, 11, M, 12],
		[5, 5, 5, 5, M]
		]
"""
"""
#Metoduchka
start_matrix = [
		[M, 11, 21, 6, 8],
		[13, M, 17, 8, 11],
		[19, 18, M, 7, 21],
		[22, 15, 11, M, 17],
		[32, 4, 12, 6, M]
		]
"""
		
start_active_raw_indexes = []
start_active_column_indexes = []

for i in range(len(start_matrix)):
	start_active_raw_indexes.append(i)
	
for i in range(len(start_matrix)):
	start_active_column_indexes.append(i)
	
graph = []
current_node = Node(matrix=start_matrix, active_raw_indexes=start_active_raw_indexes, active_column_indexes=start_active_column_indexes)
iter_amount = 0
minimal_route = []

while(iter_amount < 150):

	if len(current_node.active_raw_indexes) == 1:
			minimal_route.append([current_node.active_raw_indexes[0], current_node.active_column_indexes[0]])
			minimal_route.append(current_node.coords)
			answer_iter_amount = 0
			while(current_node.parent):
				current_node = current_node.parent
				if current_node.is_visited:
					minimal_route.append(current_node.coords)
				answer_iter_amount += 1
				if answer_iter_amount > 150:
					print("Answers: a lot of iteratios")
					break
			break
	
	#if not current_node.is_visited:
	if current_node in graph:
		graph.remove(current_node)
	current_node = reduction(current_node)
	graph.append(current_node)
	
	highest_zero_coords = iteration_with_zero(current_node)
			
	unvisited_node = Node(True, False, highest_zero_coords, current_node.lowerbound, current_node, deepcopy(current_node.matrix), deepcopy(current_node.active_raw_indexes), deepcopy(current_node.active_column_indexes))
	unvisited_node.matrix[highest_zero_coords[0]][highest_zero_coords[1]] = M
	unvisited_node.lowerbound = count_lowerbound(unvisited_node)
	graph.append(unvisited_node)
	
	visited_node = Node(True, True, highest_zero_coords, current_node.lowerbound, current_node, deepcopy(current_node.matrix), deepcopy(current_node.active_raw_indexes), deepcopy(current_node.active_column_indexes))
	visited_node.matrix[highest_zero_coords[1]][highest_zero_coords[0]] = M
	visited_node.active_raw_indexes.remove(highest_zero_coords[0])
	visited_node.active_column_indexes.remove(highest_zero_coords[1])
	visited_node.lowerbound = count_lowerbound(visited_node)
	graph.append(visited_node)
	
	graph.remove(current_node)
	current_node.is_a_leaf = False
	graph.append(current_node)
	
	if visited_node.lowerbound <= unvisited_node.lowerbound:
		if visited_node.lowerbound <= current_node.lowerbound:
			current_node = visited_node
		else:
			temp_node = visited_node
			for node in graph:
				if node.is_a_leaf and node.lowerbound < temp_node.lowerbound:
					temp_node = node
		
			current_node = temp_node
			
	else:
		if unvisited_node.lowerbound <= current_node.lowerbound:
			current_node = unvisited_node
		else:
			temp_node = unvisited_node
			for node in graph:
				if node.is_a_leaf and node.lowerbound < temp_node.lowerbound:
					temp_node = node
			current_node = temp_node
	
	#print("UNVISIT lowerbound", unvisited_node.lowerbound)
	#print("Visit loverbound:", visited_node.lowerbound)
	#break
	iter_amount += 1
	
if iter_amount == 150:
	for node in graph:
		print(node.lowerbound)
	print("Lowerbound", current_node.lowerbound)
	print("Coords:", current_node.coords)
	print("A lot of iterations")
	
else:
	print_answer_iterator = 1
	answer_stop_iterator = 0
	last_direction = minimal_route[0]
	minimal_route_length = start_matrix[last_direction[0]][last_direction[1]]
	print("minimal route:")
	print(last_direction, end=" ")
	while(print_answer_iterator < len(minimal_route)):
		for direction in minimal_route:
			if direction[0] == last_direction[1]:
				print_answer_iterator += 1
				last_direction = direction
				minimal_route_length += start_matrix[last_direction[0]][last_direction[1]]
				print(last_direction, end=" ")
				
		answer_stop_iterator += 1
		if answer_stop_iterator == 150:
			print(minimal_route)
			print("A lot of iterations in answerprinting")
			break
			
	print("")
	print("Route length:", minimal_route_length)

