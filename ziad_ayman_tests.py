# Ziad Ayman Tests

# Tasks:-
# 1- Implement the algorithm & take care of objects in each iterate
# 2- Integrate with the UI design
from graphics import *
import time
win= GraphWin("sc3",950,540)
def text(sentence,x,y,color):
    #Text
    text=Text(Point(x,y),sentence)
    text.setStyle("bold")
    text.setTextColor(color)
    text.setSize(36)
    text.draw(win)
    #Underline
    line=Line(Point(x-100,y+50),Point(x+100,y+50))
    line.setWidth(5)
    line.setFill(color="#5C5C5C")
    line.draw(win)
def des(content,x,color):
    #Content
    text=Text(Point(x,205),content)
    text.setStyle("bold")
    text.setSize(20)
    text.setTextColor(color)
    text.draw(win)
    #Cell
    # cell=Circle(Point(x,270),25)
    # cell.setWidth(3)
    # cell.setOutline(color)
    # cell.setFill(color)
    # cell.draw(win)
    return text
#move function to des
def goto(obj,x):
    d=int(-obj.getAnchor().getX()+x.getCenter().getX())
    obj.move(d,0)
    # for i in range(d):
    #     obj.move(i,0)
#founded
def founded():
    tx=Text(Point(425,380),"element is Found!!") #ziad wael look here  <-----
    tx.setFace("arial")
    tx.setStyle("bold")
    tx.setSize(30)
    tx.draw(win)
    return tx
text("Searching...",480,100,color_rgb(0, 108, 250))
l=[]
data=[i*2 for i in range(1,11)]
dt2=[]
for i in range(10):
    # circles
    l.append(Circle(Point(125+i*80,270),35).draw(win))
    l[i].setWidth(3)
    l[i].setOutline("#1f1f1f")
    #array
    dt2.append(Text(Point(125+i*80,335),data[i]).draw(win))
    dt2[i].setStyle("bold")
    dt2[i].setSize(30)
    dt2[i].setTextColor("#1f1f1f")


#function to color
def Change_Colors(lst,color,start,end):
    for i in range(start,end+1):
        lst[i].setFill(color)
        # time.sleep(.01)
#colors list
colors=["#1f1f1f","#fa2d00","#02a114","#C7C7C7"]
#binary search
def Binary_Search(data,item,low=0,high=9):
    f=0
    #describtion        
    mid=low+(high-low)//2
    m_x=l[mid].getCenter()
    md=des("M",m_x.getX(),colors[0])
    l_x=l[low].getCenter()
    ld=des("L",l_x.getX(),colors[0])
    ld.move(0,-22)
    h_x=l[high].getCenter()
    hd=des("H",h_x.getX(),colors[0])
    hd.move(0,-42)
    mid=low+(high-low)//2

    while low<=high:
        
        l[mid].setFill(colors[1])
        time.sleep(1)
        if data[mid]==item :
            l[mid].setFill(colors[2])
            f=1
            break
        elif data[mid]<item:
            Change_Colors(l,colors[3],low,mid)
            low=mid+1

        else:
            Change_Colors(l,colors[3],mid,high)
            high=mid-1
        # time.sleep(1)
        mid=low+(high-low)//2
        goto(md,l[mid])
        goto(ld,l[low])
        goto(hd,l[high])
    # if f:
    #     return #found()
    # else:
    #     time.sleep(2)
    #     return #sc4()
    return f #we will f to deterimne which lable to show in sc4
flag=Binary_Search(data,20)
if flag:
    founded()
#Button
# ----------
try:
    win.getKey()
except:
    print()