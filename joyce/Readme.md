# 2020-6-2 Homework 1
- Joyce
## *Install Python
>Google Search:python download

>Search Result:Download Python | Python.org

[Python Website] [https://www.python.org/downloads/]


```py
print("helloworld")
```

cd: change directory
```sh
cd workspace
cd python
python hello.py
```
creating an env file.
First,type in (python -- version).
 Secondly, type in (python -m venv env).
 Thirdly, (FOR APPLE ONLY) type in (source env/bin/activate).

```How to get the help(print)

     print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
...skipping...
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

# Homework 06/04/20

## Creating the red circle with arrow
 ```
 
 from turtle import *
 t1 = Turtle()
 t1.dot(20,'red')
 mainloop()
 ```

## Creating a circle Without circle
```
from turtle import *

t1 = Turtle()
t1.dot(20,'red')
t1.hideturtle()
mainloop()
```
### Creating a black circle at diffent areas.

 ```
 from turtle import *

t1 = Turtle(visible=False)

def draw():
    t1.pu()
    tracer(False)
    t1.setpos(0, -180)
    t1.dot(20)

draw()
mainloop()   
 ```
# Homework 6-10-2020
## Circle.py
 ```
from math import pi

def circle_area(r):
    return r*r*pi

if __name__ == '__main__':
    a =circle_area(4)
    print(a)
```
len - tells you how many total elements in a container, in builtins module
```
len(obj, /)
```
