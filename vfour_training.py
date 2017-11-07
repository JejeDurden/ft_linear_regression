#!/usr/bin/python3

import os.path
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def compute_cost(X, y, theta):
    m = len(y)
    J = np.subtract(np.dot(X, theta), y)
    J = np.dot(np.transpose(J), J)
    return (np.sum(J) / (2.0 * m))

def gradient_descent(X, y, theta, alpha, num_iters):
    m = len(y)
    J_history = np.zeros((num_iters, 1))
    coeff = alpha/m;
    for i in range(num_iters):
        tmp = X.T @ (X @ theta - y)
        theta = theta - coeff * tmp
        J_history[i] = compute_cost(X, y, theta)
    return theta, J_history

def main():
    if os.path.exists('data.csv'):
        data = pd.read_csv('data.csv')
    else:
        print("There is no data.csv file. Please add one to the same directory as " + sys.argv[0])
        sys.exit()

    X = np.array(data.loc[:,'km'], dtype = 'float32')
    y = np.array(data.loc[:,'price'], dtype = 'float32')
    m = len(y)
    y = y.reshape((m,1))
    X = np.hstack([np.ones((m, 1)), X.reshape((m, 1))])
    print (X)
    theta = np.zeros((2,1))
    iterations = 1500
    alpha = 0.01

    print(compute_cost(X, y, theta))

    theta, j_history = gradient_descent(X, y, theta, alpha, iterations)

    print(theta)
#    display_line(h, data.km, data.price)
#    with open('values.txt', 'w') as f:
#        f.write(str(theta[0]))
#        f.write("\n")
#        f.write(str(theta[1]))


if __name__ == "__main__":
    main()
