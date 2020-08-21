import pygame
import sys, random

# creating variable for the screen size
width = 800
height = 600
# must initialize pygame modules
pygame.init()
Red = (255, 0, 0)
Blue = (0, 0, 255)
yellow = (255, 255, 0)
player_size = 50
player_position = [width/2, height-1.5*player_size]
background_color = (0, 0, 0)
enemy_size = 50
enemy_position = [random.randint(0, width-enemy_size), random.randint(0, height-570)]
enemy_list = [enemy_position]
clock = pygame.time.Clock()
myFont = pygame.font.SysFont('cambria', 15)
speed = 10
score = 0

# creating a screen for display
screen = pygame.display.set_mode((width, height))
# creating a flag for the game loop
game_over = False


def set_level(score, speed):
    if score < 20:
        speed = 15
    elif score < 40:
        speed = 20
    elif score < 80:
        speed = 25
    else:
        speed = 30
    return speed


def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, width-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])


def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        # draws the enemy
        pygame.draw.rect(screen, Blue, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))


def updated_enemy_position(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        # update the position of the enemy
        if 0 <= enemy_pos[1] < height:
            enemy_pos[1] += speed
        else:
            # enemy_pos[0] = random.randint(0, width - enemy_size)
            # enemy_pos[1] = 0
            score += 1
            enemy_list.pop(idx)
    return score


def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False


def detect_collision(player_pos, enemy_pos):
    # top left corner of the player rectangle
    p_x = player_pos[0]
    p_y = player_pos[1]
    # top left corner of the enemy rectangle
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    # checks if the (x,y) coordinates of the rectangles have intersected
    if (p_x <= e_x <= (p_x+player_size)) or (e_x <= p_x < (e_x+enemy_size)):
        if ((p_y+player_size) > e_y >= p_y) or (e_y <= p_y < (e_y+enemy_size)):
            return True
    return False


# creating a game loop
while not game_over:
    # creating a loop to handle the game events
    for event in pygame.event.get():
        # creating a condition to handle the game closing
        if event.type == pygame.QUIT:
            sys.exit()
        # creating a condition if a user physically pushes down on a key
        if event.type == pygame.KEYDOWN:
            x = player_position[0]  # x-coordinate
            y = player_position[1]  # y-coordinate
            # if the left arrow key is pressed moves player to the left
            if event.key == pygame.K_LEFT:
                x -= player_size
            # if the right arrow key is pressed moves player to the right
            elif event.key == pygame.K_RIGHT:
                x += player_size
            player_position = [x, y]
    screen.fill(background_color)

    # checks if enemy has collided with the player
    # if detect_collision(player_position, enemy_position):
    #     game_over = True
    #     break

    # calling functions that drop enemies on to the screen
    drop_enemies(enemy_list)
    score = updated_enemy_position(enemy_list, score)
    text = "Score:" + str(score)
    label = myFont.render(text, 1, yellow)
    screen.blit(label, (width-200, height-20))
    speed = set_level(score, speed)
    if collision_check(enemy_list, player_position):
        game_over = True
        break
    draw_enemies(enemy_list)
    # rect(Surface, color, rect, width=0)
    pygame.draw.rect(screen, Red, (player_position[0], player_position[1], player_size, player_size))

    clock.tick(30)
    # updates the screen to create the rectangle
    pygame.display.update()
