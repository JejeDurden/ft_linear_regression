#!/usr/bin/python3
import os.path
import sys
import pandas as pd

def main():
    if os.path.exists('data.csv'):
        data = pd.read_csv("data.csv")
    else:
        print("There is no data.csv file. Please add one to the same directory as " + sys.argv[0])
        sys.exit()
    mileage = input("Please enter a mileage: ")
    try:
        mileage = float(mileage)
    except ValueError:
        print("That's not a number!")
        sys.exit()
    if mileage < 0 :
        print("Be realistic, mileage cannot be a negative value !")
        sys.exit()
    if mileage > 3039122 :
        print("You should check for a smaller mileage, no car in the world has been on the road that much !")
        sys.exit()
    norm_mileage = (mileage - min(data.km))/(max(data.km)-min(data.km))
    if os.path.exists('values.txt'):
        with open('values.txt') as f:
            theta1 = float(f.readline())
            theta0 = float(f.readline())
    else:
        theta0 = 0
        theta1 = 0
    norm_price = theta1 * norm_mileage + theta0
    estimated_price = norm_price * (max(data.price)-min(data.price)) + min(data.price)
    print ("This car is worth " + str(estimated_price) + "$")

if __name__ == "__main__":
    main()
