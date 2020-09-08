"""
Sarah Xiao
CS-UY 1114
2 May 2019
Homework 9

"""

import math
import turtle

class Point:
    def __init__(self, x, y):
        # sig: Point, float, float -> NoneType
        # Construct a new Point from coordinates
        self.x = x
        self.y = y
    def move(self, horiz, vert):
        # sig: Point, float, float -> NoneType
        # Move the point by some amount in both axes
        self.x += horiz
        self.y += vert
    def draw(self):
        # sig: Point -> NoneType
        # Use turtle to draw the point as a dot on the screen
        turtle.up()
        turtle.goto(self.x, self.y)
        turtle.down()
        turtle.dot(5)
    def distance(self, other):
        # sig: Point, Point -> float
        # Calculate the distance between the point and
        # another point
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

class Rectangle:
    def __init__(self, upperleft, lowerright):
        # sig: Rectangle, Point, Point -> NoneType
        # Construct a new Rectangle from two points
        self.upperleft = upperleft
        self.lowerright = lowerright
    def diagonal_length(self):
        # sig: Rectangle -> float
        # Return the distance between the upper left point
        # and the lower right point
        return Point.distance(self.upperleft,self.lowerright)
    def draw(self):
        # sig: Rectangle -> NoneType
        # Use turtle to draw the rectangle on the screen
        turtle.penup()
        turtle.goto(self.upperleft.x, self.upperleft.y)
        turtle.pendown()
        turtle.goto(self.lowerright.x, self.upperleft.y)
        turtle.goto(self.lowerright.x, self.lowerright.y)
        turtle.goto(self.upperleft.x, self.lowerright.y)
        turtle.goto(self.upperleft.x, self.upperleft.y)
    def width(self):
        # sig: Rectangle -> float
        # Return the (positive) width of the rectangle
        return self.lowerright.x - self.upperleft.x
    def height(self):
        # sig: Rectangle -> float
        # Return the (positive) height of the rectangle
        return abs(self.lowerright.y - self.upperleft.y)
    def area(self):
        # sig: Rectangle -> float
        # Return the area of the rectangle
        return self.width()*self.height()
    def move(self, horiz, vert):
        # sig: Rectangle, float, float -> NoneType
        # Move the rectangle in both axes
        Point.move(self.upperleft, horiz, vert)
        Point.move(self.lowerright, horiz, vert)
        
        
    def overlaps(self, other):
##        # sig: Rectangle, Rectangle -> bool
##        # Determine if the two rectangles overlap
##        sleft = self.upperleft.x
##        sright = self.upperleft.x + self.width()
##        stop = self.upperleft.y
##        sbot = self.upperleft.y - self.height()
##
##        oleft = other.upperleft.x
##        oright = other.upperleft.x + other.width()
##        otop = other.upperleft.y
##        obot = other.upperleft.y - other.height()
##
##        #left-right 
##        if ((sleft > oleft and sleft < oright) or (sright < oright and sright > oleft)):
##              #up-down
##            if ((stop > otop and stop < obot) or (sbot < obot and sbot > otop) or (stop > otop and sbot < obot) or (stop < otop and sbot > obot)):
##                return True
##
##        
##        return False

        if other.upperleft.x>self.lowerright.x:
            return False
        elif other.lowerright.x<self.upperleft.x:
            return False
        elif other.lowerright.y>self.upperleft.y:
            return False
        elif other.upperleft.y<self.lowerright.y:
            return False
        else:
            return True

    def intersection(self, other):
        # sig: Rectangle, Rectangle -> Rectangle:
        # If the two rectangles overlap, return a rectangle
        # that identifies their intersection (i.e. a rectangle
        # containing all the area contained in both of them).
        # If the rectangles don't intersect (i.e.. there is not
        # overlap), return an "empty" rectangle identified by
        # points 0,0 and 0,0.
        if not self.overlaps(other):
            return Rectangle(Point(0.0, 0.0), Point(0.0, 0.0))
        else:
            point1 = Point(max(other.upperleft.x,self.upperleft.x),min(other.upperleft.y,self.upperleft.y))
            point2 = Point(min(other.lowerright.x,self.lowerright.x),max(other.lowerright.y,self.lowerright.y))
            return Rectangle(point1,point2)

class Line:
    def __init__(self , first , second):
        self.first = first
        self.second = second
    def draw(self):
        turtle.penup()
        turtle.goto(self.first.x , self.first.y)
        turtle.pendown()
        turtle.goto(self.second.x , self.second.y)
    def slope(self):
        m = (self.second.y-self.first.y)/(self.second.x-self.first.x)
        if str(round(m)).isdigit() == True:
            return m
        else:
            return "ValueError"

def line_slope_test():
    l1 = Line(Point(1.0, 1.0),Point(3.0, 3.0))
    l2 = Line(Point(1.0, 1.0),Point(-3.0, 3.0))
    print("l1 has slope " + str(l1.slope()))
    print("l2 has slope " + str(l2.slope()))
    
line_slope_test()

def point_move_test():
    turtle.hideturtle()
    p1 = Point(50.0, 40.0)
    turtle.color("black")
    for _ in range(20):
        p1.draw()
        p1.move(5.0, 5.0)

def rectangle_area_test():
    r1 = Rectangle(Point(50.0, 260.0), Point(160.0, 150.0))
    print("r1 has width " + str(r1.width()))
    print("r1 has height " + str(r1.height()))
    print("r1 has area " + str(r1.area()))
    print("r1 has diagonal length: " + str(r1.diagonal_length()))

rectangle_area_test()

def rectangle_move_test():
    turtle.hideturtle()
    r1 = Rectangle(Point(50.0, 260.0), Point(160.0, 150.0))
    for i in range(20):
        turtle.color(["black", "green", "red"][i % 3])
        r1.draw()
        r1.move(5.0, 5.0)

rectangle_move_test()

def rectangle_draw_test():
    turtle.hideturtle()
    r1 = Rectangle(Point(10.0, 300.0),Point(90.0, 100.0))
    r2 = Rectangle(Point(70.0, 180.0), Point(200.0, 150.0))
    turtle.color("black")
    r1.draw()
    r2.draw()

def overlap_test():
    r1 = Rectangle(Point(10.0, 300.0),Point(90.0, 100.0))
    r2 = Rectangle(Point(70.0, 180.0), Point(200.0, 150.0))
    print("r1 width: " + str(r1.width()) + " r1 height: " + str(r1.height()));
    print("r2 width: " + str(r2.width()) + " r2 height: " + str(r2.height()));
    print("r1 and r2 overlap? " + str(r1.overlaps(r2)))    

    r3 = Rectangle(Point(10.0, 300.0),Point(90.0, 100.0))
    r4 = Rectangle(Point(100.0, 180.0), Point(200.0, 150.0))
    print("r3 and r4 overlap? " + str(r3.overlaps(r4)))

overlap_test()

def intersection_test():
    turtle.hideturtle()
    r1 = Rectangle(Point(10.0, 300.0),Point(90.0, 100.0))
    r2 = Rectangle(Point(70.0, 180.0), Point(200.0, 150.0))
    turtle.color("black")
    r1.draw()
    r2.draw()
    turtle.color("red")
    theintersection = r1.intersection(r2)
    theintersection.draw()
    print("Area of interesection: " + str(theintersection.area()))
intersection_test()
