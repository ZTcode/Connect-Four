from graphics import*
from button import Button
import Connect4RulesScreen
import Connect4GameScreenfor1Player
import Connect4GameScreenfor2Players 

def main():
    win = GraphWin("Connect 4", 500, 500)
    win.setBackground("White")

    #Title

    titlebox = Rectangle(Point(150, 25), Point(325, 75))
    titlebox.setFill("Red")
    titlebox.setOutline("Red")
    titlebox.draw(win)

    titlecir = Circle(Point(325,50), 25)
    titlecir.setFill("Yellow")
    titlecir.setOutline("Yellow")
    titlecir.draw(win)

    label1 = Text(Point(225, 50), "Connect")
    label1.setSize(28)
    label1.setTextColor("Yellow")
    label1.draw(win)

    label2 = Text(Point(325, 50), "4")
    label2.setSize(28)
    label2.setTextColor("Red")
    label2.draw(win)

    #Title screen objects

    cir = Circle(Point(75,50), 35)
    cir.setFill("Blue")
    cir.setOutline("Blue")
    cir.draw(win)

    cir2 = Circle(Point(425,50), 35)
    cir2.setFill("Red")
    cir2.setOutline("Red")
    cir2.draw(win)

    #Game options

    onePlayer = Button(win, Point(250,200), 75, 25, "")
    option = Text(Point(250, 200), "1 Player")
    option.setSize(16)
    option.setTextColor("Blue")
    option.draw(win)
    
    twoPlayer = Button(win, Point(250,250), 75, 25, "")
    option2 = Text(Point(250, 250), "2 Players")
    option2.setSize(16)
    option2.setTextColor("Blue")
    option2.draw(win)
    
    rules = Button(win, Point(250,300), 75, 25, "")
    option3 = Text(Point(250, 300), "Rules")
    option3.setSize(16)
    option3.setTextColor("Blue")
    option3.draw(win)

    leave = Button(win, Point(250,350), 75, 25, "")
    option4 = Text(Point(250, 350), "Exit")
    option4.setSize(16)
    option4.setTextColor("Blue")
    option4.draw(win)

    #Other texts

    label3 = Text(Point(250, 450), "Connect 4 (V 1.1)")
    label3.setSize(10)
    label3.setTextColor("Red")
    label3.draw(win)

    label4 = Text(Point(250, 475), "Created by Tyler Z. & Ciaran F.")
    label4.setSize(10)
    label4.setTextColor("Red")
    label4.draw(win)


    pt = win.getMouse()
    if onePlayer.clicked(pt):
        win.close()
        Connect4GameScreenfor1Player.main()
        
    if twoPlayer.clicked(pt):
        win.close()
        Connect4GameScreenfor2Players.main()
    
    if rules.clicked(pt):
        win.close()
        Connect4RulesScreen.main()
        
    if leave.clicked(pt):
        win.close()
        
    
