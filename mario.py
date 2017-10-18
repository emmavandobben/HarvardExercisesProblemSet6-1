import cs50

while True: 
    print("Height: ", end="")
    height = cs50.get_int()
    if height >= 0 and height < 24:
        break
for actualHeight in range(height): 
        print(" " * (height-1-actualHeight) , end="")
        print("#" * (2+actualHeight) , end="")
        print("")