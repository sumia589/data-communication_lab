import matplotlib.pyplot as plt
import numpy as np
def plot(fm,fc):
    t=np.linspace(0,1,1000)
    
    ms=np.sin(2*np.pi*fm*t)
    cs=np.sin(2*np.pi*fc*t)

    am_signal=(1+ms)*cs
    kf=5
    fm_signal=np.sin(2*np.pi*fc*t+kf*np.cumsum(ms)/len(t))
    kp=np.pi
    pm_signal=np.sin(2*np.pi*fc*t+kp*ms)

    plt.figure(figsize=(10,10))

    plt.subplot(4,1,1)
    plt.title("AM")
    plt.xlabel("amplitude")
    plt.ylabel("Time")
    plt.plot(t,am_signal,color='r')
    plt.grid(True)
    plt.subplot(4,1,3)
    plt.title("FM")
    plt.xlabel("amplitude")
    plt.ylabel("Time")
    plt.plot(t,fm_signal,color='g')
    plt.grid(True)
    
    plt.tight_layout()
    plt.subplots_adjust(hspace=.08)
    plt.show()

fc=float(input("enter fc"))
fm=float(input("enter fm"))
plot(fm,fc)