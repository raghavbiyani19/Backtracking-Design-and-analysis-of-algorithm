"""
x[]--------> Solution list.
matrix[] --> connection matrix of my Graph
k----------> Vertex to be coloured
m----------> number of colours used.
n----------> number of nodes in my graph
"""
import networkx
import matplotlib.pyplot as plt
sol=[]

def nextValue(k,m,n,matrix,x):    
    while(True):
        x[k]=(x[k]+1)%(m+1)
        if(x[k]==0):
            return
        for j in range(n):
            if( (matrix[k][j] != 0) and (x[k]==x[j]) ):
                break
        if(j==n-1):
            return

def mColor(k,m,n,matrix,x):
    while(True):
        nextValue(k,m,n,matrix,x)
        if(x[k]==0):
            return
        if(k==n-1):
            if x not in sol:
                sol.append(x)
            for solutions in sol:    
                print("Solution:",solutions)
        else:
            mColor(k+1,m,n,matrix,x)

def main():
    matrix=[]
    x=[]
    n = int(input("ENTER THE NUMBER OF NODES\n"))
    print("Enter the connectivity details of nodes: (1->if connected else->0)")

    for i in range(n):
        a = list(map(int,input().split(" ")))[:n] 
        matrix.append(a)
    
    print("Your connection matrix is:\n")
    for i in range(n):
        for j in range(n): 
            print(matrix[i][j], end = " ") 
        print()
    
    G = networkx.Graph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==1:
                G.add_edge(i,j)
    networkx.draw(G,with_labels=1)
    plt.show()
    
    for i in range(n):
        x.append(0)
    
    counts=[]
    
    for lists in matrix:
        count=0
        for i in range(n):
            if lists[i]==1:
                count = count + 1
        counts.append(count)
    counts.sort()
    
    print("\nCHOOSE: 1. All Solutions requiring minimum colours\n        2.All solutions with number of colours as your choice")
    
    option=int(input())
    
    if(option==2):
        m = int(input("ENTER THE NUMBER OF COLORS"))
        mColor(0,m,n,matrix,x) 
    elif(option==1):
        mColor(0,counts[n-1],n,matrix,x) 
    else:
        print("INVALID INPUT Try again!!\n")

main()