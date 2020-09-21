import pygame
import math

# Screen

SCREEN_WIDTH = 720
ROWS = 9
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
pygame.display.set_caption("Sudoku")

# Colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialazing pygame

pygame.init()

# Images

image_1 = pygame.transform.scale(pygame.image.load("D:/1.jpg"), (30, 30))
image_2 = pygame.transform.scale(pygame.image.load("D:/2.jpg"), (30, 30))
image_3 = pygame.transform.scale(pygame.image.load("D:/3.jpg"), (30, 30))
image_4 = pygame.transform.scale(pygame.image.load("D:/4.jpg"), (30, 30))
image_5 = pygame.transform.scale(pygame.image.load("D:/5.jpg"), (30, 30))
image_6 = pygame.transform.scale(pygame.image.load("D:/6.jpg"), (30, 30))
image_7 = pygame.transform.scale(pygame.image.load("D:/7.jpg"), (30, 30))
image_8 = pygame.transform.scale(pygame.image.load("D:/8.jpg"), (30, 30))
image_9 = pygame.transform.scale(pygame.image.load("D:/9.jpg"), (30, 30))

# Fonts

END_FONT = pygame.font.SysFont('courier', 40)


def draw_grid():
    gap = SCREEN_WIDTH // ROWS

    for i in range(ROWS):
        x = i * gap

        pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_WIDTH), 3)
        pygame.draw.line(screen, BLACK, (0, x), (SCREEN_WIDTH, x), 3)


def initialize_grid():
    dis_to_cen = SCREEN_WIDTH // ROWS // 2

    # Initializing the array

    game_array = [[None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None]]

    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x = dis_to_cen * (2 * j + 1)
            y = dis_to_cen * (2 * i + 1)

            # Adding center coordinates
            game_array[i][j] = (x, y, "", True)

    return game_array


def click(game_array, key):
    mass_1 = {1: {"text": "1", "picture": image_1}, 2: {"text": "2", "picture": image_2},
              3: {"text": "3", "picture": image_3},
              4: {"text": "4", "picture": image_4}, 5: {"text": "5", "picture": image_5},
              6: {"text": "6", "picture": image_6},
              7: {"text": "7", "picture": image_7}, 8: {"text": "8", "picture": image_8},
              9: {"text": "9", "picture": image_9}, 10: {"text": None}}

    # Mouse position
    x_pos, y_pos = pygame.mouse.get_pos()

    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x, y, char, can_play = game_array[i][j]

            # Distance between mouse and the centre of the square
            dis = math.sqrt((x - x_pos) ** 2 + (y - y_pos) ** 2)

            # If it's inside the square
            if dis < SCREEN_WIDTH // ROWS // 2 and can_play and key < 10:
                for n in game_array:
                    count = 0
                    for m in n:
                        if str(key) in m:
                            print(game_array)
                            count += 1
                            if count > 1:
                                display_message("No!")
                                return False
                        elif count == 0:
                            images.append((x, y, mass_1[key]["picture"]))
                            game_array[i][j] = (x, y, mass_1[key]["text"], False)

            if dis < SCREEN_WIDTH // ROWS // 2 and key == 10:
                for image in images:
                    if image[0] == x and image[1] == y:
                        images.remove(image)
                        game_array[i][j] = (x, y, mass_1[key]["text"], True)


def has_won(game_array):
    for i in game_array:
        for j in i:
            if True in j:
                return False

    display_message("You won!")
    return True


def render():
    screen.fill(WHITE)
    draw_grid()
    for image in images:
        x, y, IMAGE = image
        screen.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))

    pygame.display.update()


def display_message(content):
    pygame.time.delay(500)
    screen.fill(WHITE)
    end_text = END_FONT.render(content, 1, BLACK)
    screen.blit(end_text, ((SCREEN_WIDTH - end_text.get_width()) // 2, (SCREEN_WIDTH - end_text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(300)


def main():
    global images
    images = []
    run = True
    game_array = initialize_grid()
    clock = pygame.time.Clock()
    key = None
    inputs = {pygame.K_1: 1, pygame.K_2: 2, pygame.K_3: 3, pygame.K_4: 4, pygame.K_5: 5,
              pygame.K_6: 6, pygame.K_7: 7, pygame.K_8: 8, pygame.K_9: 9, pygame.K_DELETE: 10}

    while run:
        clock.tick(10)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key in inputs:
                    key = inputs.get(event.key)
            if event.type == pygame.MOUSEBUTTONDOWN and key is None:
                pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click(game_array, key)

        render()

        if has_won(game_array):
            run = False


while True:
    if __name__ == "__main__":
        main()
