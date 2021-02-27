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
    '''
    adjmat = [[0 for i in range(len(codelist))] for j in range(len(codelist))]
    for sublist in isi:
        for i in range(len(sublist)):
            if(i > 0):
                adjmat[codelist.index(sublist[i])][codelist.index(sublist[0])] = 1;
    return adjmat

def countIn(isi,codelist): 
    '''
    Mencari derajat masuk tiap node
    '''
    listIn = [0 for i in range(len(codelist))]
    for sublist in isi:
        listIn[codelist.index(sublist[0])] = len(sublist) - 1;
    return listIn    


def topSort(adjmat):
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

def generateCode(order,codelist):
    '''
    Mencocokan hasil pengurutan dengan kode kuliah pada codelist
    '''
    finList = []
    for num in order:
        finList.append(codelist[num])
    return finList


#def topSort(adjmat,listIn,visited):
    #while(len(visited) < len(listIn)):
        #for i in range(len(listIn)):
            #if(listIn[i] == 0 and (i not in visited)):
                #visited.append(i)
                #selected = i
                #break
