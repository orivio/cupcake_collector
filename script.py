import pygame
pygame.init()

class Player:
    def __init__(self):
        self.x = 100
        self.y = 300
        self.dy = 1

        self.idle = pygame.image.load(r"png sprites\paperclip idle.png").convert_alpha()
        self.idle = pygame.transform.scale(self.idle, (50, 50))

        self.fall = pygame.image.load(r"png sprites\paperclip fall.png").convert_alpha()
        self.fall = pygame.transform.scale(self.fall, (50, 50))

        self.jump = pygame.image.load(r"png sprites\paperclip jump.png").convert_alpha()
        self.jump = pygame.transform.scale(self.jump, (50, 50))

        self.left = pygame.image.load(r"png sprites\paperclip left.png").convert_alpha()
        self.left = pygame.transform.scale(self.left, (50, 50))

        self.right = pygame.image.load(r"png sprites\paperclip right.png").convert_alpha()
        self.right = pygame.transform.scale(self.right, (50, 50))

        self.anim = self.idle

gameloop = True
WIDTH = 600
HEIGHT = 400
clock = pygame.time.Clock()
pygame.display.set_caption("Clippy Collector")
screen = pygame.display.set_mode((WIDTH, HEIGHT), vsync = 1)

player = Player()
player_box = pygame.Rect(player.x, player.y, 30, 50)
grav_velocity = 1
on_ground = False

while gameloop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        if event.type == pygame.KEYDOWN:
             if event.key in (pygame.K_UP, pygame.K_SPACE, pygame.K_w) and on_ground:
                  player.dy = -15
                  on_ground = False

    keys = pygame.key.get_pressed()

    player.dy += grav_velocity
    player.y += player.dy
    player_box.x = player.x
    player_box.y = player.y

    if player_box.bottom >= HEIGHT:
        player.dy = 0
        on_ground = True
    if player_box.right >= WIDTH:
        player_box.x -=1 + (player_box.x - WIDTH)
    if player_box.top <= 0:
        player_box.y += 1 + (abs(player_box.y))
    if player_box.left <= 0:
        player_box.x += 1 + (abs(player_box.x))

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.x -= 3
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.x += 3

    if on_ground:
         grav_velocity = 0
         if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
              player.anim = player.right
         elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
              player.anim = player.left
         else:
              player.anim = player.idle
    else:
         grav_velocity = 1
         if player.dy < 1:
              player.anim = player.jump
         else:
              player.anim = player.fall

    screen.fill((84, 156, 105))
    screen.blit(player.anim, (player.x, player.y))
    
    clock.tick(60)
    pygame.display.flip()

pygame.quit()