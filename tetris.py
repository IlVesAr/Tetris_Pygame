import pygame
import Pygame_Plus as pg_plus
import random

pygame.init()


width, height = 700, 600

block = (height - height / 6) / 20 
areaw, areah = block * 10, block * 20
areax, areay = (width - areaw) / 2, (height - areah) / 2
startx, starty = areax + 4 * block, areay - 2 * block

w = 1
            #LINE
blocks = [[pg_plus.Kvadrat(startx, starty, block, block, w, block, pg_plus.color.cyan),
           pg_plus.Kvadrat(startx - block, starty, block, block, w, block, pg_plus.color.cyan),
           pg_plus.Kvadrat(startx + block, starty, block, block, w, block, pg_plus.color.cyan),
           pg_plus.Kvadrat(startx + block * 2, starty, block, block, w, block, pg_plus.color.cyan)],

            #J
          [pg_plus.Kvadrat(startx, starty, block, block, w, block, pg_plus.color.blue),
           pg_plus.Kvadrat(startx - block, starty, block, block, w, block, pg_plus.color.blue),
           pg_plus.Kvadrat(startx + block, starty, block, block, w, block, pg_plus.color.blue),
           pg_plus.Kvadrat(startx + block, starty + block, block, block, w, block, pg_plus.color.blue)],

            #L
          [pg_plus.Kvadrat(startx, starty, block, block, w, block, pg_plus.color.orange),
           pg_plus.Kvadrat(startx - block, starty, block, block, w, block, pg_plus.color.orange),
           pg_plus.Kvadrat(startx + block, starty, block, block, w, block, pg_plus.color.orange),
           pg_plus.Kvadrat(startx - block, starty + block, block, block, w, block, pg_plus.color.orange)],
          
            #CUBE
          [pg_plus.Kvadrat(startx, starty, block, block, w, block, pg_plus.color.yellow),
           pg_plus.Kvadrat(startx + block, starty, block, block, w, block, pg_plus.color.yellow),
           pg_plus.Kvadrat(startx, starty + block, block, block, w, block, pg_plus.color.yellow),
           pg_plus.Kvadrat(startx + block, starty + block, block, block, w, block, pg_plus.color.yellow)],

            
          [pg_plus.Kvadrat(startx, starty + block, block, block, w, block, pg_plus.color.green),
           pg_plus.Kvadrat(startx, starty, block, block, w, block, pg_plus.color.green),
           pg_plus.Kvadrat(startx + block, starty + block, block, block, w, block, pg_plus.color.green),
           pg_plus.Kvadrat(startx + block, starty + block * 2, block, block, w, block, pg_plus.color.green)],

          [pg_plus.Kvadrat(startx, starty + block, block, block, w, block, pg_plus.color.red),
           pg_plus.Kvadrat(startx, starty + block * 2, block, block, w, block, pg_plus.color.red),
           pg_plus.Kvadrat(startx + block, starty, block, block, w, block, pg_plus.color.red),
           pg_plus.Kvadrat(startx + block, starty + block, block, block, w, block, pg_plus.color.red)],

          [pg_plus.Kvadrat(startx + block, starty, block, block, w, block, pg_plus.color.purple),
           pg_plus.Kvadrat(startx - block, starty, block, block, w, block, pg_plus.color.purple),
           pg_plus.Kvadrat(startx, starty, block, block, w, block, pg_plus.color.purple),
           pg_plus.Kvadrat(startx, starty + block, block, block, w, block, pg_plus.color.purple)]

            
          ]

win = pygame.display.set_mode((width, height))

peace = random.choice(blocks)
area = pg_plus.Kvadrat((width - areaw) / 2, (height - areah) / 2, block * 10, block * 20, 2, 0, pg_plus.color.red)

