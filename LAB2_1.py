import pygame
import math

# Inicjalizacja pygame
pygame.init()

# Ustawienia ekranu
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Transformacje ośmiokąta")

# Kolory
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Tworzenie ośmiokąta
cx, cy = WIDTH // 2, HEIGHT // 2  # Środek ekranu
radius = 150


def get_octagon(cx, cy, radius):
    angles = [2 * math.pi * i / 8 for i in range(8)]
    return [(cx + radius * math.cos(a), cy + radius * math.sin(a)) for a in angles]


octagon = get_octagon(cx, cy, radius)

# Parametry transformacji
scale_x, scale_y = 1.0, 1.0
rotation_angle = 0
shear_x, shear_y = 0, 0
reflect_x, reflect_y = False, False
attach_top = False
attach_right = False

running = True
while running:
    screen.fill(YELLOW)
    transformed_octagon = []
    for x, y in octagon:
        x = cx + (x - cx) * scale_x
        y = cy + (y - cy) * scale_y
        x_new = cx + (x - cx) * math.cos(rotation_angle) - (y - cy) * math.sin(rotation_angle) + shear_x * (y - cy)
        y_new = cy + (x - cx) * math.sin(rotation_angle) + (y - cy) * math.cos(rotation_angle) + shear_y * (x - cx)

        # Odbicie
        if reflect_x:
            x_new = WIDTH - x_new
        if reflect_y:
            y_new = HEIGHT - y_new

        # Przeniesienie na górę
        if attach_top:
            y_new -= cy - 50  # Przesuwa figurę wyżej, ale zostawia ją widoczną

        # Przeniesienie na prawą krawędź
        if attach_right:
            x_new += WIDTH // 2 - radius  # Przesuwa figurę w prawo, ale zostawia widoczną

        transformed_octagon.append((x_new, y_new))

    pygame.draw.polygon(screen, BLUE, transformed_octagon, 0)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                scale_x *= 1.2
                scale_y *= 1.2
            elif event.key == pygame.K_2:
                rotation_angle += math.radians(15)
            elif event.key == pygame.K_3:
                scale_x, scale_y = scale_y, scale_x
            elif event.key == pygame.K_4:
                shear_x = 0.5
            elif event.key == pygame.K_5:
                scale_y = 0.7  # Zmniejszone spłaszczenie, żeby figura była widoczna
                attach_top = True  # Przesunięcie figury w górę
            elif event.key == pygame.K_6:
                rotation_angle = math.radians(90)
                shear_x = 0.5
            elif event.key == pygame.K_7:
                scale_x, scale_y = scale_y, scale_x
                rotation_angle = math.radians(180)
            elif event.key == pygame.K_8:
                shear_x, shear_y = 0.5, 0.5
                reflect_x = True
            elif event.key == pygame.K_9:
                rotation_angle = math.radians(180)
                shear_x = 0.5
                attach_right = True  # Przesunięcie figury na prawą krawędź
            elif event.key == pygame.K_0:
                scale_x, scale_y = 1.0, 1.0
                rotation_angle = 0
                shear_x, shear_y = 0, 0
                reflect_x, reflect_y = False, False
                attach_top = False
                attach_right = False

pygame.quit()
