#The values for each color range from 0 – 255, a total of 256 values
#color3 = pygame.Color(128, 128, 128)   # Grey
#color4 = pygame.Color(255, 0, 0)       # Red

import pygame
import random
pygame.init()
white=(255,255,255)      #color_light = (170,170,170)
                          #color_dark = (100,100,100)
                           #color_white = (255,255,255) 
red=(255,0,0)
black=(0,0,0)
screen_width=900
screen_height=600

gameWindow=pygame.display.set_mode((screen_width,screen_height))
#game title
pygame.display.set_caption("saakshi with snakes")
pygame.display.update()

exit_game=False
game_over=False
snake_x=45
snake_y=55
velocity_x = 0
velocity_y = 0
snake_size=10
score=0
init_velocity=5
food_x=random.randint(20,screen_width/2)
food_y=random.randint(20,screen_height)/2
fps=30

font = pygame.font.SysFont(None, 55)   #There are generally two different ways to use fonts in pygame. pygame.font.Font() and pygame.font.SysFont(). The difference between the two of them is that pygame.font.Font() requires the file path for a font to be passed into it’s parameters whereas pygame.font.SysFont() just requires the name of the font. 

#pygame.font.Font("arial.ttf", 20)
#The first parameter is the file path, and the second is the font size.
#The obvious benefit of this is that there is no chance of the font you’ve selected not being available.
#font = pygame.font.Font(None, size)

#Pygame.font.SysFont()
#If you’re not looking to be including any ttf files in your code, we then turn to using pygame.font.SysFont(). This is the #method I personally recommend and use in my own pygame programs.
#dialogue_font = pygame.font.SysFont('arial', 15)
#name_font = pygame.font.SysFont('Helvetica', 20)
#game_over_font = pygame.font.SysFont('Verdana', 60)
#The SysFont() function only requires the name of the font, not the file path. For this reason the ttf extension is not included. The second parameter remains the same however, representing font size.





#render()
#draw text on a new Surface
#render(text, antialias, color, background=None) -> Surface 
#The antialias argument is a boolean. If true the characters will have smooth edges.
#This creates a new Surface with the specified text rendered on it. pygame provides no way to directly draw text on an existing Surface: instead you must use Font.render() to create an image (Surface) of the text, then blit this image onto another Surface.

def text_screen(text, color, x, y): #what should i print,in which colour,kaha par, kaha par
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])             #updates screen

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


snk_list = []
snk_length = 1

clock=pygame.time.Clock()
#while True:
    #pygame.display.update()
    #for event in pygame.event.get():
       # if event.type == QUIT:
          #  pygame.quit()
           # sys.exit()
#We call both pygame.quit() and sys.exit() to close the pygame window and the python script respectively. Simply using sys.#exit() can cause your IDE to hang due to a bug.

#A Pygame “Event” occurs when the user performs a specific action, such as clicking his mouse or pressing a keyboard button. Pygame records each and every event that occurs.

#We can find out which events have happened by calling the pygame.event.get() function (shown previously), which returns a ##list of pygame.event.Event objects (which we will just call Event objects for short).

#One of the many attributes (or properties) held by event objects is type. The type attribute tells us what kind of event #the object represents.
#If you take a look at the example shown earlier, you’ll see we used event.type == QUIT to determine whether the game was to #be closed or not. We can even create our own custom events to signal certain types of events (such as an enemy spawning).



while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:     
            exit_game=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x+=init_velocity
                velocity_y=0
            
            if event.key == pygame.K_LEFT:
                velocity_x-=init_velocity
                velocity_y=0
            
            if event.key == pygame.K_UP:
                velocity_y-=init_velocity
                velocity_x=0
            
            if event.key == pygame.K_DOWN:
                velocity_y+=init_velocity
                velocity_x=0

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y
    if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
        score +=1
        food_x = random.randint(20, screen_width / 2)
        food_y = random.randint(20, screen_height / 2)
        snk_length += 5
        

    gameWindow.fill(white)
    text_screen("Score: " + str(score * 10), red, 5, 5)    #calling func
                                                            #def text_screen(text, color, x, y): 
                                                            #screen_text = font.render(text, True, color)
                                                            #gameWindow.blit(screen_text, [x,y])    
    pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
    #gamewindow=where to have rectangle   black=whcih colour of rectangle  
    pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
                                    #  xand y coordinate #length       height
    pygame.display.update()
    clock.tick(fps)



pygame.quit()
quit()