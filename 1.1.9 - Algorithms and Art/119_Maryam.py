# create custom turtle
import turtle as trtl
ice_cream = trtl.Turtle()
trtl.addshape("heart",((0,0),(-2,2),(-4,1),(-4,-1),(0,-5),(4,-1),(4,1),(2,2)))
ice_cream.shape("heart")
ice_cream.shapesize(2,3,1)
#####################

# draw ice cream 
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

######################

# draw cone
ice_cream.goto(145,120)
ice_cream.right(117)
ice_cream.pencolor("#CFB19D")
ice_cream.fillcolor("#CFB19D")
ice_cream.begin_fill()
ice_cream.pendown()
ice_cream.forward(300)
ice_cream.right(122)
ice_cream.forward(310)
ice_cream.end_fill()

#toppings
draw_cherry = trtl.textinput("What is the largest planet in our solar system?", "")

if draw_cherry == "jupiter":
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

else:
  print("Incorrect!")

draw_sprinkles = trtl.textinput("Who was the first Disney princess?", "")

if draw_sprinkles == "snow white":
    ice_cream.pencolor("white")
    ice_cream.penup()
    ice_cream.goto(50,250)
    ice_cream.pendown()
    ice_cream.forward(10)
    ice_cream.penup()
    ice_cream.goto(25,210)
    ice_cream.pendown()
    ice_cream.forward(10)
    ice_cream.penup()
    ice_cream.goto(-10,200)
    ice_cream.pendown()
    ice_cream.forward(10)
    ice_cream.penup()
    ice_cream.goto(75,200)
    ice_cream.pendown()
    ice_cream.forward(10)
    ice_cream.penup()
    ice_cream.goto(60,165)
    ice_cream.pendown()
    ice_cream.forward(10)

else:
   print("Incorrect!")
  
  

ice_cream.hideturtle()
wn = trtl.Screen()
wn.mainloop()