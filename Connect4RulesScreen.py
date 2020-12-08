from graphics import*
from button import Button
import Connect4TitleScreen

def main():
    win = GraphWin("Connect 4", 500,500)
    win.setBackground("White")

    #Game Board
  
    mainbox = Rectangle(Point(105, 175), Point(395, 425))
    mainbox.setFill('yellow')
    mainbox.setOutline("Red")
    mainbox.draw(win)

    base = Rectangle(Point(50,426), Point(450, 450))
    base.setFill("Blue")
    base.draw(win)

    sidebase1 = Rectangle(Point(75, 275), Point(90, 425))
    sidebase1.setFill("Blue")
    sidebase1.setOutline("Blue")
    sidebase1.draw(win)

    sidebase2 = Rectangle(Point(410, 275), Point(425, 425))
    sidebase2.setFill("Blue")
    sidebase2.setOutline("Blue")
    sidebase2.draw(win)

    sideconnect1 = Rectangle(Point(90, 275), Point(105,295))
    sideconnect1.setFill("Blue")
    sideconnect1.setOutline("Blue")
    sideconnect1.draw(win)

    sideconnect2 = Rectangle(Point(395, 275), Point(410, 295))
    sideconnect2.setFill("Blue")
    sideconnect2.setOutline("Blue")
    sideconnect2.draw(win)


    #Row 1

    cir1 = Circle(Point(130, 200), 15)
    cir1.setFill("White")
    cir1.draw(win)

    cir2 = Circle(Point(170, 200), 15)
    cir2.setFill("White")
    cir2.draw(win)

    cir3 = Circle(Point(210, 200), 15)
    cir3.setFill("White")
    cir3.draw(win)

    cir4 = Circle(Point(250, 200), 15)
    cir4.setFill("White")
    cir4.draw(win)

    cir5 = Circle(Point(290, 200), 15)
    cir5.setFill("White")
    cir5.draw(win)

    cir6 = Circle(Point(330, 200), 15)
    cir6.setFill("White")
    cir6.draw(win)

    cir7 = Circle(Point(370, 200), 15)
    cir7.setFill("White")
    cir7.draw(win)

    #Row 2

    cir8 = Circle(Point(130, 240), 15)
    cir8.setFill("White")
    cir8.draw(win)

    cir9 = Circle(Point(170, 240), 15)
    cir9.setFill("White")
    cir9.draw(win)

    cir10 = Circle(Point(210, 240), 15)
    cir10.setFill("White")
    cir10.draw(win)

    cir11 = Circle(Point(250, 240), 15)
    cir11.setFill("White")
    cir11.draw(win)

    cir12 = Circle(Point(290, 240), 15)
    cir12.setFill("White")
    cir12.draw(win)

    cir13 = Circle(Point(330, 240), 15)
    cir13.setFill("White")
    cir13.draw(win)

    cir14 = Circle(Point(370, 240), 15)
    cir14.setFill("White")
    cir14.draw(win)

    #Row 3

    cir15 = Circle(Point(130, 280), 15)
    cir15.setFill("White")
    cir15.draw(win)

    cir16 = Circle(Point(170, 280), 15)
    cir16.setFill("White")
    cir16.draw(win)

    cir17 = Circle(Point(210, 280), 15)
    cir17.setFill("White")
    cir17.draw(win)

    cir18 = Circle(Point(250, 280), 15)
    cir18.setFill("White")
    cir18.draw(win)

    cir19 = Circle(Point(290, 280), 15)
    cir19.setFill("White")
    cir19.draw(win)

    cir20 = Circle(Point(330, 280), 15)
    cir20.setFill("White")
    cir20.draw(win)

    cir21 = Circle(Point(370, 280), 15)
    cir21.setFill("White")
    cir21.draw(win)

    #Row 4

    cir22 = Circle(Point(130, 320), 15)
    cir22.setFill("White")
    cir22.draw(win)

    cir23 = Circle(Point(170, 320), 15)
    cir23.setFill("White")
    cir23.draw(win)

    cir24 = Circle(Point(210, 320), 15)
    cir24.setFill("White")
    cir24.draw(win)

    cir25 = Circle(Point(250, 320), 15)
    cir25.setFill("White")
    cir25.draw(win)

    cir26 = Circle(Point(290, 320), 15)
    cir26.setFill("White")
    cir26.draw(win)

    cir27 = Circle(Point(330, 320), 15)
    cir27.setFill("White")
    cir27.draw(win)

    cir28 = Circle(Point(370, 320), 15)
    cir28.setFill("White")
    cir28.draw(win)

    #Row 5

    cir29 = Circle(Point(130, 360), 15)
    cir29.setFill("White")
    cir29.draw(win)

    cir30 = Circle(Point(170, 360), 15)
    cir30.setFill("White")
    cir30.draw(win)

    cir31 = Circle(Point(210, 360), 15)
    cir31.setFill("White")
    cir31.draw(win)

    cir32 = Circle(Point(250, 360), 15)
    cir32.setFill("White")
    cir32.draw(win)

    cir33 = Circle(Point(290, 360), 15)
    cir33.setFill("White")
    cir33.draw(win)

    cir34 = Circle(Point(330, 360), 15)
    cir34.setFill("White")
    cir34.draw(win)

    cir35 = Circle(Point(370, 360), 15)
    cir35.setFill("White")
    cir35.draw(win)

    #Row 6

    cir36 = Circle(Point(130, 400), 15)
    cir36.setFill("White")
    cir36.draw(win)

    cir37 = Circle(Point(170, 400), 15)
    cir37.setFill("White")
    cir37.draw(win)

    cir38 = Circle(Point(210, 400), 15)
    cir38.setFill("White")
    cir38.draw(win)

    cir39 = Circle(Point(250, 400), 15)
    cir39.setFill("White")
    cir39.draw(win)

    cir40 = Circle(Point(290, 400), 15)
    cir40.setFill("White")
    cir40.draw(win)

    cir41 = Circle(Point(330, 400), 15)
    cir41.setFill("White")
    cir41.draw(win)

    cir42 = Circle(Point(370, 400), 15)
    cir42.setFill("White")
    cir42.draw(win)


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

    #Other Objects to go with game background

    leftcir = Circle(Point(75,50), 35)
    leftcir.setFill("Blue")
    leftcir.setOutline("Blue")
    leftcir.draw(win)

    rightcir = Circle(Point(425,50), 35)
    rightcir.setFill("Red")
    rightcir.setOutline("Red")
    rightcir.draw(win)

