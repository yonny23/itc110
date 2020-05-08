#Here i am drawing a face

from graphics import *

def main():
     win = GraphWin('Face', 900, 900) 
     win.setBackground("white")

     circle = Circle(Point(300, 300), 200)
     circle.draw(win)
     circle.setOutline("red")
     circle.setWidth(2)
     circle.setFill("yellow")

     leftEye = Circle(Point(400, 200), 30)
     leftEye.setOutline("purple")
     leftEye.setWidth(6)
     rightEye = leftEye.clone()
     rightEye.move(-200, 0)
     leftEye.draw(win)
     rightEye.draw(win)

     mouth = Oval(Point(430, 475), Point(200, 400)) # set corners of bounding box
     mouth.setFill("white")
     mouth.draw(win)
     
main()
