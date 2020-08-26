"""
make this
    1 
   2 2
  3 3 3
 4 4 4 4 
"""
for i in range(1, 5):
    for k in range(5,i,-1):
        print(" ", end='')
    for j in range(i):
        print(i, end=' ')
    print()