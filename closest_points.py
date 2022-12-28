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
            x = random.random()*n
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

def draw_points(Points):
    for i in range(0,len(Points)):
        plt.scatter(Points[i][0],Points[i][1],color='k')
        plt.axis('square')
        plt.xlim([0,n])
        plt.ylim(0,n)



plane = 'c'
n = 200

points=points_generator(n, plane)
draw_points(points)
