import random
gm = []
dogs = []
stv = 0
asdfg=True
lo=input ("Load? [y/n]: ")
while True==True:
    if lo == "y":
        break
    if lo == "n":
        break
    else:
        lo=input ("=====================================\nLoad a world? Write y (yes) or n (no): ")
if lo == "n":
    n = input("World name: ")
    w = input("Width: ")
    h = input("Height: ")
    while asdfg==True:
        try:
            w=int(w)
            h=int(h)
            asdfg=False
        except:
            print("Writ a number for width and height your world!")
            w = input("Width: ")
            h = input("Height: ")
            asdfg=True
    for udfuis in range(h):
        for iuasd in range(w):
            gm.append(" ")
    gm[0] = "◯"
    dog = 0
gysdz = 0
doopenfile=True
if lo == "y":
    file=input("File name: ")
    while doopenfile==True:
        try:
            n=file
            f = open(file)
            doopenfile=False
        except FileNotFoundError:
            print("============================================================\nFile not found, try full path with extension or create a world!")
            file=input("Write file name: ")
            doopenfile=True
    for line in f:
        gysdz = gysdz+1
        if gysdz==1:
            w=int(line)
        if gysdz==2:
            h=int(line)
        if gysdz==3:
            stv=int(line)
        if gysdz==4:
            dog=int(line)
        if gysdz==5:
            gm=list(line)
        if gysdz > 5:
            for jisef in range(dog):
                dogs.append(int(line))
        
bufer=" "
DAI=True
collision=False
step = ""
DM = "pos"
buffer = " "
thisdog = 0
dog=int(dog)
def prmap():
    forprint = ""
    a=0
    for i in range (h):
        for x in range (w):
            forprint = forprint + gm[a]
            a=a+1
        print(forprint)
        forprint = ""
def DebugM():
    if DM == "pos":
        print("Debug: Position="+str(stv))
    if DM == "ColOn":
        print ("Debug: Collision oned!")
    if DM == "ColOff":
        print ("Debug: Collision offed!")
    if DM == "DAON":
        print ("Debug: Dogs AI oned!")
    if DM == "DAOFF":
        print ("Debug: Dogs AI offed!")
    if DM == "worldsave":
        print ("Debug: Saved!")
prmap()
DebugM()
while True==True:
    DM = "pos"
    step = input("Command: ")
    if step == "d":
        if stv < w*h-1:
            if collision == True:
                if gm[stv+1] == " ":
                    gm[stv+1] = "◯"
                    gm[stv] = bufer
                    stv = stv+1
            else:
                gm[stv+1] = "◯"
                gm[stv] = bufer
                stv = stv+1
    if step == "a":
        if stv-1 > -1:
            if collision == True:
                if gm[stv-1]  == " ":
                    gm[stv-1] = "◯"
                    gm[stv] = bufer
                    stv = stv-1
            else:
                gm[stv-1] = "◯"
                gm[stv] = bufer
                stv = stv-1
    if step == "w":
        if stv > w-1:
            if collision == True:
                if gm[stv-w] == " ":
                    gm[stv-w] = "◯"
                    gm[stv+1] = bufer
                    stv = stv-w
            else:
                gm[stv-w] = "◯"
                gm[stv] = bufer
                stv = stv-w
    if step == "s":
        if stv < w*h-w:
            if collision == True:
                if gm[stv+w] == " ":
                    gm[stv+w] = "◯"
                    gm[stv] = bufer
                    stv = stv+w
            else:
                gm[stv+w] = "◯"
                gm[stv] = bufer
                stv = stv+w
    if step == "DogAI on":
        DAI = True
        DM = "DAON"
    if step == "DogAI off":
        DAI = False
        DM = "DAOFF"
    bufer=" "
    if step == "b":
        gm[stv] = "█"
        bufer="█"
    if step == "save":
        handle = open(n, "w")
        handle.write(str(w) + '\n')
        handle.write(str(h) + '\n')
        handle.write(str(stv) + '\n')
        handle.write(str(dog) + '\n')
        for savethis in range(w*h):
            handle.write(gm[savethis])
        handle.write('\n')
        for savethisa in range(dog):
            handle.write(str(dogs[savethisa]))
            handle.write("\n")
        handle.close()
        DM='worldsave'
    if step == "@":
        dogs.append(stv)
        gm[dogs[thisdog]] = "@"
        dog=dog+1
    if step == "exit":
        break
    if step == "collision on":
        collision=True
        DM="ColOn"
    if step == "collision off":
        collision=False
        DM="ColOff"
    try:
        for thisdog in range(dog):
            if DAI == True:
                randstep=random.randint(1, 4)
                if randstep == 1:
                    if dogs[thisdog] < w*h-1:
                        if gm[dogs[thisdog]+1] == " ":
                            gm[dogs[thisdog]+1] = "@"
                            if gm[dogs[thisdog]] == "@":
                                gm[dogs[thisdog]] = " "
                            dogs[thisdog] = dogs[thisdog]+1
                if randstep == 2:
                    if dogs[thisdog-1] > 0:
                        if gm[dogs[thisdog]-1] == " ":
                            gm[dogs[thisdog]-1] = "@"
                            if gm[dogs[thisdog]] == "@":
                                gm[dogs[thisdog]] = " "
                            dogs[thisdog] = dogs[thisdog]-1
                if randstep == 3:
                    if dogs[thisdog] > w-1:
                        if gm[dogs[thisdog]-w] == " ":
                            gm[dogs[thisdog]-w] = "@"
                            if gm[dogs[thisdog]] == "@":
                                gm[dogs[thisdog]] = " "
                            dogs[thisdog] = dogs[thisdog]-w
                if randstep == 4:
                    if dogs[thisdog] < w*h-w:
                        if gm[dogs[thisdog]+w] == " ":
                            gm[dogs[thisdog]+w] = "@"
                            if gm[dogs[thisdog]] == "@":
                                gm[dogs[thisdog]] = " "
                            dogs[thisdog] = dogs[thisdog]+w
            if stv == dogs[thisdog]:
                    dogs.remove(stv)
                    dog=dog-1
    except:
        print("Dog Error!")
    prmap()
    DebugM()