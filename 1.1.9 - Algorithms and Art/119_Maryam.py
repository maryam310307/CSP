# create custom turtle
import turtle as trtl
ice_cream = trtl.Turtle()
trtl.addshape("heart",((0,0),(-2,2),(-4,1),(-4,-1),(0,-5),(4,-1),(4,1),(2,2)))
ice_cream.shape("heart")
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
'''ice_cream.hideturtle()'''
######################

# draw cone
ice_cream.penup()
ice_cream.goto(145,120)
ice_cream.right(117)
ice_cream.pencolor("#CFB19D")
ice_cream.pendown()
ice_cream.forward(300)
ice_cream.right(123)
ice_cream.forward(318)


wn = trtl.Screen()
wn.mainloop()