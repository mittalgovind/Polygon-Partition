'Please make sure that the INPUT is A CLOSED RECTILINEAR POLYGON,'
'CONSTRUCTED WHILE GOING IN ANTI-CLOCKWISE ONLY'
# importing libraries
import networkx as nx
import turtle
import matplotlib.pyplot as plt
import warnings
from networkx.algorithms import bipartite
import math

warnings.filterwarnings("ignore")
# declaration list
wn = turtle.Screen()
# a turtle called gopu 
gopu = turtle.Turtle() 
# co-ordinate points
x = [] 
y = []
# vertex-type := rectilinear = -1; convex = 0; concave = 1 
vertex_type = [] 
# store the bipartite graph of chords
G = nx.Graph()
# the line below can be commented if one needs animation
gopu.speed(0)
# starts recording keys being pressed
gopu.begin_poly()

# Event handlers
stride = 25
# Up  = up() - vertex to be deleted = -1
def up():
    vertex_type.append(-1)
    gopu.forward(stride)
 
# left = left() ; make vertex - convex = 0
def left():
    vertex_type.append(0)
    gopu.setheading(gopu.heading()+90)
    gopu.forward(stride)
 
# right = right() ; make vertex - concave = 1
def right():
    vertex_type.append(1)
    gopu.setheading(gopu.heading()-90)
    gopu.forward(stride)
 
# back = back() -- doing undo is allowed only once.
def back():
    vertex_type.pop()
    gopu.undo()

# quits the screen and outputs the plots the partitioned polygon
def partition_polygon():
    # closing the screen
    wn.bye()
    # stopped recording the polygon
    gopu.end_poly()
    p = gopu.get_poly()
    p = list(p)
    compute_partition(p)  
    
