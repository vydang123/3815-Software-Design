import pygame, sys
from button import Button
from copy import deepcopy
from random import choice, randrange
from pgu import gui

pygame.init()


SCREEN = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Menu")

button_surface = pygame.image.load("button.png")
button_surface = pygame.transform.scale(button_surface, (500, 100))
score_screen = pygame.display.set_mode((680, 680))

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
        MENU_TEXT_YCC = get_font(50).render("Year: 2023    Course Code: 3815ICT", True, "White")
        MENU_RECT_YCC = MENU_TEXT_YCC.get_rect(center=(640, 190))
        GROUP_NUMNAME = get_font(50).render("Group: Vy Dang - s5245519", True, "White")
        GROUP_RECT_NUMNAME = GROUP_NUMNAME.get_rect(center=(640, 250))

        PLAY_BUTTON = Button(button_surface, pos=(640, 350), text_input="PLAY", font=get_font(60), base_color="White",
                             hovering_color="Green")
        CONFIGURE_BUTTON = Button(button_surface, pos=(640, 450), text_input="CONFIGURE", font=get_font(60), base_color="White",
                             hovering_color="Green")
        SCORE_BUTTON = Button(button_surface, pos=(640, 550), text_input="SCORE", font=get_font(60), base_color="White",
                             hovering_color="Green")
        EXIT_BUTTON = Button(button_surface, pos=(640, 650), text_input="EXIT", font=get_font(60), base_color="White",
                             hovering_color="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT,)
        SCREEN.blit(MENU_TEXT_YCC, MENU_RECT_YCC)
        SCREEN.blit(GROUP_NUMNAME, GROUP_RECT_NUMNAME)

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

        CON_TEXT = get_font(60).render("Configure", True, "White")
        CON_RECT = CON_TEXT.get_rect(center=(640, 90))
        SCREEN.blit(CON_TEXT, CON_RECT)

        FIELD_SIZE = get_font(30).render("Size of filed: 10 x 17", True, "White")
        FIELD_SIZE_RECT = FIELD_SIZE.get_rect(center=(640, 190))
        SCREEN.blit(FIELD_SIZE, FIELD_SIZE_RECT)

        GAME_LEVEL = get_font(30).render("Game Level: 1", True, "White")
        GAME_LEVEL_RECT = GAME_LEVEL.get_rect(center=(640, 290))
        SCREEN.blit(GAME_LEVEL, GAME_LEVEL_RECT)

        GAME_MODE = get_font(30).render("Game Mode: Normal", True, "White")
        GAME_MODE_RECT = GAME_MODE.get_rect(center=(640, 390))
        SCREEN.blit(GAME_MODE, GAME_MODE_RECT)

        PLAYER_MODE = get_font(30).render("Player Mode: Normal Player", True, "White")
        PLAYER_MODE_RECT = PLAYER_MODE.get_rect(center=(640, 490))
        SCREEN.blit(PLAYER_MODE, PLAYER_MODE_RECT)

        CON_BACK = Button(button_surface, pos=(640, 590), text_input="OK", font=get_font(40), base_color="White",
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
    SCREEN = pygame.display.set_mode((1280, 720))
    score_screen = pygame.Surface((640, 680))
    pygame.display.set_caption("Score")
    top_scores = [
        ("Player 1", 1000),
        ("Player 2", 850),
        ("Player 3", 700),
        ("Player 4", 600),
        ("Player 5", 500),
        ("Player 6", 400),
        ("Player 7", 300),
        ("Player 8", 200),
        ("Player 9", 100),
        ("Player 10", 50),
    ]
    while True:
        SCORE_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")


        SCORE_TEXT = get_font(45).render("Top Score", True, "White")
        SCORE_RECT = SCORE_TEXT.get_rect(center=(640, 90))
        SCREEN.blit(SCORE_TEXT, SCORE_RECT)

        SCORE_BACK = Button(button_surface, pos=(640, 660), text_input="OK", font=get_font(40), base_color="White",
                           hovering_color="Green")

        SCORE_BACK.changeColor(SCORE_MOUSE_POS)
        SCORE_BACK.update(SCREEN)

        for idx, (player, score) in enumerate(top_scores):
            score_text = f"{idx + 1}. {player}: {score}"
            score_rendered = get_font(30).render(score_text, True, "White")
            score_rect = score_rendered.get_rect(center=((640, 190 + idx * 40)))
            SCREEN.blit(score_rendered, score_rect)

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

    #figures
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

    #speed elements
    anim_count, anim_speed, anim_limit = 0, 60, 2000
    figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))

    bg = pygame.image.load('bg.jpg').convert()

    #titles
    title_tetris = get_font(80).render("Tetris", True, pygame.Color("darkorange"))
    next_block = get_font(50).render("Next Block", True, pygame.Color("darkorange"))
    title_score = get_font(60).render('Score', True, pygame.Color('green'))
    game_over = get_font(80).render("Game Over", True, pygame.Color("darkorange"))


    get_color = lambda : (randrange(30, 256), randrange(30, 256), randrange(30, 256))

    figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))
    color, next_color = get_color(), get_color()

    #score
    score, lines = 0, 0
    scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}

    line_count = 0

    #esc pop-up
    esc_dialog = pygame.Surface((400, 400))
    esc_dialog.fill("grey")
    show_escape_dialog = False
    def return_to_menu():
        nonlocal show_escape_dialog
        show_escape_dialog = False
        start_up()

    def continue_playing():
        nonlocal show_escape_dialog
        show_escape_dialog = False

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
                elif event.key == pygame.K_ESCAPE:
                    show_escape_dialog = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if show_escape_dialog:
                    mouse_pos = pygame.mouse.get_pos()
                    if yes_button.checkForInput(mouse_pos):
                        return_to_menu()
                    elif no_button.checkForInput(mouse_pos):
                        continue_playing()

        #escape game or not
        if show_escape_dialog:
            sc.blit(esc_dialog, (175, 160))
            # Create "YES" and "NO" buttons
            yes_button = Button(image=None, pos=(280, 450), text_input="YES", font=get_font(40), base_color="White",
                           hovering_color="Green")
            no_button = Button(image=None, pos=(480, 450), text_input="NO", font=get_font(40), base_color="White",
                           hovering_color="Green")

            # Display the dialog text
            dialog_text = get_font(27).render("Would you like to end the game?", True, pygame.Color('white'))
            esc_dialog.blit(dialog_text, (20, 80))

            # Update and draw buttons
            yes_button.changeColor(pygame.mouse.get_pos())
            yes_button.update(sc)
            no_button.changeColor(pygame.mouse.get_pos())
            no_button.update(sc)

            pygame.display.update()
            continue


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
        line = H - 1
        lines = 0
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
                line_count +=1

        #compute score
        score += scores[lines]

        #grid
        [pygame.draw.rect(game_sc, (40, 40, 40), i_rect, 1) for i_rect in grid]

        #display figures
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

        #titles display
        sc.blit(title_tetris, (495, 20))
        sc.blit(next_block, (470, 130))
        sc.blit(title_score, (535, 600))
        sc.blit(get_font(45).render(str(score), True, pygame.Color('white')), (570, 660))
        lines_eliminated_text = get_font(40).render("Lines Eliminated", True, pygame.Color('Purple'))
        sc.blit(lines_eliminated_text, (450, 330))
        sc.blit(get_font(45).render(str(line_count), True, pygame.Color('white')), (570, 380))

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

