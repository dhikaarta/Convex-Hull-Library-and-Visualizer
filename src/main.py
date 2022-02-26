import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import matplotlib.pyplot as plt
from ConvexHull import ConvexHull
from os import path

print("===============================================")
print("Pilihan dataset :")
print("DATASET SCIKIT LEARN")
print("1 Iris")
print("2 Wine")
print("3 Breast Cancer")
print(" Program ini juga bisa menerima file csv, untuk melakukan ini masukkan csv ke folder target")
print("4. CSV sendiri (ada target)")
print("5. CSV sendiri (tidak ada target)")
print("===============================================")
cc = int(input())

if (cc == 1) :
    data = datasets.load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    hastarget = True
elif (cc == 2) :
    data = datasets.load_wine()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    hastarget = True
elif (cc == 3) :
    data = datasets.load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    hastarget = True
elif (cc == 4) :
    data = input("Nama file csv (c/: heart.csv) = ")
    file = ".\\target\\" + data
    while not path.exists(file) :
        print("File tidak dapat ditemukan")
        data = input("Nama file csv (c/: heart.csv) = ")
        file = ".\\target\\" + data
    df = pd.read_csv(file)
    if ('target') in df :
        hastarget = True
    if (hastarget == False) :
        print("CSV TIDAK ADA TARGET ! pilih 5 untuk csv tanpa target")
elif (cc == 5) :
    hastarget = False
    data = input("Nama file csv (c/: heart.csv) = ")
    file = ".\\target\\" + data
    while not path.exists(file) :
        print("File tidak dapat ditemukan")
        data = input("Nama file csv (c/: heart.csv) = ")
        file = ".\\target\\" + data
    df = pd.read_csv(file)
df.head()


#visualisasi hasil ConveXHull
if(hastarget) :
    if(cc == 4) :
        print("===========================================================")
        print("Kolom - kolom pada dataset :")
        col = df.columns.values.tolist()
        i = 1
        for col_names in col :
            if (str.lower(col_names) != "target") :
                print(f"{i}.{col_names}")
                i += 1
           
        print("===========================================================")
        print("Pilih 2 kolom Yang ingin di plot (dalam angka):")
        X = 0
        Y = 0
        while (X <= 0 or X >= len(col)) :
            X = int(input("Kolom Yang menjadi X : "))
        while (Y <= 0 or Y >= len(col)) :
            Y = int(input("Kolom Yang menjadi Y : "))
        ## 4. INISIALISASI PYPLOT
        plt.figure(figsize = (10, 6))
        colors = ['b','r','g']
        plt.title(label='ConveX Hull', fontsize=20)
        plt.xlabel(col[X-1])
        plt.ylabel(col[Y-1])
        target = df.target.unique()
        print(X)
        print(Y)
        ## 5. MEMBUAT CONVEXHULL
        for i in range(len(target)) :
            bucket = df[df['target'] == target[i]]
            bucket = bucket.iloc[:,[X-1,Y-1]].values
            hull = ConvexHull(bucket)
            plt.scatter(bucket[:, 0], bucket[:, 1], label=target[i])
            Xarray, Yarray = zip(*hull)
            plt.plot(Xarray, Yarray, '-o')
    elif(cc == 1 or cc ==2 or cc == 3) :
        print("===========================================================")
        print("Kolom - kolom pada dataset :")
        col = df.columns.values.tolist()
        i = 1
        for col_names in col :
            if (str.lower(col_names) != "target") :
                print(f"{i}.{col_names}")
                i += 1
           
        print("===========================================================")
        print("Pilih 2 kolom Yang ingin di plot (dalam angka):")
        X = 0
        Y = 0
        while (X <= 0 or X >= len(col)) :
            X = int(input("Kolom Yang menjadi X : "))
        while (Y <= 0 or Y >= len(col)) :
            Y = int(input("Kolom Yang menjadi Y : "))
        plt.figure(figsize = (10, 6))
        colors = ['b','r','g']
        xname = data.feature_names[X-1]
        yname = data.feature_names[Y-1]
        plt.title(f'{xname} vs {yname}')
        plt.xlabel(xname)
        plt.ylabel(yname)
        for i in range(len(data.target_names)):
            bucket = df[df['Target'] == i]
            bucket = bucket.iloc[:,[X-1,Y-1]].values
            hull = ConvexHull(bucket)  #bagian ini diganti dengan hasil implementasi
        #ConvexHull Divide & Conquer
            plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
            print(hull)
            x, y = zip(*hull)

            plt.plot(x, y, '-o')
    plt.legend()
    plt.show()
else :
    print("===========================================================")
    print("Kolom - kolom pada dataset :")
    col = df.columns.values.tolist()
    i = 1
    for col_names in col :
        if (str.lower(col_names) != "target") :
            print(f"{i}.{col_names}")
            i += 1
        
    print("===========================================================")
    print("Pilih 2 kolom Yang ingin di plot (dalam angka):")
    X = 0
    Y = 0
    while (X <= 0 or X >= len(col)) :
        X = int(input("Kolom Yang menjadi X : "))
    while (Y <= 0 or Y >= len(col)) :
        Y = int(input("Kolom Yang menjadi Y : "))
    ## 4. INISIALISASI PYPLOT
    plt.figure(figsize = (10, 6))
    colors = ['b','r','g']
    plt.title(label='ConveX Hull', fontsize=20)
    plt.xlabel(col[X-1])
    plt.ylabel(col[Y-1])
    print(X)
    print(Y)
    ## 5. MEMBUAT CONVEXHULL


    bucket = df.iloc[:,[X-1,Y-1]].values
    hull = ConvexHull(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1])
    Xarray, Yarray = zip(*hull)
    plt.plot(Xarray, Yarray, '-o')
    plt.show()

