import pygame
pygame.init()

class Player:
    def __init__(self):
        self.x = 300
        self.y = 200
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

class Platform:
     def __init__ (self, x, y, length, height):
          self.rect = pygame.Rect(x, y, length, height)

gameloop = True
WIDTH = 600
HEIGHT = 400
clock = pygame.time.Clock()
pygame.display.set_caption("Clippy Collector")
screen = pygame.display.set_mode((WIDTH, HEIGHT), vsync = 1)

player = Player()
player_box = pygame.Rect(player.x, player.y, 30, 42)
grav_velocity = 1
on_ground = False

platforms = [
     Platform(0, HEIGHT-50, WIDTH, HEIGHT),
     Platform(50, 230, 100, 30),
     Platform(400, 210, 100, 30)
]

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
    player_box.y += player.dy

    if player_box.right >= WIDTH:
        player_box.x -=1 + (player_box.x - WIDTH)
    if player_box.top <= 0:
        player_box.y += 1 + (abs(player_box.y))
    if player_box.left <= 0:
        player_box.x += 1 + (abs(player_box.x))

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_box.x -= 3
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_box.x += 3


    screen.fill((84, 156, 105))
    screen.blit(player.anim, (player_box.x, player_box.y))
    on_ground = False
    for platform in platforms:
         pygame.draw.rect(screen, (0, 0, 0), platform.rect)
         if player_box.colliderect(platform.rect):
                if player.dy > 0:
                     player.dy = 0
                     on_ground = True
                     player_box.bottom = platform.rect.top
                   
                elif player.dy < 0:
                     player_box.top = platform.rect.bottom
                     player.dy = 1
                     on_ground = False

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
    if player.dy < 0:
        player.anim = player.jump
    elif player.dy > 0:
        player.anim = player.fall
    
    clock.tick(60)
    pygame.display.flip()

pygame.quit()