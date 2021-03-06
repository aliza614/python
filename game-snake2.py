import random
import curses
#SET SCREEN
#initalie screen
screen =curses.initscr()
#cursor does not show up
curses.curs_set(0)

screen_height, screen_width =screen.getmaxyx()
#uses height and width of screen starting in top left hand corner
window=curses.newwin(screen_height,screen_width, 0,0)
#accepts keypad input
window.keypad(1)
#100 miliseconds refresh
window.timeout(100)

#SET UP SNAKE
snk_x=screen_width/4
snk_y=screen_height/2
snake = [
   [snk_y,snk_x],
   [snk_y,snk_x-1],
   [snk_y,snk_x-2]
]
#inital dierection of snake
key =curses.KEY_RIGHT

#SETUP SNACK
snack=[screen_height/2, screen_width/2]
window.addch(int(snack[0]), int(snack[1]), curses.ACS_DIAMOND)


while True:
    #get character input
    next_key=window.getch()
    key=key if next_key == -1 else next_key

    #if they lost the game
    if snake[0][0] in [0, screen_height] or snake[0][1] in [0,screen_width] or snake[0] in snake [1:]:
        curses.endwin()
        quit()

    new_head=[snake[0][0],snake[0][1]]

    if key==curses.KEY_DOWN:
        new_head[0]+=1

    if key==curses.KEY_UP:
        new_head[0]-=1
    
    if key==curses.KEY_RIGHT:
        new_head[1]+=1
    
    if key==curses.KEY_LEFT:
        new_head[1]-=1

    snake.insert(0,new_head)

    if snake[0]==snack:
        snack=None
        while snack is None:
           new_snack=[random.randint(0,screen_height-1), random.randint(0,screen_width-1)]

           snack=new_snack if new_snack not in snake else None

        window.addch(snack[0], snack[1],curses.ACS_CKBOARD)

    else:
        tail=snake.pop()
        window.addch(int(tail[0]),int(tail[1]),' ')
    window.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
