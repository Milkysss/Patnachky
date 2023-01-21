import pygame
import os
import random
import sys
import datetime

pygame.mixer.init()

pygame.mixer.music.load("fon_p.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.init()

WIDTH = 600
HEIGHT = 600

screen_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(screen_size)

screen_rect = (0, 0, WIDTH, HEIGHT)

global IMAGE_CHIPS

# Комбинация выигрыша

win = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

FPS = 50
gravity = 0.25


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


def terminate():
    pygame.quit()
    pygame.mixer.music.pause()
    sys.exit()


def start_screen():
    is_fine_name = False
    user = 'Введите имя:'
    instr = 'Выигрышная ситуация: 1 2 3 4   5 6 7 8   9 10 11 12   13 14 15 '
    while not is_fine_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    user += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    user = user[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(user) > 2:
                        global USERNAME
                        USERNAME = user
                        is_fine_name = True
                        break

        screen.fill((0, 0, 0))
        fon = pygame.transform.scale(load_image('zastavka.jpg'), [600, 600])
        screen.blit(fon, (10, 10))

        font = pygame.font.Font(None, 40)
        text_welcome = font.render("Welcome!", True, (255, 255, 255))
        screen.blit(text_welcome, (400, 20))

        font = pygame.font.Font(None, 40)
        text_user = font.render(user, True, (255, 255, 255))
        rect_user = text_user.get_rect()
        rect_user.center = screen.get_rect().center
        screen.blit(text_user, (300, 400))

        font = pygame.font.Font(None, 20)
        text_instr = font.render(instr, True, (255, 255, 255))
        screen.blit(text_instr, (40, 490))
        #  rect_instr.center = screen.get_rect().center
        #  screen.blit(text_instr, (550, 150))

        pygame.display.flip()
        clock.tick(FPS)

clock = pygame.time.Clock()
start_screen()
pygame.mixer.music.play(-1)


def get_images():
    try:
        IMAGE_CHIPS = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        IMAGE_CHIPS[1] = pygame.image.load(os.path.join('images', 'i1.jpg'))
        IMAGE_CHIPS[2] = pygame.image.load(os.path.join('images', 'i2.jpg'))
        IMAGE_CHIPS[3] = pygame.image.load(os.path.join('images', 'i3.jpg'))
        IMAGE_CHIPS[4] = pygame.image.load(os.path.join('images', 'i4.jpg'))
        IMAGE_CHIPS[5] = pygame.image.load(os.path.join('images', 'i5.jpg'))
        IMAGE_CHIPS[6] = pygame.image.load(os.path.join('images', 'i6.jpg'))
        IMAGE_CHIPS[7] = pygame.image.load(os.path.join('images', 'i7.jpg'))
        IMAGE_CHIPS[8] = pygame.image.load(os.path.join('images', 'i8.jpg'))
        IMAGE_CHIPS[9] = pygame.image.load(os.path.join('images', 'i9.jpg'))
        IMAGE_CHIPS[10] = pygame.image.load(os.path.join('images', 'i10.jpg'))
        IMAGE_CHIPS[11] = pygame.image.load(os.path.join('images', 'i11.jpg'))
        IMAGE_CHIPS[12] = pygame.image.load(os.path.join('images', 'i12.jpg'))
        IMAGE_CHIPS[13] = pygame.image.load(os.path.join('images', 'i13.jpg'))
        IMAGE_CHIPS[14] = pygame.image.load(os.path.join('images', 'i14.jpg'))
        IMAGE_CHIPS[15] = pygame.image.load(os.path.join('images', 'i15.jpg'))
    except pygame.error as message:
        print('Не удаётся загрузить изображение')
        raise SystemExit(message)
    return IMAGE_CHIPS


def print_blocks():
    # отрисовка поля
    x = 0
    y = 0
    for i in range(16):
        if deck[i] > 0:
            screen.blit(IMAGE_CHIPS[deck[i]], (x, y))

        x = x + 100
        if i == 3 or i == 7 or i == 11:
            x = 0
            y = y + 100


def possible_moves(new_game):
    
    # Список доступных ходов
    
    moves = []
    ind = new_game.index(0)
    if ind == 0:
        moves.append(new_game[1])
        moves.append(new_game[4])
    elif ind == 1:
        moves.append(new_game[0])
        moves.append(new_game[2])
        moves.append(new_game[5])
    elif ind == 2:
        moves.append(new_game[1])
        moves.append(new_game[3])
        moves.append(new_game[6])
    elif ind == 3:
        moves.append(new_game[2])
        moves.append(new_game[7])
    elif ind == 4:
        moves.append(new_game[0])
        moves.append(new_game[5])
        moves.append(new_game[8])
    elif ind == 5:
        moves.append(new_game[1])
        moves.append(new_game[4])
        moves.append(new_game[6])
        moves.append(new_game[9])
    elif ind == 6:
        moves.append(new_game[2])
        moves.append(new_game[5])
        moves.append(new_game[7])
        moves.append(new_game[10])
    elif ind == 7:
        moves.append(new_game[3])
        moves.append(new_game[6])
        moves.append(new_game[11])
    elif ind == 8:
        moves.append(new_game[4])
        moves.append(new_game[9])
        moves.append(new_game[12])
    elif ind == 9:
        moves.append(new_game[5])
        moves.append(new_game[8])
        moves.append(new_game[10])
        moves.append(new_game[13])
    elif ind == 10:
        moves.append(new_game[6])
        moves.append(new_game[9])
        moves.append(new_game[11])
        moves.append(new_game[14])
    elif ind == 11:
        moves.append(new_game[7])
        moves.append(new_game[10])
        moves.append(new_game[15])
    elif ind == 12:
        moves.append(new_game[8])
        moves.append(new_game[13])
    elif ind == 13:
        moves.append(new_game[9])
        moves.append(new_game[12])
        moves.append(new_game[14])
    elif ind == 14:
        moves.append(new_game[10])
        moves.append(new_game[13])
        moves.append(new_game[15])
    else:
        moves.append(new_game[11])
        moves.append(new_game[14])

    return moves


def get_new_random():
    line = list(range(16))
    random.shuffle(line)
    return line


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    fire = [load_image("star.png")]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость - это вектор
        
        self.velocity = [dx, dy]
        
        # и свои координаты
        
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой
        
        self.gravity = gravity


    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        
        self.velocity[1] += self.gravity
        
        # перемещаем частицу
        
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
        # убиваем, если частица ушла за экран
        
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position):
    
    # количество создаваемых частиц
    
    particle_count = 20
    
    # возможные скорости
    
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))

