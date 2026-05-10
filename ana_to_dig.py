import matplotlib.pyplot as plt
import numpy as np
A=5
f=5
T=1
fs_ana=10000
fs_sampled=50
bits=8

t=np.linspace(0,T,fs_ana)
analog=np.sin(2*np.pi*f*t)

ts=np.arange(0,T,1/fs_sampled)
sampled=np.sin(2*np.pi*f*ts)

level=2**bits
max_val=A
min_val=-A
step=(max_val-min_val)/level
quantized=np.round((sampled-min_val)/step)*step+min_val

dig_dec=np.round((quantized-min_val)/step).astype(int)
dig_bin=[format(x,f'0{bits}b')for x in dig_dec]

plt.figure(figsize=(12,8))
plt.plot(t,analog,label="analog",alpha=0.4)
plt.stem(ts,sampled,label="sampled")
plt.step(ts,quantized,label="digital")

plt.legend()
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.title("A to D")
plt.grid(True)
plt.show()