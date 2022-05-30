import pygame
import os
import time

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')


def print_text(screen, message, x, y, font_colour=(0, 0, 0), font_type='font_from_games.otf', font_size=30):
    font_type = os.path.join(img_folder, font_type)
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_colour)
    screen.blit(text, (x, y))


def pause(screen):
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text(screen, 'Пауза. Чтобы продолжить игру нажмите ENTER', 200, 400)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        #clock.tick(15)


def action1(screen):
    action = True
    action_image = pygame.image.load(os.path.join(img_folder, 'action1.jpg')).convert()

    while action:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(action_image, (0, 17))
        print_text(screen, 'Чтобы продолжить нажмите ENTER', 175, 530, (0, 0, 0), 'font_from_games.otf', 40)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            action = False

        pygame.display.update()


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (13, 162, 58)
        self.active_color = (23, 204, 58)

    def draw(self, screen, x, y, message, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (x < mouse[0] < x + self.width) and (y < mouse[1] < y + self.height):
            pygame.draw.rect(screen, self.active_color, (x, y, self.width, self.height))

            if (click[0] == 1) and (action is not None):
                if action == quit:
                    pygame.quit()
                    quit()
                #  музыка
                action()

        else:
            pygame.draw.rect(screen, self.inactive_color, (x, y, self.width, self.height))

        print_text(screen=screen, message=message, x=x + 25, y=y + 10, font_size=font_size)


def show_menu(screen, action):
    show = True
    menu_background = pygame.image.load(os.path.join(img_folder, 'fon.jpg')).convert()
    start_button = Button(300, 70)
    quit_button = Button(350, 70)

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(menu_background, (0, 0))
        start_button.draw(screen, 300, 420, 'Начать игру', action, 50)
        quit_button.draw(screen, 273, 500, 'Выйти из игры', quit, 50)
        pygame.display.update()
        #  clock.tick(60)


def action2(screen):
    action = True
    action_image = pygame.image.load(os.path.join(img_folder, 'action2.jpg')).convert()

    while action:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(action_image, (0, 17))
        print_text(screen, 'Чтобы начать игру нажмите ENTER', 175, 545, (0, 0, 0), 'font_from_games.otf', 40)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            action = False

        pygame.display.update()


def defeat(screen):

    action = True
    action_image = pygame.image.load(os.path.join(img_folder, 'defeat_action.jpg')).convert()

    while action:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(action_image, (0, 0))
        pygame.display.update()

        time.sleep(7)
        pygame.quit()
        quit()


def win(screen):

    action = True
    action_image = pygame.image.load(os.path.join(img_folder, 'win.jpg')).convert()

    while action:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(action_image, (0, 0))
        pygame.display.update()

        time.sleep(7)
        pygame.quit()
        quit()


def action3(screen):
    action = True
    action_image = pygame.image.load(os.path.join(img_folder, 'action3.jpg')).convert()

    while action:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(action_image, (0, 0))
        print_text(screen, 'Чтобы начать игру нажмите ENTER', 175, 545, (0, 0, 0), 'font_from_games.otf', 40)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            action = False

        pygame.display.update()


def action4(screen):
    action = True
    action_image = pygame.image.load(os.path.join(img_folder, 'action4.jpg')).convert()

    while action:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(action_image, (0, 0))
        print_text(screen, 'Чтобы начать игру нажмите ENTER', 175, 545, (0, 0, 0), 'font_from_games.otf', 40)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            action = False

        pygame.display.update()

