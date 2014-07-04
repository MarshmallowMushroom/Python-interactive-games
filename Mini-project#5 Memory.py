# implementation of card game - Memory

import simplegui
import random

card_list = range(0,8) + range(0,8)
#random.shuffle(card_list)
exposed = []
#exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
compare_list = []
state = 0
counter = 0

# helper function to initialize globals
def new_game():
    global exposed, counter, card_list
    i = 0
    while (i < 16):
        exposed.append(False)
        i += 1
    random.shuffle(card_list)
    #exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    counter = 0 
     
# define event handlers
def mouseclick(pos):
    global state, compare_list, exposed, card_list, counter
    for i in range(len(card_list)):
        if pos[0] >= 50*i and pos[0] <= (50+50*i) and exposed[i]== False:
            exposed[i] = True
            compare_list.append(i)
            if state ==0:
                state = 1
            elif state == 1:
                state = 2
                counter += 1 # counter is incremented after the second card is flipped during a turn
            else:
                if card_list[compare_list[-2]] != card_list[compare_list[-3]]:
                    exposed[compare_list[-2]] = False
                    exposed[compare_list[-3]]= False
                state = 1                
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed
    for i in range(len(card_list)):
        if exposed[i] == True:
            canvas.draw_text(str(card_list[i]),(25+50*i,50), 30, "White")
        else:
            canvas.draw_polygon([(0+50*i,0),(50+50*i,0),(50+50*i,100),(0+50*i,100)],2, "Yellow", "Green")
    label.set_text("Turns = " + str(counter)) # draw the label text
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

