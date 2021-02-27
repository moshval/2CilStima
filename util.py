'''
Nama      : Mohammad Sheva Almeyda Sofjan
NIM/Kelas : 13519018/K01
Deskripsi : Tugas Kecil 2 IF2211 Strategi Algoritma
            Aplikasi penyusunan kuliah 
            menggunakan Topological Sort, 
            penerapan Decrease n Conquer 
Deskripsi File : File Utility
'''

def reader(): 
    '''
    Reader file text, mereturn list isi(list berisi kode kuliah dan kode kuliah prereq) dan list codelist(list yang berisi kode kuliah unik)
    '''
    notfound = True
    while notfound :
        #fname = input("Masukkan Nama File (dengan ekstensi, sebagai contoh : tc1.txt) : ")
        try:
            file = open("tc2.txt","r")
            notfound = False
        except:
             print("File tidak ditemukan. Ulangi lagi")

    isi = file.readlines() # Membaca isi file
    file.close()
    # Mengubah ke array, menghapus karakter tak guna
    for i in range(len(isi)):
        isi[i] = isi[i].replace("\n","")
        isi[i] = isi[i].replace(" ","")
        isi[i] = isi[i].replace(".","")
        isi[i] = isi[i].split(",")

    # List of Unique nodes
    codelist = []

    # Append ke list of unique nodes
    for sublist in isi:
        for code in sublist:
            try:
                codelist.index(code)
            except:
                codelist.append(code)
                
    codelist = sorted(codelist) #sort kode kuliah

    return isi,codelist

def inputPrinter(isi): 
    '''
    Mencetak input(dari file teks) yang sudah dikonversi kedalam list isi ke layar dalam format semula
    '''
    for sublist in isi:
        for i in range(len(sublist)):
            if(i < len(sublist)-1):
                print(sublist[i],end="")
                print(",",end="")
            else:
                print(sublist[i],end="")
                print(".")
            
    
def matrixPrinter(mat):
    '''
    Mencetak Matrix
    '''
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j],end=" ")
        print()