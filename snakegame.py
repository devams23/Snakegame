import pygame
import random
# initializing the pygame
x = pygame.init()

# creating a variable for game window
s_width = 700
s_height = 500
high_score = 0
gamewindow = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Snake Game!")
pygame.display.update()
# game specified variables


def show_text(text, color, x, y):
    font = pygame.font.SysFont(None, 55)
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])


def plot_snake(gamewindow, green, snk_list, size_snake):
    for x, y in snk_list:
        pygame.draw.rect(gamewindow, green, [x, y, size_snake, size_snake])


# making a loop that will run until there is no game over
def gameloop(high_score):
    gamewindow = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption("Snake Game!")
    fps = 50
    score = 0
    snk_list = []
    snk_len = 1
    clock = pygame.time.Clock()
    x_food = random.randint(50, 400)
    y_food = random.randint(50, 200)
    backg = (25, 0, 40)
    green = (0, 200, 20)
    red = (255, 0, 0)
    head_c = (255, 155, 155)
    text_c = (255, 255, 255)
    game_over = False
    game_exit = False
    x_direc = 100
    y_direc = 100
    init_velo = 4
    x_velo = 0
    y_velo = 0
    size_snake = 15
    while not game_exit:
        if game_over:
            gamewindow.fill(backg)
            show_text("Game Over Press Enter To Continue!", text_c, 10, 200)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop(high_score)

        else:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        x_velo = init_velo
                        y_velo = 0
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a :
                        x_velo = -init_velo
                        y_velo = 0
                    if event.key == pygame.K_UP or  event.key == pygame.K_w:
                        y_velo = - init_velo
                        x_velo = 0
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        y_velo = init_velo
                        x_velo = 0
                    if event.key == pygame.K_ESCAPE:
                        game_exit = True

            x_direc += x_velo
            y_direc += y_velo

            if abs(x_direc - x_food) < 15 and abs(y_direc - y_food) < 15:
                x_food = random.randint(50, 400)
                y_food = random.randint(50, 400)
                score += 10
                snk_len += 5

            head = []
            head.append(x_direc)
            head.append(y_direc)
            snk_list.append(head)

            if len(snk_list) > snk_len:
                del snk_list[0]

            if x_direc <= 0 or x_direc >= s_width or y_direc <= 0 or y_direc >= s_height:
                game_over = True
                print("game over")
            if head in snk_list[:-1]:
                game_over = True

            
            gamewindow.fill(backg)
            x_head = head[0]
            y_head = head[1]
            show_text("Score: " + str(score ), text_c, 10, 10)
            if score > high_score:
                high_score = score
            show_text("High Score: " + str(high_score), text_c, 300, 10)
                
            pygame.draw.rect(gamewindow, red, [x_food, y_food, size_snake, size_snake])
            pygame.draw.rect(gamewindow, head_c, [ x_head, y_head, size_snake, size_snake])
            plot_snake(gamewindow, green, snk_list[:-1], size_snake)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()


gameloop(high_score)
