n=5
i=1
while i<=5:
    j=1
    while j<=5:
        if j<i:
            print(i, end=" ")
        else:
            print(j,end=" ")
        j=j+1
    print()
    i=i+1