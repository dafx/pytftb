#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 jaidev <jaidev@newton>
#
# Distributed under terms of the MIT license.

"""
Example from section 3.3.2 of the tutorial.
"""

from tftb.generators import fmlin
from tftb.processing.linear import gabor
import matplotlib.pyplot as plt
import numpy as np

N1 = 256
Ng = 33
Q = 1
sig = fmlin(N1)[0]
window = np.exp(np.log(0.005) * np.linspace(-1, 1, Ng) ** 2)
window = window / np.linalg.norm(window)
tfr, dgr, h = gabor(sig, 16, Q, window)

plt.imshow(np.flipud(tfr)[8:, :], aspect='auto', extent=[0, 16, 0, 0.5],
           interpolation='none')
plt.xlabel('Time')
plt.ylabel('Normalized frequency')
plt.title('Squared modulus of the Gabor coefficients')
plt.show()
