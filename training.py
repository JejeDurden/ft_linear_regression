#!/usr/bin/python3
import os.path
import sys
import pandas as pd
import matplotlib.pyplot as plt

def display_data(A, B):
    plt.figure(figsize=(10, 10))
    plt.plot(A, B, "b.")
    plt.axis([0, 250000, 0, 10000])
    plt.show()

def main():
    if os.path.exists('data.csv'):
        data = pd.read_csv('data.csv')
    else:
        print("There is no data.csv file. Please add one to the same directory as " + sys.argv[0])
        sys.exit()
    print (data)
    display_data(data.km, data.price)
    alpha = 0.01
    cur_x = 6
    precision = 0.00001
    previous_step_size = cur_x

    def df(x):
        return 4 * x**3 - 9 * x**2

    while previous_step_size > precision:
        prev_x = cur_x
        cur_x += -gamma * df(prev_x)
        previous_step_size = abs(cur_x - prev_x)


if __name__ == "__main__":
    main()
