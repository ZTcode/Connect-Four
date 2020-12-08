from graphics import*
import random
from button import Button
import os
import Connect4TitleScreen

def main():
#____________________________Game BackGround____________________________

    #Game Board

    win = GraphWin("Connect 4", 500,500)
    win.setBackground("White")
  
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

    column1 = [cir1, cir8, cir15, cir22, cir29, cir36]
    column2 = [cir2, cir9, cir16, cir23, cir30, cir37]
    column3 = [cir3, cir10, cir17, cir24, cir31, cir38]
    column4 = [cir4, cir11, cir18, cir25, cir32, cir39]
    column5 = [cir5, cir12, cir19, cir26, cir33, cir40]
    column6 = [cir6, cir13, cir20, cir27, cir34, cir41]
    column7 = [cir7, cir14, cir21, cir28, cir35, cir42]
    
    columns = [column1, column2, column3, column4, column5, column6, column7]
    for i in range(7):                              
        for j in range(6):
            columns[i][j].color = 'white'

    row1 = [cir1, cir2, cir3, cir4, cir5, cir6, cir7]
    row2 = [cir8, cir8, cir10, cir11, cir12, cir13, cir14]
    row3 = [cir15, cir16, cir17, cir18, cir19, cir20, cir21]
    row4 = [cir22, cir23, cir24, cir25, cir26, cir27, cir28]
    row5 = [cir29, cir30, cir31, cir32, cir33, cir34, cir35]
    row6 = [cir36, cir37, cir38, cir39, cir40, cir41, cir42]

    rows = [row1, row2, row3, row4, row5, row6]
    for i in range(6):
        for j in range(7):
            rows[i][j].color = 'white'
    
