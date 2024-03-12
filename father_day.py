import pygame
import time

pygame.init()

WIDTH = 700
HEIGHT = 700
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Fathers day")
img = pygame.image.load("father_day.jpg")
image = pygame.transform.scale(img, (700, 700))

while True:
    font = pygame.font.SysFont("Academy Engraved LET", 70)
    text_1 = font.render("Happy", True, (50, 100, 150))
    text_2 = font.render("Fathers day", True, (50, 20, 150))
    text_4 = font.render("!!!", True, (50, 60, 150))


    text1_rect = text_1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    text2_rect = text_2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10))
    text4_rect = text_4.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))

    display_surface.fill("white")
    display_surface.blit(image, (0, 0))
    display_surface.blit(text_1, text1_rect)
    display_surface.blit(text_2, text2_rect)
    display_surface.blit(text_4, text4_rect)
    pygame.display.update()
    time.sleep(3)

    image_2 = pygame.image.load("father_cake.png")
    font_2 = pygame.font.SysFont("Academy Engraved LET", 60)
    text_3 = font_2.render("have the best day", True, (40,100,130))
    display_surface.fill((137,207,240))
    display_surface.blit(image_2, (0,0))
    display_surface.blit(text_3, (30,350))
    pygame.display.update()
    time.sleep(2)
    