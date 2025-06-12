# WRITE YOUR CODE HERE
## Function to greet a person

#Write a function named `greet` that takes one argument, say `name`, and **returns** a greeting string. For example, `greet("Thomas")` should **return** the string:

#Hello Thomas. How are you?
def personalized_greeting(name):
     print(f"Hello {name}. How are you?")

# personalized_greeting("Thomas")

## Greet a few friends

#Create a simple list (not a dictionary) with the names of some friends. For example:
my_friends = ["Frodo", "Sam", "Gandalf"]

#Then write a function that takes the list of friends and **prints** a greeting for every one of them using function `greet(name)` from earlier.
def personalized_greeting(names):
     for name in names:
        print(f"Hello {name}. How are you?")

personalized_greeting(my_friends)

## Solve an equation
import math

def solve_quadratic(a, b, c):
    discriminant = b*b - 4*a*c

    if discriminant < 0:
        print("no real solutions")
    else:
        x1 = (-b - math.sqrt(discriminant)) / (2 * a)
        x2 = (-b + math.sqrt(discriminant)) / (2 * a)
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")

solve_quadratic(15,20,6)

# Reflection
# Throughout this assignment, I was able to do most of the questions, the first and second question was fairly easy due to their simple nature, and also due to the demo and notes from the first and second week of class.
# The third question however posed quite a challange, due to its more complex nature, for this question, I initially had difficulties, as I had to apply different techniques, and knowledge across several lectures, not only that but after trying and failing multiple times, I ended up having to consult my friend who was an expert in coding, and as it tuns out, I was simply missing a defenition code right at the end, an so with that I was able to finish this assignment.
# Overall, this assignment was fairly easy aside from the last question, and after checking with the solutions everything was in order, I would award myself with an 85% for this assignment, this grade is due to the help I received from my friend for the third question. 