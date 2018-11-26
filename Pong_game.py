# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

VEL = 7 #regulate paddle's vel
CONST = 1.1 # increase ball's vel after paddle strike
REG = 40 # regulate ball's initial vel

# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists   
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [random.randrange(120 // REG, 240 // REG), - random.randrange(60 // REG, 180 // REG)]  
    if direction == LEFT:
        ball_vel[0] = - ball_vel[0]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, score1, score2, ball_vel  
    paddle1_pos = paddle2_pos = HEIGHT / 2
    paddle1_vel, paddle2_vel, score1, score2 = 0, 0, 0, 0   
    spawn_ball(random.choice([RIGHT, LEFT]))
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel    
    # ---- update paddles ---------
    check1 = paddle1_pos + paddle1_vel
    check2 = paddle2_pos + paddle2_vel
    # ------ update ball -------
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    # ------- determine whether ball collides with and bounces off of the top and bottom walls -------
    if (ball_pos[1] <= BALL_RADIUS + 1) or (ball_pos[1] >= HEIGHT - BALL_RADIUS - 1):
        ball_vel[1] = - ball_vel[1]
    # ----------- determine whether paddle and ball collide --------------------
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS + 1: # check whether ball hits left gutter
        if (ball_pos[1] < check1 - HALF_PAD_HEIGHT) or (ball_pos[1] > check1 + HALF_PAD_HEIGHT):
            score2 += 1
            spawn_ball(RIGHT)
        # Physics: if ball hits EDGES of left paddle, flip resultant vel
        #elif (ball_pos[1] == check1 - HALF_PAD_HEIGHT) or (ball_pos[1] == check1 + HALF_PAD_HEIGHT):
        #   ball_vel[0] = - CONST * ball_vel[0]
        # 	ball_vel[1] = - CONST * ball_vel[1]
         
        else: ball_vel[0] = - CONST * ball_vel[0]# if ball hits left paddle, flip x vel component  
    
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS - 1:# check whether ball hits right gutter
        if (ball_pos[1] < check2 - HALF_PAD_HEIGHT) or (ball_pos[1] > check2 + HALF_PAD_HEIGHT):
            score1 += 1
            spawn_ball(LEFT)
        # Physics: if ball hits EDGES of right paddle, flip resultant vel
        #elif (ball_pos[1] == check2 - HALF_PAD_HEIGHT) or (ball_pos[1] == check2 + HALF_PAD_HEIGHT):
        #   ball_vel[0] = - CONST * ball_vel[0]
        #   ball_vel[1] = - CONST * ball_vel[1]
                 
        else: ball_vel[0] = - CONST * ball_vel[0]# if ball hits right paddle, flip x vel component 
    
    # -------- update paddle's vertical position, keep paddle on the screen ----------------
    #left paddle
    if check1 < HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
    elif check1 > HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    else: paddle1_pos += paddle1_vel
    
    #right paddle    
    if check2 < HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    elif check2 > HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
    else: paddle2_pos += paddle2_vel
    
    # -------------- draw mid line and gutters -----------------
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, 'White')
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, 'White')
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, 'White')    
    
    # -------------- draw ball ------------------
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'Blue', 'White') 
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos - HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], [0, paddle1_pos + HALF_PAD_HEIGHT]], 1, 'Yellow', 'Yellow')
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT]], 1, 'Lime', 'Lime')   
    
    # draw scores
    canvas.draw_text(str(score1), (WIDTH / 2 - 65, 50), 48, 'Yellow', 'sans-serif')
    canvas.draw_text(str(score2), (WIDTH / 2 + 40, 50), 48, 'Lime', 'sans-serif')

def keydown(key):
    global paddle1_vel, paddle2_vel, VEL
    # left paddle
    if key == simplegui.KEY_MAP['W']:
        paddle1_vel -= VEL
    if key == simplegui.KEY_MAP['S']:
        paddle1_vel += VEL
    if (key == simplegui.KEY_MAP['W']) and (key == simplegui.KEY_MAP['S']):
        paddle1_vel = 0
    # right paddle
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel -= VEL
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel += VEL
    if (key == simplegui.KEY_MAP['up']) and (key == simplegui.KEY_MAP['down']):
        paddle2_vel = 0
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    # left paddle
    if (key == simplegui.KEY_MAP['W']) or (key == simplegui.KEY_MAP['S']):
        paddle1_vel = 0
    # right paddle
    if (key == simplegui.KEY_MAP['up']) or (key == simplegui.KEY_MAP['down']):
        paddle2_vel = 0

def restart():
    new_game()
    
# create frame
frame = simplegui.create_frame('Pong', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', restart)

# start frame
new_game()
frame.start()