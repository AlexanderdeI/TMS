import sys
import time
import pygame
import random
from ball import Ball
from bricks import Brick, IronBrick
from improvments import Improvment


# ЭКРАН
def update_screen(conf_screen, screen, fps, statistics, sb, improvments,
                  bat, balls, bricks, iron_bricks, play_button,
                  exit_button, continue_button):
    """Обновляет экран"""
    # При каждом проходе цикла перерисовывается экран
    screen.fill(conf_screen.BG_COLOR)
    for ball in balls.sprites():
        ball.blit_ball()
    for improvment in improvments.sprites():
        improvment.blit()
    bat.blit_bat()
    sb.show_score()
    bricks.draw(screen)
    iron_bricks.draw(screen)
    if not statistics.game_active:
        play_button.draw_button()
        exit_button.draw_button()
    elif statistics.K_ESCAPE_active:
        continue_button.draw_button()
        exit_button.draw_button()
    # Отображение последнего экрана
    pygame.display.flip()
    fps.tick(conf_screen.FPS)


# СОБЫТИЯ МЫШКИ И КЛАВИАТУРЫ
def check_events(statistics, sb, improvments, play_button, exit_button,
                 continue_button, screen, bat, balls,
                 bricks, iron_bricks, levels):
    """Отслеживание клавиатуры и мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check_high_score_bf_exit(statistics, sb)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, bat, balls, statistics, sb)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, bat)
        else:
            check_mouse_event(event, statistics, sb, improvments, play_button,
                              exit_button, continue_button, screen, bat,
                              balls, bricks, iron_bricks, levels)


def check_keydown_events(event, screen, bat, balls, statistics, sb):
    # Передвигает ракетку при нажатии клавиш
    if event.key == pygame.K_RIGHT:
        bat.moving_right = True
    elif event.key == pygame.K_LEFT:
        bat.moving_left = True
    # Запускает мячик при нажатии
    elif event.key == pygame.K_SPACE:
        run_ball(screen, bat, balls)
    # Действия при нажатии Esc
    elif event.key == pygame.K_ESCAPE:
        # Выйти из игры
        if not statistics.game_active:
            check_high_score_bf_exit(statistics, sb)
        # Вызов/отмена паузы
        elif not statistics.K_ESCAPE_active:
            statistics.K_ESCAPE_active = True
            pygame.mouse.set_visible(True)
        else:
            statistics.K_ESCAPE_active = False
            pygame.mouse.set_visible(False)


def check_keyup_events(event, bat):
    # Прекращает движение рактеки при отжатии клавиш
    if event.key == pygame.K_RIGHT:
        bat.moving_right = False
        bat.set_default_power()
    if event.key == pygame.K_LEFT:
        bat.moving_left = False
        bat.set_default_power()


def check_mouse_event(event, statistics, sb, improvments, play_button,
                      exit_button, continue_button, screen, bat, balls,
                      bricks, iron_bricks, levels):
    """Отслеживает дввижение и нажатие клавиш мыши"""
    # Передвижение ракетки мышкой
    if event.type == pygame.MOUSEMOTION:
        mousex, mousey = event.pos
        screen_rect = screen.get_rect()
        if mousex < screen_rect.width - bat.lenght:
            bat.center = mousex + 0.5 * bat.lenght
        else:
            bat.center = screen_rect.width - 0.5 * bat.lenght
    # Действия левой кнопки мышки
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mousex, mousey = pygame.mouse.get_pos()
        if not statistics.game_active:
            check_play_button(statistics, sb, improvments, play_button, mousex,
                              mousey, screen, bat, balls,
                              bricks, iron_bricks, levels)
            check_exit_button(exit_button, mousex, mousey, statistics, sb)
        elif statistics.game_active:
            run_ball(screen, bat, balls)
        elif statistics.K_ESCAPE_active:
            check_continue_button(statistics, continue_button, mousex, mousey)
            check_exit_button(exit_button, mousex, mousey, statistics, sb)


def check_play_button(statistics, sb, improvments, play_button, mousex, mousey,
                      screen, bat, balls, bricks, iron_bricks, levels):
    """Запускает новую игру при нажатии"""
    if play_button.rect.collidepoint(mousex, mousey):
        statistics.reset_statistics()
        remove_level(statistics, sb, improvments, bat, balls,
                     bricks, iron_bricks)
        level_number = statistics.level
        create_level(screen, statistics, sb, improvments, bat, balls,
                     bricks, iron_bricks, levels, level_number)


def check_exit_button(exit_button, mousex, mousey, statistics, sb):
    """Выходит из игры при нажатии"""
    if exit_button.rect.collidepoint(mousex, mousey):
        check_high_score_bf_exit(statistics, sb)


def check_continue_button(statistics, continue_button, mousex, mousey):
    """Продолжает игру по нажатию"""
    if continue_button.rect.collidepoint(mousex, mousey):
        statistics.K_ESCAPE_active = False
        pygame.mouse.set_visible(False)


# МЯЧИК
def run_ball(screen, bat, balls):
    # Создание нового шарика и включение его в группу balls
    ball = Ball(screen, bat)
    ball.count += 1
    if len(balls) < ball.count:
        ball.moving = True
        balls.add(ball)


def update_balls(conf_screen, screen, statistics, sb, improvments,
                 bat, balls, bricks, iron_bricks, levels):
    """Обновляет позиции мячей"""
    balls.update(bat)
    for ball in balls.copy():
        if ball.rect.top >= conf_screen.HEIGHT:
            balls.remove(ball)
        if len(balls) < ball.count:
            balls_out(statistics, sb, bat, improvments)
        check_balls_bricks_collisions(screen, statistics, sb, improvments, bat,
                                      balls, bricks, iron_bricks, levels)


def balls_out(statistics, sb, bat, improvments):
    """Выполняет ряд действий при выходе мячика за экран"""
    if statistics.lifes > 1:
        statistics.lifes -= 1
        sb.prep_lifes()
        time.sleep(1)
        bat.center_bat()
        improvments.empty()
    else:
        statistics.lifes = 0
        sb.prep_lifes()
        statistics.game_active = False
        pygame.mouse.set_visible(True)


def check_balls_bricks_collisions(screen, statistics, sb, improvments,
                                  bat, balls, bricks, iron_bricks, levels):
    # Проверка попаданий в кирпичи
    collision_with_brick(screen, improvments, balls, bricks, statistics, sb)
    collision_with_iron_brick(balls, iron_bricks)
    if len(bricks) == 0:
        try:
            # Создание нового уровня
            create_level(screen, statistics, sb, improvments, bat, balls,
                         bricks, iron_bricks, levels, statistics.level)
        except FileNotFoundError:
            # При достижении лимита уровней - повтор всех уровней
            statistics.level = 0
            create_level(screen, statistics, sb, improvments, bat, balls,
                         bricks, iron_bricks, levels, statistics.level)


def collision_with_brick(screen, improvments, balls, bricks, statistics, sb):
    # Обработка столкновений мячика с кирпичом
    for ball in balls:
        brick = pygame.sprite.spritecollideany(ball, bricks)
        if not brick:
            continue
        elif brick.rect.left < ball.x < brick.rect.right:
            ball.reflect_from_brick()
        else:
            ball.reflect_from_brick(reverse=True)
        bricks.remove(brick)
        update_score_chance_improvment(screen, statistics, sb,
                                       improvments, brick)


def collision_with_iron_brick(balls, iron_bricks):
    # Обрабатывает столкновение с железными кирпичами
    for ball in balls:
        iron_brick = pygame.sprite.spritecollideany(ball, iron_bricks)
        if not iron_brick:
            continue
        elif iron_brick.rect.left < ball.x < iron_brick.rect.right:
            ball.reflect_from_brick()
        else:
            ball.reflect_from_brick(reverse=True)


def update_score_chance_improvment(screen, statistics, sb, improvments, brick):
    # Обновление счета
    statistics.score += brick.cost
    sb.prep_score()
    check_high_score(statistics, sb)
    # Шанс выбить улучшение
    if random.choice(range(1, 12)) == 10:
        add_improvment(screen, improvments, brick)


def update_improvments(conf_screen, screen, improvments, bat,
                       balls, statistics, sb):
    # Обновление позиции улучшений на экране
    improvments.update()
    for imp in improvments.copy():
        imp.fall_down()
        if imp.rect.colliderect(bat.rect):
            improvments.remove(imp)
            bring_improvment(screen, imp, bat, balls, statistics,
                             sb, improvments)
        if imp.y > conf_screen.HEIGHT:
            improvments.remove(imp)


def add_improvment(screen, improvments, brick):
    # Создает улучшение
    improvment = Improvment(screen, brick)
    improvments.add(improvment)


def bring_improvment(screen, improvment, bat, balls, statistics,
                     sb, improvments):
    # Определяет тип улучшения
    if improvment.type == "life":
        add_life(statistics, sb)
    elif improvment.type == "ball":
        add_ball(screen, bat, balls)
    elif improvment.type == "death":
        reduce_life_count(statistics, sb, bat, balls, improvments)


def add_life(statistics, sb):
    # Добавляет жизнь
    statistics.lifes += 1
    sb.prep_lifes()


def add_ball(screen, bat, balls):
    # Вызывает дополнительный шарик
    ball = Ball(screen, bat)
    ball.count += 1
    ball.moving = True
    balls.add(ball)


def reduce_life_count(statistics, sb, bat, balls, improvments):
    # Отнимает жизнь
    balls_out(statistics, sb, bat, improvments)
    balls.empty()


# ОБНОВЛЕНИЕ ИГРОВОЙ САТИСТИКИ
def check_high_score(statistics, sb):
    """Проверяет появился ли новый рекорд"""
    if statistics.score > statistics.high_score:
        statistics.high_score = statistics.score
        sb.prep_high_score()


def check_high_score_bf_exit(statistics, sb):
    """Если текущий счет больше максимального записывает в файл"""
    if statistics.score == statistics.high_score:
        statistics.record_file.write("\n" + str(statistics.high_score))
    sys.exit()


def increase_level(statistics, sb):
    """Повышает уровень"""
    statistics.level += 1
    sb.prep_level()


# """СОЗДАНИЕ КИРПИЧЕЙ И УРОВНЕЙ"""
def create_brick(screen, bricks, brick_number, row_number, brick_type=Brick):
    # Создает кирпич и размещает его в ряду
    if brick_type == Brick:
        brick = Brick(screen)
    elif brick_type == IronBrick:
        brick = IronBrick(screen)
    brick.rect.x = brick.width + brick.width * brick_number
    brick.rect.y = brick.height + brick.height * row_number
    bricks.add(brick)


def get_number_lines(level):
    """Определение количества рядов"""
    lines_number = len(level)
    return lines_number


def get_elements_number(level, line_number):
    """Определение длинны ряда"""
    el_number = len(level[line_number])
    return el_number


def create_level(screen, statistics, sb, improvments, bat, balls, bricks,
                 iron_bricks, levels, level_number):
    """Создание уровня"""
    level = levels.load_level(level_number)
    lines_number = range(get_number_lines(level))
    remove_level(statistics, sb, improvments, bat, balls, bricks, iron_bricks)
    increase_level(statistics, sb)
    for line, row_number in zip(level, lines_number):
        el_number = range(get_elements_number(level, row_number))
        for el, brick_number in zip(line, el_number):
            if el == "b":
                create_brick(screen, bricks, brick_number, row_number)
            if el == "i":
                create_brick(screen, iron_bricks, brick_number,
                             row_number, brick_type=IronBrick)


def remove_level(statistics, sb, improvments, bat, balls, bricks, iron_bricks):
    """Очистка уровня"""
    pygame.mouse.set_visible(False)
    sb.prep_level()
    sb.prep_score()
    sb.prep_lifes()
    bat.center_bat()
    balls.empty()
    bricks.empty()
    improvments.empty()
    iron_bricks.empty()
    statistics.game_active = True
    time.sleep(1)
