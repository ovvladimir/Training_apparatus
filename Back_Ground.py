import pygame
from settings import *
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '0,30'
pygame.init()
info = pygame.display.Info()
WIDTH_WIN, HEIGHT_WIN = info.current_w, info.current_h
pygame.display.set_icon(pygame.image.load('img/inv_lamp_button.png'))
pygame.display.set_caption('Стёпа-робот')
screen = pygame.display.set_mode((WIDTH_WIN, HEIGHT_WIN))
clock = pygame.time.Clock()

part1 = pygame.Surface((WIDTH_WIN // 6, HEIGHT_WIN))
part1_rect = part1.get_rect(topleft=(0, 0))
part1.fill(com_BG)

part2 = pygame.Surface((WIDTH_WIN // 2, HEIGHT_WIN))
part2_rect = part2.get_rect(topleft=(WIDTH_WIN // 2, 0))
part2.fill(BG_COLOR1)

part3 = pygame.Surface((WIDTH_WIN // 2, HEIGHT_WIN // 6))
part3_rect = part3.get_rect(topleft=(WIDTH_WIN // 2, 0))
part3.fill(BG_COLOR2)

part4 = pygame.Surface((WIDTH_WIN, HEIGHT_WIN), pygame.SRCALPHA)
part4_rect = part4.get_rect(topleft=(0, 0))
part4.fill(BG_4)

BG_map = pygame.image.load('img/коридор.jpg')
BG_map = pygame.transform.scale(
    BG_map, (part2.get_width(), part2.get_height() - part3.get_height()))
BG_map_rect = BG_map.get_rect(topleft=(0, part3.get_height()))

Kletky = pygame.image.load('img/kletky.png')
Kletky = pygame.transform.scale(Kletky, (600, 640))
Kletky_rect = Kletky.get_rect(
    bottomleft=(
        part2_rect.bottomleft[0] + (part2.get_width() - Kletky.get_width()) // 2, part2_rect.bottomleft[1]))

dict_draw = {
    part1: part1_rect, part2: part2_rect,
    part3: part3_rect, BG_map: BG_map_rect
}

image_btn = pygame.image.load('img/start_button.png')
image_btn = pygame.transform.scale(image_btn, (100, 100))
image_btn_rect = image_btn.get_rect(center=(part3_rect.left + 100, part3_rect.centery))

st_btn = pygame.image.load('img/pause_button.png')
st_btn = pygame.transform.scale(st_btn, (90, 90))

speed = pygame.image.load('img/speed_button.png')
speed = pygame.transform.scale(speed, (100, 100))
speed_rect = speed.get_rect(center=(part3_rect.left + 400, part3_rect.centery))

speed1 = pygame.image.load('img/inv_speed_button.png')
speed1 = pygame.transform.scale(speed1, (100, 100))

res = pygame.image.load('img/restart_button.png')
res = pygame.transform.scale(res, (100, 100))
res_rect = res.get_rect(center=(part3_rect.left + 250, part3_rect.centery))

res1 = pygame.image.load('img/inv_restart_button.png')
res1 = pygame.transform.scale(res1, (100, 100))

lamp = pygame.image.load('img/lamp_button.png')
lamp = pygame.transform.scale(lamp, (100, 100))
lamp_rect = lamp.get_rect(center=(part3_rect.left + 550, part3_rect.centery))

inv_lamp = pygame.image.load('img/inv_lamp_button.png')
inv_lamp = pygame.transform.scale(inv_lamp, (100, 100))

task = pygame.image.load('img/task_button.png')
task = pygame.transform.scale(task, (100, 100))
task_rect = task.get_rect(center=(part3_rect.left + 700, part3_rect.centery))

inv_task = pygame.image.load('img/inv_task_button.png')
inv_task = pygame.transform.scale(inv_task, (100, 100))

pods1_1 = pygame.image.load('img/Bot1.png')
pods1_1 = pygame.transform.scale(pods1_1, (200, 200))
pods1_1_rect = pods1_1.get_rect(center=(WIDTH_WIN // 2 - 100, HEIGHT_WIN // 2))
pods1_2 = pygame.image.load('img/Bot2.png')
pods1_2 = pygame.transform.scale(pods1_2, (200, 200))
pods1_2_rect = pods1_2.get_rect(center=(WIDTH_WIN // 2 - 100, HEIGHT_WIN // 2))
podskazki = [pods1_1, pods1_2]


def draw():
    pygame.draw.rect(part1, pygame.Color('black'),
                     [0, 0, WIDTH_WIN // 6 - 1, HEIGHT_WIN - 1], 3)

    pygame.draw.rect(part2, pygame.Color('black'),
                     [0, 0, WIDTH_WIN // 2, HEIGHT_WIN], 3)

    pygame.draw.rect(screen, pygame.Color('black'),
                     [WIDTH_WIN // 6, 0, WIDTH_WIN // 3, HEIGHT_WIN], 3)

    pygame.draw.rect(part3, pygame.Color('black'),
                     [0, 0, WIDTH_WIN, HEIGHT_WIN], 3)
