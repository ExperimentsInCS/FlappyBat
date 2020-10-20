import pygame 

import player 
import obstacle 
import score_board

class FlappyBatGame:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)

    DISPLAY_WIDTH = 600
    DISPLAY_HEIGHT = 400

    '''
    This class represents the entire game.
    '''

    def __init__(self):
        pygame.init()

        # setup the game window
        self.display = pygame.display.set_mode((FlappyBatGame.DISPLAY_WIDTH, FlappyBatGame.DISPLAY_HEIGHT))
        pygame.display.set_caption('Flappy Bat')

        self.debug = True 

        # create the player
        self.player = player.Player(self)

        # create a score board
        self.score_board = score_board.ScoreBoard(self)

        # create some obstacles
        self.obstacles = [
            obstacle.Obstacle(self, x_offset=obstacle.Obstacle.OBSTACLE_1_INITIAL_POS),
            obstacle.Obstacle(self, x_offset=obstacle.Obstacle.OBSTACLE_2_INITIAL_POS),
            obstacle.Obstacle(self, x_offset=obstacle.Obstacle.OBSTACLE_3_INITIAL_POS),
        ]

        self.all_sprites_list = pygame.sprite.Group()

        # add the sprites to the sprite group
        self.all_sprites_list.add(self.player)
        self.all_sprites_list.add(self.obstacles)
        self.all_sprites_list.add(self.score_board)

        # create a clock (maintains the FPS)
        self.clock = pygame.time.Clock()

    def reset(self):
        # reset the obstacles
        self.obstacles[0].set_x_offset(obstacle.Obstacle.OBSTACLE_1_INITIAL_POS)
        self.obstacles[1].set_x_offset(obstacle.Obstacle.OBSTACLE_2_INITIAL_POS)
        self.obstacles[2].set_x_offset(obstacle.Obstacle.OBSTACLE_3_INITIAL_POS)

        # reset the player
        self.player.reset()

    def play(self):
        game_over = False 
        user_quit = False 
        time_passed = 0.0

        while not game_over and not user_quit:
            # handle the user events 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    user_quit = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.flap()
                    elif event.key == pygame.K_d:
                        self.debug = not self.debug 

            # update the game objects
            delta_time = self.clock.get_time()

            # update the player
            self.player.update(delta_time)

            # update the obstacles
            for obstacle in self.obstacles:
                obstacle.update()

            # check if the player has died (off screen)
            if self.player.is_dead():
                game_over = True

            # check if the player has collided with an obstacle
            for obstacle in self.obstacles:
                if obstacle.does_collide(self.player.rect):
                    game_over = True

            # draw the game objects 

            # clear the screen
            self.display.fill(FlappyBatGame.BLACK)

            # draw all of the sprites
            self.all_sprites_list.draw(self.display)

            # draw the debug obstacle collision rectangles
            if self.debug:
                for obstacle in self.obstacles:
                    top,bottom = obstacle.get_collision_rects()
                    pygame.draw.rect(self.display, FlappyBatGame.YELLOW, top)
                    pygame.draw.rect(self.display, FlappyBatGame.YELLOW, bottom)

            pygame.display.update()

            # go to the next frame
            self.clock.tick(30)  # 30 FPS

            # keep track of how much time has passed in the game
            time_passed += delta_time / 1000
            pygame.display.set_caption(f'Flappy Bat - {time_passed:.2f}s')
            # display the score on a score board
            self.score_board.update_score(time_passed)

        return not user_quit
