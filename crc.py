# Checksum Error Detection using 1's Complement

data = []

# Input
n = int(input("Enter number of words: "))
bits = int(input("Enter bits per word: "))

print("\nEnter binary words:")

for i in range(n):
    word = input(f"Word {i+1}: ")

    # Validation
    if len(word) != bits or not all(b in "01" for b in word):
        print("Invalid Input")
        exit()

    data.append(word)


# Function for 1's complement addition
def add(a, b):

    # Binary to decimal addition
    total = int(a, 2) + int(b, 2)

    # Carry handling
    if total >= 2 ** bits:
        total = (total % (2 ** bits)) + 1

    # Convert back to binary
    return format(total, f'0{bits}b')


# Sender Side
s = "0" * bits

for word in data:
    s = add(s, word)

print("\nSum:", s)

# Generate checksum (1's complement)
checksum = ""

for bit in s:
    if bit == "0":
        checksum += "1"
    else:
        checksum += "0"

print("Checksum:", checksum)


# Transmitted Data
print("\nTransmitted Data:")

for word in data:
    print(word)

print(checksum)


# Receiver Side
received = data + [checksum]

result = "0" * bits

for word in received:
    result = add(result, word)

print("\nReceiver Sum:", result)


# Final Checking
if result == "1" * bits:
    print("No Error Detected")
else:
    print("Error Detected")