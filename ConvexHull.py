import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn import datasets

def ConvexHull(numpyarray) :
    solution = []
    points = numpyarray.tolist()
    sortedArray = sorted(points , key=lambda k: [k[0], k[1]])
    p1 = sortedArray[0]
    pn = sortedArray[-1]
    solution += [p1,pn]

    sortedArray.pop(0) 
    sortedArray.pop(-1)
    s1,s2 = aboveOrBelow(p1,pn,sortedArray)
    solution += recursiveconvex(p1,pn,s1,1)
    solution += recursiveconvex(p1,pn,s2,2)
    solution = np.asarray(solution)
    return solution



def recursiveconvex(p1,p2,points,int) :
    if points == [] or p1 is None or p2 is None :
        return[]
    
    solution = []
    farthest = farthestpoint(p1,p2,points)
    solution += [farthest]
    points.remove(farthest)

    above1, below1 = aboveOrBelow(p1,farthest,points)
    above2, below2 = aboveOrBelow(p2,farthest,points)

    
    if int == 1 :
        solution += recursiveconvex(p1,farthest,above1,1)
        solution += recursiveconvex(farthest,p2,above2,1)
    else :
        solution += recursiveconvex(p1,farthest,below1,2)
        solution += recursiveconvex(farthest,p2,below2,2)

    return solution

def aboveOrBelow(p1,p2,array) :
    s1 = []
    s2 = []

    if p2[0] - p1[0] == 0 :
        return s1,s2

    grad = (p2[1] - p1[1]) / (p2[0] - p1[0])
    c = p1[1] - (grad * p1[0])
    for points in array :
        if points[1] <= grad * (points[0]) + c :
            s2.append(points) 
        if points[1] >= grad * (points[0]) + c :
            s1.append(points) 
        
    return s1,s2

def distance(p1,p2,p3) :
    p1 = np.asarray(p1)
    p2 = np.asarray(p2)
    p3 = np.asarray(p3)
    return np.abs(np.cross(p2-p1, p1-p3)) / np.linalg.norm(p2-p1)

def farthestpoint(p1,p2,c) :
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
    ang = math.degrees(math.atan2(p2[1]-pmax[1], p2[0]-pmax[0]) - math.atan2(p1[1]-pmax[1], p1[0]-pmax[0]))
    return ang + 360 if ang < 0 else ang



data = datasets.load_iris()
#create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
df.head()

#visualisasi hasil ConvexHull
plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('Petal Width vs Petal Length')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    hull = ConvexHull(bucket)  #bagian ini diganti dengan hasil implementasi
#ConvexHull Divide & Conquer
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    print(hull)
    x, y = zip(*hull)

    plt.plot(x, y, '-o')
plt.legend()
plt.show()