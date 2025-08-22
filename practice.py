n=5
space=(2*(n-1))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j," "*(n+1-(2*i)),end="")
    for j in range(i):
        print(" "*(space),end=" ")
        space-=2
    for k in range(i,0,-1):
        print(k,end=" ")
        #print(j,end="")
    print()