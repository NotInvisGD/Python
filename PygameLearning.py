import pygame
import os

WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Pygame Project!")
WHITE = (255, 255, 255)
RED_COLOR = (255, 0, 0)
YELLOW_COLOR = (255, 255, 0)
ORANGE_COLOR = (255, 165, 0)
MIDDLE_BORDER = pygame.Rect((WIDTH//2 - 5), 0, 10, HEIGHT)
FPS = 60
VEL = 4
BULLET_VELOCITY = 6.5
TOTAL_BULLETS = 10
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 60, 45
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_window(red, yellow, red_bullets, yellow_bullets):
    WINDOW.fill(WHITE)
    pygame.draw.rect(WINDOW, RED_COLOR, MIDDLE_BORDER)
    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))
    
    for bullet in red_bullets:
        pygame.draw.rect(WINDOW, ORANGE_COLOR, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WINDOW, YELLOW_COLOR, bullet)
        
    pygame.display.update()
    
def yellow_movement_handle(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < MIDDLE_BORDER.x:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:
        yellow.y += VEL

def red_movement_handle(keys_pressed, red):
    if keys_pressed[pygame.K_j] and red.x - VEL > MIDDLE_BORDER.x + MIDDLE_BORDER.width:
        red.x -= VEL
    if keys_pressed[pygame.K_l] and red.x + VEL + red.width < WIDTH:
        red.x += VEL
    if keys_pressed[pygame.K_i] and red.y - VEL > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_k] and red.y + VEL + red.height < HEIGHT - 15:
        red.y += VEL

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VELOCITY
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
    
    for bullet in red_bullets:
        bullet.x -= BULLET_VELOCITY
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            yellow_bullets.remove(bullet)
    
def main():
    red = pygame.Rect(650, 240, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(150, 240, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red_bullets = []
    yellow_bullets = []
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        WINDOW.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < TOTAL_BULLETS:
                    bullet_yellow = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2, 10, 5)
                    yellow_bullets.append(bullet_yellow)
                
                if event.key == pygame.K_RCTRL and len(red_bullets) < TOTAL_BULLETS:
                    bullet_red = pygame.Rect(red.x, red.y + red.height//2, 10, 5)
                    red_bullets.append(bullet_red)
                    
        
        keys_pressed = pygame.key.get_pressed()
        yellow_movement_handle(keys_pressed, yellow)
        red_movement_handle(keys_pressed, red)
   
        draw_window(red, yellow, red_bullets, yellow_bullets)
    
    pygame.quit()

if __name__ == "__main__":
    main()
