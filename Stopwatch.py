# "Stopwatch: The Game"

import simplegui

# define global variables
count = 0
tot = 0
win = 0

# --------------------- helper functions ------------------------ 
# converts time in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t // 600
    B = (t // 100) % 6
    C = (t // 10) % 10
    D = t % 10
    return str(A) + ':' + str(B) + str(C) + '.' + str(D)

# returns current score
def score():
    return str(win) + '/' + str(tot)

# --------------------- event handlers ------------------------    
# buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
def stop():
    global tot, win
    if timer.is_running():
        timer.stop()
        tot += 1
        if (count % 10) == 0:
            win += 1
def reset():
    global count, tot, win
    timer.stop()
    count, tot, win = 0, 0, 0
# timer with 0.1 sec interval
def tick():
    global count
    count += 1
# draw handler
def draw(canvas):
    canvas.draw_text(format(count), (100, 110), 48, 'White')
    canvas.draw_text(score(), (240, 40), 36, 'Yellow')

# create frame, register event handlers, start frame  
frame = simplegui.create_frame('Stopwatch', 310, 200)

timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)
button1 = frame.add_button('Start', start, 100)
button2 = frame.add_button('Stop', stop, 100)
button3 = frame.add_button('Reset', reset, 100)

frame.start()

