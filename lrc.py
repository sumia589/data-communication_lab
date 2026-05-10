data=[]
rows=int(input("Enter number of data rows:"))
cols=int(input("Enter number of bits in row"))
print("\nEnrer binary data row:")

for i in range(rows):
    row=input(f"Row{i+1}:")
    if len(row)!=cols or not all(bit in "10" for bit in row):
        print("Invalid")
        exit()
    data.append(row)


lrc=[]
for col in range(cols):
    count=0
    for row in range(rows):
            if data[row][col]=='1':
             count+=1
    if count%2==0:
           lrc+='0'
    else:
           lrc+='1'
print("LRC bits:",lrc)
print("TRransmitted data:")
for row in data:
     print(row)
print(lrc)


received_data=data+[lrc]
error=False
for col in range(cols):
     count=0
     for row in range(rows+1):
          if received_data[row][col]=='1':
               count+=1
     if count%2!=0:
          error=True
          break
     

if error==False:
     print("Accepted")
else:
     print("Rejected")
     
        
    
