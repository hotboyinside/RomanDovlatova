import pygame
import os
import events
import classes
import stats
import gameinfo
import tabs

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
game_icon = pygame.image.load(os.path.join(img_folder, 'game_icon.jpg'))
WIDTH = 900
HEIGHT = 600
FPS = 60
colours = {'BLACK': (0, 0, 0), 'WHITE': (255, 255, 255), 'RED': (255, 0, 0),
           'GREEN': (0, 255, 0), 'BLUE': (0, 0, 255)}


def game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Роман Довлатова")
    pygame.display.set_icon(game_icon)
    clock = pygame.time.Clock()
    clock.tick(FPS)
    player = classes.Player(screen)
    things = pygame.sprite.Group()
    events.create_row_things(screen, things, player)
    user_data = stats.Stats()
    score = gameinfo.Score(screen, user_data)
    tabs.action2(screen)

    while True:
        events.all_events(player, user_data, screen)
        if user_data.run_game:
            player.update()
            events.update_things(screen, things, player, user_data, score)
            events.update_screen(screen, player, things, score)


if __name__ == '__main__':
    pygame.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_icon(game_icon)
    pygame.display.set_caption("Роман Довлатова")
    tabs.action1(display)
    tabs.show_menu(display, game)
