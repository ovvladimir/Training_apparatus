import pygame
from settings import *
from Back_Ground import *


class Bot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        sprite = pygame.image.load('img/Bot4.png')
        sprite = pygame.transform.scale(sprite, (size_x, size_y))
        animation = [sprite.subsurface((0, 0, size_x // 2, size_y)),
                     sprite.subsurface((size_x // 2, 0, size_x // 2, size_y))]
        self.images = animation

        self.index = 0
        self.range = len(self.images)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(topleft=(Kletky_rect.topleft))

    def update(self):
        # для проверки
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += 2
        if keys[pygame.K_LEFT]:
            self.rect.x -= 2
        if keys[pygame.K_UP]:
            self.rect.y -= 2
        if keys[pygame.K_DOWN]:
            self.rect.y += 2


bot = Bot()
group = pygame.sprite.Group(bot)
