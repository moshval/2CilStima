'''
Nama      : Mohammad Sheva Almeyda Sofjan
NIM/Kelas : 13519018/K01
Deskripsi : Tugas Kecil 2 IF2211 Strategi Algoritma
            Aplikasi penyusunan kuliah 
            menggunakan Topological Sort, 
            penerapan Decrease n Conquer 
Deskripsi File : File Utama (Driver)
'''

import importlib # Library import module

#import sols
sols = importlib.import_module('13519018_sols') # Solusi
#import util
util = importlib.import_module('13519018_util') # Utility

from time import time # Library Waktu

print("\n=======================================================")
print("             <<Memorable MatKul Planner>>                ")
print("  Dapat menyusun rencana pengambilan mata kuliah anda    ")
print("            Cr : Mohammad Sheva (13519018)               ")
print("=======================================================\n")

parse = util.reader() # Parsing dari text file , parse[0] = list isi dan parse[1] = list codelist
inittime = time() # Time start

print("\nInput :")
util.inputPrinter(parse[0]) # Print input

adjmat = sols.makeAdj(parse[0],parse[1]) # Merepresentasikan graf dalam matriks adjacency

listIn = sols.countIn(adjmat) # Membuat list yang berisi derajat masuk tiap node
order = sols.topSort(adjmat,listIn) # Membuat list yang berisi index kode mata kuliah  yang sudah terurut menggunakan topological sort

if(len(order)!=0):
    print("\nBanyak Mata Kuliah :",end=" ")
    print(len(parse[1]))
    print("Banyak Semester yang dibutuhkan :",end=" ")
    print(len(order))
    finList = util.generateCode(order,parse[1]) # Membuat list yang berisi kode mata kuliah yang sudah terurut pada list order 
    print("\nOutput :")
    util.printSems(finList) # Print output per semester

print("\nLama eksekusi : ",time()-inittime," detik")

exitter = input("Masukkan input apapun untuk keluar dari program...")

