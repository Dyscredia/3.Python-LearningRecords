y = 1
while y <= 9:
    x = 1
    while x <= y:
        print(y , "*" , x , "=" , y*x , end="\t")
        x += 1
    print()
    y += 1