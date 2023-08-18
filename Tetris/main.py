import pygame, sys
from button import Button
from copy import deepcopy
from random import choice, randrange

pygame.init()


SCREEN = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Menu")

button_surface = pygame.image.load("button.png")
button_surface = pygame.transform.scale(button_surface, (500, 100))
def get_font(size):
    return pygame.font.SysFont("cambria", size)

def start_up():
    pygame.display.set_caption("Menu")
    SCREEN = pygame.display.set_mode((1280, 720))
    while True:
        SCREEN.fill("black")

        MENU_MOUSE_POS= pygame.mouse.get_pos()

        MENU_TEXT = get_font(120).render("TETRIS", True, "White")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(button_surface, pos=(640, 300), text_input="PLAY", font=get_font(60), base_color="White",
                             hovering_color="Green")
        CONFIGURE_BUTTON = Button(button_surface, pos=(640, 400), text_input="CONFIGURE", font=get_font(60), base_color="White",
                             hovering_color="Green")
        SCORE_BUTTON = Button(button_surface, pos=(640, 500), text_input="SCORE", font=get_font(60), base_color="White",
                             hovering_color="Green")
        EXIT_BUTTON = Button(button_surface, pos=(640, 600), text_input="EXIT", font=get_font(60), base_color="White",
                             hovering_color="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, CONFIGURE_BUTTON, SCORE_BUTTON, EXIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if CONFIGURE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    configure_page()
                if SCORE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    score_page()
                if EXIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def configure_page():
    pygame.display.set_caption("Configure")
    while True:
        CON_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")

        CON_TEXT = get_font(45).render("This is the Configure Page.", True, "White")
        CON_RECT = CON_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(CON_TEXT, CON_RECT)

        CON_BACK = Button(image=None, pos=(640, 460), text_input="BACK", font=get_font(75), base_color="White",
                           hovering_color="Green")

        CON_BACK.changeColor(CON_MOUSE_POS)
        CON_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CON_BACK.checkForInput(CON_MOUSE_POS):
                    start_up()
        pygame.display.update()
def score_page():
    pygame.display.set_caption("Play")
    while True:
        SCORE_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")

        SCORE_TEXT = get_font(45).render("This is the Score Screen.", True, "White")
        SCORE_RECT = SCORE_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(SCORE_TEXT, SCORE_RECT)

        SCORE_BACK = Button(image=None, pos=(640, 460), text_input="BACK", font=get_font(75), base_color="White",
                           hovering_color="Green")

        SCORE_BACK.changeColor(SCORE_MOUSE_POS)
        SCORE_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SCORE_BACK.checkForInput(SCORE_MOUSE_POS):
                    start_up()
        pygame.display.update()
def play():
    pygame.display.set_caption("Play")
    clock = pygame.time.Clock()
    W, H = 10, 17
    TILE = 40
    GAME_RES = W * TILE, H * TILE
    RES = 750, 720
    FPS = 60
    sc = pygame.display.set_mode(RES)
    game_sc = pygame.Surface(GAME_RES)
    grid = [pygame.Rect(x*TILE, y*TILE, TILE, TILE) for x in range(W) for y in range(H)]
    figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
                  [(0, -1), (-1, -1), (0, 0), (-1, 0)],
                  [(0, 0), (1, 0), (0, -1), (-1, -1)],
                  [(0, 0), (-1, 0), (0, -1), (1, -1)],
                  [(-1, 0), (0, 0), (-1, -1), (-1, -2)],
                  [(0, 0), (-1, 0), (0, -1), (0, -2)],
                  [(0, 0), (-1, 0), (1, 0), (0, -1)]]
    figures = [[pygame.Rect(x + W // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
    figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)
    field = [[0 for i in range(W)] for j in range(H)]

    anim_count, anim_speed, anim_limit = 0, 60, 2000
    figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))

    bg = pygame.image.load('bg.jpg').convert()

    title_tetris = get_font(80).render("Tetris", True, pygame.Color("darkorange"))
    next_block = get_font(50).render("Next Block", True, pygame.Color("darkorange"))
    title_score = get_font(60).render('Score', True, pygame.Color('green'))
    game_over = get_font(80).render("Game Over", True, pygame.Color("darkorange"))


    get_color = lambda : (randrange(30, 256), randrange(30, 256), randrange(30, 256))

    figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))
    color, next_color = get_color(), get_color()

    score, lines = 0, 0
    scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}

    def check_borders():
        if figure[i].x < 0 or figure[i].x > W - 1:
            return False
        elif figure[i].y > H - 1 or field[figure[i].y][figure[i].x]:
            return False
        return True
    while True:
        dx = 0
        sc.blit(bg, (0, 0))
        rotate = False
        sc.blit(game_sc, (20, 20))
        game_sc.fill("black")

        #delay for full lines
        for i in range(lines):
            pygame.time.wait(200)

        #control
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #move left
                if event.key == pygame.K_LEFT:
                    dx = -1
                #move right
                elif event.key == pygame.K_RIGHT:
                    dx = 1
                #increase block speed
                elif event.key == pygame.K_DOWN:
                    anim_limit = 100
                #rotate
                elif event.key == pygame.K_UP:
                    rotate = True

        #move blocks right or left
        figure_old = deepcopy(figure)
        for i in range(4):
            figure[i].x += dx
            if not check_borders():
                figure = deepcopy(figure_old)
                break

        #increase block speed
        anim_count += anim_speed
        if anim_count > anim_limit:
            anim_count = 0
            figure_old = deepcopy(figure)
            for i in range(4):
                figure[i].y += 1
                if not check_borders():
                    for i in range(4):
                        field[figure_old[i].y][figure_old[i].x] = color
                    figure, color = next_figure, next_color
                    next_figure, next_color = deepcopy(choice(figures)), get_color()
                    anim_limit = 2000
                    break

        #rotate
        center = figure[0]
        figure_old = deepcopy(figure)
        if rotate:
            for i in range(4):
                x = figure[i].y - center.y
                y = figure[i].x - center.x
                figure[i].x = center.x - x
                figure[i].y = center.y + y
                if not check_borders():
                    figure = deepcopy(figure_old)
                    break

        #check lines
        line, lines = H - 1, 0
        for row in range(H - 1, -1, -1):
            count = 0
            for i in range(W):
                if field[row][i]:
                    count += 1
                field[line][i] = field[row][i]
            if count < W:
                line -= 1
            else:
                anim_speed += 3
                lines += 1

        #compute score
        score += scores[lines]
        [pygame.draw.rect(game_sc, (40, 40, 40), i_rect, 1) for i_rect in grid]

        #figures
        for i in range(4):
            figure_rect.x = figure[i].x * TILE
            figure_rect.y = figure[i].y * TILE
            pygame.draw.rect(game_sc, color, figure_rect)

        #field
        for y, raw in enumerate(field):
            for x, col in enumerate(raw):
                if col:
                    figure_rect.x, figure_rect.y = x * TILE, y * TILE
                    pygame.draw.rect(game_sc, col, figure_rect)

        #next figure
        for i in range(4):
            figure_rect.x = next_figure[i].x * TILE + 383
            figure_rect.y = next_figure[i].y * TILE + 220
            pygame.draw.rect(sc, next_color, figure_rect)

        #titles
        sc.blit(title_tetris, (495, 20))
        sc.blit(next_block, (470, 130))
        sc.blit(title_score, (535, 600))
        sc.blit(get_font(45).render(str(score), True, pygame.Color('white')), (570, 660))

        #game over
        game_is_over = False
        for i in range(W):
            if field[0][i]:
                game_is_over = True
                break
        if game_is_over:
            sc.blit(game_over, (40, 330))
            pygame.display.update()
            pygame.time.wait(2000)  # Display the "Game Over" text for 2 seconds
            start_up()  # Return to the main menu

        pygame.display.update()
        clock.tick(FPS)

start_up()