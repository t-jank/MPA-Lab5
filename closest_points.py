# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 10:47:49 2022

@author: t-jan
"""
import random
import math
import matplotlib.pyplot as plt
import statistics


def points_generator(n, plane):
    Points=[]
    if plane=='s' or plane=='square':
        for i in range(0,n):
            x = random.uniform(0,10*n)
            y = random.uniform(0,10*n)
            Points.append([x,y])
    elif plane=='c' or plane=='circle':
        while(len(Points) < n):
            x = random.random()*n
            y = random.random()*n
            ray = n/2
            distance_from_centre = math.sqrt( (n/2-x)**2 + (n/2-y)**2 )
            if distance_from_centre <= ray:
                Points.append([x,y])
    elif plane=='b':
        while(len(Points) < n):
            x = random.uniform(0,10*n)
            while x < 7.5*n and x > 2.5*n:
                x = random.uniform(0,10*n)
            y = random.uniform(0,10*n)
            Points.append([x,y])
    elif plane=='gd':
        while(len(Points) < n):
            y = random.uniform(0,10*n)
            while y < 7.5*n and y > 2.5*n:
                y = random.uniform(0,10*n)
            x = random.uniform(0,10*n)
            Points.append([x,y])
    elif plane=='srh':
        while(len(Points) < n):
            y = random.uniform(0,10*n)
            while y > 7.5*n or y < 2.5*n:
                y = random.uniform(0,10*n)
            x = random.uniform(0,10*n)
            Points.append([x,y])
    elif plane=='srv':
        while(len(Points) < n):
            x = random.uniform(0,10*n)
            while x > 7.5*n or x < 2.5*n:
                x = random.uniform(0,10*n)
            y = random.uniform(0,10*n)
            Points.append([x,y])
    elif plane=='n':
        for i in range(0,n):
            x = random.gauss(mu=5*n, sigma=2.5*n)
            y = random.gauss(mu=5*n, sigma=2.5*n)
            Points.append([x,y])
    elif plane=='invn':
        while(len(Points) < n):
            p=random.random()
            x = random.uniform(0,10*n)
            if p>0.5:
                while x < 7.5*n and x > 2.5*n:
                    x = random.uniform(0,10*n)
            y = random.uniform(0,10*n)
            if p>0.5:
                while y < 7.5*n and y > 2.5*n:
                    y = random.uniform(0,10*n)
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


counter_of_distances_to_compute = 0

def distance(A,B):
    global counter_of_distances_to_compute
    counter_of_distances_to_compute += 1
    return math.sqrt( (A[0]-B[0])**2 + (A[1]-B[1])**2 )


def nearest_brute_force(points):
    n=len(points)
    d=999999
    sol=[]
    sol.append([0,0])
    sol.append([1,1])
    for i in range(0,n):
        for j in range(0,n):
            if i!=j:
                tmp_distance=distance(points[i], points[j])
                if tmp_distance<d:
                    d=tmp_distance
                    sol[0]=points[i]
                    sol[1]=points[j]
    return sol

def nearest_up_down(points_top,points_bottom,Psol,d):
    n_top=len(points_top)
    n_bottom=len(points_bottom)
    for t in range(0, n_top):
        for b in range(0, n_bottom):
            d_temp = distance(points_top[t], points_bottom[b])
            if  d_temp < d:
                d=d_temp
                Psol[0]=points_bottom[b]
                Psol[1]=points_top[t]
    return Psol
    

def nearest_points(points):
    n=len(points)
    if n<4:
        return nearest_brute_force(points)
    mid=math.floor(n/2)
    T=[]
    B=[]
    for i in range(0,mid):
        B.append(points[i])
    for i in range(mid,n):
        T.append(points[i])
    kreska = T[0][1]
    b=nearest_points(B)
    t=nearest_points(T)
    d_b=distance(b[0],b[1])
    d_t=distance(t[0],t[1])
    if d_t<d_b:
        psol = t
        d = d_t
    else:
        psol = b
        d = d_b
    bottom_to_check=[]
    top_to_check=[]
    for bb in range(0,len(B)):
        if kreska - B[bb][1] < d:  # sprawdzamy odleglosc od kreski podzialu
            bottom_to_check.append(B[bb])
    for tt in range(0,len(T)):
        if T[tt][1] - kreska < d:
            top_to_check.append(T[tt])
    return nearest_up_down(top_to_check, bottom_to_check, psol, d)



plane = 'invn'
nMin=5
nMax=10000
nStep=100
nRepeat=5

ox=[]
nlogn=[]
dupa=[]
for n in range(nMin,nMax,nStep):
    counter_of_distances_to_compute=0
    for r in range(0,nRepeat):
        points=points_generator(n, plane)
        points=sorted(points, key=lambda k: [k[1], k[0]]) # sort points by y
        np=nearest_points(points)
    ox.append(n)
    wsp=1.68
    nlogn.append(wsp*n*math.log(n))
    if n==nMin:
        plt.scatter(n,counter_of_distances_to_compute/nRepeat,color='k',label='symulacja')
    else:
        plt.scatter(n,counter_of_distances_to_compute/nRepeat,color='k')
plt.plot(ox,nlogn,color='orangered',label=str(wsp)+'*n*logn',linewidth=2.5)

plt.title(plane)
plt.xlabel('n')
plt.ylabel('Liczba odległości do policzenia')
plt.legend()
plt.show()

