import pygame
import time
from threading import Thread
pygame.init()

"""CREATE MASSIVE FOR BLOCKS (block = 1[block is allow for use] else if block = 0 [block not allowed for use]||||| block_col = block color! (r, b, g)||||| block_type = if 1  Block; if 2  Spike; if 3 size changer (for 3 type i create special massive [size_changer] if this massive = o massive not use size_changer[1]=change x else 2 change y 4 -text
block_col guide === block_col 1-3 = 1 block because bc[1]= (this, 0, 0) bc[2]= (0, this, 0) bc[3]= (0, 0, this). 6 = block 2 blue. for find block block(7) * 3 = 21 it red for 7 block !!! red green blue
block_size = 6 block x = 6*2-1 = 11\^-^/ and size_changer also work :D and block_coords x,y
i worked on 1 space for 1 block
b worked for 2 space for 1 block
and c worked 3 space for 1 block 
prymer: block coordinates(c) because x y z  and size changer on b change player on x and y block worked on i because on or off 1 space
"""

_r = pygame.image.load('game\\images\\_r.png')
totalb = 0
loops = True
speed = 1
b = 0
c = 0
size = 70
i = 0
block = []
block_col = []
block_type = []
size_changer = []
block_coords = []
block_move = []
block_size = []
text = []
for yo in range(size):
    block.append(0)
    block_type.append(1)
    text.append('')





    i += 1
for yo in range(size*3):
    block_col.append(0)
    block_move.append(0)
    block_coords.append(0)






    i += 1
for yo in range(size*2):
    block_size.append(10)

    size_changer.append(10)





    i += 1

block_color = 0
#print (block)

def all_loops():
    print('hi')

def testlevel_loop1():
    block_move[1] = 1
    time.sleep(1)
    block_move[1] = -1
    time.sleep(1)
    testlevel_loop1()

def test_loop2():
    time.sleep(0.01)
    text[5] = '_'
    test_loop2()


def test():

    #if loops:
        #tl_loop1 = Thread(target=test_loop2, args=())
        #tl_loop1.start()
    block[4] = 1
    block_col[12] = 0
    block_col[13] = 2
    block_col[14] = 255
    block_coords[12] = 356
    block_coords[13] = 654


    block[1] = 1
    block_col[3] = 255
    block_col[4] = 83
    block_col[5] = 73
    block_coords[3] = 356
    block_coords[4] = 674
    block_size[2] = 20
    block_size[3] = 20

    block[2] = 1
    block_col[6] = 100
    block_col[7] = 0
    block_col[8] = 0
    block_coords[6] = 734
    block_coords[7] = 500

    block_size[5] = 100

    block[3] = 1
    block_col[9] = 255
    block_col[10] = 0
    block_col[11] = 255
    block_coords[10] = 734
    block_coords[11] = 50

    block[0] = 1
    block_col[0] = 65
    block_col[1] = 5
    block_col[2] = 255
    block_coords[0] = 376
    block_coords[1] = 614
    block_coords[2] = 405

    block[5] = 1
    block_type[5] = 4

    block_coords[15] = 376
    block_coords[16] = 604


testlvl = Thread(target=test, args=())
level_list = ['test', ] # print your levelname here
print('Levels:')
for level_now in level_list:
    print(level_now)

level = str(input("\n\nType level name here\n--->"))
if level == 'test':
    testlvl.start()




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
b1sy = 100
"""BLOCK 1"""
"""MOVE TRUE OR FALSE"""
left = False
right = False
up = False
down = False
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

            if event.key == pygame.K_a:
                sleft = False
                left = True
                x1_change += -speed

                  # Указываем шаг изменения положения змейки
                # в 10 пикселей.aaaaaaaaaaaaaaaa0
                y1_change += 0
            elif event.key == pygame.K_d:
                sright = False
                right = True
                x1_change += speed
                y1_change += 0
            elif event.key == pygame.K_w:
                sup = False
                up = True
                y1_change += -speed
                x1_change += 0
            elif event.key == pygame.K_s:
                sdown = False
                down = True
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
                    up = False
                    y1_change -= -speed
                    x1_change -= 0
            elif event.key == pygame.K_s:
                if not sdown:
                    down = False

                    y1_change -= speed
                    x1_change -= 0


    #NO MOVE DETECTOR







