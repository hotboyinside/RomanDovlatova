import time
import pygame
import random
import sys
import os
import classes
import tabs


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
main_fon = pygame.image.load(os.path.join(img_folder, 'main_fon.png'))  # основной фон
time_to_play = True


def all_events(player, user_data, screen):
    if user_data.score >= 15 and player.action_1 is False:
        player.move_left = False
        player.move_right = False
        tabs.action3(screen)
        user_data.score = 0
        player.action_1 = True
    elif user_data.score >= 15 and player.action_1 and player.action_2 is False:
        player.move_left = False
        player.move_right = False
        tabs.action4(screen)
        user_data.score = 0
        player.action_2 = True
    elif user_data.score >= 15 and player.action_1 and player.action_2:
        tabs.win(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.move_right = True
            elif event.key == pygame.K_a:
                player.move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.move_right = False
            elif event.key == pygame.K_a:
                player.move_left = False


def update_screen(screen, player, things, score):
    """Отрисовываем спрайты"""
    screen.blit(main_fon, (0, 0))
    score.show_score()
    for thing in things.sprites():
        thing.draw()
    player.draw_player()
    pygame.display.flip()


def update_things(screen, things, player, stats, score):
    """Отображаем спрайты"""
    things.update()
    for thing in things.copy():
        if thing.rect.top >= 600:
            things.remove(thing)

    for thing in things:
        if pygame.sprite.collide_mask(player, thing) and thing.benefit is False:
            player_die(stats, screen, player, things, score)
        elif pygame.sprite.collide_mask(player, thing) and thing.benefit is True:
            things.remove(thing)
            stats.score += 1
            score.draw_image_score()
            score.image_lifes()

    if len(things) == 0:
        things.empty()
        create_row_things(screen, things, player)


def player_die(stats, screen, player, things, score):
    """столкновение игрока и неправильных предметов"""
    if stats.player_life > 0:
        stats.player_life -= 1
        score.image_lifes()
        things.empty()
        create_row_things(screen, things, player)
        player.create_player()
        time.sleep(2)
    else:
        tabs.defeat(screen)
        stats.run_game = False
        sys.exit()


def create_row_things(screen, things, player):
    """Создание ряда из вещей"""

    if player.action_1 and player.action_2 is False:
        bottle = classes.Bottle(screen)
        bottle.benefit = True
        coin = classes.Coin(screen)
        bottle.speed += 0.03
        coin.speed += 0.04
        subjects = [bottle, classes.Cigarette(screen), bottle,
                    classes.Cigarette(screen), bottle, classes.Cigarette(screen),
                    coin, coin, classes.Book(screen), classes.Book(screen)]

    elif player.action_1 and player.action_2:
        cigarette = classes.Cigarette(screen)
        cigarette.benefit = True
        cigarette.speed += 0.07
        book = classes.Book(screen)
        book.benefit = False
        book.speed += 0.06
        subjects = [classes.Bottle(screen), cigarette, classes.Bottle(screen),
                    cigarette, classes.Bottle(screen), cigarette,
                    book, book]

    else:
        subjects = [classes.Bottle(screen), classes.Cigarette(screen), classes.Bottle(screen),
                    classes.Cigarette(screen), classes.Bottle(screen), classes.Cigarette(screen),
                    classes.Book(screen), classes.Book(screen)]
    spots_numbs = int((900 - 100 * 2) / 135)  # кол-во точек откуда летят вещи

    for thing_number in range(spots_numbs):
        thing = random.choice(subjects)
        thing.x = 50 + 180 * thing_number
        thing.rect.x = thing.x
        things.add(thing)
