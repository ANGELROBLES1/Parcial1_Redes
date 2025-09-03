import numpy as np
import matplotlib.pyplot as plt

fs = 2000  # Frecuencia de muestreo
T = 1  # Duración total
N = int(fs * T)  # Número de muestras
t = np.linspace(0, T, N, endpoint=False)  # Vector de tiempo

pulse_period = 0.05
pulse_width = 0.01
signal = np.zeros_like(t)  # Señal de pulso
for i in range(int(T / pulse_period)):
    start = int(i * pulse_period * fs)
    end = int(start + pulse_width * fs)
    if end > len(signal):
        end = len(signal)
    signal[start:end] = 1

fft_signal = np.fft.fft(signal)
freqs = np.fft.fftfreq(N, 1/fs)

half = N // 2
freqs_pos = freqs[:half]  # Frecuencias positivas
fft_magnitude = np.abs(fft_signal[:half]) / N

plt.figure(figsize=(8, 4))
plt.step(t * 1000, signal, color='black')
plt.title('Tren de pulsos (dominio del tiempo)')
plt.xlabel('Tiempo (ms)')
plt.ylabel('Amplitud')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(freqs_pos, fft_magnitude, color='orange')
plt.title('Transformada de Fourier (dominio de la frecuencia)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
