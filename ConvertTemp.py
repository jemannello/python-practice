''' ConvertTemp.py
        Reference for this assignment is from John Zelle's Python textbook.
        Jenny Mannello
        This program converts the given Celcius temperature to Fahrenheit."
'''

def main():
	Celcius = eval(input("What is the current Celcius temperature? "))
	Fahrenheit = 9/5 * Celcius +32
	print("The temperature is", Fahrenheit, "degrees Fahrenheit.")
main()
