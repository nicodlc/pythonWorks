import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
X = 2 * np.random.rand(100, 1)      # column vector of 100 rows, the input vector so to speak
Y = 4 + 3*X + np.random.rand(100,1) # column vector of 100 rows, the existing information vector [so to speak]

def linear_regression(X, theta):    # linear regression model
    return X.dot(theta)

def mean_squared_error(y_pred, y_true):  # that formula in statistics used to show error
    return np.mean((y_pred - y_true)**2)

theta = np.random.rand(1,2)  # parameter vector of 2 rows and 1 column

learning_rate = 0.01
num_iterations = 1000

for iteration in range(num_iterations):
    # compute predictions
    y_pred = linear_regression(X, theta)

    # compute the gradient descent function
    gradient = (X.T.dot(y_pred - Y))/len(Y)
    # print(f"Theta value: {theta}, Gradient value: {gradient}")

    # update the parameters
    theta = theta - learning_rate*gradient

    # compute and print the loss
    loss = (mean_squared_error(y_pred, Y))
    print(f"Iteration {iteration+1}/{num_iterations}, Loss: {loss}")

# plot original data points
plt.scatter(X, Y, label="Data")

# plot the regression line
x_range = np.linspace(0, 2, 100)
y_range = theta[0] + theta[1] * x_range
plt.plot(x_range, y_range, color='r', label="Regression Line")

plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()