def victory_game():
    now = datetime.datetime.now()
    with open('result.txt', 'a', encoding = 'utf-8') as file:
        file.write(USERNAME[12:] + '  Victory  ' + now.strftime("%d-%m-%Y %H:%M") + '\n')
    # sys.exit()

# Основной код игры

def start_game():
    pass


# Получаем список изображений
IMAGE_CHIPS = get_images()

# Новый расклад
deck = get_new_random()

# Готовим экран

black = 0, 0, 0
size = width, height = 399, 399
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
pygame.display.set_caption("Пятнашки" + '    ' + USERNAME[12:])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    movies = possible_moves(deck)
    
    # Ждем щелчок мыши на поле
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = event.pos
        ansver = int(pos[0] / 100) + (int(pos[1] / 100)) * 4
        if deck[ansver] in movies:
            nul = deck.index(0)
            deck[nul] = deck[ansver]
            deck[ansver] = 0

        if deck == vin:
            victory_game()
            break


    screen.fill(black)
    print_blocks()
    pygame.display.flip()

# create_particles(pygame.mouse.get_pos())

create_particles((100, 100))
pygame.mouse.set_visible(0)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            running = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
            # создаем частицы по щелчку мыши
        # создаем частицы при любом событии мыши
        create_particles(pygame.mouse.get_pos())
        # create_particles((100, 100))

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()












