import copy
import math
import random

import job_scheduling.neighborhood as neighborhood


def temperature(i):
    amplitude = 100
    center = 0
    width = 100
    return amplitude * (1 / (1 + math.exp((i - center) / width)))


def simulated_annealing(test):
    schedule = neighborhood.construct_first_solution(test)
    print("first solution: " + str(neighborhood.calculate_duration(schedule)))
    i = 0
    iter = 1000

    best_s = copy.copy(schedule)
    best_d = neighborhood.calculate_duration(schedule)

    while i < iter:
        options = neighborhood.create_neighborhood(schedule)
        if not options:
            break
        alter = random.choice(options)
        d_schedule = neighborhood.calculate_duration(schedule)
        d_alter = neighborhood.calculate_duration(alter)
  #      print(math.exp((d_schedule - 1 - d_alter)/temperature(i)))
        if d_schedule >= d_alter or random.uniform(0, 1) < math.exp(-(d_alter - 1 - d_schedule)/temperature(i)):
            schedule = alter
        if d_alter < best_d:
            best_d = d_alter
            best_s = copy.copy(alter)
        i += 1
    print("best solution: " + str(best_d))
    return best_s