def Clear(cubes):
    global block
    topop = []
    lines = []
    for i in range(1, 21):
        lines.append(area.y + i * block)
    to_clear = []
    for line in lines:
        i = 0
        for cube in cubes:
            if cube.y == line:
                i += 1

        if i >= 10:
            to_clear.append(line)

    for clear in to_clear:
        for cube in cubes:
            if cube.y == clear:
                topop.append(cube)
                
    for popp in topop:
        cubes.remove(popp)
            
    for clear in to_clear:
        for cube in cubes:   
            if cube.y < clear:
                cube.y += block
        

def Bullshhit(block):
    min_x = 2000000
    max_x = -2000000
    for p in peace:
        if p.x < min_x:
            min_x = p.x
        if p.x > max_x:
            max_x = p.x
            
    if min_x < area.x:
        for ii in peace:
            ii.x += ii.vel
            min_x += block
    if min_x < area.x:
        for ii in peace:
            ii.x += ii.vel
            min_x += block
    if min_x < area.x:
        for ii in peace:
            ii.x += ii.vel
            min_x += block
    if min_x < area.x:
        for ii in peace:
            ii.x += ii.vel
            min_x += block

    if max_x + block > area.x + area.w:
        for ii in peace:
            ii.x -= ii.vel
            max_x -= block
    if max_x + block > area.x + area.w:
        for ii in peace:
            ii.x -= ii.vel
            max_x -= block
    if max_x + block > area.x + area.w:
        for ii in peace:
            ii.x -= ii.vel
            max_x -= block
    if max_x + block > area.x + area.w:
        for ii in peace:
            ii.x -= ii.vel
            max_x -= block
    

def DrAw(win, peace, area):
    win.fill(pg_plus.color.black)
    area.draw(win)
    for bl in peace:
        bl.draw(win)
    for b in cubes:
        b.draw(win)
    pygame.display.flip()

def Drop(dropping, peace, level, key):
    if key[pygame.K_DOWN]:
        level = level // 3
    if dropping % level == 0:
        for p in peace:
            p.y += p.vel
        return True

def Move(key, peace, area):
    global block
    canright = True
    canleft = True
    for j in cubes:
        for i in peace:
            if i.x == j.x - block and i.y == j.y:
                canright = False
            if i.x == j.x + block and i.y == j.y:
                canleft = False
    for pp in peace:
        if pp.x <= area.x and key[pygame.K_LEFT]:
            return True
        if pp.x + pp.w >= area.x + area.w and key[pygame.K_RIGHT]:
            return True
    
    if key[pygame.K_LEFT] and canleft:
        for p in peace:
            p.x -= p.vel
        return False
    if key[pygame.K_RIGHT] and canright:
        for p in peace:
            p.x += p.vel
        return False
        
    return True


def Rotate(peace):
    max_x = max_y = -2000000
    min_x = min_y = 2000000
    for p in peace:
        if p.x > max_x:
            max_x = p.x
        if p.x < min_x:
            min_x = p.x
        if p.y > max_y:
            max_y = p.y
        if p.y < min_y:
            min_y = p.y

    if max_x - min_x > max_y - min_y:
        n = max_x - min_x
    else:
        n = max_y - max_y

    for j in peace:
        j.x -= min_x
        j.y -= min_y
        j.x, j.y = n - j.y, j.x
        j.x += min_x
        j.y += min_y

    minn_x = 2000000
    for p in peace:
        if p.x < minn_x:
            minn_x = p.x

    if minn_x < min_x:
        for ii in peace:
            ii.x += ii.vel

cubes = []    
    


clock = pygame.time.Clock()

