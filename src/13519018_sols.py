'''
Nama      : Mohammad Sheva Almeyda Sofjan
NIM/Kelas : 13519018/K01
Deskripsi : Tugas Kecil 2 IF2211 Strategi Algoritma
            Aplikasi penyusunan kuliah 
            menggunakan Topological Sort, 
            penerapan Decrease n Conquer 
Deskripsi File : File Algoritma Penyelesaian
'''

def makeAdj(isi,codelist): 
    '''
    Membuat adjacency matrix
    isi : list yang berisi input pengguna
    codelist : list yang berisi kode mata kuliah, unik
    '''
    adjmat = [[0 for i in range(len(codelist))] for j in range(len(codelist))]
    for sublist in isi:
        for i in range(len(sublist)):
            if(i > 0):
                adjmat[codelist.index(sublist[i])][codelist.index(sublist[0])] = 1;
    return adjmat

def countIn(adjmat): 
    '''
    Mencari derajat masuk tiap node, mereturn list yang berisi derajat masuk tiap node
    adjmat : matriks adjacency
    '''
    listIn = [0 for i in range(len(adjmat))]
    for i in range(len(adjmat)):
        count = 0
        for j in range(len(adjmat[0])):
            if(adjmat[j][i]==1):
                count+=1
        listIn[i] = count
    return listIn

def topSort(adjmat,listIn):
    '''
    Topological Sort untuk menentukan urutan pengambilan mata kuliah, implementasi source-removal algo (ref : Levitin page 141), 
    mereturn list order yaitu list yang berisi urutan pengambilan mata kuliah
    adjmat : matriks adjacency
    listIn : list berisi derajat masuk tiap node
    Decrease and conquer pada algoritma ini terletak pada pengulangan operasi pemilihan dan penghapusan node dengan derajat masuk 0 
    sehingga banyaknya node yang harus diurus semakin berkurang hingga habis (memenuhi ketentuan stop pada while len(zeroIn) > 0) 
    dan order mengandung semua node
    '''
    order = [] # inisialisasi list order dan zeroIn (list yang berisi node yang derajat masuknya = 0)
    zeroIn = []
    for i in range(len(listIn)): # Base case, Memasukkan node dengan derajat masuk 0 ke list zeroIn (dapat dianggap queue juga)
        if(listIn[i] == 0):
            zeroIn.append(i)
    while(len(zeroIn)>0): # Loop akan berjalan selama masih ada list dengan derajat masuk 0
        order.append(list(zeroIn)) # Memasukkan list zeroIn kedalam list order sehingga zeroIn merupakan sublist dari list order
        for num in range(len(zeroIn)): # Iterasi pada list zeroIn, sehingga dapat menghasilkan lebih dari satu mata kuliah pada satu semester 
            currnode = zeroIn[0] # Ambil elemen pertama zeroIn
            nextnodes = getNextNodes(currnode,adjmat) # Node-node berikutnya dari currnode
            for node in nextnodes: # Iterasi pada node-node berikutnya (akan disebut node) dari currnode 
                adjmat[currnode][node] = 0 # Mengeliminasi/menghapus edge dari currnode ke node
                listIn[node] -= 1  # Mengurangi derajat masuk node akibat perubahan pada perintah sebelumnya
                if(listIn[node] == 0): # Jika node sudah tidak memiliki derajat masuk akibat eliminasi
                    zeroIn.append(node) # Masukkan ke list zeroIn
            zeroIn.pop(0) # Hapus elemen pertama zeroIn (elemen pertama sudah selesai diproses)

    if(sum(listIn) > 0): # Input bukan DAG berarti masih ada edge yang tidak tereliminasi
        print("\nGraf input bukan merupakan DAG (Directed Acyclic Graph), sehingga tidak dapat dicari urutan pengambilan mata kuliahnya.")
        return []
    else:
        return order # return urutan pengambilan


def getNextNodes(currnode,adjmat):
    '''
    Untuk mendapatkan node-node tetangga di mana terdapat busur dari currnode ke node tetangga tersebut , mereturn list yang berisi informasi tersebut
    currnode : node yang akan dicari tetangganya
    adjmat : adjacency matrix
    '''
    nextnodes = []
    for i in range(len(adjmat)):
        if(adjmat[currnode][i]==1):
            nextnodes.append(i)
    return nextnodes





        