# "Stopwatch: The Game"

import simplegui
import time

# define global variables
current_time = 0
format_time = 0
success_stops = 0
total_stops = 0
timer_running = True


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(current_time):
    """A stands for minutes, B&C stand for seconds, 
    D stands for tenths of second"""
    global D
    D = current_time%10
    B = int((current_time%600)/100)
    C = int(((current_time%600)/10)%10)
    A = int(current_time/600)
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global timer_running
    timer_running = True
    timer.start()

def stop_handler():
    global D
    global success_stops
    global total_stops
    global timer_running
    if timer_running == True:
        total_stops += 1
        if D == 0:
            success_stops += 1
    timer_running = False
    timer.stop()
        
def reset_handler():
    global current_time
    global success_stops
    global total_stops
    global timer_running
    timer_running = False
    current_time =0
    success_stops = 0
    total_stops = 0
    timer.stop()
    draw_handler
 
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global current_time
    current_time += 1
    #return format(current_time)
   
# define draw handler
def draw_handler(canvas):
    global current_time
    global success_stops
    global total_stops
    score = str(success_stops) + "/" + str(total_stops)
    canvas.draw_text(format(current_time),(100,150),45, "White")
    canvas.draw_text(str(score), (250, 30), 30, "Red")
    
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 300)
frame.set_canvas_background("Black")
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.set_draw_handler(draw_handler)
start_button = frame.add_button("Start", start_handler, 100)
stop_button = frame.add_button("Stop", stop_handler, 100)
reset_button = frame.add_button("Reset", reset_handler, 100)


# start frame
frame.start()



