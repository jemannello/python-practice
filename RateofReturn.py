'''     RateofReturn.py
        Jenny Mannello
        Sources include: Program Assignment 1 requirement.
        This program calculates cash flow values at incremented dates from the original amount.
'''

def main():
        principal = eval(input("The amount to invest each year is: "))
        rateOfReturn = eval(input("The interest rate is: "))
        years = eval(input("The number of years for investment is: "))
        for years in range(5):        
                principal = principal * (1 + rateOfReturn)
        print("The amount in 5 years is:", principal)
main()