#_____________________________GamePlay____________________________________

    #Choosing to be which player
    
    choose = Text(Point(250, 125), "Click on Blue to be Player Blue or Red to be Player Red.")
    choose.setStyle("italic")
    choose.setSize(14)
    choose.setTextColor("Black")
    choose.draw(win)
   
    blue = Button(win, Point(75,50), 70, 70, "")     
    red = Button(win,Point(425,50), 70, 70, "")

    PlayerBlue = 'Blue'
    PlayerRed = 'Red'

    color = 'blue' or 'red'

    players = [PlayerBlue, PlayerRed]

    human = PlayerRed or PlayerBlue
    human2 = PlayerRed or PlayerBlue 

    while True:
        pt = win.getMouse()
        if blue.clicked(pt):
            choose.undraw()
            human = 'blue'
            if human == 'blue':
                human2 == 'red'
            break
        if red.clicked(pt):
            choose.undraw()
            human = 'red'
            if human == 'red':
                human2 == 'blue'
            break

    win.getMouse
    blue.deactivate
    red.deactivate
    choose.undraw()

    #Deciding who will go first
    
    random.choice(players)
    if random.choice(players) == PlayerBlue:
        firstPick = Text(Point(250, 125), "Player Blue will go first.")
        firstPick.setStyle("italic")
        firstPick.setSize(14)
        firstPick.setTextColor("Blue")
        firstPick.draw(win)
        human = 'blue' #blue circle will be colored 1st
    else:
        firstPick = Text(Point(250, 125), "Player Red will go first.")
        firstPick.setStyle("italic")
        firstPick.setSize(14)
        firstPick.setTextColor("Red")
        firstPick.draw(win)
        human = 'red' #circle circle will be colored 1st

    #Game Function
    counts = [0,0,0,0,0,0,0]
    while True:
        move = win.getMouse()
        firstPick.undraw()
        if 115 <= move.getX() <= 145 and 175 <= move.getY() <= 425: #Column 1
            if counts[0] == 0:
                cir36.setFill(human)
                cir36.color = human
                counts[0] +=1
            elif counts[0]==1:
                cir29.setFill(human)
                cir29.color = human
                counts[0] += 1
            elif counts[0]==2:
                cir22.setFill(human)
                cir22.color = human
                counts[0]+= 1 
            elif counts[0]==3:
                cir15.setFill(human)
                cir15.color = human
                counts[0]+=1
            elif counts[0]==4:
                cir8.setFill(human)
                cir8.color = human
                counts[0]+=1
            elif counts[0]==5:
                cir1.setFill(human)
                cir1.color = human
                counts[0]+=1

            if human == 'blue':
                human = 'red'
            else:
                human = 'blue'
            
        elif 155 <= move.getX() <= 185 and 175 <= move.getY() <= 425: #Column 2
            if counts[1] == 0:
                cir37.setFill(human)
                cir37.color = human
                counts[1] +=1
            elif counts[1]==1:
                cir30.setFill(human)
                cir30.color = human
                counts[1] += 1
            elif counts[1]==2:
                cir23.setFill(human)
                cir23.color = human
                counts[1]+= 1 
            elif counts[1]==3:
                cir16.setFill(human)
                cir16.color = human
                counts[1]+=1
            elif counts[1]==4:
                cir9.setFill(human)
                cir9.color = human
                counts[1]+=1
            elif counts[1]==5:
                cir2.setFill(human)
                cir2.color = human
                counts[1]+=1

            if human == 'blue':
                human = 'red'
            else:
                human = 'blue'
            
        elif 195 <= move.getX() <= 225 and 175 <= move.getY() <= 425: #Column 3
            if counts[2] == 0:
                cir38.setFill(human)
                cir38.color = human
                counts[2] +=1
            elif counts[2]==1:
                cir31.setFill(human)
                cir31.color = human
                counts[2] += 1
            elif counts[2]==2:
                cir24.setFill(human)
                cir24.color = human
                counts[2]+= 1 
            elif counts[2]==3:
                cir17.setFill(human)
                cir17.color = human
                counts[2]+=1
            elif counts[2]==4:
                cir10.setFill(human)
                cir10.color = human
                counts[2]+=1
            elif counts[2]==5:
                cir3.setFill(human)
                cir3.color = human
                counts[2]+=1

            if human == 'blue':
                human = 'red'
            else:
                human = 'blue'
                
        elif 235 <= move.getX() <= 265 and 175 <= move.getY() <= 425: #Column 4
            if counts[3] == 0:
                cir39.setFill(human)
                cir39.color = human
                counts[3] +=1
            elif counts[3]==1:
                cir32.setFill(human)
                cir32.color = human
                counts[3] += 1
            elif counts[3]==2:
                cir25.setFill(human)
                cir25.color = human
                counts[3]+= 1 
            elif counts[3]==3:
                cir18.setFill(human)
                cir18.color = human
                counts[3]+=1
            elif counts[3]==4:
                cir11.setFill(human)
                cir11.color = human
                counts[3]+=1
            elif counts[3]==5:
                cir4.setFill(human)
                cir4.color = human
                counts[3]+=1

            if human == 'blue':
                human = 'red'
            else:
                human = 'blue'
        
        elif 275 <= move.getX() <= 305 and 175 <= move.getY() <= 425: #Column 5
            if counts[4] == 0:
                cir40.setFill(human)
                cir40.color = human
                counts[4] +=1
            elif counts[4]==1:
                cir33.setFill(human)
                cir33.color = human
                counts[4] += 1
            elif counts[4]==2:
                cir26.setFill(human)
                cir26.color = human
                counts[4]+= 1 
            elif counts[4]==3:
                cir19.setFill(human)
                cir19.color = human
                counts[4]+=1
            elif counts[4]==4:
                cir12.setFill(human)
                cir12.color = human
                counts[4]+=1
            elif counts[4]==5:
                cir5.setFill(human)
                cir5.color = human
                counts[4]+=1

            if human == 'blue':
                human = 'red'
            else:
                human = 'blue'

        elif 315 <= move.getX() <= 345 and 175 <= move.getY() <= 425: #Column 6
            if counts[5] == 0:
                cir41.setFill(human)
                cir41.color = human
                counts[5] +=1
            elif counts[5]==1:
                cir34.setFill(human)
                cir34.color = human
                counts[5] += 1
            elif counts[5]==2:
                cir27.setFill(human)
                cir27.color = human
                counts[5]+= 1 
            elif counts[5]==3:
                cir20.setFill(human)
                cir20.color = human
                counts[5]+=1
            elif counts[5]==4:
                cir13.setFill(human)
                cir13.color = human
                counts[5]+=1
            elif counts[5]==5:
                cir6.setFill(human)
                cir6.color = human
                counts[5]+=1
            
            if human == 'blue':
                human = 'red'
            else:
                human = 'blue'
                
        elif 355 <= move.getX() <= 385 and 175 <= move.getY() <= 425: #Column 7
            if counts[6] == 0:
                cir42.setFill(human)
                cir42.color = human
                counts[6] +=1
            elif counts[6]==1:
                cir35.setFill(human)
                cir35.color = human
                counts[6] += 1
            elif counts[6]==2:
                cir28.setFill(human)
                cir28.color = human
                counts[6]+= 1 
            elif counts[6]==3:
                cir21.setFill(human)
                cir21.color = human
                counts[6]+=1
            elif counts[6]==4:
                cir14.setFill(human)
                cir14.color = human
                counts[6]+=1
            elif counts[6]==5:
                cir7.setFill(human)
                cir7.color = human
                counts[6]+=1

            if human == 'blue':
                human = 'red'
            else:
                human = 'blue'

        

        #Def Check Winner 
        winner = None
        #Checking Columns
        for i in range(6):
            for j in range(4):
                c = columns[j][i].color #c = rows[j][i].color, should be c = columns[j][i].color FIXED
                if c != 'white':
                    if columns[j+1][i].color == columns[j+2][i].color == columns[j+3][i].color == c:
                        winner = c
                        if winner == 'blue':
                            winnernote = Text(Point(250, 125), "Player Blue wins.")
                            winnernote.setStyle("italic")
                            winnernote.setSize(14)
                            winnernote.setTextColor("Blue")
                            winnernote.draw(win)
                        if winner == 'red':
                            winnernote = Text(Point(250, 125), "Player Red wins.")
                            winnernote.setStyle("italic")
                            winnernote.setSize(14)
                            winnernote.setTextColor("Red")
                            winnernote.draw(win)

                        rect1 = Rectangle(Point(15, 465), Point(105, 495))
                        rect1.setOutline("Blue")
                        rect1.draw(win)

                        rect2 = Rectangle(Point(425, 465), Point(480, 495))
                        rect2.setOutline("Blue")
                        rect2.draw(win)

                        playAgain = Button(win, Point(60,480), 90, 25, "Play Again")
                        quitButton = Button(win, Point(450,480), 75, 25, "Quit")
                    
                        #Event Loop
                        pt = win.getMouse()
                        if playAgain.clicked(pt):
                            win.close()
                            main()
                        if quitButton.clicked(pt):
                            win.close()
                            Connect4TitleScreen.main()
                                
                
        #Checking Rows
        for i in range(7):
            for j in range(3):
                c = rows[j][i].color
                if c != 'white':
                    if rows[j+1][i].color == rows[j+2][i].color == rows[j+3][i].color == c:
                        winner = c
                        if winner == 'blue':
                            winnernote = Text(Point(250, 125), "Player Blue wins.")
                            winnernote.setStyle("italic")
                            winnernote.setSize(14)
                            winnernote.setTextColor("Blue")
                            winnernote.draw(win)
                        if winner == 'red':
                            winnernote = Text(Point(250, 125), "Player Red wins.")
                            winnernote.setStyle("italic")
                            winnernote.setSize(14)
                            winnernote.setTextColor("Red")
                            winnernote.draw(win)

                        rect1 = Rectangle(Point(15, 465), Point(105, 495))
                        rect1.setOutline("Blue")
                        rect1.draw(win)

                        rect2 = Rectangle(Point(425, 465), Point(480, 495))
                        rect2.setOutline("Blue")
                        rect2.draw(win)

                        playAgain = Button(win, Point(60,480), 90, 25, "Play Again")
                        quitButton = Button(win, Point(450,480), 75, 25, "Quit")
                    
                        #Event Loop
                        pt = win.getMouse()
                        if playAgain.clicked(pt):
                            win.close()
                            main()
                        if quitButton.clicked(pt):
                            win.close()
                            Connect4TitleScreen.main()
                                        
                        
            #Checking Left Diagonal \
            for i in range(3):
                for j in range(4):
                    c = rows[i][j].color
                    if c != 'white':
                        if rows[i+1][j+1].color == rows[i+2][j+2].color == rows[i+3][j+3].color == c:
                            winner = c
                            if winner == 'blue':
                                winnernote = Text(Point(250, 125), "Player Blue wins.")
                                winnernote.setStyle("italic")
                                winnernote.setSize(14)
                                winnernote.setTextColor("Blue")
                                winnernote.draw(win)
                            if winner == 'red':
                                winnernote = Text(Point(250, 125), "Player Red wins.")
                                winnernote.setStyle("italic")
                                winnernote.setSize(14)
                                winnernote.setTextColor("Red")
                                winnernote.draw(win)

                            rect1 = Rectangle(Point(15, 465), Point(105, 495))
                            rect1.setOutline("Blue")
                            rect1.draw(win)

                            rect2 = Rectangle(Point(425, 465), Point(480, 495))
                            rect2.setOutline("Blue")
                            rect2.draw(win)

                            playAgain = Button(win, Point(60,480), 90, 25, "Play Again")
                            quitButton = Button(win, Point(450,480), 75, 25, "Quit")
                        
                            #Event Loop
                            pt = win.getMouse()
                            if playAgain.clicked(pt):
                                win.close()
                                main()
                            if quitButton.clicked(pt):
                                win.close()
                                Connect4TitleScreen.main()
        
            #Checking Right Diagonal /
            for i in range(3):
                for j in range(3, 7):
                    c = rows[i][j].color
                    if c != 'white':
                        if rows[i+1][j-1].color == rows[i+2][j-2].color == rows[i+3][j-3].color == c:
                            winner = c
                            if winner == 'blue':
                                winnernote = Text(Point(250, 125), "Player Blue wins.")
                                winnernote.setStyle("italic")
                                winnernote.setSize(14)
                                winnernote.setTextColor("Blue")
                                winnernote.draw(win)
                            if winner == 'red':
                                winnernote = Text(Point(250, 125), "Player Red wins.")
                                winnernote.setStyle("italic")
                                winnernote.setSize(14)
                                winnernote.setTextColor("Red")
                                winnernote.draw(win)

                            rect1 = Rectangle(Point(15, 465), Point(105, 495))
                            rect1.setOutline("Blue")
                            rect1.draw(win)

                            rect2 = Rectangle(Point(425, 465), Point(480, 495))
                            rect2.setOutline("Blue")
                            rect2.draw(win)

                            playAgain = Button(win, Point(60,480), 90, 25, "Play Again")
                            quitButton = Button(win, Point(450,480), 75, 25, "Quit")
                        
                            #Event Loop
                            pt = win.getMouse()
                            if playAgain.clicked(pt):
                                win.close()
                                main()
                            if quitButton.clicked(pt):
                                win.close()
                                Connect4TitleScreen.main()
    

            if winner == None and sum(counts)>=42:  
                winnernote = Text(Point(250, 125), 'No more choices available.')
                winnernote.setStyle("italic")
                winnernote.setSize(14)
                winnernote.draw(win)

                rect1 = Rectangle(Point(15, 465), Point(105, 495))
                rect1.setOutline("Blue")
                rect1.draw(win)

                rect2 = Rectangle(Point(425, 465), Point(480, 495))
                rect2.setOutline("Blue")
                rect2.draw(win)

                playAgain = Button(win, Point(60,480), 90, 25, "Play Again")
                quitButton = Button(win, Point(450,480), 75, 25, "Quit")
            
                #Event Loop
                pt = win.getMouse()
                if playAgain.clicked(pt):
                    win.close()
                    main()
                if quitButton.clicked(pt):
                    win.close()
                    Connect4TitleScreen.main()


    win.close()

            
        

