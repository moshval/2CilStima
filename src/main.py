'''
Nama      : Mohammad Sheva Almeyda Sofjan
NIM/Kelas : 13519018/K01
Deskripsi : Tugas Kecil 2 IF2211 Strategi Algoritma
            Aplikasi penyusunan kuliah 
            menggunakan Topological Sort, 
            penerapan Decrease n Conquer 
Deskripsi File : File Utama (Driver)
'''

from sols import countIn, makeAdj, topSort,getNextNodes # Solusi
from util import inputPrinter, matrixPrinter, printSems, reader, generateCode  # Utility
from time import time # Library Waktu

print("\n=======================================================")
print("             <<Memorable MatKul Planner>>                ")
print("  Dapat menyusun rencana pengambilan mata kuliah anda    ")
print("            Cr : Mohammad Sheva (13519018)               ")
print("=======================================================\n")

parse = reader() # Parsing dari text file , parse[0] = list isi dan parse[1] = list codelist
inittime = time() # Time start

print("\nInput :")
inputPrinter(parse[0])

adjmat = makeAdj(parse[0],parse[1]) # Merepresentasikan graf dalam matriks adjacency
# matrixPrinter(adjmat)

listIn = countIn(adjmat) # Membuat list yang berisi derajat masuk tiap node
# print(listIn)

order = topSort(adjmat,listIn) # Membuat list yang berisi index kode mata kuliah  yang sudah terurut menggunakan topological sort
# print(order)
if(len(order)!=0):
    finList = generateCode(order,parse[1]) # Membuat list yang berisi kode mata kuliah yang sudah terurut pada list order 
    # print(finList)
    print("\nOutput :")
    printSems(finList)

print("\nLama eksekusi : ",time()-inittime," detik")

