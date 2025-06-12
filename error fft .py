import numpy as np
import matplotlib.pyplot as plt

# Input signal
def gaussian(x):
    return np.exp(-x**2)

def calculate_error_near_peak(n, peak_range=0.2):
    t = np.linspace(-5, 5, n)
    x = gaussian(t)

    # Compute FFT
    dt = t[1] - t[0]
    frequencies = np.fft.fftshift(np.fft.fftfreq(n, d=dt))
    f = np.fft.fft(x)
    magnitude = np.abs(f) * dt
    shifted_magnitude = np.fft.fftshift(magnitude)

    # Analytical Fourier Transform
    analytical = np.sqrt(np.pi) * np.exp(-np.pi**2 * frequencies**2)

    # Select frequencies near the peak (around zero)
    peak_indices = np.where(np.abs(frequencies) <= peak_range)
    peak_shifted_magnitude = shifted_magnitude[peak_indices]
    peak_analytical = analytical[peak_indices]

    # Compute relative error for points around the peak
    error = np.abs(peak_shifted_magnitude - peak_analytical) / (peak_analytical + 1e-10) * 100
    mean_error = np.mean(error)
    return mean_error

# Example usage
range_n = [2**i for i in range(2, 20)]
error_list = [calculate_error_near_peak(n, peak_range=0.2) for n in range_n]

plt.plot(range_n, error_list, marker='o', markersize=5, label="Error Near Peak")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Number of Points")
plt.ylabel("Error")
plt.title("Error vs Number of Sample Points")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()
plt.show()
