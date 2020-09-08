# Sarah Xiao
# CS-UY 1114
# 22 Feb 2019
# Homework 2

##Problem 1
##
##Program 1
##10
##60
##37
##
##Program 2
##
##A1
##B1
##C
##B2
##A2
##
##Program 3
##Ok!Ok!

##Problem 2

def print_top (offset) :
    print (offset * ' ' + '^')
def print_middle (offset , width) :
    print (offset * ' ' + '/' + width * ' ' + '\\')
def print_bottom (offset , width):
    print (offset * ' ' + width * '-')

def print_triangle ():
    print_top (3)
    print_middle ( 2, 1)
    print_middle ( 1, 3)
    print_middle ( 0, 5)
    print_bottom ( 0, 7)
    
print_triangle()

##Problem 3

def double (n) :
 signature: int -> int
    # return doubled value of parameter
    return n * 2

def succ (n) :
    # signature: int -> int
    # returns successor of parameter
    return n + 1

def f (n) :
    # signature: int -> int
    # returns the value 2*n + 1
    w = double (n)
    y = succ (w)
    return y
def g (n) :
    # signature: int -> int
    # returns the value 4*n
    x = double (n)
    z = double (x)
    return z
def h (n) :
    # signature: int -> int
    # returns the value 8*n + 4
    p= f(n)
    q= g(p)
    return q

##print(f(5))
##print(g(9))
##print(h(7))

##Problem 4

import math
def hypotenuse(a, b):
    x= math.sqrt (a ** 2 + b ** 2)
    return x
 
print(hypotenuse(6, 8))

##Problem 5

def distance (x1 , y1 , x2 , y2) :
    c = x1 - x2
    d = y1 - y2
    h = hypotenuse(c, d)
    return h
print (distance(27, 6, 2, 1))

##Problem 6 
def interactive_distance():
    x1= float(input("What is the x-coordinate of the first point?"))
    y1= float(input("What is the y-coordinate of the first point?"))
    x2= float(input("What is the x-coordinate of the second point?"))
    y2= float(input("What is the y-coordinate of the second point?"))
    z= distance (x1 , y1 , x2 , y2)
    print("The distance between (" + str(x1) + " , "+ str(y1) + ") and (" + str(x2) + " , " + str(y2) + ") is " + str(z) + ".")
interactive_distance()

