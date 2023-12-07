import pygame
import button

# Initialize Pygame
pygame.init()


# Set Size of Screen Size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Main Menu")

# Game variables
game_paused = False

# Font
font = pygame.font.SysFont("arialblack", 40)
color = (255, 255, 255)

# Load Images
start_img = pygame.image.load("assets/others icons/start.png").convert_alpha()
# exit_img = pygame.image.load("assets/others icons/exit.png").convert_alpha()

# Create Instaces
start_button = button.Button(304, 125, start_img, 0.2)
# exit_button = button.Button(304, 325, exit_img, 0.2)


def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


run = True
while run:
    screen.fill((52, 78, 91))

    if game_paused == True:
        draw_text("Press SPACE to pause", font, color, 160, 250)
    else:
        if start_button.draw(screen):
            game_paused = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()















































"""
# Load Musics
track1 = pygame.mixer.music.load("assets/musics/careless.mp3")
track1 = pygame.mixer.Sound("assets/musics/careless.mp3")

pygame.mixer.music.set_volume(0.2)


# Load Images
OG_KEY={
    "w_key": "assets/keyboard/w key.png",
    "a_key": "assets/keyboard/a key.png",
    "s_key": "assets/keyboard/s key.png",
    "d_key": "assets/keyboard/d key.png",
    "space_key": "assets/keyboard/space key.png"
}
AL_KEY={
    "w_key": "assets/keyboard/w key(after).png",
    "a_key": "assets/keyboard/a key(after).png",
    "s_key": "assets/keyboard/s key(after).png",
    "d_key": "assets/keyboard/d key(after).png",
    "space_key": "assets/keyboard/space key(after).png"
}
FALSE_KEY={
    "w_key": "assets/keyboard/w key(wrong).png",
    "a_key": "assets/keyboard/a key(wrong).png",
    "s_key": "assets/keyboard/s key(wrong).png",
    "d_key": "assets/keyboard/d key(wrong).png"
}
BG={
    "dreamy": "assets/background/dreamy.png",
    "mountain": "assets/background/mountain.png",
    "nightsky": "assets/background/nightsky.png",
    "redsky": "assets/background/redsky.png",
    "sunset": "assets/background/sunset.png"
}
TASKBAR={
    "dreamy": "assets/taskbar/redsky+dreamy.png",
    "mountain": "assets/taskbar/mountain.png",
    "nightsky": "assets/taskbar/nightsky.png",
    "redsky": "assets/taskbar/redsky+dreamy.png",
    "sunset": "assets/taskbar/sunset.png"
}


# Set Classes
class Taskbar(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y):
        super().__init__()
        self.surface = pygame.Surface([600, 600])
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y ):
        super().__init__()
        self.image = pygame.Surface([700, 50])
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def update(self, img, new_x_pos, new_y_pos) :
        self.image = pygame.image.load(img)
        self.rect.x = new_x_pos
        self.rect.y = new_y_pos
class Keyboard(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface([700, 50])
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y                 
class Group(pygame.sprite.Group):
    def update(self):
        for Object in self.sprites():
            Object.update()


# Set Functions
def evaluate_time(current_time, start_time, obstacle_group):
    if current_time-start_time > 1000:
        obstacle_group.empty()
def choose_random(list_name):
    selection = []
    chosen_value = ()
    for k in list_name :
        selection.append(k)
    chosen_value = random.choice(selection)
    return chosen_value
def evaluate_xdistance(obstacle_sequence):
    if obstacle_sequence == 10 or obstacle_sequence == 6:
        x = 300
    elif obstacle_sequence == 7 or obstacle_sequence == 8 or obstacle_sequence == 9:
        x = 290
    elif obstacle_sequence == 3 or obstacle_sequence == 4 or obstacle_sequence == 5:
        x = 400 - (obstacle_sequence - 3) * 50
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
def create_key(lib):
    use_key = pygame.image.load(lib)
    return use_key
def OG_key():
    screen.blit(create_key(OG_KEY["w_key"]), [SCREEN_WIDTH - 1000, SCREEN_HEIGHT - 100])
    screen.blit(create_key(OG_KEY["a_key"]), [SCREEN_WIDTH - 1000, SCREEN_HEIGHT - 55])
    screen.blit(create_key(OG_KEY["s_key"]), [SCREEN_WIDTH - 1050, SCREEN_HEIGHT - 55])
    screen.blit(create_key(OG_KEY["d_key"]), [SCREEN_WIDTH - 950, SCREEN_HEIGHT - 55])
    screen.blit(create_key(OG_KEY["space_key"]), [SCREEN_WIDTH - 150, SCREEN_HEIGHT - 100])


# Set Main Loop
def main():
    RUNNING = True

    obstacle_group = pygame.sprite.Group()
    taskbar_group = pygame.sprite.Group() # Image Size: 686 x 52 px

    random_value = choose_random(BG)
    background = pygame.image.load(BG[random_value])

    taskbar = Taskbar(TASKBAR[random_value], 540, 665)
    taskbar_group.add(taskbar)

    screen.blit(background, [0, 0])

    while RUNNING:
        TESTING = True

        right_ans = 0
        wrong_ans = 0
        pygame.display.update()
        
        OG_key()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

        taskbar_group.draw(screen)
        pygame.display.flip()

        obstacle_sequence = random.randrange(3, 11)
        x_coord = evaluate_xdistance(obstacle_sequence)
        y_coord = 640
        distance = evaluate_ydistance(obstacle_sequence)
        z_coord = 0

        answer = []
        coordinate = []
        key = ["state"]

        print(key)

        pygame.display.update()

        for i in range(obstacle_sequence):
            new_key = ["w_key", "a_key", "s_key", "d_key"]
            generate_key = random.choice(new_key)
            answer.append(generate_key)

            obstacle = Obstacle(OG_KEY[generate_key], x_coord, y_coord)
            coordinate.append(x_coord)
            obstacle_group.add(obstacle)

            pygame.time.wait(50)
            pygame.display.update()

            x_coord += distance

            obstacle_group.draw(screen)

        pygame.display.update()
        print(answer)
        print(answer[0])
        print(coordinate[0])

        while TESTING:
            current_time = pygame.time.get_ticks()

            OG_key()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUNNING = False
                    TESTING = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        key.append("w_key")
                        screen.blit(create_key(AL_KEY["w_key"]), [SCREEN_WIDTH - 1000, SCREEN_HEIGHT - 100])
                    if event.key == pygame.K_a:
                        key.append("a_key")
                        screen.blit(create_key(AL_KEY["a_key"]), [SCREEN_WIDTH - 1050, SCREEN_HEIGHT - 55])
                    if event.key == pygame.K_s:
                        key.append("s_key")
                        screen.blit(create_key(AL_KEY["s_key"]), [SCREEN_WIDTH - 950, SCREEN_HEIGHT - 55])
                    if event.key == pygame.K_d:
                        key.append("d_key")
                        screen.blit(create_key(AL_KEY["d_key"]), [SCREEN_WIDTH - 900, SCREEN_HEIGHT - 55])
                    if event.key == pygame.K_SPACE:
                        key.append("submit")
                        screen.blit(create_key(AL_KEY["space_key"]), [SCREEN_WIDTH - 150, SCREEN_HEIGHT - 100])
                    pygame.display.flip()
                    obstacle_group.empty()

                    eva_time = pygame.time.get_ticks()
                    evaluate_time(current_time, eva_time, obstacle_group)

                    if key[-1] == answer[0]:
                        obstacle.update(AL_KEY[answer[0]], coordinate[z_coord], y_coord)
                        obstacle_group.add(obstacle)
                        obstacle_group.draw(screen)
                        right_ans += 1
                        z_coord += 1
                        answer.pop(0)
                        obstacle_group.empty()
                    elif key[-1] != answer[0]:
                        obstacle.update(FALSE_KEY[answer[0]], coordinate[z_coord], y_coord)
                        obstacle_group.add(obstacle)
                        obstacle_group.draw(screen)
                        wrong_ans += 1
                        z_coord += 1
                        answer.pop(0)
                        obstacle_group.empty()

                    eva_time = pygame.time.get_ticks()
                    evaluate_time(eva_time, current_time,obstacle_group)

                    pygame.display.flip()

                    if key[-1] == "submit":
                        TESTING = False
                    elif answer == []:
                        TESTING = False
                        pygame.time.wait(20)
                        key = []

                    eva_time = pygame.time.get_ticks()
                
                pygame.display.flip()
            pygame.display.flip()

    time.sleep(10)

main()
"""