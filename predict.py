#!/usr/bin/python3
import os.path
import sys

def main():
    mileage = input("Please enter a mileage: ")
    try:
        mileage = int(mileage)
    except ValueError:
        print("That's not a number!")
        sys.exit()
    if mileage < 0 :
        print("Be realistic, mileage cannot be a negative value !")
        sys.exit()
    if mileage > 3039122 :
        print("You should check for a smaller mileage, no car in the world has been on the road that much !")
        sys.exit()
    if os.path.exists('values.txt'):
        with open('values.txt') as f:
            theta0 = f.readline()
            theta1 = f.readline()
    else:
        theta0 = 0
        theta1 = 0
    estimatedPrice = theta0 + (theta1 * mileage)
    print ("This car is worth " + str(estimatedPrice) + "$")

if __name__ == "__main__":
    main()
