import turtle as ttl
import numpy as np


def start():
    
    ttl.reset()
    
    global letter,p1_s,p2_s,mat,change,bgcolor,x_color,y_color,complete
    complete=0
    x_color=((1,0,1))
    y_color=((1,0.5,0))
    bgcolor=((1,1,1))
    change=1
    mat=np.zeros([3,3])
    p1_s='X'
    p2_s='Y'
    letter=p1_s

    ttl.speed(0)
    ttl.hideturtle()
    ttl.bgcolor(bgcolor)


    ttl.penup()
    ttl.sety(225)
    ttl.pencolor((0,0.5,1))
    ttl.write("TIC TAC TOE",False,font=('ROG Fonts',50,'bold'),align="center")


    ttl.setpos(-220,170)
    ttl.pencolor((0,0.5,0.5))
    ttl.write("Player 1 :",False,font=('BankGothic Md BT',30,'bold'),align="center")

    ttl.setx(130)
    ttl.write("Player 2 :",False,font=('BankGothic Md BT',30,'bold'),align="center")

    ttl.setpos(-60,150)
    ttl.pencolor(x_color)
    ttl.write(p1_s,False,font=('Algerian',50,''),align="center")

    ttl.setpos(290,150)
    ttl.pencolor(y_color)
    ttl.write(p2_s,False,font=('Algerian',50,''),align='center')

    ttl.speed(10)
    
    ttl.pencolor((0,1,0))
    ttl.pensize(10)
    ttl.setpos(-60,100)
    ttl.setheading(270)
    ttl.pendown()
    ttl.fd(360)
    ttl.penup()

    ttl.setpos(60,-260)
    ttl.setheading(90)
    ttl.pendown()
    ttl.fd(360)
    ttl.penup()

    ttl.setpos(-180,-20)
    ttl.setheading(0)
    ttl.pendown()
    ttl.fd(360)
    ttl.penup()

    ttl.setpos(180,-140)
    ttl.setheading(180)
    ttl.pendown()
    ttl.fd(360)
    ttl.penup()

    ttl.speed(0)

    ttl.pensize(1)

    ttl.setpos(250,-300)
    ttl.pencolor((0.5,0.5,0))
    ttl.write("Reset",False,font=('Bauhaus 93',30,''),align='center')

    

def check():
    global letter,p1_s,p2_s,mat,change,bgcolor,x_color,y_color,complete

    ttl.setpos(-250,10)
    ttl.setheading(90)
    if(np.sum(mat[0,:])==3 or np.sum(mat[1,:])==3 or np.sum(mat[2,:])==3 or np.sum(mat[:,0])==3 or np.sum(mat[:,1])==3 or np.sum(mat[:,2])==3 or (mat[0,0]+mat[1,1]+mat[2,2])==3 or (mat[0,2]+mat[1,1]+mat[2,0])==3):
        complete=1
        ttl.pencolor(x_color)
        for i in "WINNER":
            ttl.write(i,False,font=('Curlz MT',50,'bold'),align="center")
            ttl.setx(250)
            ttl.write(i,False,font=('Curlz MT',50,'bold'),align="center")
            ttl.setpos(-250,ttl.ycor()-50)
    elif(np.sum(mat[0,:])==30 or np.sum(mat[1,:])==30 or np.sum(mat[2,:])==30 or np.sum(mat[:,0])==30 or np.sum(mat[:,1])==30 or np.sum(mat[:,2])==30 or (mat[0,0]+mat[1,1]+mat[2,2])==30 or (mat[0,2]+mat[1,1]+mat[2,0])==30):
        complete=1
        ttl.pencolor(y_color)
        for i in "WINNER":
            ttl.write(i,False,font=('Curlz MT',50,'bold'),align="center")
            ttl.setx(250)
            ttl.write(i,False,font=('Curlz MT',50,'bold'),align="center")
            ttl.setpos(-250,ttl.ycor()-50)
    elif(np.sum(mat==0)==0):
        complete=1
        ttl.pencolor((1,1,0))
        ttl.setpos(-250,0)
        for i in "DRAW":
            ttl.write(i,False,font=('Ravie',50,''),align="center")
            ttl.setpos(-250,ttl.ycor()-60)
        ttl.setpos(250,10)
        for i in "MATCH":
            ttl.write(i,False,font=('Ravie',50,''),align="center")
            ttl.setpos(250,ttl.ycor()-60)

