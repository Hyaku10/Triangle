import random
import pygame
import time
from sys import exit
# =====COLORS==============================================================================
BLACK = (100, 100, 100)
WHITE = (255, 255, 255)
AQUAMARINE = (127, 255, 212)
ORANGE = (255, 140, 0)
GREEN = (0, 255, 0)
# =====PARAMETERS==============================================================================
(width, height) = (600, 600)
WIN = pygame.display.set_mode((width, height))
SIZE = 4
grow = True
pause = False
pause_time = 0.2
LIMIT = 999999
counter = 0
NOC = 4 #number of colors
# =====CONTAINERS==============================================================================
RECTS = []
Triangle = [
    [1]
]
previous = [1] # first row for generating Triangle row by row
# =====CLASSES==============================================================================
class block:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def draw(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, SIZE, SIZE))
class super_block:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
    def draw(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.w, self.h))
# =====GENERATE=FUNCTIONS==============================================================================
def generate_new_row_by_tri(tri):
    new_arr = []
    # new_arr.append(random.choice([1,0,0,0,0,0,0,0]))
    pre = 0
    for i in tri[-1]:

        if i == pre:
            new_arr.append(1)
        else:
            new_arr.append(0)
        pre = i
    if pre == 0:
        new_arr.append(1)
    else:
        new_arr.append(random.choice([1,0,0,0,0,0,0,0,0,0,0,0]))
    tri.append(new_arr)
    return tri
def generate_new_row_by_pre(pre):
    new_row = []
    for i in pre:
        if i == pre.index(i-1):
            new_row.append(1)
        else:
            new_row.append(0)
    if previous_num == 0:
        new_row.append(1)
    else:
        new_row.append(0)
    new_row = previous
    return new_row
def generate_new_row_by_RPS_random_last_item(tri):
    new_arr = []
    new_arr.append(random.choice([1-3]))
    pre = 1
    for i in tri[-1]:
            if i == pre:
                if not i%2:
                    new_arr.append(i/2)
                else:
                    new_arr.append(random.choice([1,2,3]))
                    # new_arr.append()
            elif i == 1 and pre == 3:
                new_arr.append(1)
            elif i == 3 and pre == 1:
                new_arr.append(1)
            elif i > pre:
                new_arr.append(i)
            else:
                new_arr.append(pre)
            pre = i
    # add last item
    # new_arr.append(random.choice([1,2,3]))
    tri.append(new_arr)
    return tri
def generate_new_row_by_tri_add(tri):
    new_arr = []
    # new_arr.append(1)
    pre = random.choice([0,1,1,1,1,-1,-1,-1,-1,1])
    for i in tri[-1]:
        new_arr.append(i + pre)
    new_arr.append(1)
    tri.append(new_arr)
    return tri
# =====PRINT=FUNCTIONS==============================================================================
def print_new_row_by_tri(tri):
    for i_tri, v_tri in enumerate(tri):
        for i_row, v_row in enumerate(v_tri):
        # for i, v in enumerate(new_row(Triangle)):
            if v_row == 0:
                # RECTS.append(block(i_row*SIZE+(width-len(v_tri)*SIZE)/2, i_tri*SIZE, AQUAMARINE))
                A = block(i_row*SIZE+(width-len(v_tri)*SIZE)/2, i_tri*SIZE, AQUAMARINE)
                A.draw()
        # else:
            #     RECTS.append(block(i_row*SIZE+(width-len(v_tri)*SIZE)/2, i_tri*SIZE, BLACK))
        # for i in RECTS:
        #     i.draw()
def print_new_row_by_tri_relative(tri):
    for i_tri, v_tri in enumerate(tri):
        for i_row, v_row in enumerate(v_tri):
            if v_row == 0:
                new_block = block((width/len(v_tri))*i_row, i_tri * SIZE, AQUAMARINE)
                new_block.draw()
def print_new_row_by_tri_relative_super(tri):
    for i_tri, v_tri in enumerate(tri):
        for i_row, v_row in enumerate(v_tri):
            if v_row == 0:
                new_block = super_block((width/len(v_tri))*i_row,(height/len(tri))*i_tri, width/len(v_tri), height/len(tri), AQUAMARINE)
                new_block.draw()
            # else:
                # new_block = super_block((width/len(v_tri))*i_row,(height/len(tri))*i_tri, width/len(v_tri), height/len(tri), WHITE)
                # new_block.draw()
