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

# create empty hamming code
hamming = []
j = 0
k = 0

# insert parity & data bits
for i in range(1, m + r + 1):
    if i == 2 ** j:
        hamming.append(0)   # parity bit
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
            if hamming[j] == 1:
                count += 1

    hamming[pos - 1] = 0 if count % 2 == 0 else 1

# final code
encoded = ''.join(map(str, hamming))
print("Hamming code:", encoded)


# ---------------- RECEIVER ----------------
received = input("Enter received code: ")

if len(received) != len(encoded):
    print("Invalid received data")
    exit()

received = list(map(int, received))
error_pos = 0

# detect error
for i in range(r):
    pos = 2 ** i
    count = 0

    for j in range(len(received)):
        if (j + 1) & pos:
            if received[j] == 1:
                count += 1

    if count % 2 != 0:
        error_pos += pos

if error_pos == 0:
    print("No error detected")
else:
    print("Error at position:", error_pos)

    # correction
    received[error_pos - 1] ^= 1

    print("Corrected code:", ''.join(map(str, received)))