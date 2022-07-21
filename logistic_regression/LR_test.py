import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt

def show_data():
    path = 'ex2data1.txt'
    data = pd.read_csv(path,header=None,names=['Exam 1', 'Exam 2', 'Admitted'])

    positive = data[data['Admitted'].isin([1])]
    negative = data[data['Admitted'].isin([0])]

    fig, ax = plt.subplots(figsize=(12,8))
    ax.scatter(positive['Exam 1'], positive['Exam 2'], s=50, c='b', marker='o', label='Admitted')
    ax.scatter(negative['Exam 1'], negative['Exam 2'], s=50, c='r', marker='x', label='Not Admitted')
    ax.legend()
    ax.set_xlabel('Exam 1 Score')
    ax.set_ylabel('Exam 2 Score')
    plt.show()

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def cost(theta, X, y):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    first = np.multiply(-y, np.log(sigmoid(X * theta.T)))
    second = np.multiply((1 - y), np.log(1 - sigmoid(X * theta.T)))
    return np.sum(first - second) / (len(X))    

def gradient(theta, X, y):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    
    parameters = int(theta.ravel().shape[1]) #=3
    grad = np.zeros(parameters)
    
    error = sigmoid(X * theta.T) - y
    
    for i in range(parameters):
        term = np.multiply(error, X[:,i])
        grad[i] = np.sum(term) / len(X)
    
    return grad

def predict(theta, X):
    probability = sigmoid(X * theta.T)
    return [1 if x >= 0.5 else 0 for x in probability]  

def main():
    path = 'ex2data1.txt'
    data = pd.read_csv(path,header=None,names=['Exam 1', 'Exam 2', 'Admitted'])

    # add a ones column - this makes the matrix multiplication work out easier
    data.insert(0, 'Ones', 1)

    # set X (training data) and y (target variable)
    cols = data.shape[1]
    X = data.iloc[:,0:cols-1]
    y = data.iloc[:,cols-1:cols]

    # convert to numpy arrays and initalize the parameter array theta
    X = np.array(X.values)
    y = np.array(y.values)
    theta = np.zeros(3)

    result = opt.fmin_tnc(func=cost, x0=theta, fprime=gradient, args=(X, y))   #批量梯度下降，result[0]即为梯度下降后得到的最优的theta值

    print(cost(result[0],X,y))    #查看最终代价

    grades = np.array([[1,60,60],[1,95,85]])   #2*3
    theta_min = np.matrix(result[0])           #1*3 

    print(sigmoid(grades * theta_min.T))

    print(predict(theta_min,grades))






if __name__ == '__main__':
    main()    