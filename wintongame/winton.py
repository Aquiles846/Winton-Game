import pygame
import time
import random
import pygame.time

# initialize pygame
pygame.font.init()

# screen size
width, height = 1280, 720   
# screen
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("WINTON GAME")

# background
bg = pygame.image.load("winton.jpg")
bg = pygame.transform.scale(bg, (width, height))

bg1= pygame.image.load("winton_1.jpg")
bg1 = pygame.transform.scale(bg1, (width, height))

# player
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 10
#font
FONT = pygame.font.SysFont('comicsansms', 30)
#player rectangle
player = pygame.Rect(200, height - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)



#draw function
def draw(player, elapsed_time, stars, stars_yellow, win_counter):
    #draw background
    win.blit(bg, (0, 0))
    pygame.display.update()
    #draw time
    time_text = FONT.render("Time: " + str(round(elapsed_time)), 1, (255, 255, 255))
    win.blit(time_text, (10, 10))
    pygame.draw.rect(win, (255, 0, 0), player)
    pygame.display.update()
    #draw counter yellow stars
    counter_text = FONT.render("Yellow Stars: " + str(win_counter), 1, (255, 255, 255))
    win.blit(counter_text, (10, 40))
    pygame.display.update()
    #draw stars
    for star in stars:
        pygame.draw.rect(win, "green", star)
        pygame.display.update()
    #draw yellow stars
    for star in stars_yellow:
        pygame.draw.rect(win, "yellow", star)
        pygame.display.update()

#MENU
def menu():
    run = True
    while run:
        win.fill((0, 0, 0))
        #image
        win.blit(bg1, (0, 0))
        menu_text = FONT.render("Press any key to start", 1, (255, 255, 255))
        win.blit(menu_text, (width/2 - menu_text.get_width()/2, height/2 - menu_text.get_height()/2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                run = False 
                break


if __name__ == "__main__":  
    menu()
     

#main function
def main():
        #global variables
        run = True
        #time variables
        start_time = time.time()  
        elapsed_time = 0
        win_counter = 0
        #star variables
        star_add_increment = 2000
        star_add_increment_yellow = 2000
        star_count_yellow=0
        star_count=0
        stars = []
        stars_yellow = []   
        hit_green = False
        hit_yellow = False
        #player velocity
        PLAYER_VEL = 5
        STAR_VEL = 8
        STAR_WIDTH = 10
        STAR_HEIGHT = 20
        


        #game loop
        while run:
        

        
            #clock TICK TIME P
            clock = pygame.time.Clock()
            star_count += clock.tick(60)  
            star_count_yellow += clock.tick(60)
            elapsed_time = time.time() - start_time
            rango = 5
            #time increments IN SOME CASES CAN CAUSE ISSUES CAUSING THE BLOCK STACKING BETWEEN EACH OTHER, IN THAT CASE INCREASE OR REDUCE THE TIME SECIBDS TO MATCH THE SPAWN TIME BUT THIS SHOULD BE ENOUGH 
            if elapsed_time > 9:
                rango = 10
            if elapsed_time > 19:
                rango = 15
            if elapsed_time > 29:
                rango = 20
            if elapsed_time > 39:
                rango = 25
            if elapsed_time > 49:
                rango = 30
            if elapsed_time > 59:
                rango = 35
            if elapsed_time > 69:
                rango = 40
            if elapsed_time > 79:
                rango = 45
            if elapsed_time > 89:
                rango = 50


            #check for win
            if star_count_yellow > star_add_increment_yellow:
                for _ in range(rango):
                    star_x = random.randint(0, width - STAR_WIDTH)
                    star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                    stars_yellow.append(star)
                
                star_add_increment_yellow = max(200, star_add_increment_yellow - 50)    
                star_count_yellow = 0  

            #check for win
            if star_count > star_add_increment:
                for _ in range(rango):
                    star_x = random.randint(0, width - STAR_WIDTH)
                    star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                    stars.append(star)

                star_add_increment = max(200, star_add_increment - 50)    
                star_count = 0

        
            #check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            
            #WASD CONTROLS
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and player.x - PLAYER_VEL > 0:  # left
                player.x -= PLAYER_VEL
            if keys[pygame.K_d] and player.x + PLAYER_VEL < width - PLAYER_WIDTH: # right
                player.x += PLAYER_VEL
            if keys[pygame.K_w] and player.y - PLAYER_VEL > 0: # up
                player.y -= PLAYER_VEL
            if keys[pygame.K_s] and player.y + PLAYER_VEL < height - PLAYER_HEIGHT: # down
                player.y += PLAYER_VEL

            #key arrows controls
            if keys[pygame.K_LEFT] and player.x - PLAYER_VEL > 0:  # left
                player.x -= PLAYER_VEL
            if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL < width - PLAYER_WIDTH: # right
                player.x += PLAYER_VEL
            if keys[pygame.K_UP] and player.y - PLAYER_VEL > 0: # up
                player.y -= PLAYER_VEL
            if keys[pygame.K_DOWN] and player.y + PLAYER_VEL < height - PLAYER_HEIGHT: # down
                player.y += PLAYER_VEL



        
            #green stars   
            for star in stars[:]:
                star.y += STAR_VEL
                if star.y > height:
                    stars.remove(star)
                elif star.y + star.height >= player.y and star.colliderect(player):
                    stars.remove(star)
                    hit_green = True
                    break
                if hit_green:
                    lost_text = FONT.render("You Lost! NOOB!", 1, (255, 255, 255))
                    #draw in center of the screen
                    win.blit(lost_text, (width/2 - lost_text.get_width()/2, height/2 - lost_text.get_height()/2))
                    pygame.display.update()
                    #stops time clock
                    clock.tick(0)

                    pygame.time.delay(2000)
                    break

            #yellow stars        
            for star in stars_yellow[:]:
                star.y += STAR_VEL
                if star.y > height:
                    stars_yellow.remove(star)
                elif star.y + star.height >= player.y and star.colliderect(player):
                    stars_yellow.remove(star)
                    win_counter += 1
                    hit_yellow = True
                    break
                if hit_yellow and win_counter == 2000:
                    win_text = FONT.render("You Win!", 1, (255, 255, 255))
                    #draw in center of the screen
                    win.blit(win_text, (width/2 - win_text.get_width()/2, height/2 - win_text.get_height()/2))
                    pygame.display.update()
                    clock.tick(0)
                    pygame.time.delay(2000)
                    break

            #draw        
            draw(player, elapsed_time, stars, stars_yellow, win_counter)  
        #quit pygame
        pygame.quit()

#run main
if __name__ == "__main__":
    # run main function
    main()



