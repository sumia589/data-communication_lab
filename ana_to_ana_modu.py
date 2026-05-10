import numpy as np
import matplotlib.pyplot as plt
def plot(fm,fc):
    t=np.linspace(0,1,1000)

    ms=np.sin(2*np.pi*fm*t)
    cs=np.sin(2*np.pi*fc*t)
    am_signal=(1+ms)*cs
    kf=5
    fm_signal=np.sin(2*np.pi*fc*t+kf*np.cumsum(ms)/len(t))
    kp=np.pi/2
    pm_signal=np.sin(2*np.pi*fc*t+kf*ms)

    plt.figure(figsize=(10,10))

    plt.subplot(4,1,1)
    plt.plot(t,ms,color='m')
    plt.title("Message signal")
    plt.xlabel("time")
    plt.ylabel("Amplitude")
    plt.grid(True)

    plt.subplot(4,1,2)
    plt.plot(t,am_signal,color='b')
    plt.title("AM")
    plt.xlabel("time")
    plt.ylabel("Amplitude")
    plt.grid(True)

    plt.subplot(4,1,3)
    plt.plot(t,fm_signal,color='g')
    plt.title("FM")
    plt.xlabel("time")
    plt.ylabel("Amplitude")
    plt.grid(True)

    plt.subplot(4,1,4)
    plt.plot(t,pm_signal,color='r')
    plt.title("PM")
    plt.xlabel("time")
    plt.ylabel("Amplitude")
    plt.grid(True)

    plt.tight_layout()
    plt.subplots_adjust(hspace=.8)
    plt.show()

fm=float(input("Enter FM:"))
fc=float(input("Enter FC"))
plot(fm,fc)
    


              

              
              
             
             
             
             
             
             
             
             
             