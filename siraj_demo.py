#The optimal values of m and b can be actually calculated with way less effort than doing a linear regression. 
#this is just to demonstrate gradient descent

from numpy import *
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd

# y = mx + b
# m is slope, b is y-intercept
def compute_error_for_line_given_points(b, m, points):
    total_error = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        total_error += (y - (m * x + b)) ** 2
    return total_error / float(len(points))

def step_gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    loss_history = []
    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(points), learning_rate)
        loss_history.append(compute_error_for_line_given_points(b, m, points))
    return [b, m, loss_history]

def run():
    if os.path.exists('data.csv'):
        data = pd.read_csv("data.csv")
    else:
        print("There is no data.csv file. Please add one to the same directory as " + sys.argv[0])
        sys.exit()
    #display_data(data)
    min_km = min(data.km)
    max_km = max(data.km)
    min_price = min(data.price)
    max_price = max(data.price)
    data.km = (data.km - min_km)/(max_km-min_km)
    data.price = (data.price - min_price)/(max_price-min_price)
    points = data.as_matrix()
    learning_rate = 0.1
    initial_b = 0 # initial y-intercept guess
    initial_m = 0 # initial slope guess
    num_iterations = 10000
    print("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points)))
    print("Running...")
    [b, m, loss_history] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    sns.tsplot(data = transpose(loss_history))
    plt.show()
    with open('values.txt', 'w') as f:
       f.write(str(m))
       f.write("\n")
       f.write(str(b))
    print("After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points)))

if __name__ == '__main__':
    run()