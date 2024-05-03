import pygame
import random


screen_width =  600
screen_height = 600



class SpaceRocks:
    def __init__(self) :
        self.init_pygame()
        self.screen =pygame.display.set_mode((screen_width,screen_height))

        self.player_size=20
        self.player_x=screen_width//2
        self.player_y=screen_height//2
        self.player_img=pygame.image.load(r"C:\Users\e.saeed\Desktop\Project D\spaceship.gif")
        self.player_img=pygame.transform.scale(self.player_img,(50,50))

        self.bullets=[]
        self.bullet_size=5
        self.bullet_speed=1

        self.background_img=pygame.image.load(r"C:\Users\e.saeed\Desktop\Project D\background.jpg")
        self.background_img=pygame.transform.scale(self.background_img,(screen_width,screen_height))

        self.asteroids=[]
        self.asteroids_speed=0.25
    
    def main_loop(self):
        while True:
            self.handle_input()
            self.process_game_logic()
            self.draw()
    
    def init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Asteroids")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
      

    def handle_input(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

    def process_game_logic(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_x -=0.5
        if keys[pygame.K_RIGHT]:
            self.player_x +=0.5
        if keys[pygame.K_DOWN]:
            self.player_y +=0.5
        if keys[pygame.K_UP  ]:
            self.player_y -=0.5
        
        if self.player_x<0:
            self.player_x=0
        if self.player_x>screen_width-50:
            self.player_x=screen_width-50
        if self.player_y<0:
            self.player_y=0
        if self.player_y>screen_height-50:
            self.player_y=screen_height-50
            
        ## Asteroids
        if random.randint(0,100)<1:
            asteroid_x= random.randint(0,screen_width)
            asteroid_y=0
            asteroid_speed_x=random.randint(-1,1)
            asteroid_speed_y=random.randint(-1,1)
            self.asteroids.append((asteroid_x,asteroid_y,asteroid_speed_x,asteroid_speed_y))
        
        for i in range(len(self.asteroids)):
            asteroid=self.asteroids[i]
            new_x= asteroid[0]+asteroid[2]*asteroid_speed_x
            new_y= asteroid[1]+asteroid[3]*asteroid_speed_y
            self.asteroids[i]=(new_x,new_y,asteroid[2],asteroid[3])


    def draw(self):
        self.screen.blit(self.background_img,(0,0))
        self.screen.blit(self.player_img,(self.player_x,self.player_y))
        for asteroid in self.asteroids:
            x,y=int(asteroid[0]),int(asteroid[1])
            pygame.draw.circle(self.screen,(255,0,0),(x,y),10)
        pygame.display.flip()

game=SpaceRocks()
game.main_loop()