#______________________________________________________________________________

    label = Text(Point(250, 95), "How to play Connect 4")
    label.setStyle("italic")
    label.setSize(16)
    label.setTextColor("Blue")
    label.draw(win)

    rect = Rectangle(Point(200, 465), Point(300, 495))
    rect.setOutline("Blue")
    rect.draw(win)

    exitButton = Button(win, Point(250,480), 75, 25, "Exit to Menu")

    pt = win.getMouse()
    if exitButton.clicked(pt):
        win.close()
        Connect4TitleScreen.main()

    rule = Text(Point(250, 125), "The player will decide what color they want to be.")
    rule.setSize(13)
    rule.setTextColor("red")
    rule.draw(win)

    extra = Text(Point(250, 145), "The player can either be Blue or Red.")
    extra.setSize(11)
    extra.setTextColor("red")
    extra.draw(win)
#___________________________________________________________________________________
    pt = win.getMouse()
    if exitButton.clicked(pt):
        win.close()
        Connect4TitleScreen.main()

    rule.undraw()
    extra.undraw()

    rule2 = Text(Point(250, 125), "The computer will then decide who will get the first turn.")
    rule2.setSize(13)
    rule2.setTextColor("red")
    rule2.draw(win)
#___________________________________________________________________________________
    pt = win.getMouse()
    if exitButton.clicked(pt):
        win.close()
        Connect4TitleScreen.main()

    rule2.undraw()

    rule3 = Text(Point(250, 125), "Upon player's turn, they will then drop their color into 1 of the 7 columns.")
    rule3.setSize(12)
    rule3.setTextColor("red")
    rule3.draw(win)

    cir39.setFill('Blue')
        
#___________________________________________________________________________________
    pt = win.getMouse()
    if exitButton.clicked(pt):
        win.close()
        Connect4TitleScreen.main()

    rule3.undraw()

    rule4 = Text(Point(250, 125), "In order to win, player must get '4 In A Row' first by either getting")
    rule4.setSize(12)
    rule4.setTextColor("red")
    rule4.draw(win)

    extra2 = Text(Point(250, 145), "'4 In A Row' vertically, ")
    extra2.setSize(11)
    extra2.setTextColor("red")
    extra2.draw(win)

    cir18.setFill('blue')
    cir25.setFill('blue')
    cir32.setFill('blue')
#___________________________________________________________________________________
    pt = win.getMouse()
    if exitButton.clicked(pt):
        win.close()
        Connect4TitleScreen.main()

    extra2.undraw()

    extra3 = Text(Point(250, 145), "'4 In A Row' horzonatally, ")
    extra3.setSize(11)
    extra3.setTextColor("red")
    extra3.draw(win)

    cir18.setFill('white')
    cir25.setFill('white')
    cir32.setFill('white')

    cir38.setFill('blue')
    cir40.setFill('blue')
    cir41.setFill('blue')
#___________________________________________________________________________________
    pt = win.getMouse()
    if exitButton.clicked(pt):
        win.close()
        Connect4TitleScreen.main()

    extra3.undraw()

    extra4 = Text(Point(250, 145), " or by getting '4 In a Row' diagonally to either the left or to the right.")
    extra4.setSize(11)
    extra4.setTextColor("red")
    extra4.draw(win)

    cir38.setFill('white')
    cir40.setFill('white')
    cir41.setFill('white')

    cir15.setFill('blue')
    cir23.setFill('blue')
    cir31.setFill('blue')

    pt = win.getMouse()
    if exitButton.clicked(pt):
        win.close()
        Connect4TitleScreen.main()

    cir15.setFill('white')
    cir23.setFill('white')
    cir31.setFill('white')

    cir33.setFill('blue')
    cir27.setFill('blue')
    cir21.setFill('blue')

    
#___________________________________________________________________________________
    pt = win.getMouse()
    if exitButton.clicked(pt):
        win.close()
        Connect4TitleScreen.main()
        
    rule4.undraw()
    extra4.undraw()

    rule5 = Text(Point(250, 125), "And that is how you play Connect 4!")
    rule5.setSize(12)
    rule5.setTextColor("red")
    rule5.draw(win)

    cir33.setFill('white')
    cir27.setFill('white')
    cir21.setFill('white')
    cir39.setFill('white')

    pt = win.getMouse()
    if exitButton.clicked(pt):
        win.close()
        Connect4TitleScreen.main()

   

    


