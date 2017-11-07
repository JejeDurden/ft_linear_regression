#!/usr/bin/python3
import os.path
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import preprocessing

def display_data(data):
    x = data.km
    y = data.price
    plt.figure(figsize=(10, 10))
    plt.plot(x, y, "b.")
    plt.axis([0, 250000, 0, 10000])
    plt.show()

def display_line(a, b, data):
    y = data.price
    x = data.km
    plt.figure(figsize=(10, 10))
    plt.plot(x, y, "b.")
    norm_mileage = (0 - min(data.km))/(max(data.km)-min(data.km))
    norm_price = a * norm_mileage + b
    predict1 = norm_price * (max(data.price)-min(data.price)) + min(data.price)
    norm_mileage = (250000 - min(data.km))/(max(data.km)-min(data.km))
    norm_price = a * norm_mileage + b
    predict2 = norm_price * (max(data.price)-min(data.price)) + min(data.price)
    plt.plot([0, 250000], [predict1, predict2], "r-")
    plt.axis([0, 250000, 0, 10000])
    plt.show()

def cost_func(length, a, b, data):
    total_error = 0
    for i in range(0, length):
        x = data[i, 0]
        y = data[i, 1]
        total_error += (y - (a * x + b)) ** 2
    return total_error / float(length)

def step_gradient(a_current, b_current, data, learning_rate, length):
    a_gradient = 0
    b_gradient = 0
    for i in range(0, length):
        x = data[i, 0]
        y = data[i, 1]
        b_gradient += -(2/float(length)) * (y - ((a_current * x) + b_current))
        a_gradient += -(2/float(length)) * x * (y - ((a_current * x) + b_current))
    new_a = a_current - (learning_rate * a_gradient)
    new_b = b_current - (learning_rate * b_gradient)
    return [new_a, new_b]

def gradient_descent(starting_a, starting_b, data, learning_rate, iterations, length):
    a = starting_a
    b = starting_b
    loss_history = []
    a_history = []
    b_history = []
    for i in range(iterations):
        a, b = step_gradient(a, b, data, learning_rate, length)
        loss_history.append(cost_func(length, a, b, data))
        a_history.append(a)
        b_history.append(b) 
    return [a, b, loss_history, a_history, b_history]

def main():
    if os.path.exists('data.csv'):
        data = pd.read_csv("data.csv")
    else:
        print ("There is no data.csv file. Please add one to the same directory as " + sys.argv[0])
        sys.exit()
    display_data(data)
    min_km = min(data.km)
    max_km = max(data.km)
    min_price = min(data.price)
    max_price = max(data.price)
    data.km = (data.km - min_km)/(max_km-min_km)
    data.price = (data.price - min_price)/(max_price-min_price)
    data_norm = data.as_matrix()
    a = 0
    b = 0
    alpha = 0.1
    iterations = 1000
    length = len(data_norm)
    print ("starting gradient descent at a = {0}, b = {1}, error = {2}".format(a, b, cost_func(length, a, b, data_norm)))
    print ("Training...")
    [a, b, loss_history, a_history, b_history] = gradient_descent(a, b, data_norm, alpha, iterations, length)
    print ("ending gradient descent at iteration = {0}, a = {1}, b = {2}, error = {3}".format(iterations, a, b, cost_func(length, a, b, data_norm)))
    data.km = data.km * (max_km-min_km) + min_km
    data.price = data.price * (max_price-min_price) + min_price
    display_line(a, b, data)
    sns.tsplot(data = np.transpose(loss_history))
    plt.show()
    sns.tsplot(data = np.transpose(a_history))
    plt.show()
    sns.tsplot(data = np.transpose(b_history))
    plt.show()
    with open('values.txt', 'w') as f:
        f.write(str(a))
        f.write("\n")
        f.write(str(b))


if __name__ == "__main__":
    main()
