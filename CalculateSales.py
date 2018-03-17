''' Programming Fundamentals 140
    CalculateSales.py
    Jenny Mannello
    This program displays sales to view, edit, and display sales, display the
    sum of the yearly average, as well as the monthly average between all 12 months.
    Sources for borrowed code include the text file from class, an in-class
    solution, and some parts from the Python Programming textbook.
'''

def main():
  print("Please enter sales for each month.")
  jan = eval(input("January: "))
  feb = eval(input("February: "))
  mar = eval(input("March: "))
  apr = eval(input("April: "))
  may = eval(input("May: "))
  jun = eval(input("June: "))
  jul = eval(input("July: "))
  aug = eval(input("August: "))
  sep = eval(input("September: "))
  oct = eval(input("October: "))
  nov = eval(input("November: "))
  dec = eval(input("December: "))
  total = jan + feb + mar + apr + may + jun + jul + aug + sep + oct + nov + dec
  print()
main()

'''
print(" Please type 'view' to see the monthly sales.")
#Display monthly sales.
view = [14317, 4176, 1073, 3463, 2429, 4324, 9762, 15578, 2437, 6735, 88, 2497]
'''

sum = 0
avg = 0
total = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]

for x in total:
  #Find the yearly total (sum of all numbers)
  sum = sum + x
  size = len(total)
  
  # Find the monthly average (add and divide by # of variables)
  avg = sum / size
  
  # Sort the list
  totals.sort()

#Print out results  
print('My Sales: ',total)
print('Yearly Sales Total: ', sum)
print('Monthly Average:', avg)
