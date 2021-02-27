'''
Nama      : Mohammad Sheva Almeyda Sofjan
NIM/Kelas : 13519018/K01
Deskripsi : Tugas Kecil 2 IF2211 Strategi Algoritma
            Aplikasi penyusunan kuliah 
            menggunakan Topological Sort, 
            penerapan Decrease n Conquer 
Deskripsi File : File Utama (Driver)
'''

from sols import countIn, generateCode, makeAdj, topSort, topSortAlt,visits
from util import inputPrinter, matrixPrinter, reader # Utility

print("\nMatkul Planner")
print("Dapat menyusun rencana pengambilan mata kuliah anda")
print("Cr : Mohammad Sheva (13519018)\n")

parse = reader() # Parsing dari text file
print("\nInput anda :")
inputPrinter(parse[0])

adjmat = makeAdj(parse[0],parse[1])
matrixPrinter(adjmat)

listIn = countIn(adjmat)
print(listIn)

order = topSort(adjmat)
print(order)

finList = generateCode(order,parse[1])
print(finList)

#visited = []
#order = []
#while(len(visited) <= len(parse[1])):
 #   adjmat,listIn,visited,order = topSortAlt(adjmat,listIn,visited,order)

#print(order)

order = topSortAlt(adjmat,listIn)
print(order)
finList = generateCode(order,parse[1])
print(finList)