ground = False
lock = 0
tolock = 30
speed = 60
dropping = 0
level = 15
canmove = True
canrotate = True
down = False
run = True
while run:
    clock.tick(speed)
    dropping += 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    
    key = pygame.key.get_pressed()
    
    if canmove:
        canmove = Move(key, peace, area)

    if key[pygame.K_LEFT] or key[pygame.K_RIGHT]:
        canmove = False
    else:
        canmove = True

    
    if key[pygame.K_c] and canrotate:
        Rotate(peace)
        canrotate = False

    if not key[pygame.K_c]:
        canrotate = True

    Bullshhit(block)

    
        
    for j in cubes:
        for i in peace:
            if i.x == j.x and i.y == j.y - block:
                down = True
                break
        if down:
            break

    if down:
        down = False
        for j in cubes:
            for i in peace:
                if i.x == j.x and i.y == j.y - block:
                    down = True
                    break
            if down:
                break

        
    for jj in peace:
        if jj.y >= area.y + area.h - block:

            down = True
            break
        

    
    if down:
        lock += 1;
    if down and lock == tolock:
        for jjj in peace:
            cubes.append(jjj)
            
        r = random.randrange(7000000)
        if r % 7 == 0:
            peace = [pg_plus.Kvadrat(startx, starty, block, block, w, block, pg_plus.color.cyan),
                pg_plus.Kvadrat(startx - block, starty, block, block, w, block, pg_plus.color.cyan),
                pg_plus.Kvadrat(startx + block, starty, block, block, w, block, pg_plus.color.cyan),
                pg_plus.Kvadrat(startx + block * 2, starty, block, block, w, block, pg_plus.color.cyan)]
        elif r % 7 == 1:
            peace = [pg_plus.Kvadrat(startx, starty, block, block, w, block, pg_plus.color.blue),
                pg_plus.Kvadrat(startx - block, starty, block, block, w, block, pg_plus.color.blue),
                pg_plus.Kvadrat(startx + block, starty, block, block, w, block, pg_plus.color.blue),
                pg_plus.Kvadrat(startx + block, starty + block, block, block, w, block, pg_plus.color.blue)]
        elif r % 7 == 2:
            peace = [pg_plus.Kvadrat(startx, starty, block, block, w, block, pg_plus.color.orange),
                pg_plus.Kvadrat(startx - block, starty, block, block, w, block, pg_plus.color.orange),
                pg_plus.Kvadrat(startx + block, starty, block, block, w, block, pg_plus.color.orange),
                pg_plus.Kvadrat(startx - block, starty + block, block, block, w, block, pg_plus.color.orange)]
        elif r % 7 == 3:
            peace = [pg_plus.Kvadrat(startx, starty, block, block, w, block, pg_plus.color.yellow),
           pg_plus.Kvadrat(startx + block, starty, block, block, w, block, pg_plus.color.yellow),
           pg_plus.Kvadrat(startx, starty + block, block, block, w, block, pg_plus.color.yellow),
           pg_plus.Kvadrat(startx + block, starty + block, block, block, w, block, pg_plus.color.yellow)]
        elif r % 7 == 4:
            peace = [pg_plus.Kvadrat(startx, starty + block, block, block, w, block, pg_plus.color.green),
           pg_plus.Kvadrat(startx, starty, block, block, w, block, pg_plus.color.green),
           pg_plus.Kvadrat(startx + block, starty + block, block, block, w, block, pg_plus.color.green),
           pg_plus.Kvadrat(startx + block, starty + block * 2, block, block, w, block, pg_plus.color.green)]
        elif r % 7 == 5:
            peace = [pg_plus.Kvadrat(startx, starty + block, block, block, w, block, pg_plus.color.red),
           pg_plus.Kvadrat(startx, starty + block * 2, block, block, w, block, pg_plus.color.red),
           pg_plus.Kvadrat(startx + block, starty, block, block, w, block, pg_plus.color.red),
           pg_plus.Kvadrat(startx + block, starty + block, block, block, w, block, pg_plus.color.red)]
        elif r % 7 == 6:
            peace = [pg_plus.Kvadrat(startx + block, starty, block, block, w, block, pg_plus.color.purple),
           pg_plus.Kvadrat(startx - block, starty, block, block, w, block, pg_plus.color.purple),
           pg_plus.Kvadrat(startx, starty, block, block, w, block, pg_plus.color.purple),
           pg_plus.Kvadrat(startx, starty + block, block, block, w, block, pg_plus.color.purple)]
        down = False
        lock = 0
            
    if not down:
        
        Drop(dropping, peace, level, key)

    Clear(cubes)
    
    DrAw(win, peace, area)
    
pygame.quit()
