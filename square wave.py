import numpy as np
import matplotlib.pyplot as plt

def square_wave(t, period=2*np.pi):
    """
    Generate a perfect square wave with period T (default: 2π), 
    symmetric around t = 0 over the range [-π, π].

    Parameters:
        t (float or ndarray): Input time(s).
        period (float): Period of the square wave.

    Returns:
        ndarray: Square wave values (+1 or -1).
    """
    t_periodic = (t + period / 2) % period - period / 2  # Wrap into [-π, π]
    return np.where(t_periodic <= 0, -1, 1)  # Assign -1 for t < 0, +1 for t >= 0

# Generate time values over multiple periods
t = np.linspace(-2 * np.pi, 2 * np.pi, 100000)  # Covers 2 full periods [-2π, 2π]
square_wave_values = square_wave(t)

# Plot the square wave
plt.figure(figsize=(8, 4))
plt.plot(t, square_wave_values, color="blue", label="Square Wave")
plt.title("Perfect Square Wave over [-π, π]")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.axvline(0, color='red', linestyle='--', label="t = 0")
plt.legend()
plt.show()