def operation(x,y):
    global letter,p1_s,p2_s,mat,change,bgcolor,x_color,y_color,complete
    ttl.fillcolor(bgcolor)


    if(((x>-95 and x<-30 and y>155 and y<220) or (x>255 and x<320 and y>155 and y<220)) and change==1):
        ttl.pencolor(bgcolor)
        ttl.setpos(-95,155)
        ttl.setheading(0)
        ttl.begin_fill()
        ttl.pendown()
        ttl.fd(65)
        ttl.setheading(90)
        ttl.fd(70)
        ttl.setheading(180)
        ttl.fd(65)
        ttl.setheading(270)
        ttl.fd(70)
        ttl.end_fill()
        ttl.penup()

        ttl.pencolor(bgcolor)
        ttl.setpos(255,155)
        ttl.setheading(0)
        ttl.begin_fill()
        ttl.pendown()
        ttl.fd(65)
        ttl.setheading(90)
        ttl.fd(70)
        ttl.setheading(180)
        ttl.fd(65)
        ttl.setheading(270)
        ttl.fd(70)
        ttl.end_fill()
        ttl.penup()

        if(p1_s=='X'):
            p1_s='Y'
            p2_s='X'
            letter=p1_s

            ttl.setpos(-60,150)
            ttl.pencolor(y_color)
            ttl.write(p1_s,False,font=('Algerian',50,''),align="center")

            ttl.setpos(290,150)
            ttl.pencolor(x_color)
            ttl.write(p2_s,False,font=('Algerian',50,''),align='center')
        elif(p1_s=='Y'):
            p1_s='X'
            p2_s='Y'
            letter=p1_s

            ttl.setpos(-60,150)
            ttl.pencolor(x_color)
            ttl.write(p1_s,False,font=('Algerian',50,''),align="center")

            ttl.setpos(290,150)
            ttl.pencolor(y_color)
            ttl.write(p2_s,False,font=('Algerian',50,''),align='center')

    if(complete==0):
        if(x>-180 and x<-60 and y>-20 and y<100 and mat[0][0]==0):
            change=0
            ttl.setpos(-120,0)
            if(letter=='X'):
                ttl.pencolor(x_color)
                ttl.write(letter,False,font=('Algerian',50,''),align="center")
                letter='Y'
                mat[0][0]=1
            elif(letter=='Y'):
                ttl.pencolor(y_color)
                ttl.write(letter,False,font=('Algerian',50,''),align='center')
                letter='X'
                mat[0][0]=10
        elif(x>-60 and x<60 and y>-20 and y<100 and mat[0][1]==0):
            change=0
            ttl.setpos(0,0)
            if(letter=='X'):
                ttl.pencolor(x_color)
                ttl.write(letter,False,font=('Algerian',50,''),align="center")
                letter='Y'
                mat[0][1]=1
            elif(letter=='Y'):
                ttl.pencolor(y_color)
                ttl.write(letter,False,font=('Algerian',50,''),align='center')
                letter='X'
                mat[0][1]=10
        elif(x>60 and x<180 and y>-20 and y<100 and mat[0][2]==0):
            change=0
            ttl.setpos(120,0)
            if(letter=='X'):
                ttl.pencolor(x_color)
                ttl.write(letter,False,font=('Algerian',50,''),align="center")
                letter='Y'
                mat[0][2]=1
            elif(letter=='Y'):
                ttl.pencolor(y_color)
                ttl.write(letter,False,font=('Algerian',50,''),align='center')
                letter='X'
                mat[0][2]=10
        elif(x>-180 and x<-60 and y>-140 and y<-20 and mat[1][0]==0):
            change=0
            ttl.setpos(-120,-120)
            if(letter=='X'):
                ttl.pencolor(x_color)
                ttl.write(letter,False,font=('Algerian',50,''),align="center")
                letter='Y'
                mat[1][0]=1
            elif(letter=='Y'):
                ttl.pencolor(y_color)
                ttl.write(letter,False,font=('Algerian',50,''),align='center')
                letter='X'
                mat[1][0]=10
        elif(x>-60 and x<60 and y>-140 and y<-20 and mat[1][1]==0):
            change=0
            ttl.setpos(0,-120)
            if(letter=='X'):
                ttl.pencolor(x_color)
                ttl.write(letter,False,font=('Algerian',50,''),align="center")
                letter='Y'
                mat[1][1]=1
            elif(letter=='Y'):
                ttl.pencolor(y_color)
                ttl.write(letter,False,font=('Algerian',50,''),align='center')
                letter='X'
                mat[1][1]=10
        elif(x>60 and x<180 and y>-140 and y<-20 and mat[1][2]==0):
            change=0
            ttl.setpos(120,-120)
            if(letter=='X'):
                ttl.pencolor(x_color)
                ttl.write(letter,False,font=('Algerian',50,''),align="center")
                letter='Y'
                mat[1][2]=1
            elif(letter=='Y'):
                ttl.pencolor(y_color)
                ttl.write(letter,False,font=('Algerian',50,''),align='center')
                letter='X'
                mat[1][2]=10
        elif(x>-180 and x<-60 and y>-260 and y<-140 and mat[2][0]==0):
            change=0
            ttl.setpos(-120,-240)
            if(letter=='X'):
                ttl.pencolor(x_color)
                ttl.write(letter,False,font=('Algerian',50,''),align="center")
                letter='Y'
                mat[2][0]=1
            elif(letter=='Y'):
                ttl.pencolor(y_color)
                ttl.write(letter,False,font=('Algerian',50,''),align='center')
                letter='X'
                mat[2][0]=10
        elif(x>-60 and x<60 and y>-260 and y<-140 and mat[2][1]==0):
            change=0
            ttl.setpos(0,-240)
            if(letter=='X'):
                ttl.pencolor(x_color)
                ttl.write(letter,False,font=('Algerian',50,''),align="center")
                letter='Y'
                mat[2][1]=1
            elif(letter=='Y'):
                ttl.pencolor(y_color)
                ttl.write(letter,False,font=('Algerian',50,''),align='center')
                letter='X'
                mat[2][1]=10
        elif(x>60 and x<180 and y>-260 and y<-140 and mat[2][2]==0):
            change=0
            ttl.setpos(120,-240)
            if(letter=='X'):
                ttl.pencolor(x_color)
                ttl.write(letter,False,font=('Algerian',50,''),align="center")
                letter='Y'
                mat[2][2]=1
            elif(letter=='Y'):
                ttl.pencolor(y_color)
                ttl.write(letter,False,font=('Algerian',50,''),align='center')
                letter='X'
                mat[2][2]=10


    check()

    if(x>195 and x<305 and y>-295 and y<-255):
        start()



start()

ttl.onscreenclick(operation)
ttl.mainloop()

