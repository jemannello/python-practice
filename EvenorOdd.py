''' EvenorOdd.py
    Programming Assignment 4
    Jenny Mannello
    This program will determine whether a number given by the
    user is odd or even.
'''

def main():
    #This prompts the user for input:
    x = int(input("Enter an integer: "))
    #This is a conditional statement that needs to be met:
    if x%2 == 0:
        print('The number is even.')
    #This is the alternative if the condition is not met:   
    else:
        print('The number is odd.')
main() 
