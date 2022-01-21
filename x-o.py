# can use 1D list of int
canvas = [  [],[],[],
            [],[],[],
            [],[],[]]
xWin = [['x'],['x'],['x']]
oWin = [['y'],['y'],['y']]

def showCanvas():
    print(canvas[0:3])
    print(canvas[3:6])
    print(canvas[6:9])

def addXY(xPos,oPos):
    try:
        if xPos in range(0,9) and oPos is None:
            if canvas[xPos] == []:
                canvas[xPos] = ['x']
            else:
                print("can't add x. Position has owner") 
        elif oPos in range(0,9) and xPos is None:
            if canvas[oPos] == []:
                canvas[oPos] = ['o']
            else:
                print("can't add y. Position has owner") 
        else:
            print("out of field")
    except Exception as e:
        print(e)
    showCanvas()


def checkwin():
    c = 0
    global canvas
    if canvas[0:3] == xWin or canvas[3:6] == xWin or canvas[6:9] == xWin or canvas[0:9:4] == xWin or canvas[2:8:2] == xWin:
        print("x win")
        c = 1
    elif canvas[0:3] == oWin or canvas[3:6] == oWin or canvas[6:9] == oWin or canvas[0:9:4] == oWin or canvas[2:8:2] == oWin:
        print("o win")
        c = 1
    if c == 1:
        c = 0
        canvas = [  [],[],[],
                    [],[],[],
                    [],[],[]]
        return int(input("Do you want to continue (1-yes 0-no) : "))

while True:
    try:
        x = int(input("Please enter x position (0-8) : "))
        addXY(x,None)
        if checkwin() == 0:
            break
        y = int(input("Please enter y position (0-8) : "))
        addXY(None,y)
        if checkwin() == 0:
            break
    except Exception as e:
        print(e)




