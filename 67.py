'''67'''

ka = False
while ka == False:
    try:
        print("What is the best number")
        num = int(input())
        if num == 67:
            ka = True
            print("67 " * 100000000)
        else:
            print("You stink")
    except ValueError:
        print("You stink")




