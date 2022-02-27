# Convex-Hull-Library-and-Visualizer
> Tugas Kecil Mata Kuliah IF2211 Strategi Algoritma ITB.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
Himpunan titik pada bilang planar disebut convex jika untuk sembarang dua titik dua titik pada bidang tersebut (misal p dan q), seluruh segmen garis yang berakhir di p dan q berada pada himpunan tersebut
Program ini dapat menerima dataset, diambil 2 atribut dari dataset tersebut, diplot untuk visualisasi Tes Linear Separability Dataset dan dilakukan visualisasi convexhull dari hasil plot tersebut
## Technologies Used
- Python 3

## Features
- Library Convex Hull
- Visualisasi Tes Linear Separability Dataset & Visualisasi Convex Hull

## Setup
- Clone atau _download_ repository ini
- Buka folder repository ini pada terminal
```
pip install -r requirements.txt
```
- _Command_ tersebut akan melakukan install terhadap _library_ yang dibutuhkan untuk menjalankan program
- Jika ingin menggunakan file csv tambahan silahkan tambahkan file csv tersebut ke folder test

## Usage
- Pastikan sudah dilakukan clone atau _download_ terhadap repository ini
- Masuk ke directory tempat repo ini disimpan pada terminal
- Disarankan menggunakan virtualenv, Install terlebih dahulu virtualenv dengan _command_ pada terminal:
```
pip3 install virtualenv
virtualenv src
```
- Aktifkan virtualenv yang telah dibuat dengan _command_ :
```
src\Scripts\activate
```
- Setelah virtualenv aktif, install modul yang dibutuhkan dengan melakukan _command_ dibawah ini:
```
pip3 install -r requirements.txt
```
- _Command_ diatas melakukan install terhadap _library_ yang dibutuhkan untuk menjalankan program
- Dataset lain dapat digunakan dengan memasukkan CSV pada folder test, pastikkan atribut yang dipilih berisi hanya angka

## Acknowledgements
- Terima kasih kepada seluruh dosen pengajar dan asisten mata kuliah IF2211 Strategi Algoritma

## Contact
Created by:
- [@dhikaarta](https://github.com/dhikaarta)

