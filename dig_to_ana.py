import matplotlib.pyplot as plt
import numpy as np

fs = 10000
bit_input = input("Enter bits (e.g. 10101): ")
bits = [int(b) for b in bit_input]

Tb = 0.01  # smaller bit duration for clear waveform
t_bits = np.arange(0, Tb, 1/fs)

bpsk = []
ask = []
fsk = []

# Better separated frequencies
f0 = 500
fc = 2000

for b in bits:
    if b == 1:
        bpsk.extend(np.cos(2*np.pi*fc*t_bits))
        ask.extend(np.cos(2*np.pi*fc*t_bits))
        fsk.extend(np.cos(2*np.pi*fc*t_bits))
    else:
        bpsk.extend(-np.cos(2*np.pi*fc*t_bits))
        ask.extend(np.zeros(len(t_bits)))
        fsk.extend(np.cos(2*np.pi*f0*t_bits))

bpsk = np.array(bpsk)
ask = np.array(ask)
fsk = np.array(fsk)

# Proper time scaling
t = np.linspace(0, Tb*len(bits), len(bpsk))

plt.figure(figsize=(10, 8))

plt.subplot(3,1,1)
plt.plot(t, bpsk)
plt.title("BPSK Signal")
plt.grid()

plt.subplot(3,1,2)
plt.plot(t, ask)
plt.title("ASK Signal")
plt.grid()

plt.subplot(3,1,3)
plt.plot(t, fsk)
plt.title("FSK Signal")
plt.grid()

plt.tight_layout()
plt.show()