import pygame
import random
import threading
import time


# Initialize Pygame
pygame.init()

# Set the Screen Size
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill("white")
pygame.display.flip()

# Load the Images
OG_KEY = {
    "w_key": "assets/keyboard/w key.png",
    "a_key": "assets/keyboard/a key.png",
    "s_key": "assets/keyboard/s key.png",
    "d_key": "assets/keyboard/d key.png",
    "space_key": "assets/keyboard/space key.png",
}

Al_KEY = {
    "w_key": "assets/keyboard/w key(after).png",
    "a_key": "assets/keyboard/a key(after).png",
    "s_key": "assets/keyboard/s key(after).png",
    "d_key": "assets/keyboard/d key(after).png",
    "space_key": "assets/keyboard/space key(after).png",
}

BG = {
    "dreamy": "assets/background/dreamy.png",
    "mountain": "assets/background/mountain.png",
    "nightsky": "assets/background/nightsky.png",
    "redsky": "assets/background/redsky.png",
    "sunset": "assets/background/sunset.png",
}

TASKBAR = {
    "mountain": "assets/taskbar/mountain.png",
    "nightsky": "assets/taskbar/nightsky.png",
    "redsky": "assets/taskbar/redsky+dreamy.png",
    "dreamy": "assets/taskbar/redsky+dreamy.png",
    "sunset": "assets/taskbar/sunset.png"
}


# Create Classes
class Taskbar(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y):
        super().__init__()
        self.surface = pygame.Surface([600, 600])
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y ):
        super().__init__()
        self.image = pygame.Surface([700, 50])
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

class GameKey(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


# Create Functions
def choose_random(list_name):
    selection = []
    chosen_value = ()
    for k in list_name:
        selection.append(k)
    chosen_value = random.choice(selection)
    return chosen_value


def evaluate_xdistance(obstacle_sequence):
    if obstacle_sequence == 10 or obstacle_sequence == 6:
        x = 310
    elif obstacle_sequence == 7 or obstacle_sequence == 8 or obstacle_sequence == 9:
        x = 300
    elif obstacle_sequence == 3 or obstacle_sequence == 4 or obstacle_sequence == 5:
        x = 420 - (obstacle_sequence - 3) * 50
    return x

def evaluate_ydistance(obstacle_sequence):
    if obstacle_sequence == 10 or obstacle_sequence == 6:
        if obstacle_sequence == 10:
            y = 50
        else:
            y = 90
    elif obstacle_sequence == 7 or obstacle_sequence == 8 or obstacle_sequence == 9:
        y = 80 - (obstacle_sequence - 7) * 10
    elif obstacle_sequence == 3 or obstacle_sequence == 4 or obstacle_sequence == 5:
        y = 110
    return y


def OG_key():
    screen.blit(create_key(OG_KEY["w_key"]), (SCREEN_WIDTH - 1000, SCREEN_HEIGHT - 100))
    screen.blit(create_key(OG_KEY["a_key"]), (SCREEN_WIDTH - 1050, SCREEN_HEIGHT - 55))
    screen.blit(create_key(OG_KEY["s_key"]), (SCREEN_WIDTH - 1000, SCREEN_HEIGHT - 55))
    screen.blit(create_key(OG_KEY["d_key"]), (SCREEN_WIDTH - 950, SCREEN_HEIGHT - 55))
    screen.blit(create_key(OG_KEY["space_key"]), (SCREEN_WIDTH - 200,  SCREEN_HEIGHT - 100))


def create_key(lib):
    use_key = pygame.image.load(lib)
    return use_key


def bg_taskbar():
    random_value = choose_random(BG)

    background_x = 0
    background = pygame.image.load(BG[random_value])
    background_width = background.get_width()

    taskbar_group = pygame.sprite.Group()
    taskbar = Taskbar(TASKBAR[random_value], 540, 550)
    taskbar_group.add(taskbar)

    RUNNING = True
    while RUNNING:
        background_x -= 1
        if background_x <= -background_width:
            background_x = 0

        screen.blit(background, (background_x, 0))
        screen.blit(background, (background_x + background_width, 0))

        taskbar_group.draw(screen)

        OG_key()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print("Up")
                    screen.blit(create_key(Al_KEY["w_key"]),(SCREEN_HEIGHT - 1000, SCREEN_WIDTH - 100))
                elif event.key == pygame.K_a:
                    print("Left")
                    screen.blit(create_key(Al_KEY["a_key"]),(SCREEN_HEIGHT - 1050, SCREEN_WIDTH - 55))
                elif event.key == pygame.K_s:
                    print("Down")
                    screen.blit(create_key(Al_KEY["s_key"]),(SCREEN_HEIGHT - 1000, SCREEN_WIDTH - 55))
                elif event.key == pygame.K_d:
                    print("Right")
                    screen.blit(create_key(Al_KEY["d_key"]), (SCREEN_HEIGHT - 950, SCREEN_WIDTH - 55))
                elif event.key == pygame.K_SPACE:
                    print("Space")
                    screen.blit(create_key(Al_KEY["space_key"]), (SCREEN_HEIGHT-  200, SCREEN_WIDTH - 100))
                
                pygame.display.update()
        pygame.display.update()

def obstacle():
    PLAYING = True
    while PLAYING:
        random_value = choose_random(BG)

        obstacle_group = pygame.sprite.Group()
        obstacle_sequence = random.randrange(3, 11)

        taskbar_group = pygame.sprite.Group()
        taskbar = Taskbar(TASKBAR[random_value], 540, 550)
        taskbar_group.add(taskbar)

        x = evaluate_xdistance(obstacle_sequence)
        y = evaluate_ydistance(obstacle_sequence)

        answer = []

        for i in range(obstacle_sequence):
            new_key = ["w_key", "a_key", "s_key", "d_key"]
            generate_key = random.choice(new_key)
            answer.append(generate_key)

            obstacle = Obstacle(OG_KEY[generate_key], x, 550)
            obstacle_group.add(obstacle)

            pygame.time.wait(100)
            pygame.display.update()
                
            x += y

            obstacle_group.draw(screen)
            pygame.display.update()

        obstacle_group.empty()
        pygame.time.wait(2000)
        taskbar_group.draw(screen)
        PLAYING = False

def generate_bg_taskbar():
    bg_thread = threading.Thread(target = bg_taskbar)
    bg_thread.start()
    bg_thread.join()
    print("Done1")
def generate_obstacle():
    obstacle_thread = threading.Thread(target = obstacle)
    obstacle_thread.start()
    obstacle_thread.join()
    print("Done2")



# Create Main Loop
def main_loop():
    while True:
        generate_bg_taskbar()
        generate_obstacle()
        print("Done")

main_loop()