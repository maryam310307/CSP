import turtle as trtl
import random as rand
import time as time
wn = trtl.Screen()


# Start Screen
# set background for starting screen, title, and explain the game
writer = trtl.Turtle()
fruit_turtles = []
fruits_list = ["apple.gif", "banana.gif", "blueberry.gif", "strawberry.gif", "watermelon.gif"]
random_index = rand.randint(0, len(fruits_list)-1)
missing_fruit = fruits_list.pop(random_index)


trtl.penup()
writer.hideturtle()
trtl.goto(-222,200)
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


# click anywhere to begin and user will be asked for name
def click_anywhere(x, y):
    wn.onclick(None)
    trtl.textinput("What is your name?", "")
    trtl.clear()

    wn.addshape("apple.gif")
    apple_image = trtl.Turtle()
    apple_image.shape("apple.gif")
    apple_image.penup()
    apple_image.goto(150,300)

    wn.addshape("banana.gif")
    banana_image = trtl.Turtle()
    banana_image.shape("banana.gif")
    banana_image.penup()
    banana_image.goto(-100,-100)

    wn.addshape("blueberry.gif")
    blueberry_image = trtl.Turtle()
    blueberry_image.shape("blueberry.gif")
    blueberry_image.penup()
    blueberry_image.goto(-300,250)

    wn.addshape("strawberry.gif")
    strawberry_image = trtl.Turtle()
    strawberry_image.shape("strawberry.gif")
    strawberry_image.penup()
    strawberry_image.goto(-370,-200)

    wn.addshape("watermelon.gif")
    watermelon_image = trtl.Turtle()
    watermelon_image.shape("watermelon.gif")
    watermelon_image.penup()
    watermelon_image.goto(280,-90)

    time.sleep(5)
    strawberry_image.hideturtle()

    while True:
        missing_fruit = trtl.textinput("Which fruit went missing?", "")
        if missing_fruit.strip().lower() == missing_fruit:
            update_score()
            break
        else:
            pass
            
wn.onscreenclick(click_anywhere)
    


# import images


# timer
# timer will show how many seconds the user has left to memorize everything on the screen before 1 disappears
# timer will decrease every level by a few seconds
score = 0
font_setup = ("Times New Roman", 50, "normal")

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(370,300)
score_writer.write(score,font=font_setup) 

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write("Score: " +str(score), font=font_setup)










# score
# score will increase by one point every time the user types the missing item in correctly
# no points will be deducted for getting it wrong but only 1 chance to get it right
# either get the score or dont, user will be taken to the next level

# leaderboard
# user's name will be put in the leaderboard depending on their score








wn.mainloop()