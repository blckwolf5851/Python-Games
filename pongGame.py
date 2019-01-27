# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 5
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = False

ball_pos = [300,200]
ball_vel = [0,-1]

pad1_pos = 0
pad2_pos = 0
pad1_vel = 0
pad2_vel = 0

p1_score = 0
p2_score = 0

gravity_on = False
gravity = 0.02

#add vectors

def add_vectors(v1, v2):
    v3=[0,0]
    v3[0] = v1[0] + v2[0]
    v3[1] = v1[1] + v2[1]
    return v3

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball():
    global ball_pos, ball_vel, LEFT # these are vectors stored as lists
    ball_pos = [300,200]
    if LEFT:
        ball_vel[0] = -1.5
        ball_vel[1] = -random.random()*2.5+-0.2
    else:
        ball_vel[0] = 1.5
        ball_vel[1] = -random.random()*2.5+-0.2


#define reset
def reset():
    global p1_score, p2_score, pad1_pos, pad2_pos
    p1_score = 0
    p2_score = 0
    pad1_pos = 0
    pad2_pos = 0
    spawn_ball()

#gavity mode

def gravity_mode():
    global gravity_on
    reset()
    if gravity_on:
        gravity_on = False
    else:
        gravity_on = True


#update locations
def tick():
#ball
    global ball_pos, p1_score, p2_score, pad1_pos, pad2_pos, LEFT
    ball_pos = add_vectors(ball_pos, ball_vel)
    if gravity_on:
        ball_vel[1] += gravity
#ball wall bounce
    if ball_pos[1] > HEIGHT - BALL_RADIUS or ball_pos[1] < BALL_RADIUS:
        ball_vel [1] = -ball_vel [1]

#ball paddle1 bounce
    if ball_pos[0] - BALL_RADIUS < PAD_WIDTH:
        if pad1_pos < ball_pos[1] and ball_pos[1] < pad1_pos + PAD_HEIGHT:
            ball_vel [0] = -ball_vel[0]*1.08
            ball_vel [1] *= 1.08
        else:
            p2_score +=1
            LEFT = False
            new_game()

#ball paddle2 bounce
    if ball_pos[0] + BALL_RADIUS > WIDTH - PAD_WIDTH:
        if pad2_pos < ball_pos[1] and ball_pos[1] < pad2_pos + PAD_HEIGHT:
            ball_vel [0] = -ball_vel [0]*1.08
            ball_vel [1] *= 1.08
        else:
            p1_score +=1
            LEFT = True
            new_game()
#ball update
    if ball_pos[1] + BALL_RADIUS > HEIGHT:
        ball_pos [1] = HEIGHT - BALL_RADIUS - 2
    if ball_pos[1] - BALL_RADIUS < 0:
        ball_pos [1] = BALL_RADIUS + 2
#paddle move
    pad1_pos = pad1_pos + pad1_vel
    pad2_pos = pad2_pos + pad2_vel

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball()

def draw(canvas):
    global score1, score2, pad1_pos, pad2_pos, ball_pos, ball_vel

    # draw scores
    canvas.draw_text(str(p1_score), [140, 50], 50, "red")
    canvas.draw_text(str(p2_score), [430, 50], 50, "red")

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'White','White')

    # update paddles
    if pad1_pos<0:
        pad1_pos = 0
    if pad2_pos<0:
        pad2_pos = 0
    if pad1_pos > HEIGHT - PAD_HEIGHT:
        pad1_pos = HEIGHT - PAD_HEIGHT
    if pad2_pos > HEIGHT - PAD_HEIGHT:
        pad2_pos = HEIGHT - PAD_HEIGHT

    # ball update



    # draw paddles
    canvas.draw_polygon([[0, pad1_pos],
                        [PAD_WIDTH, pad1_pos],
                        [PAD_WIDTH, pad1_pos + PAD_HEIGHT],
                        [0, pad1_pos + PAD_HEIGHT]], 1, 'White','White')

    canvas.draw_polygon([[WIDTH - PAD_WIDTH, pad2_pos],
                        [WIDTH, pad2_pos],
                        [WIDTH, pad2_pos + PAD_HEIGHT],
                        [WIDTH - PAD_WIDTH, pad2_pos + PAD_HEIGHT]], 1, 'White','White')



def keydown(key):
    global pad1_vel, pad2_vel
    if key == simplegui.KEY_MAP['up']:
        pad2_vel = -2
    if key == simplegui.KEY_MAP['down']:
        pad2_vel = 2
    if key == simplegui.KEY_MAP['w']:
        pad1_vel = -2
    if key == simplegui.KEY_MAP['s']:
        pad1_vel = 2

def keyup(key):
    global pad1_vel, pad2_vel
    if key == simplegui.KEY_MAP['up']:
        pad2_vel = 0
    if key == simplegui.KEY_MAP['down']:
        pad2_vel = 0
    if key == simplegui.KEY_MAP['w']:
        pad1_vel = 0
    if key == simplegui.KEY_MAP['s']:
        pad1_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button('reset', reset, 100)
frame.add_button('toggle gravity', gravity_mode, 100)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer = simplegui.create_timer(10,tick)


# start frame
new_game()
frame.start()
timer.start()
