import random

import pygame
from job_scheduling.neighborhood import calculate_duration


def show(schedule):

    pygame.init()
    dis_x = 1800
    gameDisplay = pygame.display.set_mode((dis_x, 900))
    gameDisplay.fill((0, 0, 0))

    scaling = (dis_x*0.99)/calculate_duration(schedule)
    height = int(600 / len(schedule))
    start_x = 10
    y = 150
    colors = [(255, 255, 255), (0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 100, 10), (255, 255, 0), (0, 255, 170),
            (115, 0, 0), (180, 255, 100), (255, 100, 180), (240, 0, 255), (127, 127, 127), (255, 0, 230),
            (100, 40, 0), (0, 50, 0), (0, 0, 100), (210, 150, 75), (255, 255, 100), (255, 200, 0), (200, 200, 200)]

    #colors = [(random.randint(0, 240), random.randint(0, 240), random.randint(0, 240)) for i in range(50)]

    for machine in schedule:
        x = start_x + (machine[0].starting_time * scaling)
        for task in machine:
            if machine.index(task) + 1 < len(machine):
                next = machine[machine.index(task) + 1]
                width = next.starting_time - task.starting_time
            pygame.draw.rect(gameDisplay, colors[task.task_id[0]], (x, y, int(task.duration * scaling), height))
            x += width * scaling
        y += height

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
