import cs50

while True: 
    print("O hai ! How much change is owed? ")
    change = cs50.get_float()*100
    count = 0
    if change >= 0:
        break
while change >= 25:
        change -= 25
        count = count + 1
while change >= 10:
        change -= 10
        count = count + 1
while change >= 5:
        change -= 5
        count = count + 1 
while change >= 1:
        change -= 1
        count = count + 1  
print (count)