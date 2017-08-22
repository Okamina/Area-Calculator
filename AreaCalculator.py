'''
Program can calculate area of: 
circle, triangle, square, rectangle, trapezoid/trapezium, elipse, parallelogram and kite
'''

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print ("Area Calculator started")
print ("%s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute))

sleep(1)

hint = ("Don't forget to include the correct units! \nHave nice day!")

option = str(input("Enter: \nC for Circle \nT for Triangle \nS for Square \nR for Rectangle \nTR for Trapezoid/Trapezium \nE for Elipse \nP for Parallelogram \nK for Kite \n"))
print ("\n")
option = option.upper()
if option == 'C':
    radius = float(input("Enter radius: "))
    print("\n")
    area = pi * radius**2
    print ("The pie is baking...")
    print("\n")
    sleep (1)
    print ("Area %.2f. \n%s" % (area, hint))

elif option == 'T':
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print("\n")
    area = 0.5 * base * height
    print ("Uni Bi Tri...")
    print("\n")
    sleep (1)
    print ("Area %.2f. \n%s" % (area, hint))
  
elif option == 'S':
    side = float(input("Enter the length of side:"))
    print("\n")
    area = side**2
    print ("Picnic in the square...")
    print("\n")
    sleep (1)
    print ("Area %.2f. \n%s" % (area, hint))
    
elif option == 'R':
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    print("\n")
    area = width * height
    print ("The movie rec the movie...")
    print("\n")
    sleep (1)
    print ("Area %.2f. \n%s" % (area, hint))
    
elif option == 'TR':
    bottom = float(input("Enter the bottom base of the trapezoid: "))
    top = float(input("Enter the top base of the trapezoid: "))
    height = float(input("Enter the height of the trapezoid: "))
    print("\n")
    area = (bottom + top) * 0.5 * height
    print ("Fun on the trapeze...")
    print("\n")
    sleep (1)
    print ("Area %.2f. \n%s" % (area, hint))
    
elif option == 'E':
    radiusA = float(input("Enter the short radius of the elipse: "))
    radiusB = float(input("Enter the long radius of the elipse: "))
    print("\n")
    area = pi * radiusA * 0.5 * radiusB * 0.5 
    print ("The earth is circling the ellipse...")
    print("\n")
    sleep (1)
    print ("Area %.2f. \n%s" % (area, hint))
    
elif option == 'P':
    base = float(input("Enter the base of the parallelogram: "))
    height = float(input("Enter the height of the parallelogram: "))
    print("\n")
    area = base * height
    print ("Run on the parallel...")
    print("\n")
    sleep (1)
    print ("Area %.2f. \n%s" % (area, hint))
    
elif option == 'K':
    diagonalA = float(input("Enter the first diagonal of the kite: "))
    diagonalB = float(input("Enter the second diagonal of the kite: "))
    print("\n")
    area = diagonalA * diagonalB * 0.5
    print ("Colorful kites in the sky...")
    print("\n")
    sleep (1)
    print ("Area %.2f. \n%s" % (area, hint))
    
else:
	  print ("Wrong enter. Program will shut down now. Bye")