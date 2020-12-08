from graphics import *
from button import Button
import Connect4RulesScreen
import Connect4GameScreenfor1Player
import Connect4GameScreenfor2Players 
import Connect4TitleScreen
import time

def main():

    win = GraphWin('Connect 4', 500, 500)
    win.setBackground('Blue')

    titlebox = Rectangle(Point(150, 225), Point(325, 275))
    titlebox.setFill("Red")
    titlebox.setOutline("Red")
    titlebox.draw(win)

    titlecir = Circle(Point(325,250), 25)
    titlecir.setFill("Yellow")
    titlecir.setOutline("Yellow")
    titlecir.draw(win)

    label1 = Text(Point(225, 250), "Connect")
    label1.setSize(28)
    label1.setTextColor("Yellow")
    label1.draw(win)

    label2 = Text(Point(325, 250), "4")
    label2.setSize(28)
    label2.setTextColor("Red")
    label2.draw(win)

    win.getMouse()

    win.setBackground("Red")
    titlebox.setFill('Blue')
    label2.setFill('blue')

    win.getMouse()

    win.setBackground("Blue")
    titlebox.setFill('Red')
    label2.setFill('Red')

    win.getMouse()

    win.close()
    Connect4TitleScreen.main()
    
main()
