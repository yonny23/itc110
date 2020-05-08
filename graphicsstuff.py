#import graphics
from graphics import *

def main():
    win =GraphWin("First graphics", 600,600)
    point=Point(200,200)
    circ=Circle(point, 100)
    circ.setFill('Red')
    circ.draw(win)
    #rec=Rectangle(425, 525)
    #rec.draw(win)
    #win.getKey()

    circle2 = circ.clone()
    circle2.move(150,0)
    circle2.draw(win)
main()
