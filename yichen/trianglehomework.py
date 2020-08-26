"""
print a rightangle
   1 
  2 2 
 3 3 3 
4 4 4 4 
"""
def forloop():
    for i in range(1, 5,):
        for j in range(4-i):
            print("",end=" ")

        for k in range(i):
            print(i, end=' ')
        print()

forloop()