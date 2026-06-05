"""
1
1   2
1   2   3
1   2   3   4
1   2   3   4   5
1   2   3   4   5   6

"""

for row in range(1,7):

    for col in range(1,row+1):

        print(col,end=" ")
    print()


"""
1   2   3   4   5   =>(5col)5
1   2   3   4       =>(4col) 4  
1   2   3           =>(3col)  3     
1   2               =>(2col)   2      
1                   =>(1col)    1        

"""

for row in range(5,0,-1):#row=5

    for col in range(1,row+1):#col in range(1,)

        print(col,end="\t")
    print()


"""

"""