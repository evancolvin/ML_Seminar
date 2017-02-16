# Basic Scripts to generate plots for my Logistic Regression Talk

import numpy as np
import matplotlib.pyplot as plt

# The float(n)'s mean that I don't have to worry about issues with division
# when I give it an integer

def linear_function(n):
    n = float(n)
    return n

def hyperbolic_tangent(n):
    n = float(n)
    tanh_n = (np.exp(n) - np.exp(-n))/(np.exp(n) + np.exp(-n))
    return tanh_n

def logistic_function(n):
    n = float(n)
    theta = np.exp(n)/(1 + np.exp(n))
    return theta

plt.plot(np.linspace(-5, 5, num = 250), map(logistic_function,
                            np.linspace(-5, 5, num = 250)), color = 'r')

plt.plot(np.linspace(-5, 5, num = 250), map(linear_function,
                            np.linspace(-5, 5, num = 250)), color = 'r')

plt.plot(np.linspace(-5, 5, num = 250), map(hyperbolic_tangent,
                            np.linspace(-5, 5, num = 250)), color = 'r')