# move stop with block
            if event.key == pygame.K_a and leftb:
                if sleft and not right:
                    left = False
                    x1_change = 0  # Указываем шаг изменения положения змейки
                elif sleft and right:
                    x1_change += 1
                    left = False

            elif event.key == pygame.K_d and rightb:
                if sright and not left:
                    x1_change = 0
                    right = False
                elif sright and left:
                    x1_change -= 1
                    right = False


            elif event.key == pygame.K_w and upb:
                if sup:
                    y1_change = 0

            elif event.key == pygame.K_s and downb:
                if sdown:
                    y1_change = 0


    """MOVE"""

    if not leftb and x1_change < 0:
        x1 += x1_change  #aw Записываем новое значение положения змейки по оси х.
    if not rightb and x1_change > 0:
        x1 += x1_change  #aw Записываем новое значение положения змейки по оси х.
    y1 += y1_change  # Записываем новое значение положения змейки по оси y.

    i = 0
    b = 0
    c = 0
    for yo in range(size):
        if block[i] == 1:
            block_coords[c] += block_move[c]
            block_coords[c+1] += block_move[c+1]
            block_coords[c+2] += block_move[c+2]
        c+=3
        b+=2
        i+=1
    """Block DETECTOR FOR MOVE"""
    """right block"""
    totalb = 0
    i = 0
    b = 0
    c = 0
    #print(block_coords[c] + (block_size[b]/2 + p1sx/2), x1)
    for yo in range(size):
        if block[i] == 1:

            if block_coords[c] + (block_size[b]/2 + p1sx/2) == x1 and block_coords[c+1] - (block_size[b+1]/2 + p1sy/2) <= y1 <= block_coords[c+1] + (block_size[b+1]/2 + p1sy/2):
                totalb =+ 1
                leftb = True
               # print ("ye")
                sleft = True
                left = False
            else:
                if totalb == 0:
                    t = 0
                    leftb = False

                    sleft = False

              # print ("not")
        i += 1
        b += 2
        c += 3

    totalb = 0
    i = 0
    b = 0
    c = 0
  # rightb = Truet(block_coords[c] + (block_size[b]/2 + p1sx/2), x1)
    for yo in range(size):
        if block[i] == 1:

            if block_coords[c] - (block_size[b]/2 + p1sx/2) == x1 and block_coords[c+1] - (block_size[b+1]/2 + p1sy/2) <= y1 <= block_coords[c+1] + (block_size[b+1]/2 + p1sy/2):
                 totalb =+ 1
                 rightb = True
                 # print ("ye")
                 sright = True
                 right = False
            else:
                 if totalb == 0:
                    t = 0
                    rightb = False
                    sright = False

                # print ("not")
        i += 1
        b += 2
        c += 3
    """BLOCK MOVE"""
    i=0
    """
    for yo in range(size):
        if block[i] == 1:
            block_coords[i] =+ block_move[i]
        i+1
    """


        #if b1x - 10 == x1 and b1y + 10 < y1 > b1y - 10:
            #rightb = True
            #x1_change = 0
        #else:
            #righttb = False
    #print(leftb, sleft, left, rightb, right, x1_change,y1_change , b1y, y1,b1y, x1, b1x, b1x+10)



    dis.fill(white)
    """SCREEN OBJECTS"""

    pygame.draw.rect(dis, red, [x1 - p1sx/2, y1 - p1sy/2, p1sx, p1sy])
    i = 0
    c=0
    b =0

    for yo in range(size):
        print('ok')
        if block_type[i] == 1:
            print('ok0')
            if block[i] == 1:
                print('ok9')
                #block_color=(block_col[c], block_col[c+1], block_col[c+2])
                pygame.draw.rect(dis, block_color, [block_coords[c] - block_size[b]/2, block_coords[c+1] - block_size[b+1]/2, block_size[b], block_size[b+1]])

        if block_type[i] == 4:

            print('okk')
            if block[i] == 1:
                print('woow')
                if text[i] == '_':
                    #if texxt == '_':
                    print('lol')
                    dis.blit(_r, (block_coords[c], block_coords[c+1]))

        i += 1
        b += 2
        c += 3

    pygame.draw.rect(dis, red, [0, 14, 10, 10])
    pygame.display.update()
    clock.tick(120)
pygame.quit()
quit()
