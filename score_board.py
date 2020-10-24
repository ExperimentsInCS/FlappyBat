<<<<<<< HEAD
import pygame 

class ScoreBoard(pygame.sprite.Sprite):
    SCORE_X_OFFSET = 20
    SCORE_Y_OFFSET = 20
    
    def __init__(self, game):
        super().__init__()

        self.game = game 

        self.high_score = 0.0
        self.current_score = 0.0

        self.font = pygame.font.Font('assets/Jellee-Bold.ttf', 18)
        self._update_image()
    
    def _update_image(self):
        self.image = self.font.render(
            f'Best: {self.high_score:0.2f}s, Current: {self.current_score:0.2f}s',
            True,
            self.game.WHITE,
            self.game.BLACK
        )
        self.rect = self.image.get_rect() 
        self.rect.x = ScoreBoard.SCORE_X_OFFSET
        self.rect.y = ScoreBoard.SCORE_Y_OFFSET
    
    def update_score(self, new_score):
        self.current_score = new_score 

        if new_score > self.high_score:
            self.high_score = new_score
        
=======
import pygame 

class ScoreBoard(pygame.sprite.Sprite):
    SCORE_X_OFFSET = 20
    SCORE_Y_OFFSET = 20
    
    def __init__(self, game):
        super().__init__()

        self.game = game 

        self.high_score = 0.0
        self.current_score = 0.0

        self.font = pygame.font.Font('assets/Jellee-Bold.ttf', 18)
        self._update_image()
    
    def _update_image(self):
        self.image = self.font.render(
            f'Best: {self.high_score:0.2f}s, Current: {self.current_score:0.2f}s',
            True,
            self.game.WHITE,
            self.game.BLACK
        )
        self.rect = self.image.get_rect() 
        self.rect.x = ScoreBoard.SCORE_X_OFFSET
        self.rect.y = ScoreBoard.SCORE_Y_OFFSET
    
    def update_score(self, new_score):
        self.current_score = new_score 

        if new_score > self.high_score:
            self.high_score = new_score
        
>>>>>>> 029aa52e6c90dc0d74f6969d6e125c5d8f77e91a
        self._update_image()