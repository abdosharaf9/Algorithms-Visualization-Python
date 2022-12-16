# The main project file

##########################################################
#               Don't edit this now !!!                  #
##########################################################

from graphics import *
from time import *

win=GraphWin("Infinity Loop Team - Binary Search Algorithm Visualization",960,540)
win.setBackground(color="#D4D4D4")

# Globals
screen1 = []
screen2 = []
screenInput = []
screen3 = []
dess = []
screen4 = []
screen5 = []
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


##########################################################
#                     Objects functions                  #
##########################################################

# Text Object
def text(sentence,x,y,color, size, w = win):
    #Text
    text=Text(Point(x,y),sentence)
    text.setStyle("bold")
    text.setTextColor(color)
    text.setSize(size)
    text.draw(w)
    #Underline
    line=Line(Point(x-100,y+50),Point(x+100,y+50))
    line.setWidth(5)
    line.setFill(color="#5C5C5C")
    line.draw(w)
    return text, line

# Button Object
def button(purpose,x,y,color, w = win):
    #Button
    button=Polygon(Point(x-100,y+30),Point(x+100,y+30),Point(x+100,y-30),Point(x-100,y-30))
    button.setOutline(color="#D5D5D5")
    button.setFill(color="#C7C7C7")
    button.setWidth(2)
    button.draw(w)
    #Inside Text
    text=Text(Point(x,y),purpose)
    text.setStyle("bold")
    text.setTextColor(color)
    text.setSize(30)
    text.draw(w)
    return button, text

# Input Box Object
def input(x,y):
    input=Entry(Point(x,y),3)
    input.setStyle("bold")
    input.setTextColor("#1f1f1f")
    input.setFill(color="#C7C7C7")
    input.setSize(25)
    input.draw(win)
    #This Is Get Input Function!!!! "Edit This!!!"
    # searchnumber=input.getText()
    return input

# Array Cell Object
def cell(content,x,color):
    #Cell
    cell=Circle(Point(x,270),35)
    cell.setWidth(3)
    cell.setOutline(color)
    cell.draw(win)
    #Content
    text=Text(Point(x,335),content)
    text.setStyle("bold")
    text.setSize(30)
    text.setTextColor(color)
    text.draw(win)

    return cell, text

# Upper Array Description (L,R,M) Object
def des(content,x,color):
    #Content
    text=Text(Point(x,205),content)
    text.setStyle("bold")
    text.setSize(30)
    text.setTextColor(color)
    text.draw(win)
    #Cell
    cell=Circle(Point(x,270),25)
    cell.setWidth(3)
    cell.setOutline(color)
    cell.setFill(color)
    cell.draw(win)

    return text, cell


##########################################################
#                     Screens functions                  #
##########################################################

#Screen 1
def sc1():
    global screen1
    t1=text("Welcome!",480,150,color_rgb(0, 108, 250), 36)
    b1=button("Start",480,325,color_rgb(0, 108, 250))
    b2=button("Exit",480,390,color_rgb(250, 45, 0))
    b3=button("Credits",125,490,color_rgb(31, 31, 31))
    #Variable Object List
    screen1 = [t1, b1, b2, b3]

#Screen 2
def sc2():
    global screen2, screenInput
    t1=text("Please Enter Number To Search For",480,150,color_rgb(0, 108, 250), 36)
    i1=input(480,270)
    b1=button("Confirm",480,350,color_rgb(0, 108, 250))
    b2=button("Exit",480,415,color_rgb(250, 45, 0))
    b3=button("Credits",125,490,color_rgb(31, 31, 31))
    #Variable Object List
    screen2 = [t1, b1, b2, b3]
    screenInput = [i1]

#Screen 3
def sc3():
    global screen3, dess
    t1=text("Searching...",480,100,color_rgb(0, 108, 250), 36)
    c0=cell(1,125,color=("#1f1f1f"))
    c1=cell(2,205,color=("#1f1f1f"))
    c2=cell(3,285,color=("#1f1f1f"))
    c3=cell(4,365,color=("#1f1f1f"))
    c4=cell(5,445,color=("#1f1f1f"))
    c5=cell(6,525,color=("#1f1f1f"))
    c6=cell(7,605,color=("#1f1f1f"))
    c7=cell(8,685,color=("#1f1f1f"))
    c8=cell(9,765,color=("#1f1f1f"))
    c9=cell(10,845,color=("#1f1f1f"))
    d1=des("L",125,color=("#1f1f1f"))
    d2=des("M",445,color=("#D4D4D4"))
    d3=des("R",845,color=("#1f1f1f"))
    #Variable Object List
    screen3 = [t1, c0, c1, c2, c3, c4, c5, c6, c7, c8, c9]
    dess = [d1, d2, d3]

