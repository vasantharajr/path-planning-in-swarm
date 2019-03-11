import math
import numpy as np
from hungarian import Hungarian
from tkinter import *
from vis import Ball
import gradient_descent
from time import sleep

#n = int(input("Enter the number of UAVs"))
n = 9
initial_pos = []
x = 300
y = 100
initial_pos.append([x,y])
x = 300
y = 200
initial_pos.append([x,y])
x = 300
y = 300
initial_pos.append([x,y])
x = 400
y = 100
initial_pos.append([x,y])
x = 400
y = 200
initial_pos.append([x,y])
x = 400
y = 300
initial_pos.append([x,y])
x = 500
y = 100
initial_pos.append([x,y])
x = 500
y = 200
initial_pos.append([x,y])
x = 500
y = 300
initial_pos.append([x,y])

desired_shape = []
x = 100
y = 200
desired_shape.append([x,y])
x = 150
y = 250
desired_shape.append([x,y])
x = 200
y = 300
desired_shape.append([x,y])
x = 250
y = 350
desired_shape.append([x,y])
x = 300
y = 400
desired_shape.append([x,y])
x = 350
y = 350
desired_shape.append([x,y])
x = 400
y = 300
desired_shape.append([x,y])
x = 450
y = 250
desired_shape.append([x,y])
x = 500
y = 200
desired_shape.append([x,y])

k = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
	for j in range(n):
		x = -np.transpose(initial_pos[i]).dot(np.array(desired_shape[j]))
		k[i][j] = x

hungarian = Hungarian(k)
hungarian.calculate()
x_star = hungarian.get_results()
k_star = hungarian.get_total_potential()

# initialize root Window and canvas
root = Tk()
root.title("Balls")
root.resizable(True,True)
canvas = Canvas(root, width = 800, height = 800)
canvas.pack()

# create two ball objects and animate them
balls = []
color = ["red", "green", "black", "orange", "blue", "yellow", "purple", "grey", "brown", "magenta"]

balls = []

qq = []
dist = 100000
for x in range(-100, 100):
	for y in range(-100, 100):
		q = np.array([x,y])+np.array(desired_shape)
		dist_1 = gradient_descent.calculate_distance(initial_pos, q, x_star)
		if dist > dist_1:
			dist = dist_1
			qq = q 
_ = 0
for i, j in x_star:
	ball1 = Ball(canvas, initial_pos[i][0], initial_pos[i][1], color[_])
	ball = Ball(canvas, qq[j][0], qq[j][1], color[_])
	balls.append(ball1)
	_ = int(_ + 1)%10
for i, j in x_star:
	balls[i].move_ball(qq[j][0], qq[j][1])

#root.after(50, update_pos, initial_pos, desired_shape, x_star, balls)
root.mainloop()
	




'''
ds = 0
for i in desired_shape:
	x = np.transpose(i).dot(np.array(i))
	ds += x
alpha_star = (np.transpose(initial_pos).dot(np.array(desired_shape))+n*k_star)/(np.transpose(desired_shape).dot(np.array(desired_shape))-(n*ds))

d_star = (initial_pos - np.transpose(alpha_star.dot(np.transpose(desired_shape))))/n

q = np.transpose(alpha_star.dot(np.transpose(desired_shape)) + np.transpose(d_star))
q = q%600

print(q)
'''