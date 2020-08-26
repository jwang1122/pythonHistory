"""
2020-06-10
Victoria Ou
"""
"""
triangle(n)
   1
  2 2
 3 3 3
4 4 4 4

for i in range(1, 5):
    for j in range(1, 6-i):
        print(end=' ')
    for j in range(1, i+1):
        print(i, end=' ')  
    print()
"""
n=5
for i in range(1, n):
    for j in range(1, n+1-i):
        print(end=' ')
    for j in range(1, i+1):
        print(i, end=' ')  
    print()

print()

"""
upsidedown(n)
   1
  2 2
 3 3 3
4 4 4 4
 3 3 3
  2 2 
   1

for i in range(1, 5):
    for j in range(1, 6-i):
        print(end=' ')
    for j in range(1, i+1):
        print(i, end=' ')  
    print()
for i in range(3, 0, -1):
    for j in range(6-i, 1, -1):
        print(end=' ')
    for j in range(1, i+1):
        print(i, end=' ')  
    print()
"""
n = 5
for i in range(1, n):
    for j in range(1, n+1-i):
        print(end=' ')
    for j in range(1, i+1):
        print(i, end=' ')  
    print()
for i in range(n-2, 0, -1):
    for j in range(n+1-i, 1, -1):
        print(end=' ')
    for j in range(1, i+1):
        print(i, end=' ')  
    print()

print()

"""
diamond(n)
      1 
     2 2 
    3 3 3 
   4 4 4 4 
  5 5 5 5 5 
 6 6 6 6 6 6 
7 7 7 7 7 7 7 
 6 6 6 6 6 6 
  5 5 5 5 5 
   4 4 4 4 
    3 3 3 
     2 2 
      1 

for i in range(1, 8):
    for j in range(1, 9-i):
        print(end=' ')
    for j in range(1, i+1):
        print(i, end=' ')  
    print()
for i in range(6, 0, -1):
    for j in range(9-i, 1, -1):
        print(end=' ')
    for j in range(1, i+1):
        print(i, end=' ')  
    print()
"""
n = 8
for i in range(1, n):
    for j in range(1, n+1-i):
        print(end=' ')
    for j in range(1, i+1):
        print(i, end=' ')  
    print()
for i in range(n-2, 0, -1):
    for j in range(n+1-i, 1, -1):
        print(end=' ')
    for j in range(1, i+1):
        print(i, end=' ')  
    print()