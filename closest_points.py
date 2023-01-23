# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 10:47:49 2022

@author: t-jan
"""
import random
import math
import matplotlib.pyplot as plt


def points_generator(n, plane):
    Points=[]
    if plane=='s' or plane=='square':
        for i in range(0,n):
            x = random.random()*n+100
            y = random.random()*n
            Points.append([x,y])
    elif plane=='c' or plane=='circle':
        while(len(Points) < n):
            x = random.random()*n
            y = random.random()*n
            ray = n/2
            distance_from_centre = math.sqrt( (n/2-x)**2 + (n/2-y)**2 )
            if distance_from_centre <= ray:
                Points.append([x,y])
    else:
        print("Plane undefined")
        return 0
    return Points

def draw_points(Points,col):
    for i in range(0,len(Points)):
        plt.scatter(Points[i][0],Points[i][1],color=col)#'k')
        plt.axis('square')
   #     plt.xlim([0,n])
   #     plt.ylim(0,n)

def distance(A,B):
    return math.sqrt( (A[0]-B[0])**2 + (A[1]-B[1])**2 )

def nearest_few(points): # only for 2 or 3 points
    if len(points)==2:
        return points
    distances=[]
    distances.append(distance(points[0],points[1]))
    distances.append(distance(points[0],points[2]))
    distances.append(distance(points[1],points[2]))
    mi=min(distances)
    if mi==distances[0]: return points[0],points[1]
    elif mi==distances[1]: return points[0],points[2]
    else: return points[1],points[2]

def nearest_points(points):
    n=len(points)
    if n<4:
        return nearest_few(points)
    mid=math.floor(n/2)
    T=[]
    B=[]
    for i in range(0,mid):
        B.append(points[i])
    for i in range(mid,n):
        T.append(points[i])
    draw_points(T, 'b')
    draw_points(B, 'crimson')
    b=nearest_points(B)
    t=nearest_points(T)
    distb=distance(b[0],b[1])
    distt=distance(t[0],t[1])
    if distt<distb:
        draw_points(t, 'yellow')
        return t
    else:
        draw_points(b, 'limegreen')
        return b

'''
def scal(nearests1, nearests2):
    if distance(nearests1[0],nearests1[1]) < distance(nearests2[0],nearests2[1]): return nearests1
    else: return nearests2
'''

plane = 's'
n = 9

points=points_generator(n, plane)
points=sorted(points, key=lambda k: [k[1], k[0]]) # sort points by y
draw_points(points, 'k')


print(nearest_points(points))

