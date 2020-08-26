"""
print a rightangle
1 
2 2 
3 3 3 
4 4 4 4 
"""
a=1
b=5
for i in range(1, 5):
    for j in range(i):
        print(i,end=' ')
    print()

'''
number pyramid
'''

for i in range(a, b):
    for x in range(b-i-1):
        print(' ', end=' ')
    for j in range(i):
        print(i, end='   ')
    print()
