data = []

rows = int(input("Enter number of data rows: "))
cols = int(input("Enter number of bits in row: "))

print("\nEnter binary data rows:")

# INPUT
for i in range(rows):
    row = input(f"Row {i+1}: ")

    if len(row) != cols or not all(bit in "01" for bit in row):
        print("Invalid")
        exit()

    data.append(row)

# LRC generation
lrc = ""

for col in range(cols):
    count = 0

    for row in range(rows):
        if data[row][col] == '1':
            count += 1

    if count % 2 == 0:
        lrc += '0'
    else:
        lrc += '1'

print("\nLRC bits:", lrc)

print("\nTransmitted data:")
for row in data:
    print(row)

print(lrc)

# RECEIVER SIDE
received_data = data + [lrc]
error = False

for col in range(cols):
    count = 0

    for row in range(rows + 1):
        if received_data[row][col] == '1':
            count += 1

    if count % 2 != 0:
        error = True
        break

if error == False:
    print("\nAccepted")
else:
    print("\nRejected")