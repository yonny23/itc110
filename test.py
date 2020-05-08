from graphics import *

def main():

    win = GraphWin('Face', 200, 150) 
    win.setCoords(0, 0, 199, 149)

    head = Circle(Point(40,100), 25) 
    head.setFill("yellow")
    head.draw(win)

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2 = Line(Point(45, 105), Point(55, 105)) 
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = Oval(Point(30, 90), Point(50, 85))
    mouth.setFill("red")
    mouth.draw(win)

main()
