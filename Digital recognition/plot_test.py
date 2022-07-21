import numpy as np
import pandas as pd
import matplotlib
from scipy.io import loadmat
import matplotlib.pyplot as plt

def plot_images(X):

    fig,ax = plt.subplots(nrows=3, ncols=3, sharey=True, sharex=True, figsize=(6, 3))
    for i in range(3):
        for j in range(3):
            im = X[i*3+j].reshape(20,20)
            im = im.transpose(1,0)

            ax[i,j].matshow(im,cmap=matplotlib.cm.binary)
            plt.xticks(np.array([]))  # just get rid of ticks
            plt.yticks(np.array([]))

def main():
    data = loadmat('ex3data1.mat')

   
    plot_images(data['X'][4990:,:])
    plt.show()
   
  

if __name__ == '__main__':
    main()    