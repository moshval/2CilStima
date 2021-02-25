'''
Nama      : Mohammad Sheva Almeyda Sofjan
NIM/Kelas : 13519018/K01
Deskripsi : Tugas Kecil 2 IF2211 Strategi Algoritma
            Aplikasi penyusunan kuliah 
            menggunakan Topological Sort, 
            penerapan Decrease n Conquer 
Deskripsi File : File Utama (Driver)
'''

from sols import countIn, makeAdj
from util import reader # Utility

print("\nMatkul Planner")
print("Dapat menyusun rencana pengambilan mata kuliah anda")
print("Cr : Mohammad Sheva (13519018)\n")

parse = reader() # Parsing dari text file
print("\nInput anda :\n")
print(parse[0])

adjmat = makeAdj(parse[0],parse[1])
for i in range(len(parse[1])):
    for j in range(len(parse[1])):
        print(adjmat[i][j],end=" ")
    print()

listIn = countIn(parse[0],parse[1])
print(listIn)