import os 
import sys 
import pygame 
import random 

class Obstacle(pygame.sprite.Sprite):
    TOP_OBSTACLE_LEFT_OFFSET = 50
    TOP_OBSTACLE_WIDTH = 140
    TOP_OBSTACLE_HEIGHT = 145

    BOTTOM_OBSTACLE_LEFT_OFFSET = 65
    BOTTOM_OBSTACLE_TOP_OFFSET = 370
    BOTTOM_OBSTACLE_WIDTH = 140
    BOTTOM_OBSTACLE_HEIGHT = 125

    MIN_OBSTACLE_X_OFFSET = 0
    MAX_OBSTACLE_X_OFFSET = 200
    MIN_OBSTACLE_Y_OFFSET = -128
    MAX_OBSTACLE_Y_OFFSET = 0

    OBSTACLE_1_INITIAL_POS = 200
    OBSTACLE_2_INITIAL_POS = 500
    OBSTACLE_3_INITIAL_POS = 800
    
    MAP_SCROLL_SPEED = -2

    '''
    This class represents the obstacles/corridors to navigate our bird through.
    '''
    
    def __init__(self, game, x_offset = -1):
        super().__init__()

        self.game = game 

        self.image = pygame.image.load(os.path.join(sys.path[0], 'assets/obstacle.png'))

        self.rect = self.image.get_rect()
        self._randomize_position()      
        if x_offset >= 0:
            self.rect.x = x_offset

    def _randomize_position(self):
        self.rect.x = random.randint(
            self.game.DISPLAY_WIDTH + Obstacle.MIN_OBSTACLE_X_OFFSET,
            self.game.DISPLAY_WIDTH + Obstacle.MAX_OBSTACLE_X_OFFSET,
        )
        self.rect.y = random.randint(
            Obstacle.MIN_OBSTACLE_Y_OFFSET,
            Obstacle.MAX_OBSTACLE_Y_OFFSET,
        )

    def set_x_offset(self, x_offset):
        self.rect.x = x_offset

    def get_collision_rects(self):
        top_rect = pygame.Rect(
            self.rect.x + Obstacle.TOP_OBSTACLE_LEFT_OFFSET,
            self.rect.y,
            Obstacle.TOP_OBSTACLE_WIDTH,
            Obstacle.TOP_OBSTACLE_HEIGHT
        )
        bottom_rect = pygame.Rect(
            self.rect.x + Obstacle.BOTTOM_OBSTACLE_LEFT_OFFSET,
            self.rect.y + Obstacle.BOTTOM_OBSTACLE_TOP_OFFSET,
            Obstacle.BOTTOM_OBSTACLE_WIDTH,
            Obstacle.BOTTOM_OBSTACLE_HEIGHT
        )
        return top_rect, bottom_rect

    def does_collide(self, player_rect):
        top, bottom = self.get_collision_rects()
        return top.colliderect(player_rect) or bottom.colliderect(player_rect)

    def update(self):
        self.rect.x += Obstacle.MAP_SCROLL_SPEED

        # check if obstacle is off the screen
        if (self.rect.x + self.rect.width) < 0:
            self._randomize_position()
