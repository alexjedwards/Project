# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 11:06:48 2021

@author: scaje
"""

import numpy as np
import matplotlib.pyplot as pyplot
time = np.arange(0, 10, 0.1)
amplitude = np.cos(time)

pyplot.plot(time, amplitude)

pyplot.title("Cosine Curve")

pyplot.xlabel("time")

pyplot.ylabel("Amplitude")

pyplot.show()




