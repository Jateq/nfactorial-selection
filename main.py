import pygame
import math

# initialize pygame
pygame.init()

# set up the window
window_size = (800, 600)
window_size1 = (800, 550)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("I Bet You can't draw perfect circle")

# set up the colors
BLACK = (0, 0, 0)
GREY = (35, 35, 35)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
CYAN = (0, 120, 150)

GREEN = (0, 255, 0)
LIME = (36, 216, 35)
YELLOW = (255, 255, 0)
ORANGE = (255, 127, 0)
RED = (255, 0, 0)

color = LIME
font = pygame.font.Font(None, 30)
font1 = pygame.font.Font(None, 40)
# set up the brush window_size
brush_size = 3
brush_first = 7
radiuserror = 10
radius = 0

center_x = window_size[0]//2
center_y = window_size[1]//2 
center = (center_x,center_y)


dot_color = (255, 0, 0)  # red
dot_radius = 10
# set up the drawing surface
screen.fill(GREY)
drawing_surface = pygame.Surface(window_size)
drawing_surface.fill(GREY)

mouse_first_tick = None
last_pos = 0
first_pos = None
current_pos = (1000,1000)
joke = 0
firstdist = None
quality = 100
percentage = 0.0
difference = 0

# def findrad(){
#         center = 
# }
# main loop
running = True
while running:
    
    lose = False
    win = False
    totaleps = 0
    epspoints = 0
    pygame.draw.circle(drawing_surface, WHITE, center, dot_radius) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                pygame.draw.circle(drawing_surface, color, event.pos, brush_size)
                
        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]: 
                
                current_pos = pygame.mouse.get_pos()
                
                if first_pos == None:
                    first_pos = pygame.mouse.get_pos()
                    pygame.draw.circle(drawing_surface, color, event.pos, brush_first)
                    epspoints += 1
                
                distance = math.sqrt((current_pos[0]-center[0])**2 + (current_pos[1]-center[1])**2)
                
                if distance < dot_radius+20:
                    error_message = font.render("Too close to center!", True, RED)
                    screen.blit(error_message, (window_size[0]//2-100, 10))
                    pygame.display.flip()
                    lose = True
                
                if firstdist is None:
                    firstdist = math.sqrt((first_pos[0]-center[0])**2 + (first_pos[1]-center[1])**2)
                    
                epsilon = abs(firstdist-distance) 
                difference = firstdist-distance
                if difference < 5:
                    color = GREEN
                if difference > 5 and difference < 10:
                    color = LIME
                if difference >10 and difference <15:
                    color = YELLOW
                if difference >15 and difference <20:
                    color = ORANGE
                if difference > 20:
                    color = RED
                totaleps += epsilon
                epspoints +=1
                
                percentage = (100-(totaleps/(epspoints*firstdist))*100 )
                percentage = round(percentage, 1)
                

                if firstdist+70 < distance:
                    error_message = font.render("Wrong way", True, RED)
                    screen.blit(error_message, (window_size[0] // 2 - 56 , window_size[1]//2+30))
                    pygame.display.flip()
                    lose = True
                
                pygame.draw.circle(drawing_surface, color, event.pos, brush_size)
                
               

            if mouse_first_tick is None:
                mouse_first_tick = pygame.time.get_ticks()
            last_pos = pygame.time.get_ticks()
            
            # if the time between the first click and the last click is greater than 10 seconds, break out of the loop and display an error message
            if last_pos - mouse_first_tick > 7000:
                error_message = font.render("Too slow", True, RED)
                screen.blit(error_message, (window_size[0] // 2 - 42 , window_size[1]//2+30))
                pygame.display.flip()
                lose = True
            percentage_text = font1.render("{}%".format(percentage), True, WHITE)
            screen.blit(percentage_text, (window_size[0]//2-30, window_size[1]//2-50))
            # pygame.display.flip()   
            # screen.blit(percentage_text, (0,0)) 
            
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                drawing_surface.fill(GREY)
                mouse_first_tick = None
                last_pos = 0
                first_pos = None
                joke = 0
                firstdist = None
                color = GREEN

        if first_pos is not None:
            joke+=1
        if joke > 100:
            colis = math.sqrt((current_pos[0]-first_pos[0])**2 + (current_pos[1]-first_pos[1])**2)
            if colis < brush_first:
                win =True
            dist = math.sqrt((current_pos[0]-center[0])**2 + (current_pos[1]-center[1])**2)
        
        
        while win:
            message = font.render("good job", True, GREEN)
            screen.blit(message, (window_size[0] // 2 - 42 , window_size[1]//2+30))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        win = False
                        mouse_first_tick = None
                        last_pos = 0
                        drawing_surface.fill(GREY)
                        first_pos = None
                        joke = 0
                        firstdist = None
                        color = GREEN


        while lose:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        lose = False
                        mouse_first_tick = None
                        last_pos = 0
                        drawing_surface.fill(GREY)
                        first_pos = None
                        joke = 0
                        firstdist = None
                        color = GREEN

        pygame.display.flip()
    
    screen.blit(drawing_surface, (0, 0))
    # error messages
    

        
    

    
    
    
    # update the display
    # pygame.display.update()
