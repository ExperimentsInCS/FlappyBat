import pygame 
from game import FlappyBatGame

flappy_bat_game = FlappyBatGame()
while flappy_bat_game.play():
    # reset the game
    flappy_bat_game.reset()

pygame.quit()
quit()