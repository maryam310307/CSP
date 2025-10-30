import turtle as trtl
import random as rand
import time as time
wn = trtl.Screen()

# Start Screen
# set background for starting screen, title, and explain the game
wn.bgpic("background.gif")
screen_width = 500
screen_height = 50
trtl.color = "pink"
trtl.penup()
'''trtl.goto(-222,200)
trtl.write("What is missing?", font=("Times New Roman", 50))
time.sleep(2)
trtl.clear()
trtl.goto(-222,100)
trtl.write("The function of the game is simple.", font=("Times New Roman", 25)) 
time.sleep(2)
trtl.clear()
trtl.goto(-222,70)
trtl.write("You will be shown 5 images at a time," ,font=("Times New Roman", 25))
time.sleep(2)
trtl.clear()
trtl.goto(-222,40)
trtl.write("and they will disappear after a set amount of time.", font=("Times New Roman", 25)) 
time.sleep(2)
trtl.clear()
trtl.goto(-222,10)
trtl.write("Try to guess what is missing!" ,font=("Times New Roman", 25)) 
time.sleep(2)
trtl.clear()
trtl.goto(-130,100)
trtl.write("Click anywhere to begin", font=("Times New Roman", 25)) 
trtl.hideturtle()

# click anywhere to begin and user will be asked for name
def click_anywhere(x, y):
    trtl.textinput("What is your name?", "")
    trtl.clear()
wn.onscreenclick(click_anywhere)'''
    
# import images
all_fruits = ["apple.gif", "banana.gif", "blueberry.gif", "strawberry.gif", "watermelon.gif"]
for fruit in all_fruits:
    wn.addshape(fruit)

apple_image = "apple.gif"
apple_trtl = trtl.Turtle()
apple_trtl.penup()

# timer
# timer will show how many seconds the user has left to memorize everything on the screen before 1 disappears
# timer will decrease every level by a few seconds

# score
# score will increase by one point every time the user types the missing item in correctly
# no points will be deducted for getting it wrong but only 1 chance to get it right
# either get the score or dont, user will be taken to the next level

# leaderboard
# user's name will be put in the leaderboard depending on their score








wn.mainloop()