def print_new_row_by_tri_relative_super_vertical(tri):
    for i_tri, v_tri in enumerate(tri):
        for i_row, v_row in enumerate(v_tri):
            if v_row == 0:
                new_block = super_block((width/len(tri))*i_row, (height/len(v_tri))*i_row, height/len(tri), width/len(v_tri), AQUAMARINE)
                new_block.draw()
            # else:
            #     new_block = super_block((width/len(v_tri))*i_row,(height/len(tri))*i_tri, width/len(v_tri), height/len(tri), BLACK)
            #     new_block.draw()
def print_new_row_by_pre(row, counter):
    for i in row:
        if i == 0:
            A = block(i * SIZE + (width - len(row) * SIZE) / 2, counter * SIZE, AQUAMARINE)
            A.draw()
            counter += 1
            return counter
def print_new_row_by_tri_3_colors(tri):
    for i_tri, v_tri in enumerate(tri):
        for i_row, v_row in enumerate(v_tri):
            if v_row == 1:
                A = block(i_row*SIZE+(width-len(v_tri)*SIZE)/2, i_tri*SIZE, AQUAMARINE)
                A.draw()
            if v_row == 2:
                A = block(i_row * SIZE + (width - len(v_tri) * SIZE) / 2, i_tri * SIZE, ORANGE)
                A.draw()
            if v_row == 3:
                A = block(i_row * SIZE + (width - len(v_tri) * SIZE) / 2, i_tri * SIZE, GREEN)
                A.draw()
def print_new_row_by_tri_relative_3_colors(tri):
    for i_tri, v_tri in enumerate(tri):
        for i_row, v_row in enumerate(v_tri):
            if v_row == 1:
                new_block = block((width/len(v_tri))*i_row, i_tri * SIZE, AQUAMARINE)
                new_block.draw()
            if v_row == 2:
                new_block = block((width/len(v_tri))*i_row, i_tri * SIZE, ORANGE)
                new_block.draw()
            if v_row == 3:
                new_block = block((width/len(v_tri))*i_row, i_tri * SIZE, GREEN)
                new_block.draw()
            if v_row == 4:
                new_block = block((width/len(v_tri))*i_row, i_tri * SIZE, WHITE)
                new_block.draw()
def print_new_row_by_tri_by_odd_or_even(tri):
    for i_tri, v_tri in enumerate(tri):
        for i_row, v_row in enumerate(v_tri):
            if v_row > 100:
                A = block(i_row * SIZE + (width - len(v_tri) * SIZE) / 2, i_tri * SIZE, GREEN)
                A.draw()
            elif v_row % 2:
                A = block(i_row*SIZE+(width-len(v_tri)*SIZE)/2, i_tri*SIZE, AQUAMARINE)
                A.draw()
            elif not v_row % 2:
                A = block(i_row * SIZE + (width - len(v_tri) * SIZE) / 2, i_tri * SIZE, ORANGE)
                A.draw()
# =====EFFECT=FUNCTIONS==============================================================================
def hyper(tri):
    for i in tri:
        i.append(tri[len(tri)-1-tri.index(i)])
    return tri
def half(tri):
    for i, row in enumerate(tri):
        n = []
        for ij, j in enumerate(row):
            if ij < len(row)/2:
                n.append(j)
        tri[i] = n
    return tri
def upside_down(tri):
    for row in tri:
        row = tri[tri.index(row)-1-row]
    return tri
def scroll(tri):
    if len(tri)*SIZE>height:
        tri.remove(tri[0])
        # RECTS.remove(RECTS[0])
# =====LOOP==============================================================================
for RUN in range(LIMIT):
    WIN.fill(BLACK)
    generate_new_row_by_tri_add(Triangle)
    print_new_row_by_tri_by_odd_or_even(Triangle)
    # if grow == True:
    #     SIZE += 1
    #     if SIZE > 10:
    #         grow = False
    # if grow == False:
    #     SIZE = 1
    #     if SIZE < 2:
    #         grow = True
    if pause == True:
        time.sleep(pause_time)
    # controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
    pygame.display.update()

