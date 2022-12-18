import pygame
import time
speed = 2.5
"""BLOCK DETECTOR"""
upb = False
downb = False
rightb = False
leftb = False
"""BLOCK DETECTOR"""
"""FOR STOP MOVE"""
sup = False
sdown = False
sright = False
sleft = False
"""FOR STOP MOVE"""
"""BLOCK 1"""
b1 = 1
b1x = 490
b1y = 700
b1sx = 10
b1sy = 10
"""BLOCK 1"""
"""MOVE TRUE OR FALSE"""
left = False
right = False
"""MOVE TRUE OR FALSE"""
"""FIRTS COLLISION DETECTOR"""
t = 0
moveb = False
"""FIRTS COLLISION DETECTOR"""
p1sx = 10
p1sy = 10

pygame.init()

white = (100, 100, 100)
black = (0, 0, 0)
red = (255, 0, 0)

dis = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Game')

game_over = False
x1 = 500  # Указываем начальное значение положения змейки по оси х.
y1 = 500  # Указываем начальное значение положения змейки по оси y.
x1_change = 0  # Создаём переменную, которой в цикле while будут
# присваиваться значения изменения положения змейки по оси х.
y1_change = 0  # создаём переменную, которой в цикле while будут
# присваиваться значения изменения положения змейки по оси y.
clock = pygame.time.Clock()

while not game_over:
    # if not right and not left and not leftb and not rightb and not sleft and not sright:
        # x1_change = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:  # Добавляем считывание направления

            if event.key == pygame.K_a and not left:
                sleft = False
                left = True
                x1_change += -speed  # Указываем шаг изменения положения змейки
                # в 10 пикселей.aaaaaaaaaaaaaaaa0
                y1_change += 0
            elif event.key == pygame.K_d:
                sright = False
                right = True
                x1_change += speed
                y1_change += 0
            elif event.key == pygame.K_w:
                y1_change += -speed
                x1_change += 0
            elif event.key == pygame.K_s:
                y1_change += speed
                x1_change += 0
            elif event.key == pygame.K_k:
                x1_change += 0
                y1_change += 0

# MOVE STOP
        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_a and not leftb:
                if not sleft:
                    left = False
                    x1_change -= -speed  # Указываем шаг изменения положения змейки
                    y1_change -= 0
            elif event.key == pygame.K_d:
                if not sright:
                    right = False
                    x1_change -= speed
                    y1_change -= 0
            elif event.key == pygame.K_w:
                if not sup:
                    y1_change -= -speed
                    x1_change -= 0
            elif event.key == pygame.K_s:
                if not sdown:
                    y1_change -= speed
                    x1_change -= 0


    #NO MOVE DETECTOR







# move stop with block
            if event.key == pygame.K_a and leftb:
                if sleft:
                    left = False
                    x1_change = 0  # Указываем шаг изменения положения змейки
                    y1_change = 0
        """
            elif event.key == pygame.K_d:
                if not sright:
                    x1_change -= 10
                    y1_change -= 0
            elif event.key == pygame.K_w:
                if not sup:
                    y1_change -= -10
                    x1_change -= 0
            elif event.key == pygame.K_s:
                if not sdown:
                    y1_change -= 10
                    x1_change -= 0
"""
    """MOVE"""

    if left and not leftb:
        x1 += x1_change  #aw Записываем новое значение положения змейки по оси х.
    if right and not rightb:
        x1 += x1_change  #aw Записываем новое значение положения змейки по оси х.
    y1 += y1_change  # Записываем новое значение положения змейки по оси y.

    """Block DETECTOR FOR MOVE"""
    if b1 == 1:
        if b1x + 10 == x1 and b1y - 10 <= y1 <= b1y + 10:
            leftb = True

            sleft = True
            left = False
        else:
            t = 0
            leftb = False

            sleft = False

        #if b1x - 10 == x1 and b1y + 10 < y1 > b1y - 10:
            #rightb = True
            #x1_change = 0
        #else:
            #righttb = False
    print(leftb, sleft, left, rightb, x1_change, b1y, y1,b1y, x1, b1x, b1x+10)



    dis.fill(white)
    """SCREEN OBJECTS"""
    pygame.draw.rect(dis, red, [x1 - p1sx/2, y1 - p1sy/2, p1sx, p1sy])
    pygame.draw.rect(dis, red, [b1x - b1sx/2, b1y - b1sy/2, b1sx, b1sy])
    pygame.draw.rect(dis, red, [0, 14, 10, 10])
    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()
