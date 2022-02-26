import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math 
from sklearn import datasets

def ConvexHull(numpyarray) :
    solution = []
    points = numpyarray.tolist()

    #Sort array untuk mencari 2 titik terjauh awal
    sortedArray = sorted(points , key=lambda k: [k[0], k[1]])
    p1 = sortedArray[0]
    pn = sortedArray[-1]
    solution += [p1,pn]

    #Setelah dimasukkan ke array solusi, hilangkan kedua titik
    sortedArray.pop(0) 
    sortedArray.pop(-1)

    #Membagi kumpulan titik menjadi convex hull atas dan bawah
    s1,s2 = aboveOrBelow(p1,pn,sortedArray)

    #Dilakukan rekursi(divide terus menerus)
    solution += recursiveconvex(p1,pn,s1,1)
    solution += recursiveconvex(p1,pn,s2,2)

    solution = np.asarray(solution)

    #Agar garis yang dibentuk membentuk poligon mengelilingi sempurna, titik - titik di sort berdasarkan sudut yang dibuat dengan titik tengah
    x = [p[0] for p in solution]
    y = [p[1] for p in solution]
    center = (sum(x) / len(solution), sum(y) / len(solution))
    solution = sorted(solution,key = lambda k: (math.atan2(k[1]-center[1],k[0]-center[0])))
    solution.append(solution[0])
    return solution



def recursiveconvex(p1,p2,points,int) :
    #Fungsi rekursif untuk mencari titik2 convex hull lainnya, int disini menandakan arah , 1 berarti atas(kasus convex hull atas) , 2 bawah(convex hull bawah)
    #Exit case untuk rekursif
    if points == [] or p1 is None or p2 is None :
        return[]
    
    solution = []
    #Mencari titik terjauh dari garis
    farthest = farthestpoint(p1,p2,points)
    solution += [farthest]
    points.remove(farthest)

    #Membagi kumpulan titik menjadi atas dan bawah dengan garis yang baru dibuat
    above1, below1 = aboveOrBelow(p1,farthest,points)
    above2, below2 = aboveOrBelow(p2,farthest,points)

    #Rekursif
    if int == 1 :
        solution += recursiveconvex(p1,farthest,above1,1)
        solution += recursiveconvex(farthest,p2,above2,1)
    else :
        solution += recursiveconvex(p1,farthest,below1,2)
        solution += recursiveconvex(farthest,p2,below2,2)

    return solution

def aboveOrBelow(p1,p2,array) :
    #Fungsi untuk mencari kumpulan titik yang menjadi bagian atas atau bawah suatu garis dalam convex hull
    s1 = []
    s2 = []

    #X sama, garis vertikal tidak ada atas bawah
    if p2[0] - p1[0] == 0 :
        return s1,s2

    #Membuat garis menjadi rumus umum y = mx + c, setiap poin akan disubsitusi, apabila y0 > mx0 + c berarti dia diatas dan sebaliknya
    grad = (p2[1] - p1[1]) / (p2[0] - p1[0])
    c = p1[1] - (grad * p1[0])
    for points in array :
        if points[1] < grad * (points[0]) + c :
            s2.append(points) 
        if points[1] > grad * (points[0]) + c :
            s1.append(points) 
        
    return s1,s2

def distance(p1,p2,p3) :
    #fungsi menghitung jarak dari garis p1-p2 ke titik p3
    p1 = np.asarray(p1)
    p2 = np.asarray(p2)
    p3 = np.asarray(p3)
    return np.abs(np.cross(p2-p1, p1-p3)) / np.linalg.norm(p2-p1)

def farthestpoint(p1,p2,c) :
    #Mencari titik terjauh ke garis p1-p2 dari kumpulan titik c
    max = -1
    farthest = None
    for point in c :
        temp = distance(p1,p2,point)
        if temp > max :
            max = temp
            farthest = point
        elif temp == max :
            if(findAngle(p1,point,p2) > findAngle(p1,farthest,p2)) :
                farthest = point
                max = temp
    return farthest


def findAngle(p1,pmax,p2) :
    #mencari sudut antara ketiga titik, untuk kasus ini berarti sudut antara garis p1-pmax dan pmax-p2
    ang = math.degrees(math.atan2(p2[1]-pmax[1], p2[0]-pmax[0]) - math.atan2(p1[1]-pmax[1], p1[0]-pmax[0]))
    return ang + 360 if ang < 0 else ang


