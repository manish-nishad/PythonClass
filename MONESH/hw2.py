#for loop 
number=[10]
for num in range(10):
    print(num)


#while loop
count=0
while count < 15 :  #condition
    print(count)    
    count +=1 #increment 


#nested loops
counts=5
for i in range(counts):
    for j in range(i+1):
        print(i+j,end="")
        print()