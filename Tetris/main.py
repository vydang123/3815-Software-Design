import pygame, sys
from button import Button
from copy import deepcopy

pygame.init()


SCREEN = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Menu")

button_surface = pygame.image.load("button.png")
button_surface = pygame.transform.scale(button_surface, (500, 100))
def get_font(size):
    return pygame.font.SysFont("cambria", size)

def start_up():
    pygame.display.set_caption("Menu")
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
    GAME_RES = W*TILE, H*TILE
    FPS = 60
    game_sc = pygame.display.set_mode(GAME_RES)
    grid = [pygame.Rect(x*TILE, y*TILE, TILE, TILE) for x in range(W) for y in range(H)]
    figure_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
                  [(0, -1), (-1, -1), (0, 0), (-1, 0)],
                  [(0, 0), (1, 0), (0, -1), (-1, -1)],
                  [(0, 0), (-1, 0), (0, -1), (1, -1)],
                  [(-1, 0), (0, 0), (-1, -1), (-1, -2)],
                  [(0, 0), (-1, 0), (0, -1), (0, -2)],
                  [(0, 0), (-1, 0), (1, 0), (0, -1)]]
    figures = [[pygame.Rect(x + W // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figure_pos]
    figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)

    figure = deepcopy(figures[0])

    def check_borders():
        if figure[i].x < 0 or figure[i].x > W -1:
            return False
        return True
    while True:
        dx = 0
        game_sc.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -1
                elif event.key == pygame.K_RIGHT:
                    dx = 1

        figure_old = deepcopy(figure)
        for i in range(4):
            figure[i].x += dx
            if not check_borders():
                figure = deepcopy(figure_old)
                break


        [pygame.draw.rect(game_sc, (40, 40, 40), i_rect, 1) for i_rect in grid]

        for i in range(4):
            figure_rect.x = figure[i].x * TILE
            figure_rect.x = figure[i].x * TILE
            pygame.draw.rect(game_sc, pygame.Color("White"), figure_rect)
        pygame.display.update()
        clock.tick(FPS)

start_up()