import numpy as np
import matplotlib.pyplot as plt

def plot(signals,titles):
    plt.figure(figsize=(8,8))
    for i in range(len(signals)):
        
        signal=signals[i]
        title=titles[i]

        plt.subplot(3,2,i+1)

        if title =="Polar RZ":
            plt.step([x/2 for x in range(len(signal))],signal,where='post' )
        else:
            plt.step(range(len(signal)),signal,where='post')

        plt.title(title)
        plt.ylim(-1.5,1.5)
        plt.grid(True)
    plt.tight_layout()
    plt.show()

def unipolar(bits):
    return[1 if bit==1 else 0 for bit in bits]
def polar_nrz_l(bits):
    return[1 if bit==1 else -1 for bit in bits]

def polar_nrz_i(bits):
    signal=[]
    level=-1
    for bit in bits:
        if bit==1:
            level*=-1
        signal.append(level)
    return signal
def polar_rz(bits):
    signal=[]
    for bit in bits:
        if bit==1:
            signal.extend([1,0])
        else:
            signal.extend([-1,0])
    signal.pop()
    return signal

binary=input("Enter binary number:")
bits=[int(b) for b in binary]

signals=[
    bits,
    unipolar(bits),
    polar_nrz_l(bits),
    polar_nrz_i(bits),
    polar_rz(bits)

]

titles=[
     "Binary input",
    "Unipolar",
    "Polar nrz-l",
    "Polar nrz-i",
    "Polar RZ"

]
plot(signals,titles)
            


