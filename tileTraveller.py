
x = 1
y = 1
vinnutala = [x,y]


while True:
    if vinnutala == [1,1]:
        print("You can travel: (N)orth")
        innsleginn = input("Direction: ")
        if innsleginn == "N":
            vinnutala[1] += 1
        if innsleginn == "S":
            vinnutala[1] += 0
            print("Not a valid direction!")
        if innsleginn == "E":
            print("Not a valid direction!")
            vinnutala[0] += 0
        elif innsleginn == "W":
            print("Not a valid direction!")
            vinnutala[0] += 0
    elif vinnutala == [1,2]:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        innsleginn = input("Direction: ")
        if innsleginn == "N":
            vinnutala[1] += 1
        if innsleginn == "S":
            vinnutala[1] += -1
        if innsleginn == "E":
            vinnutala[0] += 1
        elif innsleginn == "W":
            print("Not a valid direction!")
            vinnutala[0] += 0
    elif vinnutala == [1,3]:
        print("You can travel: (E)ast or (S)outh.")
        innsleginn = input("Direction: ")
        if innsleginn == "N":
            print("Not a valid direction!")
            vinnutala[1] += 0
        if innsleginn == "S":
            vinnutala[1] += -1
        if innsleginn == "E":
            vinnutala[0] += +1
        elif innsleginn == "W":
            print("Not a valid direction!")
            vinnutala[0] += 0        
    elif vinnutala == [2,1]:
        print("You can travel: (E)ast or (W)est.")
        innsleginn = input("Direction: ")
        if innsleginn == "N":
            vinnutala[1] += 1
        if innsleginn == "S":
            print("Not a valid direction!")
            vinnutala[1] += 0
        if innsleginn == "E":
            print("Not a valid direction!")
            vinnutala[0] += 0
        elif innsleginn == "W":
            vinnutala[0] += 0
            print("Not a valid direction!")
    elif vinnutala == [2,2]:
        print("You can travel: (E)ast or (S)outh.")
        innsleginn = input("Direction: ")
        if innsleginn == "N":
            vinnutala[1] += 0
            print("Not a valid direction!")
        if innsleginn == "S":
            vinnutala[1] += -1
        if innsleginn == "E":
            print("Not a valid direction!")
            vinnutala[0] += 0
        elif innsleginn == "W":
            vinnutala[0] += -1
    elif vinnutala == [2,3]:
        print("You can travel: (E)ast  or (W)est.")
        innsleginn = input("Direction: ")
        if innsleginn == "N":
            print("Not a valid direction!")
            vinnutala[1] += 0
        if innsleginn == "S":
            print("Not a valid direction!")
            vinnutala[1] += 0
        if innsleginn == "E":
            vinnutala[0] += +1
        elif innsleginn == "W":
            vinnutala[0] += -1
    elif vinnutala == [3,1]:
        print("Victory!")
        break
    elif vinnutala == [3,2]:
        print("You can travel: (N)orth or (S)outh.")
        innsleginn = input("Direction: ")
        if innsleginn == "N":
            vinnutala[1] += 1
        if innsleginn == "S":
            vinnutala[1] += 1
        if innsleginn == "E":
            vinnutala[0] += 0
            print("Not a valid direction!")
        elif innsleginn == "W":
            vinnutala[0] += -1
    elif vinnutala == [3,3]:
        print("You can travel: (S)outh or (W)est.")
        innsleginn = input("Direction: ")
        if innsleginn == "N":
            print("Not a valid direction!")
            vinnutala[1] += 0
        if innsleginn == "S":
            vinnutala[1] += -1
        if innsleginn == "E":
            print("Not a valid direction!")
            vinnutala[0] += 0
        elif innsleginn == "W":
            vinnutala[0] += 1
    #print(vinnutala)

