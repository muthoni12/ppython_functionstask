'''
given a YOB provided by the user,
calculate and return the age of the user.
requirements:
1. use at least one function
2. prompt the user
3. one of your functions should have at least one parameter
'''

def calculateage(yob, cy):
    age = cy - yob

    return age

def userInput():
    cy = int(input("Enter the year it is today"))
    yob = int(input("Enter your yob"))
    age = calculateage(yob, cy)

    print(age)

userInput()


def calculateage(cy, yob):
    age = cy - yob

    return age

print(calculateage(2021, 2002))

print(calculateage(2021, 1995))
