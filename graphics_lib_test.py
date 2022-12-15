from graphics import *
import turtle
import time
win= GraphWin("test",500,500)
l=[]

data=[i for i in range(20)]
dt2=[]
for i in range(20):
    l.append(Circle(Point(150+i*20,250),10).draw(win))
    dt2.append(Text(Point(150+i*20,250),data[i]).draw(win))
print(l)
def cha(x,y,i):
    # dt2[i].undraw()
    a=x.getCenter()
    p1=a.getX()
    b=y.getCenter()
    p2=b.getX()
    d1=p1-p2
    d2=p2-p1
    x.move(d2,0)
    time.sleep(1)
    y.move(d1,0)
    # dt2[i].draw(win)

def win2():
    # wiin=GraphWin("ts2",200,100)
    wiin=turtle.Screen()
    
    # turtle.done()
    # wiin.bye()
    return wiin
l[2].setFill("red")
r=l[2].getCenter()
# rr,rrr=r
l[3].setFill("green")
# print()
a=win.getMouse()
# l[2],l[3]=l[3],l[2]
if a:
    cha(l[2],l[1],2)
    # win2()

win.getKey()