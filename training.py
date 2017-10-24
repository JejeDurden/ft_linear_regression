#!/usr/bin/python3
import os.path
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing

def display_data(data):
    x = data.km
    y = data.price
    plt.figure(figsize=(10, 10))
    plt.plot(x, y, "b.")
    plt.axis([0, 250000, 0, 10000])
    plt.show()

def display_line(h, data):
    y = data.price
    x = data.km
    plt.figure(figsize=(10, 10))
    plt.plot(x, y, "b.")
    plt.axis([0, 250000, 0, 10000])
    predict1 = np.dot(np.array([1.0, 3.5]), h)
    predict2 = np.dot(np.array([1.0, 7.0]), h)
    plt.plot(predict1, predict2)
    plt.show()

def cost_func(m, h, data):
    cost = 0
    for i in range(m):
        x = data[i, 0]
        y = data[i, 1]
        cost += (y - (h[0] * x + h[1])) **2
    return cost / float(m)

def gradient_descent(h, data, alpha, iteration, m):
    a = h[0]
    b = h[1]
    for i in range(iteration):
        a, b = step_gradient(a, b, data, alpha, m)
    return a, b

def step_gradient(a, b, data, alpha, m):
    a_gradient = 0
    b_gradient = 0
    for i in range(0, m):
        x = data[i, 0]
        y = data[i, 1]
        a_gradient = -(2/float(m)) * x * (y - (a * x) + b)
        b_gradient = -(2/float(m)) * (y - ((a * x) + b))
    new_a = a - (alpha * a_gradient)
    new_b = b - (alpha * b_gradient)
    return new_a, new_b

def main():
    if os.path.exists('data.csv'):
        data = pd.read_csv('data.csv')
    else:
        print("There is no data.csv file. Please add one to the same directory as " + sys.argv[0])
        sys.exit()
    print (data)
    display_data(data)
    data_norm = preprocessing.normalize(data, norm='l2')
    h = [0, 0]
    alpha = 0.001
    iteration = 10000
    m = len(data)
    print ("starting gradient descent at a = {0}, b = {1}, error = {2}".format(h[0], h[1], cost_func(m, h, data_norm)))
    h[0], h[1] = gradient_descent(h, data_norm, alpha, iteration, m)    
    print ("ending gradient descent at iteration = {0}, a = {1}, b = {2}, error = {3}".format(iteration, h[0], h[1], cost_func(m, h, data_norm)))
    display_line(h, data)
    with open('values.txt', 'w') as f:
        f.write(str(h[0]))
        f.write("\n")
        f.write(str(h[1]))


if __name__ == "__main__":
    main()
