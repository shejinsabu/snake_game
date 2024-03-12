#Shejin Sabu
#Snake Game
#started on 3/5/24
#ended on 3/11/24
from tkinter import *
import random


GAME_WIDTH = 650
GAME_HEIGHT = 650
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag = "snake")
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_oval(x,y, x + SPACE_SIZE, y  + SPACE_SIZE, fill = FOOD_COLOR, tag = "food")


def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR)
    snake.squares.insert(0, square)


    if x  == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text = "Score:{}".format(score))
        canvas.delete("food")
        food = Food()


    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_coll(snake):
        game_over()
    else:
     window.after(SPEED, next_turn, snake, food)

def change_direct(new_direct):
    global direction

    if new_direct == 'left':
        if direction != 'right':
            direction = new_direct
    elif new_direct == 'right':
        if direction != 'left':
            direction = new_direct
    elif new_direct == 'up':
        if direction != 'down':
            direction = new_direct
    elif new_direct == 'down':
        if direction != 'up':
            direction = new_direct

def check_coll(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return TRUE
    elif y < 0 or y >= GAME_HEIGHT:
        return TRUE
    

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return TRUE
    return FALSE


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font = ('consolas', 70), text = "GAME OVER LOSER!", fill = "red", tag = "game_over")


window = Tk()
window.title("Snake~Game! - Shejin Sabu")
window.resizable(False, False)

score = 0
direction = 'down'
label = Label(window, text = "Score:{}".format(score), font = ('consolas', 40))
label.pack()

canvas = Canvas(window, bg = BACKGROUND_COLOR, height = GAME_HEIGHT, width = GAME_WIDTH)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.bind('<Left>', lambda event: change_direct('left'))
window.bind('<Right>', lambda event: change_direct('right'))
window.bind('<Up>', lambda event: change_direct('up'))
window.bind('<Down>', lambda event: change_direct('down'))

snake = Snake()
food = Food()
next_turn(snake, food)

window.mainloop()