import turtle as trtl
ice_cream = trtl.Turtle()

# draw ice cream 
ice_cream.pensize(3)
ice_cream.pencolor("pink")
ice_cream.setheading(80)
ice_cream.penup()
ice_cream.goto(145,120)
ice_cream.fillcolor("pink")
ice_cream.begin_fill()
ice_cream.circle(150,200)
ice_cream.left(80)
ice_cream.forward(158)
ice_cream.end_fill()
ice_cream.hideturtle()
######################

# draw cone


wn = trtl.Screen()
wn.mainloop()