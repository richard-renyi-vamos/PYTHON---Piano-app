import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Piano 🎹")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define keys and sounds
keys = [
    {"key": pygame.K_a, "sound": "sounds/c.wav", "color": WHITE, "x": 0},
    {"key": pygame.K_s, "sound": "sounds/d.wav", "color": WHITE, "x": 100},
    {"key": pygame.K_d, "sound": "sounds/e.wav", "color": WHITE, "x": 200},
    {"key": pygame.K_f, "sound": "sounds/f.wav", "color": WHITE, "x": 300},
    {"key": pygame.K_g, "sound": "sounds/g.wav", "color": WHITE, "x": 400},
    {"key": pygame.K_h, "sound": "sounds/a.wav", "color": WHITE, "x": 500},
    {"key": pygame.K_j, "sound": "sounds/b.wav", "color": WHITE, "x": 600},
    {"key": pygame.K_k, "sound": "sounds/c2.wav", "color": WHITE, "x": 700},
]

# Load sounds
for key in keys:
    key["sound"] = pygame.mixer.Sound(key["sound"])

# Main loop
run = True
while run:
    WIN.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            for key in keys:
                if event.key == key["key"]:
                    key["sound"].play()
                    key["color"] = BLACK
        if event.type == pygame.KEYUP:
            for key in keys:
                if event.key == key["key"]:
                    key["color"] = WHITE

    # Draw keys
    for key in keys:
        pygame.draw.rect(WIN, key["color"], (key["x"], 0, 100, HEIGHT))

    pygame.display.update()

pygame.quit()
