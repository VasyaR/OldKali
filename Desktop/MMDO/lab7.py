from sympy import *
import numpy as np
from scipy import optimize

x = Symbol('x')

print("Enter your function")
strf = input()
f = lambdify(x, strf, 'numpy')
length = -1
while (length <= 0):	
	print("Enter a")
	a = float(input())
	print("Enter b")
	b = float(input())
	length = b - a
	if length <=0:
		print("b must me bigger than a")

a0 = a
b0 = b
eps = -1
while (eps <= 0):
	print("Enter eps")
	eps = float(input())
	if eps <= 0:
		print("Eps must be bigger than 0")
		
fibonacci_list = [1, 1]
n_1 = 1
n_2 = 1
n = (b - a) / eps
iterator = 3
while iterator:
	n_1, n_2 = n_2, n_1 + n_2
	fibonacci_list.append(n_2)
	if iterator < 3:
		iterator -= 1
		continue
	if n_2 >= n:
		n = len(fibonacci_list) - 1
		iterator -= 1
	
	
y = a + fibonacci_list[n] / fibonacci_list[n + 2] * length
z = a + fibonacci_list[n + 1] / fibonacci_list[n + 2] * length
for i in range(n):
	if i == 0:
		continue
	if y == z:
		print("X =", y)
		print("Function minimum:", )
		break
	if f(y) < f(z):
		b = z
		z = y
		y = a + fibonacci_list[n - i]/fibonacci_list[n - i + 2] * (b - a)
		print(f"X{i} =", y)
		print(f"Function minimum{i}:", f(y))
	if f(y) > f(z):
		a = y
		y = z
		z = a + fibonacci_list[n - i + 1]/fibonacci_list[n - i + 2] * (b - a)
		print(f"X{i} =", z)
		print(f"Function minimum{i}:", f(z))
print("")
print("Final answer:")
print("X =", (y + z) / 2)
print("Function minimum:", f((y + z) / 2))
print("")
	
	
print("Imbedded function results:")
print("X:", optimize.fminbound(f, a0, b0))
print("Function minimum:", f(optimize.fminbound(f, a0, b0)))
#x**4 + 4*x**2 - 32*x + 1

	


	
