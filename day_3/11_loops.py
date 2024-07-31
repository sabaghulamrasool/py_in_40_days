# loops

# while loop
x=0
while (x<9):
    
    print(x)
    x=x+1


# foor loop
for i in range(2,17):
    print(i)


# array
days=["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

for d in days:
    # if(d=="tue"):break       #loop stops
    # print(d)                 #prints mon, tue, wed, thu, fri
    if(d=="tue"):continue    #skip tue
    print(d)




