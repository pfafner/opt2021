# Spectral clustering
# Author: Alan Reyes-Figueroa
# Date:   Aug 15, 2021

import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sp
import scipy.sparse.linalg as ln

import pandas as pd
from PIL import Image

from time import time
from math import exp, sqrt



# ---------- Affinity matrix computation ----------

def similarity(x1, y1, x2, y2, I, sigma=1., alpha=0.5, beta=0.5):
    ''' Computes the similarity between two pixels in an image.
        Inputs:  x1, y1 = pixel 1 coordinates
                 x2, y2 = pixel 2 coordinates
                 I      = RGB image
                 sigma  = variance (1.0 is the default)
                 alpha, beta = weights for the spatial and color components
        Output:  similarity s_ij between I[pixel 1] and I[pixel 2] values.
    '''
    (h, w) = I.shape[:2]
    space_distance = (np.abs(x2-x1) + np.abs(y2-y1))/float(h+w)             # spatial component
    color_distance = np.linalg.norm(I[x1, y1, :] - I[x2, y2, :], 1)         # color component
    return np.exp(-(alpha*space_distance + beta*color_distance) / (2.*sigma**2))



def jit_similarity(x1, y1, x2, y2, I1, I2, h, w, sigma=1., alpha=1, beta=1):
    ''' Fast computing of the similarity between two pixels in an image.
        Uses a Numba @jit scheme.
        Inputs:  x1, y1 = pixel 1 coordinates
                 x2, y2 = pixel 2 coordinates
                 I      = RGB image
                 sigma  = variance (1.0 is the default)
                 alpha, beta = weights for the spatial and color components
        Output:  similarity s_ij between I[pixel 1] and I[pixel 2] values.
    '''
    space_distance = (abs(x2-x1) + abs(y2-y1))/(h+w)                            # spatial component
    color_distance = (abs(I1[0]-I2[0]) + abs(I1[1]-I2[1]) + abs(I1[2]-I2[2]))   # color component
    return exp(-(alpha*space_distance + beta*color_distance) / (2.*sigma**2))



def idx2ij(a, shape):
    ''' Converts a flat list of pixels into x, y pixel coordinates.
        Inputs:  a     = list of pixels = np.arange(0, image size)
                 shape = shape of image I            
        Output:  x, y  = list of x and y pixel coordinates.
    '''    
    (h,w) = shape
    x = np.zeros(a.shape).astype(int)
    y = np.zeros(a.shape).astype(int)
    for i in range(0, len(a)):
        x[i] = a[i]//w
        y[i] = a[i] - x[i]*w
    return x, y



def imageGraph_sparse(I, std=1., alpha=1., beta=1., p=0.):
    ''' Constructs the affinity matrix of an image I.
        Inputs:  I      = RGB input image as numpy array of shape (h,w,3).
                 sigma  = standard deviation (to be called in the similarity function). Default sigma = 1.
                 alpha, beta = weights for the spatial and color components in similarity function.
                               Default values 0.5.
        Output:  W      = affinity matrix of I.
    '''
    #If = I.reshape(-1,3)
    (h, w) = I.shape[:2]      # shape of image
    sh = h*w                  # shape of graph matrix W
      
    # fill W
    coords = []
    for i in range(0, h):
        for j in range(0, w-1):
            sim = jit_similarity(i, j, i, j+1, I[i,j,:], I[i,j+1,:], h, w, sigma, alpha, beta)
            coords.append([sim, i*w+j, i*w+(j+1)])
            coords.append([sim, i*w+(j+1), i*w+j])

    for i in range(0, h-1):
        for j in range(0, w):
            sim = jit_similarity(i, j, i+1, j, I[i,j,:], I[i+1,j,:], h, w, sigma, alpha, beta)
            coords.append([sim, i*w+j, (i+1)*w+j])
            coords.append([sim, (i+1)*w+j, i*w+j])
            
    # add randoms
    radds = []
    for pix in range(0, sh-2):
        q = int(p * (sh-pix-2))
        if (q > 0):
            ll = list(np.arange(pix+2, sh))
            if (pix+w in ll): ll.remove(pix+w)
            ll = np.array(ll)
            sel = np.random.permutation(np.arange(len(ll)))[:q]
            i = pix//w
            j = pix - i*w
            for s in sel:
                ii = s//w
                jj = s - ii*w
                sim = jit_similarity(i, j, ii, jj, I[i,j,:], I[ii,jj,:], h, w, sigma, alpha, beta)
                radds.append([sim, pix, s])
                radds.append([sim, s, pix])
        
    # define sparse matrix
    coords = np.array(coords)
    radds  = np.array(radds)
    W = sp.coo_matrix((coords[:,0], (coords[:,1], coords[:,2])), shape=(sh,sh))
    if (len(radds) > 0):
        R = sp.coo_matrix((radds[:,0], (radds[:,1], radds[:,2])), shape=(sh,sh))
        W = W + R
    return W