#Screen 4
def sc4():
    global screen4
    t1=text("Your Number Isn't In Array",480,150,color_rgb(250, 45, 0), 36)
    b1=button("Start Over",480,325,color_rgb(0, 108, 250))
    b2=button("Exit",480,390,color_rgb(250, 45, 0))
    b3=button("Credits",125,490,color_rgb(31, 31, 31))
    #Variable Object List
    screen4 = [t1, b1, b2, b3]

#Screen 5
def sc5(w: GraphWin):
    global screen5
    t0=text("Omar khairy ElEtrby",175,125,color_rgb(0, 108, 250),20, w)
    t1=text("Amr Mohamed Fawzy",175,225,color_rgb(0, 108, 250),20, w)
    t2=text("Mahmoud Ibrahim Ewida",175,325,color_rgb(0, 108, 250),20, w)
    t3=text("Abd ElHamed Ashraf Sharaf",480,75,color_rgb(0, 108, 250),20, w)
    t4=text("Asem Ibrahim Gadu",480,175,color_rgb(0, 108, 250),20, w)
    t5=text("Asem Reda ElEtrby",480,275,color_rgb(0, 108, 250),20, w)
    t6=text("Ziad Wael ElGammal",480,400,color_rgb(0, 108, 250),20, w)
    t7=text("Ziad Ayman Ragab",785,125,color_rgb(0, 108, 250),20, w)
    t8=text("Mahmoud Reda Ebid",785,225,color_rgb(0, 108, 250),20, w)
    t9=text("Youssef Hassan Kamal",785,325,color_rgb(0, 108, 250),20, w)
    t10=text("Infinity Loop Team",815,475,color_rgb(31, 31, 31),20, w)
    b1=button("Exit",125,490,color_rgb(250, 45, 0), w)
    #Variable Object List
    screen5 = [t0,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,b1]

# Handle screen 5 clicks
def screen5Clicks():
    # Show credits screen & Handle its clicks
    try:
        win2 = GraphWin("Infinity Loop Team - Binary Search Algorithm Visualization",960,540)
        win2.setBackground(color="#D4D4D4")
        sc5(win2)
        point2 = win2.getMouse()
        while True:
            if point2.getX() >= 25 and point2.getX() <= 225 and point2.getY() >= 460 and point2.getY() <= 520:
                break
            else:
                point2 = win2.getMouse()
        win2.close()
    except:
        print("Window 2 is closed")


##########################################################
#                     Main Program                       #
##########################################################

