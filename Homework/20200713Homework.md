# 2020-07-13 Python level 1 Homework

* Based on the following right-angle triangle 
```py
"""
print a rightangle
1 
2 2 
3 3 3 
4 4 4 4 
"""
def forloop():
    for i in range(1, 5):
        for j in range(i):
            print(i, end=' ')
        print()

forloop()
```

modify the code, make it has the following output:
```
    1 
   2 2 
  3 3 3 
 4 4 4 4 
```