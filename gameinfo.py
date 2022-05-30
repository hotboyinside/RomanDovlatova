import pygame.font
from pygame.sprite import Group
from classes import Heart


class Score:
    """вывод игровой информации"""
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_colour = (139, 195, 74)
        self.font = pygame.font.SysFont(None, 36)
        self.draw_image_score()
        self.image_lifes()

    def draw_image_score(self):
        """Вырисовывает текст"""
        self.image = self.font.render(str(self.stats.score), True, self.text_colour, (0, 0, 0))
        self.score_rect = self.image.get_rect()
        self.score_rect.right = self.score_rect.right - 40
        self.score_rect.top = 20

    def show_score(self):
        """вывод счета на экран"""
        self.screen.blit(self.image, self.screen_rect)
        self.lifes.draw(self.screen)

    def image_lifes(self):
        """кол-во жизней"""
        self.lifes = Group()
        for life_number in range(self.stats.player_life):
            heart = Heart(self.screen)
            heart.rect.x = 785 + life_number * heart.rect.width
            heart.rect.y = 12
            self.lifes.add(heart)

