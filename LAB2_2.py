import pygame

# Inicjalizacja pygame
pygame.init()

# Ustawienia ekranu
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Czarny okrąg z żółtym kwadratem")

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Wymiary
circle_radius = 200
square_size = 200

# Położenie środka
cx, cy = WIDTH // 2, HEIGHT // 2

# Pętla gry
running = True
while running:
    screen.fill(WHITE)

    # Rysowanie czarnego okręgu
    pygame.draw.circle(screen, BLACK, (cx, cy), circle_radius)

    # Rysowanie żółtego kwadratu na środku
    square_x = cx - square_size // 2
    square_y = cy - square_size // 2
    pygame.draw.rect(screen, YELLOW, (square_x, square_y, square_size, square_size))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()