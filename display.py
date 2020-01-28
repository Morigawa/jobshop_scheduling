import random
import pygame
from functions import find_max_duration


# used to visualize a single schedule

def show(schedule, am_jobs):

    # window initialization
    pygame.init()
    dis_x = 1800
    game_display = pygame.display.set_mode((dis_x, 900))    # change if problem with window size
    game_display.fill((0, 0, 0))

    scaling = (dis_x*0.99)/find_max_duration(schedule)  # scaling factor, so each schedule will fit
    height = int(600 / len(schedule))   # total height the same every time, single height depends on amount of machines
    start_x = 10
    y = 150

    # random color list, to assign each job a different color
    colors = [(random.randint(0, 240), random.randint(0, 240), random.randint(0, 240)) for i in range(50)]

    # calculate size and position of each task and create corresponding rectangle
    for machine in schedule:
        x = start_x + (machine[0][1] * scaling)
        for task in machine:
            if machine.index(task) + 1 < len(machine):
                next = machine[machine.index(task) + 1]
                width = next[1] - task[1]
            pygame.draw.rect(game_display, colors[task[0][0]], (x, y, int(task[0][3] * scaling), height))
            x += width * scaling
        y += height

    # window loop
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()