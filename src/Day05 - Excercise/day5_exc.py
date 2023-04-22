"""
Day 5 of python learning (Excercise)
--------------------------
Author:     Akshay
Date:       22/04/2023
--------------------------
"""

# temperature converter: 

f = float(input('temp in Fahrenheit: '))
c = (f - 32) / 1.8
print('%.1f Fahrenheit = %.1f Celsius' % (f, c))