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
        fname = input("Masukkan Nama File (dengan ekstensi, sebagai contoh : tc1.txt) : ")
        try:
            file = open('../test/'+fname,"r")
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

    # List of Unique nodes/codes
    codelist = []

    # Append ke list of unique nodes/codes
    for sublist in isi:
        for code in sublist:
            try:
                codelist.index(code)
            except:
                codelist.append(code)
                
    codelist = sorted(codelist) #sort kode kuliah secara alfanumerik

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

def generateCode(order,codelist):
    '''
    Mencocokan hasil pengurutan dengan kode kuliah pada codelist
    '''
    finList = []
    for sublist in order:
        templist = []
        for num in sublist:
            templist.append(codelist[num])
        finList.append(list(templist))
    return finList


def printSems(finList):
    '''
    Print Output per semester
    '''
    i = 1
    for sublist in finList:
        print("Semester",end=" ")
        print(i,end=" : ")
        for j in range(len(sublist)-1):
            print(sublist[j],end=", ")
        print(sublist[len(sublist)-1])
        i+=1
