import pygame
from settings import *
from Back_Ground import *
from Bot_cl import group, bot

bot_pos = Kletky_rect.topleft
font = pygame.font.Font(None, 30)
card = pygame.Surface((200, 50))
card.fill(grey)
looseCard = []
LooseCardPos = []
card_rect = card.get_rect(center=(part1.get_width() // 2, 50))
text = font.render("Forward", 1, black, None)
text_pos = text.get_rect(center=(card.get_width() // 2, card.get_height() // 2))
card.blit(text, text_pos)

cardR = pygame.Surface((200, 50))
cardR.fill(greyR)
cardR_rect = cardR.get_rect(center=(part1.get_width() // 2, 100))
textR = font.render("Right", 1, black, None)
textR_pos = textR.get_rect(center=(cardR.get_width() // 2, cardR.get_height() // 2))
cardR.blit(textR, textR_pos)

cardL = pygame.Surface((200, 50))
cardL.fill(greyL)
cardL_rect = cardL.get_rect(center=(part1.get_width() // 2, 150))
textL = font.render("Left", 1, black, None)
textL_pos = textR.get_rect(center=(cardL.get_width() // 2, cardL.get_height() // 2))
cardL.blit(textL, textL_pos)

cardB = pygame.Surface((200, 50))
cardB.fill(greyU)
cardB_rect = cardB.get_rect(center=(part1.get_width() // 2, 200))
textB = font.render("Back", 1, black, None)
textB_pos = textB.get_rect(center=(cardB.get_width() // 2, cardB.get_height() // 2))
cardB.blit(textB, textB_pos)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or \
                e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                if btn1.collidepoint(e.pos) and len(card_list) != 0 and not card_move:
                    i.reverse()
                    card_move = True
                    block = True
                if btn2.collidepoint(e.pos):
                    if not card_move and not block:
                        w.reverse()
                        if w[0]:
                            de = 150
                        else:
                            de = 650
                if btn3.collidepoint(e.pos):
                    if not card_move and not block:
                        q.reverse()
                        bot.rect.topleft = bot_pos
                        card_list.clear()
                        move_list.clear()
                        card_pos_list.clear()
                if btn4.collidepoint(e.pos):
                    if not card_move and not block:
                        r.reverse()
                        dimming_screen.reverse()
                        mode.reverse()
                        if N[0]:
                            N.reverse()
                if btn5.collidepoint(e.pos):
                    if not card_move and not block:
                        t.reverse()
                ##
                if crd1.collidepoint(e.pos):
                    card_list.append(card)
                    card_open = True
                elif crd2.collidepoint(e.pos):
                    card_list.append(cardR)
                    card_open = True
                elif crd3.collidepoint(e.pos):
                    card_list.append(cardL)
                    card_open = True
                elif crd4.collidepoint(e.pos):
                    card_list.append(cardB)
                    card_open = True
                else:
                    card_open = False
                if card_open:
                    move_list.append(False)
                    card_pos_list.append(
                        (card_pos[0] + 50, card_pos[1] + card.get_height() * (
                            len(card_list) - 1)))
                for k, crd in enumerate(card_list):
                    if (screen.blit(crd, card_pos_list[k])).collidepoint(e.pos):
                        move_list[k] = True

        for j, cpl in enumerate(card_pos_list):
            if e.type == pygame.MOUSEBUTTONUP:
                move_list[j] = False
            elif e.type == pygame.MOUSEMOTION and move_list[j]:
                card_pos_list[j] = (
                    e.pos[0] - card.get_width() // 2,
                    e.pos[1] - card.get_height() // 2)
            if cpl[0] < part1.get_width() - card.get_width() // 2:
                card_list.pop(j)
                move_list.pop(j)
                card_pos_list.pop(j)
    for index, obj_1 in enumerate(card_pos_list):
        for obj_2 in card_pos_list[index + 1:]:
            if abs(obj_1[1] - obj_2[1]) < 70 and abs(obj_1[0] - obj_2[0]) < 70:
                if obj_1[1] < obj_2[1]:
                    card_pos_list[card_pos_list.index(obj_2)] = obj_1[0], obj_1[1] + 50
                else:
                    if e.type == pygame.MOUSEBUTTONUP:
                        LooseCard = card_list[card_pos_list.index(obj_2)]
                        LooseCardPos = obj_2
                        LooseCardPos = obj_1[0], obj_1[1] - 50

                        card_list.remove(LooseCard)
                        card_pos_list.remove(obj_2)
                        card_pos_list.insert(0, LooseCardPos)
                        card_list.insert(0, LooseCard)

    screen.fill(BG_COLOR)
    for k, v in dict_draw.items():
        screen.blit(k, v) if k != BG_map else part2.blit(k, v)
    draw()
    btn1 = screen.blit(st_btn if i[0] else image_btn, image_btn_rect)
    btn3 = screen.blit(res1 if q[0] else res, res_rect)
    btn2 = screen.blit(speed1 if w[0] else speed, speed_rect)
    btn4 = screen.blit(inv_lamp if r[0] else lamp, lamp_rect)
    btn5 = screen.blit(inv_task if t[0] else task, task_rect)
    if mode[0]:
        screen.blit(podskazki[0] if N[0] else podskazki[1], pods1_1_rect)
    screen.blit(Kletky, Kletky_rect)
    '---------------------------------------------------------'
    if card_move and len(card_list) != 0:
        if bot.rect.centery < Kletky_rect.top or bot.rect.centery > Kletky_rect.bottom:
            bot.rect.right = Kletky_rect.left
        if bot.rect.right < Kletky_rect.left + 55 or bot.rect.left > Kletky_rect.right - 55:
            block2 = True
            bot.rect.y += 15
            if bot.rect.top > HEIGHT_WIN:
                block2 = False
                card_move = False
                card_score = 0
                if i[0]:
                    i.reverse()
                bot.rect.topleft = bot_pos
                bot.index = 0
                card_score -= 1
                block = False
        elif block:
            bot.rect.topleft = bot_pos
            bot.index = 0
            card_score -= 1
            block = False
        elif card_list[card_score] == card:
            bot.rect.y += 150
            bot.index += 1
        elif card_list[card_score] == cardR:
            bot.rect.x += 150
            bot.index += 1
        elif card_list[card_score] == cardL:
            bot.rect.x -= 150
            bot.index += 1
        elif card_list[card_score] == cardB:
            size_y -= 25
            size_x -= 25
            bot.rect.y -= 150
            bot.index += 1

        if not block2:
            bot.image = bot.images[int(bot.index % bot.range)]
            card_score += 1
            pygame.time.wait(de)
            if card_score >= len(card_list):
                card_move = False
                card_score = 0
                i.reverse()
    if bot.rect.right < Kletky_rect.left + 55 or bot.rect.left > Kletky_rect.right - 55 \
            or bot.rect.centery < Kletky_rect.top or bot.rect.centery > Kletky_rect.bottom:
        card_move = True

    # group.update()
    group.draw(screen)
    '---------------------------------------------------------'
    crd1 = part1.blit(card, card_rect)
    crd2 = part1.blit(cardR, cardR_rect)
    crd3 = part1.blit(cardL, cardL_rect)
    crd4 = part1.blit(cardB, cardB_rect)
    if len(card_list) > 0:
        for z, c in enumerate(card_list):
            screen.blit(c, card_pos_list[z])

    if dimming_screen[0] is True:
        screen.blit(part4, part4_rect)
    pygame.display.update()
    clock.tick(FPS)
    if q[0]:
        pygame.time.wait(250)
        q.reverse()
    if r[0]:
        pygame.time.wait(250)
        r.reverse()
    if t[0]:
        pygame.time.wait(250)
        t.reverse()
