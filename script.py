import pygame
pygame.init()


class Player:
    def __init__(self):
        self.x = 100
        self.y = 300
        self.dy = 1

        self.idle = pygame.image.load(r"png sprites\paperclip idle.png").convert_alpha()
        self.idle = pygame.transform.scale(self.idle, (50, 50))

gameloop = True
WIDTH = 600
HEIGHT = 400
clock = pygame.time.Clock()
pygame.display.set_caption("Clippy Collector")
screen = pygame.display.set_mode((WIDTH, HEIGHT), vsync = 1)

player = Player()
player_box = pygame.Rect(player.x, player.y, 30, 50) #added w/o test
grav_velocity = 1

while gameloop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    keys = pygame.key.get_pressed()

    screen.fill((84, 156, 105))
    screen.blit(player.idle, (player.x, player.y))
    player.dy += grav_velocity
    player.y += player.dy


    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= 3
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += 3

    #if keys[pygame.K_UP] or keys[pygame.K_SPACE] or keys[pygame.K_w]:
     #   player.y += 50
      #  player.grav_velocity = -1

#added w/o test
    if player_box.y >= HEIGHT:
        player_box.y -= 1 + (player_box.y - HEIGHT)
    if player_box.x >= WIDTH:
        player_box.x -=1 + (player_box.x - WIDTH)
    if player_box.y <= 0:
        player_box.y += 1 + (abs(player_box.y))
    if player_box.x <= 0:
        player_box.x += 1 + (abs(player_box.x))
    
    clock.tick(60)
    pygame.display.flip()

pygame.quit()