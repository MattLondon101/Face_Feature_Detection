# Run this file to import useful computer vision packages.
# If package not already installed, use subprocess (line 7) to install (e.g. replace nibabel with needed package)
# Use 'imsh' function, at bottom, to quickly display an image.
import subprocess
import sys
import pip
import glob
#subprocess.check_call(["python",'-m','pip','install','--upgrade','nibabel'])
import nibabel
import natsort
from natsort import natsorted,ns
import csv
import cv2 as cv
import itertools
from itertools import groupby
import keras
import math
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
from numpy import int32
import os 
from os import listdir
from os.path import isfile, join
from os import walk
import pandas as pd
from PIL import Image
from PIL import ImageStat
import PIL.ImageOps
import resizeimage
from resizeimage import resizeimage
import scipy
import skimage
from skimage.transform import rotate
from skimage.feature import local_binary_pattern
from skimage import data
from skimage.color import rgb2gray
from skimage.color import label2rgb
from skimage import io, color
from skimage.util.shape import view_as_windows as vaw
import statistics as stats
from scipy import signal
from scipy import ndimage
import tensorflow as tf

def imsh(img,nrows=1,ncols=1,cmap='gray'):
    fig,ax=plt.subplots(nrows=nrows,ncols=ncols,
    figsize=(5,5))
    ax.imshow(img,cmap='gray')
    ax.axis('off')
    return fig,ax
