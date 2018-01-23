import sys
import turtle
wn = turtle.Screen()
s = turtle.Turtle()

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
def test_suite():
    test(sum_even(mylist) == -16)
    test(sam(mylist2) == 5)
    
mylist = [12, 8, 13, 4, 83, -72, 17]
mylist2 = ["fneo", "cneif","ncoe","ncis" "cmoejsw","wrrf"]

def count_odd(numlist):
    count=0
    for n in numlist:
        if n % 2 !=0:
            count += 1
    return count


def sum_even(numlist):
    sum=0
    for n in numlist:
        if n % 2 == 0:
            sum = sum + n
    return sum

def sum_neg(numlist):
    sum = 0
    for n in numlist:
        if n < 0:
            sum = sum+ n
    return sum

def count_words(numlist):
    count = 0
    for n in numlist:
        if len(n) ==5:
            count += 1
    return count

def sum_even_nofirst(numlist):
    sum = 0
    for n in numlist:
        if n % 2 == 0:
            break
        else:
            sum += n
    return sum

def sam(numlist):
    count = 0
    for i in numlist:
        if i == "sam":
            count += 1
            break
        else:
            count += 1
    return count

def sqrt(n):
    """Ex 7:Newtons square root function -"""
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        print("better",better)
        if abs(approx - better) < 0.001:
            return better
        approx = better


print("sqrt",sqrt(36.0))

def is_prime(n):
    """Write a function, is_prime, which takes a single integer
    argument and returns True when the argument is a prime number and False otherwise"""
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

        
"""Revisit the drunk pirate problem from the exercises in chapter 3. This time,
the drunk pirate makes a turn, and then takes some steps forward, and repeats this.
Our social science student now records pairs of data: the angle of each turn, and the
number of steps taken after the turn. Her experimental data is [(160, 20), (-43, 10),
(270, 8), (-43, 12)]. Use a turtle to draw the path taken by our drunk friend.
"""

import turtle
wn = turtle.Screen()
fun = turtle.Turtle()

steps = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

for (angle, moves) in steps:
    fun.right(angle)
    fun.forward(moves)
 
    
"""Many interesting shapes can be drawn by the turtle by giving a list of pairs like we did
above, where the first item of the pair is the
angle to turn, and the second item is the distance to move forward. Set up a list of pairs
so that the turtle draws a house with a cross through the centre, as show here. This should
be done without going over any of the lines / edges more than once, and without lifting your
pen."""

import turtle
wn = turtle.Screen()
fun = turtle.Turtle()
fun.pensize(10)
house = [(270,50), (30, 50), (120,50), (120,50), (225,70.1), (225,50), (225,70.1), (225,50) ]

for (angle,moves) in house:
    fun.right(angle)
    fun.forward(moves)
#thx Hunter https://github.com/ForestMilles/homework/blob/master/Chapter7.py from Hunter. 


print(count_odd(mylist))
print(sum_even(mylist))
print(sum_neg(mylist))
print(count_words(mylist2))
print(sum_even_nofirst(mylist))
test_suite()
