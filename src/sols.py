'''
Nama      : Mohammad Sheva Almeyda Sofjan
NIM/Kelas : 13519018/K01
Deskripsi : Tugas Kecil 2 IF2211 Strategi Algoritma
            Aplikasi penyusunan kuliah 
            menggunakan Topological Sort, 
            penerapan Decrease n Conquer 
Deskripsi File : File Algoritma Penyelesaian (Driver)
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
    '''
    order = [] # inisialisasi list order dan zeroIn (list yang berisi node yang derajat masuknya = 0)
    zeroIn = []
    for i in range(len(listIn)): # Memasukkan node dengan derajat masuk 0 ke list zeroIn 
        if(listIn[i] == 0):
            zeroIn.append(i)
    while(len(zeroIn)>0): # Loop akan berjalan selama masih ada list dengan derajat masuk 0
        order.append(list(zeroIn))
        for num in range(len(zeroIn)):
            currnode = zeroIn[0]
            nextnodes = getNextNodes(currnode,adjmat)
            for node in nextnodes:
                adjmat[currnode][node] = 0
                listIn = countIn(adjmat)
                if(listIn[node] == 0):
                    zeroIn.append(node)
            zeroIn.pop(0)

    if(sum(listIn) > 0):
        print("\nGraf input bukan merupakan DAG (Directed Acyclic Graph), sehingga tidak dapat dicari urutan pengambilan mata kuliahnya.")
        return []
    else:
        return order


def getNextNodes(currnode,adjmat):
    '''
    Untuk mendapatkan node-node tetangga di mana terdapat busur dari currnode ke node tetangga tersebut , mereturn list yang berisi informasi tersebut
    '''
    nextnodes = []
    for i in range(len(adjmat)):
        if(adjmat[currnode][i]==1):
            nextnodes.append(i)
    return nextnodes


# Algoritma Alternatif

def topSortAlt(adjmat):
    '''
    Topological Sort untuk mendapatkan urutan pengambilan kuliah
    '''
    visited = [0 for k in range(len(adjmat))]
    order = [0 for k in range(len(adjmat))]
    i = len(adjmat) - 1

    for at in range(len(adjmat)):
        if(visited[at]==0):
            visitedNodes = []
            visits(at,visited,visitedNodes,adjmat)
            for node in visitedNodes:
                order[i] = node
                i-=1
    return order

def visits(at,visited,visitedNodes,adjmat):
    '''
    Mengunjungi node yang belum dikunjungi, skema dfs (depth first search)
    '''
    visited[at] = 1
    nextnodes = []
    for i in range(len(adjmat)):
        if(adjmat[at][i]==1):
            nextnodes.append(i)
    for node in nextnodes:
        if(visited[node] == 0):
            visits(node,visited,visitedNodes,adjmat)

    visitedNodes.append(at)




        