'''
The movements of the turtle are recorded and the rectilinear graph thus 
obtained is converted into bipartite graph of chords
'''
def compute_partition(p):
    # p now contains the list of coordinates of vertices
    # last one is same as the origin
    # and the origin is always going to be a convex vertex
    p.pop()
    vertex_type[0] = 0
    
    # x and y contain list of x and y coordinates respectively
    for i,j in p:
        x.append(i)
        y.append(j)

    # this is done as there are some very small errors in recording the 
    # position by the turtle library
    for i in range(len(x)):
        x[i] = int(x[i])
        y[i] = int(y[i])

    for i in range(len(x)):
        if x[i] % stride != 0:
            x[i] += (stride - x[i] % stride)
        if y[i] % stride != 0:
            y[i] += (stride - y[i] % stride)
    
    collinear_vertices = [i for i,val in enumerate(vertex_type) if val == -1]
    # finding the chords inside the polygon
    horizontal_chords = []
    vertical_chords = []
    concave_vertices = [i for i,val in enumerate(vertex_type) if val == 1]

    # middles is used because, there are cases when there is a chord between vertices
    # and they intersect with external chords, hence if there is any vertex in between 
    # two vertices then skip that chord. 
    for i in range(len(concave_vertices)):
        for j in range(i+1,len(concave_vertices)):
            if concave_vertices[j] != concave_vertices[i] + 1:
                middles = []
                if y[concave_vertices[i]] == y[concave_vertices[j]]:
                    for k in range(len(x)):
                        if y[concave_vertices[i]] == y[k] and (x[concave_vertices[i]] < x[k] and x[concave_vertices[j]] > x[k] \
                                                              or x[concave_vertices[i]] > x[k] and x[concave_vertices[j]] < x[k]):
                            middles.append(k)
                    if len(middles) == 0:
                        horizontal_chords.append((concave_vertices[i],concave_vertices[j]))
                middles = []
                if x[concave_vertices[i]] == x[concave_vertices[j]]:
                    for k in range(len(x)):
                        if x[concave_vertices[i]] == x[k] and (y[concave_vertices[i]] < y[k] and y[concave_vertices[j]] > y[k] \
                                                              or y[concave_vertices[i]] > y[k] and y[concave_vertices[j]] < y[k]):
                            middles.append(k)
                    if len(middles) == 0:
                        vertical_chords.append((concave_vertices[i],concave_vertices[j]))
            

    
    fig, ax = plt.subplots()
    ax.plot(x+[0], y+[0], color='black')
    ax.scatter(x+[0], y+[0], color='black')
    for i in range(len(x)):
        ax.annotate(i, (x[i],y[i]))
    plt.show()
    plt.clf()
    print("Horizontal chords before collinear vertices = ", horizontal_chords)
    print("vertical_chords = ", vertical_chords)

    fig, ax = plt.subplots()
    ax.plot(x+[0], y+[0], color='black')
    ax.scatter(x+[0], y+[0], color='black')
    for i in range(len(x)):
        ax.annotate(i, (x[i],y[i]))
    for i,j in horizontal_chords:
        ax.plot([x[i],x[j]],[y[i],y[j]],color='black')
    for i,j in vertical_chords:
        ax.plot([x[i],x[j]],[y[i],y[j]], color='black')
    plt.show()
    plt.clf()
    for i in range(len(collinear_vertices)):
        for j in range(len(concave_vertices)):
            middles = []
            if y[collinear_vertices[i]] == y[concave_vertices[j]]:
                if collinear_vertices[i] < concave_vertices[j]:
                    for k in range(len(x)):
                        if y[k] == y[collinear_vertices[i]] and (x[k] < x[concave_vertices[j]] \
                            and x[k] > x[collinear_vertices[i]] or x[k] > x[concave_vertices[j]] \
                            and x[k] < x[collinear_vertices[i]]):
                            middles.append(k)
                    if collinear_vertices[i]+1 == concave_vertices[j]:
                        middles.append(0)
                else:
                    for k in range(len(x)):
                        if y[k] == y[collinear_vertices[i]] and (x[k] > x[concave_vertices[j]] \
                            and x[k] < x[collinear_vertices[i]] or x[k] < x[concave_vertices[j]] \
                            and x[k] > x[collinear_vertices[i]]):
                            middles.append(k)
                    if collinear_vertices[i] == concave_vertices[j]+1:
                        middles.append(0)
                if len(middles) == 0:
                    horizontal_chords.append((collinear_vertices[i],concave_vertices[j]))
            middles = []
            if x[collinear_vertices[i]] == x[concave_vertices[j]]:
                if collinear_vertices[i] < concave_vertices[j]:
                    for k in range(len(x)):
                        if x[k] == x[collinear_vertices[i]] and (y[k] < y[concave_vertices[j]] \
                            and y[k] > y[collinear_vertices[i]] or y[k] > y[concave_vertices[j]] \
                            and y[k] < y[collinear_vertices[i]]):
                            middles.append(k)
                    if collinear_vertices[i]+1 == concave_vertices[j]:
                        middles.append(0)
                else:
                    for k in range(len(x)):
                        if x[k] == x[collinear_vertices[i]] and (y[k] > y[concave_vertices[j]] \
                            and y[k] < y[collinear_vertices[i]] or y[k] < y[concave_vertices[j]] \
                            and y[k] > y[collinear_vertices[i]]):
                            middles.append(k)
                    if collinear_vertices[i] == concave_vertices[j]+1:
                        middles.append(0)
                if len(middles) == 0:
                    vertical_chords.append((collinear_vertices[i],concave_vertices[j]))
    
    # displaying all attributes and important parameters involved
#     print("p = ",p)
#     print("vertex_Type = ",vertex_type)
#     print ("x = ", x)
#     print ("y = ", y)
#     print("collinear_vertices = ", collinear_vertices)
#     print("concave_vertices =", concave_vertices)
    print("horizontal_chords = " ,horizontal_chords)
    print("vertical_chords = ",vertical_chords)
    # drawing the partitioned polygon 
    fig, ax = plt.subplots()
    ax.plot(x+[0], y+[0], color='black')
    ax.scatter(x+[0], y+[0], color='black')
    for i in range(len(x)):
        ax.annotate(i, (x[i],y[i]))
    for i,j in horizontal_chords:
        ax.plot([x[i],x[j]],[y[i],y[j]],color='black')
    for i,j in vertical_chords:
        ax.plot([x[i],x[j]],[y[i],y[j]],color='black')
    plt.show()

# Defining the keys function
wn.onkey(up, "Up")
wn.onkey(left, "Left")
wn.onkey(right, "Right")
wn.onkey(back, "Down")
wn.onkey(partition_polygon, "Escape")
wn.listen()
wn.mainloop()

