import random
import pygame
from job_scheduling.functions import find_max_duration


def show(schedule, am_jobs):

    pygame.init()
    dis_x = 1800
    game_display = pygame.display.set_mode((dis_x, 900))
    game_display.fill((0, 0, 0))

    scaling = (dis_x*0.99)/find_max_duration(schedule)
    height = int(600 / len(schedule))
    start_x = 10
    y = 150
    colors = [(random.randint(0, 240), random.randint(0, 240), random.randint(0, 240)) for i in range(50)]

    for machine in schedule:
        x = start_x + (machine[0][1] * scaling)
        for task in machine:
            if machine.index(task) + 1 < len(machine):
                next = machine[machine.index(task) + 1]
                width = next[1] - task[1]
            pygame.draw.rect(game_display, colors[task[0][0]], (x, y, int(task[0][3] * scaling), height))
            x += width * scaling
        y += height

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()