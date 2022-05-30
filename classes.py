import pygame
import os

WIDTH = 900  # ширина игрового окна
HEIGHT = 600  # высота игрового окна
FPS = 30  # частота кадров в секунду

# настройка папки ассетов
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
image_counter = 0
player_images = [pygame.image.load(os.path.join(img_folder, 'довлатов (1).png')),
                 pygame.image.load(os.path.join(img_folder, 'довлатов (2).png')),
                 pygame.image.load(os.path.join(img_folder, 'довлатов (3).png')),
                 pygame.image.load(os.path.join(img_folder, 'довлатов (4).png')),
                 pygame.image.load(os.path.join(img_folder, 'довлатов (5).png')),
                 pygame.image.load(os.path.join(img_folder, 'довлатов (6).png'))]


class Player(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Player, self).__init__()
        self.screen = screen
        self.image = player_images[1]
        self.images = player_images
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False
        self.action_1 = False
        self.action_2 = False
        self.action_3 = False

    def output(self):
        """отрисовка изображения"""
        self.screen.blit(self.image, self.rect)

    def draw_player(self):
        global image_counter
        if image_counter == 600:
            image_counter = 0
        self.images[image_counter // 100].set_colorkey('WHITE')
        self.screen.blit(self.images[image_counter // 100], self.rect)
        image_counter += 1

    def update(self):
        if self.move_right:
            self.center += 0.3
        if self.move_left:
            self.center -= 0.3
        if self.rect.left > WIDTH:
            self.center = 0
        if self.rect.right < 0:
            self.center = WIDTH

        self.rect.centerx = self.center

    def create_player(self):
        """создают игрока"""
        self.center = self.screen_rect.centerx


class Cigarette(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Cigarette, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(os.path.join(img_folder, 'cigarette.png')).convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey('BLACK')
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed = 0.3
        self.benefit = False

    def draw(self):
        """отрисовка изображения"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y


class Bottle(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Bottle, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(os.path.join(img_folder, 'бутылка.png')).convert()
        self.image.set_colorkey('WHITE')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed = 0.3
        self.benefit = False

    def draw(self):
        """отрисовка изображения"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y


class Book(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Book, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(os.path.join(img_folder, 'book.png')).convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey('BLACK')
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed = 0.3
        self.benefit = True

    def draw(self):
        """отрисовка изображения"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y


class Coin(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Coin, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(os.path.join(img_folder, 'МОНЕТА.png')).convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey('WHITE')
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed = 0.3
        self.benefit = True

    def draw(self):
        """отрисовка изображения"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y


class Heart(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Heart, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(os.path.join(img_folder, 'heart.png')).convert()
        self.image.set_colorkey('BLACK')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
