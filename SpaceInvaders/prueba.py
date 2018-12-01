import tensorflow
import numpy as np
import retro

from skimage import transform
from skimage.color import rgb2gray

import matplotlib.pyplot as plt

from collections import deque

import random

import warnings
# Create our environment
    env = retro.make(game='SpaceInvaders-Atari2600')

print("The size of our frame is: ", env.observation_space)
print("The action size is : ", env.action_space.n)

# Here we create an hot encoded version of our actions
# possible_actions = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]...]
possible_actions = np.array(np.identity(env.action_space.n, dtype=int).tolist())
warnings.filterwarnings('ignore')

