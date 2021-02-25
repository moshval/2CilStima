'''
Nama      : Mohammad Sheva Almeyda Sofjan
NIM/Kelas : 13519018/K01
Deskripsi : Tugas Kecil 2 IF2211 Strategi Algoritma
            Aplikasi penyusunan kuliah 
            menggunakan Topological Sort, 
            penerapan Decrease n Conquer 
Deskripsi File : File Algoritma Penyelesaian (Driver)
'''

def makeAdj(isi,codelist): #Membuat adjacency matrix
    adjmat = [[0 for i in range(len(codelist))] for j in range(len(codelist))]
    for sublist in isi:
        for i in range(len(sublist)):
            if(i > 0):
                adjmat[codelist.index(sublist[i])][codelist.index(sublist[0])] = 1;
    return adjmat

def countIn(isi,codelist): #Mencari derajat masuk tiap node
    listIn = [0 for i in range(len(codelist))]
    for sublist in isi:
        listIn[codelist.index(sublist[0])] = len(sublist) - 1;
    return listIn    


