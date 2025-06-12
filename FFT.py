import numpy as np
import matplotlib.pyplot as plt

# Input signal
n1 = 2**10
def gaussian(x):
    return np.exp(-x**2)  # Gaussian without normalization

t = np.linspace(-5, 5, n1)
x1 = gaussian(t)

# Padding to next power of 2
if n1 & (n1 - 1) != 0:
    n = int(2**np.ceil(np.log2(n1)))
    x = np.pad(x1, (0, n - n1), 'constant')
else:
    n = n1
    x = x1

# FFT
dt = t[1] - t[0]  # Time step
f = np.fft.fft(x)
magnitude = abs(f)*dt  # Normalize by sampling interval

# Manual implementation of frequency bins
frequencies = np.concatenate((
    np.arange(0, n // 2) / (n * dt),
    np.arange(-n // 2, 0) / (n * dt)
))

# Apply fftshift to frequencies and FFT output
shifted_frequencies = np.fft.fftshift(frequencies)
shifted_magnitude = np.fft.fftshift(magnitude)

# Analytical Fourier Transform
analytical = np.sqrt(np.pi) * np.exp(-np.pi**2 * shifted_frequencies**2)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(shifted_frequencies, shifted_magnitude, label="FFT Result", lw=2)
plt.plot(shifted_frequencies, analytical, label="Analytical Solution", linestyle="dashed", lw=2)
plt.xlim(-5, 5)  # Focus on low frequencies
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.legend()
plt.title("Fourier Transform of $e^{-x^2}$ (With Scaling)")
plt.grid()
plt.show()
