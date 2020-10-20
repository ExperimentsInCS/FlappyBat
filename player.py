import os
import sys 
import pygame 

class Player(pygame.sprite.Sprite):
    PLAYER_X_OFFSET = 100
    PLAYER_JUMP_SPEED = -10
    PLAYER_SCALE = 0.25
    GRAVITY_FORCE = 0.02

    '''
    This class represents our player (a bat)
    '''

    def __init__(self, game):
        super().__init__()

        self.game = game 

        self.dead = False 

        # load the animation frames
        self.frames = self._load_frames()
        self.frame_num = 0
        self.image = self.frames[self.frame_num]

        self.rect = self.image.get_rect()
        self.rect.x = Player.PLAYER_X_OFFSET
        self.rect.y = game.DISPLAY_HEIGHT // 2 

        self.velocity_y = 0
    
    def _load_frames(self):
        return [
            self._load_frame('assets/bat-1.png'),
            self._load_frame('assets/bat-2.png'),
            self._load_frame('assets/bat-3.png'),
            self._load_frame('assets/bat-4.png'),
            self._load_frame('assets/bat-5.png')
        ]
    
    def _load_frame(self, filename):
        image = pygame.image.load(os.path.join(sys.path[0], filename))
        image_size = image.get_size()
        width = int(image_size[0] * Player.PLAYER_SCALE)
        height = int(image_size[1] * Player.PLAYER_SCALE)
        return pygame.transform.scale(image, (width, height))

    def reset(self):
        self.rect.y = self.game.DISPLAY_HEIGHT // 2
        self.velocity_y = 0
        self.dead = False 
    
    def is_dead(self):
        return self.dead 
    
    def flap(self):
        self.velocity_y = Player.PLAYER_JUMP_SPEED

    def update(self, delta_time):
        # update the vertical velocity and position
        self.velocity_y += Player.GRAVITY_FORCE * delta_time
        self.rect.y += self.velocity_y

        # check if fell off the screen
        if self.rect.y > self.game.DISPLAY_HEIGHT:
            self.dead = True 

        # update the image 
        self.image = self.frames[self.frame_num]

        # go to the next frame
        self.frame_num = (self.frame_num + 1) % len(self.frames)