try:
    while True:
        sc1()
        takeInput = False
        beginSearch = False
        openScreen4 = False
        founded = False
        exitProgram = False
        startOver = False
        searchKey = -1
        point = win.getMouse()

        # Handle screen 1 clicks
        while True:
            # Credits button
            if point.getX() >= 25 and point.getX() <= 225 and point.getY() >= 460 and point.getY() <= 520:
                screen5Clicks()
                point = win.getMouse()

            # Start button
            elif point.getX() >= 380 and point.getX() <= 580 and point.getY() >= 295 and point.getY() <= 355:
                # remove screen 1 & Go to screen 2 to take input
                takeInput = True
                for object in screen1:
                    object[0].undraw()
                    object[1].undraw()
                break

            # Exit button
            elif point.getX() >= 380 and point.getX() <= 580 and point.getY() >= 360 and point.getY() <= 420:
                exitProgram = True
                break

            else:
                point = win.getMouse()

        # If the user clicked exit in screen 1
        if exitProgram:
            break

        # Handle screen 2 clicks if the user went to it
        if takeInput:
            sc2()

            point = win.getMouse()
            while True:
                # Credits button
                if point.getX() >= 25 and point.getX() <= 225 and point.getY() >= 460 and point.getY() <= 520:
                    # Show credits screen & Handle its clicks
                    screen5Clicks()
                    point = win.getMouse()

                # Confirm button
                elif point.getX() >= 380 and point.getX() <= 580 and point.getY() >= 320 and point.getY() <= 380:
                    # Take input, and go to screen 3
                    if len(screenInput[0].getText()) != 0:
                        for object in screen2:
                            object[0].undraw()
                            object[1].undraw()
                        searchKey = int(screenInput[0].getText())
                        screenInput[0].undraw()
                        beginSearch = True
                        break
                    else:
                        point = win.getMouse()

                # Exit button
                elif point.getX() >= 380 and point.getX() <= 580 and point.getY() >= 385 and point.getY() <= 445:
                    exitProgram = True
                    break

                else:
                    point = win.getMouse()

        # If the user clicked exit in screen 2
        if exitProgram:
            break

        # Handle screen 3 clicks if the user went to it
        if beginSearch:
            sc3()
            start = 0
            end = 9

            while start <= end:

                mid = start + (end - start)//2
                # Draw mid border
                dess[1][0].undraw()
                dess[1][1].undraw()
                dess[1] = des("M", 125 + (mid * 80),color=("#fa2d00"))

                if arr[mid] == searchKey:
                    sleep(1)
                    founded = True
                    # Draw mid border when the key is found
                    dess[1][0].undraw()
                    dess[1][1].undraw()
                    dess[1] = des("M", 125 + (mid * 80),color=("#02a114"))

                    # Change screen 3 title when the key is found
                    screen3[0][0].undraw()
                    screen3[0][1].undraw()
                    screen3[0] = text("Your number is found!",480,100,color_rgb(2, 161, 20), 36)
                    break

                elif arr[mid] > searchKey:
                    sleep(1)
                    end = mid - 1
                    # Draw mid border when the key is found
                    dess[2][0].undraw()
                    dess[2][1].undraw()
                    dess[2] = des("R", 125 + (end * 80),color=("#1f1f1f"))

                elif arr[mid] < searchKey:
                    sleep(1)
                    start = mid + 1
                    # Draw mid border when the key is found
                    dess[0][0].undraw()
                    dess[0][1].undraw()
                    dess[0] = des("L", 125 + (start * 80),color=("#1f1f1f"))
            
            if not founded:
                openScreen4 = True

                for object in screen3:
                    object[0].undraw()
                    object[1].undraw()
                
                for object in dess:
                    object[0].undraw()
                    object[1].undraw()
            
            else:
                b1=button("Exit",480,415,color_rgb(250, 45, 0))
                b2=button("Credits",125,490,color_rgb(31, 31, 31))

                # Show the buttons & Handle the clicks
                point = win.getMouse()
                while True:
                    # Exit button
                    if point.getX() >= 380 and point.getX() <= 580 and point.getY() >= 285 and point.getY() <= 445:
                        exitProgram = True
                        break

                    # Credits button
                    if point.getX() >= 25 and point.getX() <= 225 and point.getY() >= 460 and point.getY() <= 520:
                        # Show credits screen & Handle its clicks
                        screen5Clicks()
                        point = win.getMouse()

        # If the user clicked exit in screen 3
        if exitProgram:
            break

        # Handle screen 4 clicks if the user went to it
        if openScreen4:
            sc4()
            point = win.getMouse()

            while True:
                # Credits button
                if point.getX() >= 25 and point.getX() <= 225 and point.getY() >= 460 and point.getY() <= 520:
                    # Show credits screen & Handle its clicks
                    screen5Clicks()
                    point = win.getMouse()
                
                # Try again button
                elif point.getX() >= 380 and point.getX() <= 580 and point.getY() >= 295 and point.getY() <= 355:
                    startOver = True
                    break
                
                # Exit button
                elif point.getX() >= 380 and point.getX() <= 580 and point.getY() >= 360 and point.getY() <= 420:
                    exitProgram = True
                    break
                
                else:
                    point = win.getMouse()
            
            if exitProgram:
                break

            if startOver:
                for object in screen4:
                    object[0].undraw()
                    object[1].undraw()
                continue
except:
    print("The program is closed")
