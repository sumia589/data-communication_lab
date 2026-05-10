# ---------------- SENDER ----------------

data = input("Enter data bits: ")

# check binary input
if not all(bit in "01" for bit in data):
    print("Invalid input")
    exit()

data = list(data)

# find parity bits
m = len(data)
r = 0

while (2 ** r) < (m + r + 1):
    r += 1

# create hamming structure
hamming = []
j = 0
k = 0

# insert parity + data bits
for i in range(1, m + r + 1):

    if i == 2 ** j:
        hamming.append(0)
        j += 1

    else:
        hamming.append(int(data[k]))
        k += 1

# calculate parity
for i in range(r):

    pos = 2 ** i
    count = 0

    for j in range(len(hamming)):

        if (j + 1) & pos:
            count += hamming[j]

    hamming[pos - 1] = 0 if count % 2 == 0 else 1

encoded = ''.join(map(str, hamming))

print("\nHamming Code:", encoded)


# ---------------- RECEIVER ----------------

received = input("\nEnter received code: ")



error_pos = 0

# check parity
for i in range(r):

    pos = 2 ** i
    count = 0

    for j in range(len(received)):

        if (j + 1) & pos:
            count += received[j]

    if count % 2 != 0:
        error_pos += pos

# result
if error_pos == 0:

    print("\nNo error detected")

else:

    print("\nError detected at position:", error_pos)

    # correct error
    received[error_pos - 1] ^= 1

    corrected = ''.join(map(str, received))

    print("Corrected code:", corrected)