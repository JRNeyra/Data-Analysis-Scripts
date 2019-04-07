#########################################################
# Description: This script implements the Additive White
# Gaussian Noise model and compares it to random data
# generated using the numpy library.
# Author: Jose Neyra
#########################################################

import numpy as np
from scipy import special
import matplotlib.pyplot as plt
import time

tic = time.time()

# Set a signal to noise ratios
snrs = 2**np.arange(-2, 4, 0.1)
N = 10**6
errors = np.zeros(len(snrs))

for i, snr in enumerate(snrs):
    # Generate random bits
    bits = np.random.randint(0, 2, size=N)

    # Convert to bpsk signal
    bpskSignal = 2*bits-1

    # Add noise
    sigma = np.sqrt(1/(2*snr))
    bpskSignal = bpskSignal + sigma*np.random.randn(N)

    # ML detector
    bitsHat = np.zeros(N, dtype='bool')
    bitsHat[bpskSignal > 0] = True

    # Calculate error
    nOfErrors = np.sum(np.logical_xor(bits.astype('bool'), bitsHat))
    errors[i] = nOfErrors/N

# Plot theoretical vs empirical
thrErrors = 0.5*special.erfc(np.sqrt(snrs))
toc = time.time()

print('time elapsed: %.3f seconds' % (toc-tic))

plt.plot(10*np.log10(snrs), np.log10(thrErrors))
plt.plot(10*np.log10(snrs), np.log10(errors), 'ro')
plt.xlabel(r'$\frac{E_b}{N_0}$dB')
plt.ylabel(r'$log_{10}P_{err}$')
plt.figure()
plt.hist(np.random.randn(N), bins=1000)
plt.title('histogram of noise')
plt.show()
