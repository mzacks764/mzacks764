

from graphics import Canvas
import time
import random

WIDTH = 400
HEIGHT = 400
SIZE = 20
DELAY = 0.3

def main():
    # create the canvas
    canvas = Canvas(WIDTH, HEIGHT,"babysnake")
    snake = create_snake(canvas)
    goal = create_goal(canvas)
    x_coord = canvas.get_left_x(snake)
    key_press = 'Right'
    while True:
        key_press = move_snake(canvas,snake,key_press)

        #Need to out out of bounds check here
        if check_bounds(canvas,snake):
            print(f'You went off the Canvas.  Your turn is over')
            break


        if find_collision(canvas,snake,goal):
            move_goal(canvas,goal)
        canvas.update()  # this causes canvas to redraw after each move

        # If no key pressed during loop, continue to use last key
        # selected for next loop.  Otherwise, use new key to set movement
        # in next loop
        new_key_press = get_key_press(canvas, key_press)
        if new_key_press != None:
            key_press = new_key_press

        time.sleep(DELAY)   # pauses to allow user to see change


    # canvas.mainloop() required to wait for the user to close the window
    canvas.mainloop()

def create_snake(canvas):
    left_x = 0
    top_y = 0
    right_x = left_x + SIZE
    bottom_y = top_y + SIZE

    snake = canvas.create_rectangle(
        left_x,
        top_y,
        right_x,
        bottom_y,
        "blue"
    )
    return snake

def create_goal(canvas):
    left_x = 200
    top_y = 200
    right_x = left_x + SIZE
    bottom_y = top_y + SIZE

    goal = canvas.create_rectangle(
        left_x,
        top_y,
        right_x,
        bottom_y,
        "yellow"
    )
    return goal


def move_snake(canvas,snake,key_press):
    if key_press == "Left":
        canvas.move(snake,-20,0)
    if key_press == "Right":
        canvas.move(snake,20,0)
    if key_press == "Up":
        canvas.move(snake, 0, -20)
    if key_press == "Down":
        canvas.move(snake, 0, 20)
    return key_press


def get_key_press(canvas, key_press):

    presses = canvas.get_new_key_presses()
    for press in presses:
        if press.keysym == 'Up':
            return 'Up'
            #print('up arrow pressed!')
        if press.keysym == 'Down':
            return 'Down'
            #print('down arrow pressed!')
        if press.keysym == 'Right':
            #print('right arrow pressed!')
            return 'Right'
        if press.keysym == 'Left':
           # print('left arrow pressed!')
            return 'Left'


def find_collision(canvas, snake, goal):
    snake_x = canvas.get_left_x(snake)
    snake_y = canvas.get_top_y(snake)
    goal_x = canvas.get_left_x(goal)
    goal_y =  canvas.get_top_y(goal)
    if (snake_x == goal_x) and  (snake_y == goal_y):
        print(f'snake and goal have collided')
        return True
        b

def move_goal(canvas,goal):
    x_coord = gen_mult_twenty()
    y_coord = gen_mult_twenty()
    canvas.moveto(goal,x_coord, y_coord)


def gen_mult_twenty():
    max_mult =int(WIDTH/SIZE)-1
    rand_mult = int(random.randint(0,max_mult))
    rand_mult_20 = rand_mult*20
    return rand_mult_20

def check_bounds(canvas,snake):
    x_coor = canvas.get_left_x(snake)
    y_coor = canvas.get_top_y(snake)
    if x_coor < 0 or x_coor >= WIDTH + SIZE \
        or y_coor <0 or y_coor >= HEIGHT+SIZE:
            #print(f'out of bounds')
            return True


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
