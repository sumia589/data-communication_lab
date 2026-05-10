import matplotlib.pyplot as plt


# ---------- Plot Function ----------
def plot_signal(signals, titles):

    plt.figure(figsize=(14,10))

    for i in range(len(signals)):

        signal = signals[i]
        title = titles[i]

        plt.subplot(3,3,i+1)

        if title == "Polar RZ":
            plt.step([x/2 for x in range(len(signal))],
                     signal,
                     where='post')
        else:
            plt.step(range(len(signal)),
                     signal,
                     where='post')

        plt.title(title)
        plt.ylim(-1.5,1.5)
        plt.grid(True)

    plt.tight_layout()
    plt.show()


# ---------- Unipolar ----------
def unipolar(bits):
    return [1 if bit == 1 else 0 for bit in bits]


# ---------- NRZ-L ----------
def polar_nrz_l(bits):
    return [1 if bit == 1 else -1 for bit in bits]


# ---------- NRZ-I ----------
def polar_nrz_i(bits):

    signal = []
    level = -1

    for bit in bits:
        if bit == 1:
            level = -level
        signal.append(level)

    return signal


# ---------- Polar RZ ----------
def polar_rz(bits):

    signal = []

    for bit in bits:
        if bit == 1:
            signal.extend([1, 0])
        else:
            signal.extend([-1, 0])

    return signal


# ---------- Manchester ----------
def manchester(bits):

    signal = []

    for bit in bits:
        if bit == 1:
            signal.extend([1, -1])
        else:
            signal.extend([-1, 1])

    return signal


# ---------- Differential Manchester ----------
def diff_manchester(bits):

    signal = []
    level = 1

    for bit in bits:
        if bit == 0:
            level = -level
        signal.extend([level, -level])

    return signal


# ---------- AMI ----------
def ami(bits):

    signal = []
    level = 1

    for bit in bits:
        if bit == 1:
            signal.append(level)
            level = -level
        else:
            signal.append(0)

    return signal


# ---------- Input ----------
binary = input("Enter binary data: ")
bits = [int(b) for b in binary]


# ---------- Signals ----------
signals = [
    unipolar(bits),
    polar_nrz_l(bits),
    polar_nrz_i(bits),
    polar_rz(bits),
    manchester(bits),
    diff_manchester(bits),
    ami(bits)
]


titles = [
    "Unipolar",
    "Polar NRZ-L",
    "Polar NRZ-I",
    "Polar RZ",
    "Manchester",
    "Differential Manchester",
    "AMI"
]


# ---------- Plot ----------
plot_signal(signals, titles)