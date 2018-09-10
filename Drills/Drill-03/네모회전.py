from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
def left_right():
        x = 40
        y = 0
        while (x < 760):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x, 90)
                x = x + 2
                delay(0.002)
def south_north():
        x = 0
        y = 0
        while (y + 90 <= 540):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(760, 90 + y)
                y = y + 2
                delay(0.002)
def right_left():
        x = 760
        while(40 <= x):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x, 540)
                x = x - 2
                delay(0.002)
def north_south():
        y = 540
        while(y >= 90):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(40, y)
                y = y - 2
                delay(0.002)
while (True):
        left_right()
        south_north()
        right_left()
        north_south()
close_canvas()
