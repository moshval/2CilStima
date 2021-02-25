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
    Reader file text, mereturn 
    '''
    notfound = True
    while notfound :
        #fname = input("Masukkan Nama File (dengan ekstensi, sebagai contoh : tc1.txt) : ")
        try:
            file = open("tc1.txt","r")
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
                
    codelist = sorted(codelist)

    print(isi)
    print(codelist)
    return isi,codelist
    
