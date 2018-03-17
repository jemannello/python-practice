''' NestedConditionals.py
    Programming Assignment 4
    Jenny Mannello
    This program determines eligibility for a U.S. Senator and a U.S. Representative
    based on the user's input of age and years of U.S. citizenship.
'''

def main():
    #This prompts the user for two inputs:
    x = int(input("Enter your age: "))
    y = int(input("Enter the number of years you've been a U.S. Citizen: "))
    #These are nested conditionals with multiple execution options:
    if x >= 30 and y >= 9:
        print('You can run for U.S. Senate!')
    if x >= 27 and y >= 7:
        print('You can run for U.S. Representative!')
    else:
        print('You are not eligible yet.')
main() 
