from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
delta = 0
r = 200
while (True) :
    while (x < 800 and y < 300) :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 4
        delta = math.sqrt((400 - x)**2 + (300 - y)**2) 
        y = y + (delta - r)
        if (x > 800) :
            x = 800
        delay(0.002)
        
    while (x > 400 and y < 600) :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y + 4
        delta = math.sqrt((400 - x)**2 + (300 - y)**2)
        if ( r > delta) :
            x = x - (r - delta)
        else :
            x = x - (delta - r)
        delay(0.002)
    
    while (x > 0 and y > 300) :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 4
        delta = math.sqrt((400 - x)**2 + (300 - y)**2) 
        if ( r > delta) :
            y = y - (r - delta)
        else :
            y = y - (delta - r)
        delay(0.002)
        
    while (x < 400 and y > 90) :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 4
        delta = math.sqrt((400 - x)**2 + (300 - y)**2)
        if ( r > delta) :
            y = y - (r - delta)
        else :
            y = y - (delta - r)
        delay(0.002)

close_canvas()    
