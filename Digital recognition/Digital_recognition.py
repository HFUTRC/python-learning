import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from scipy.io import loadmat
from scipy.optimize import minimize


def sigmoid(z):
    return 1/(1+np.exp(-z))

def costFunction(theta,x,y,learningRate):
    theta = np.matrix(theta)
    X = np.matrix(x)
    y = np.matrix(y)
    
    first = np.multiply(-y, np.log(sigmoid(X * theta.T)))
    second = np.multiply((1 - y), np.log(1 - sigmoid(X * theta.T)))
    reg = (learningRate / (2 * len(X))) * np.sum(np.power(theta[:,1:theta.shape[1]], 2))
    return np.sum(first - second) / len(X) + reg

def gradient(theta, X, y, learningRate):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    
    parameters = int(theta.ravel().shape[1])
    error = sigmoid(X * theta.T) - y
    
    grad = ((X.T * error) / len(X)).T + ((learningRate / len(X)) * theta)
    
    # intercept gradient is not regularized
    grad[0, 0] = np.sum(np.multiply(error, X[:,0])) / len(X)
    
    return np.array(grad).ravel()    

def one_vs_all(X, y, num_labels, learning_rate):
    rows = X.shape[0]
    params = X.shape[1]
    
    # k X (n + 1) array for the parameters of each of the k classifiers
    all_theta = np.zeros((num_labels, params + 1))
    
    # insert a column of ones at the beginning for the intercept term
    X = np.insert(X, 0, values=np.ones(rows), axis=1)
    
    # labels are 1-indexed instead of 0-indexed
    for i in range(1, num_labels + 1):
        theta = np.zeros(params + 1)
        y_i = np.array([1 if label == i else 0 for label in y])
        y_i = np.reshape(y_i, (rows, 1))
        
        # minimize the objective function
        fmin = minimize(fun=costFunction, x0=theta, args=(X, y_i, learning_rate), method='TNC', jac=gradient)
        #fun:优化的目标函数  x0:theta初值  args:传递给目标函数的参数  method:优化使用的方法  jac:目标函数的梯度
        all_theta[i-1,:] = fmin.x
    
    return all_theta

def predict_all(X, all_theta):
    rows = X.shape[0]
    params = X.shape[1]
    num_labels = all_theta.shape[0]
    
    # same as before, insert ones to match the shape
    X = np.insert(X, 0, values=np.ones(rows), axis=1)
    
    # convert to matrices
    X = np.matrix(X)
    all_theta = np.matrix(all_theta)
    
    # compute the class probability for each class on each training instance
    h = sigmoid(X * all_theta.T)
    
    # create array of the index with the maximum probability
    h_argmax = np.argmax(h, axis=1)
    
    # because our array was zero-indexed we need to add one for the true label prediction
    h_argmax = h_argmax + 1
    
    return h_argmax
def plot_an_image(image):
#     """
#     image : (400,)
#     """
    im = image.reshape(20,20)
    im = im.transpose(1, 0)
    fig, ax = plt.subplots(figsize=(1, 1))
    ax.matshow(im, cmap=matplotlib.cm.binary)
    plt.xticks(np.array([]))  # just get rid of ticks
    plt.yticks(np.array([]))
#绘图函数
def plot_images(X):

    fig,ax = plt.subplots(nrows=3, ncols=3, sharey=True, sharex=True, figsize=(5, 3))
    for i in range(3):
        for j in range(3):
            im = X[i*3+j].reshape(20,20)
            im = im.transpose(1,0)

            ax[i,j].matshow(im,cmap=matplotlib.cm.binary)
            plt.xticks(np.array([]))  # just get rid of ticks
            plt.yticks(np.array([]))

def main():
    data = loadmat('ex3data1.mat')

    all_theta = one_vs_all(data['X'], data['y'], 10, 1)
    h = predict_all(data['X'][2234:2244,:],all_theta)
    print(h)
    plot_images(data['X'][2234:2244,:])
    plt.show()
    
  

if __name__ == '__main__':
    main()    
