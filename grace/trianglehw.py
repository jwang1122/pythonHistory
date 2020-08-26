"""
GRACE YANG TRIANGLE HW COMPLETED 
"""


def triangle(n):
    for i in range(1, n):
        for j in range(i):
            print(i, end=' ')
        print()


def equalateralTriangle(n):
    for i in range(1, n):
        for k in range(n-1, i, -1):
            print(' ', end='')
        for j in range(i):
            print(i, end=' ')
        print()


def upsidedownTriangle(n):
    for i in range(n-2, 0, -1):
        for k in range(i, n-2):
            print(' ', end='')
        for j in range(i):
            print('', i, end='')
        print()


def diamond(n):
    equalateralTriangle(n)
    upsidedownTriangle(n)

if __name__ == '__main__':
    triangle(7)
    print()

    equalateralTriangle(8)
    print()

    diamond(8)

