# create custom turtle
import turtle as trtl
import time
import random
ice_cream = trtl.Turtle()
ice_cream_writer = trtl.Turtle()
ice_cream_writer.hideturtle()
trtl.addshape("heart",((0,0),(-2,2),(-4,1),(-4,-1),(0,-5),(4,-1),(4,1),(2,2)))
ice_cream_colors = ["red", "#CFB19D", "pink", "white"]
ice_cream.shape("heart")
ice_cream.shapesize(2,3,1)
#####################


# draw cone
ice_cream.penup()
ice_cream.goto(145,120)
ice_cream.pendown()
ice_cream.right(117)
ice_cream.pencolor("#CFB19D")
ice_cream.fillcolor("#CFB19D")
ice_cream.begin_fill()
ice_cream.pendown()
ice_cream.forward(300)
ice_cream.right(122)
ice_cream.forward(310)
ice_cream.end_fill()
#####################


# draw ice cream scoop 
while True:
    draw_scoop = trtl.textinput("What is the tallest mountain in the world?", "")
    if draw_scoop == "mount everest":
        ice_cream.pensize(3)
        ice_cream.pencolor("pink")
        ice_cream.setheading(80)
        ice_cream.penup()
        ice_cream.goto(145,120)
        ice_cream.pendown()
        ice_cream.fillcolor("pink")
        ice_cream.begin_fill()
        ice_cream.circle(150,200)
        ice_cream.left(80)
        ice_cream.forward(158)
        ice_cream.end_fill()
        break
    else:
        ice_cream_writer.color("black")
        ice_cream_writer.write("Incorrect!", align="left", font=("Times New Roman", 20))
        time.sleep(2)
        ice_cream_writer.clear()
######################


#toppings
while True:
    draw_cherry = trtl.textinput("How many colors are in a rainbow?", "")
    if draw_cherry == "7":
        ice_cream.pencolor("red")
        ice_cream.fillcolor("red")
        ice_cream.setheading(80)
        ice_cream.penup()
        ice_cream.goto(27,275)
        ice_cream.pendown()
        ice_cream.begin_fill()
        ice_cream.circle(25)
        ice_cream.end_fill()
        ice_cream.penup()
        ice_cream.goto(10,285)
        ice_cream.pendown()
        ice_cream.forward(35)
        break
    else:
        ice_cream_writer.color("black")
        ice_cream_writer.write("Incorrect!", align="left", font=("Times New Roman", 20))
        time.sleep(2)
        ice_cream_writer.clear()
#######################


while True:
    draw_sprinkles = trtl.textinput("Who was the first Disney princess?", "")
    if draw_sprinkles == "snow white":
        ice_cream.pencolor("red")
        for i in range(30):
            rand_x = random.randint(-100,100)
            rand_y = random.randint(150,270)
            ice_cream.penup()
            ice_cream.goto(rand_x,rand_y)
            ice_cream.pencolor("white")
            ice_cream.pendown()
            ice_cream.forward(10)
        break
    else:
        ice_cream_writer.color("black")
        ice_cream_writer.write("Incorrect!", align="left", font=("Times New Roman", 20))
        time.sleep(2)
        ice_cream_writer.clear()
############################



ice_cream.hideturtle()
wn = trtl.Screen()
wn.mainloop()