data=input("Enter 4 bit binary data:")

if not all(bit=='0' or bit=='1' for  bit in data):
    print("Invalid data")
else:
    count=data.count('1')
    if count%2==0:
        parity='0'
    else:
        parity='1'
        
    transmitted=data+parity
    print("TRansmitted data:",transmitted)
    received=input("Enter input data:")
    if not all(bit=='0' or bit=='1' for bit in received):
        print("invalid")
    else:
        r_count=received.count('1')
        if r_count%2==0:
            print("Accepted")
        else:
            print("Rejected")

        