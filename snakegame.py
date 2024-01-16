import turtle
import random
import time

delay=0.1
score=0
highestscore=0

#Body of snake
bodies=[]

#getting a screen on which the game will be displayed.
s=turtle.Screen()
s.title("Snake Game")
s.bgcolor("Gray")
s.setup(width=600,height=600)

#Now firstly creating the head of the snake.
head=turtle.Turtle()
head.speed=(0)
head.shape("square")
head.color("white")
head.fillcolor("white")
head.penup()
head.goto(0,0)
head.direction="stop"


#The food of snake
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0,200)
food.st()

#Score Board
sb=turtle.Turtle()
sb.shape("square")
sb.fillcolor("pink")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("Score:0 | highest Score:0", align="left", font=("Courier", 12, "normal"))
sb.pendown()

def moveup():
    if head.direction!="down":
        head.direction="up"
def movedown():
    if head.direction!="up":
        head.direction="down"
def moveleft():
    if head.direction!="right":
        head.direction="left"
def moveright():
    if head.direction!="left":
        head.direction="right"
def movestop():
    head.direction="stop"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

#Mapping of the keys
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveright,"Right")
s.onkey(moveleft,"Left")
s.onkey(movestop,"space")


#main loop
while True:
    s.update() #this is to update the screen
    #checking the collision with border
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)

    #checking the collision with food
    if head.distance(food)<20:
         #move the food to some random position
         x=random.randint(-290,290)
         y=random.randint(-290,290)
         food.goto(x,y)


         #increase the length of the snake
         body=turtle.Turtle()
         body.speed(0)
         body.penup()
         body.shape("square")
         body.color("yellow")
         body.fillcolor("yellow")
         bodies.append(body)

         #to increase the score
         score+=10

         #changing the delay
         delay-=0.001

         #update the highest score
         if score>highestscore:
             highestscore=score
         sb.clear()
         sb.write("Score: {} | Highest Score: {}".format(score, highestscore))

    #Movement of snake body
    for index in range (len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)

    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()

    #checking the collision of snake with it's body
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            #hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()

            score=0
            delay=0.1

            #updating the score board
            sb.clear()
            sb.write("Score:{} | Highest Score:{}".format(score,highestscore))
    time.sleep(delay)
s.mainloop()


            

        
         
    










    
    
        










 








