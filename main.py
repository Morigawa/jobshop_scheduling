import math
from itertools import zip_longest
from operator import itemgetter
import random
import job_scheduling.input as inp
import job_scheduling.functions as f
import job_scheduling.display as display


def temperature(i):
    amplitude = 1000
    center = 0
    width = 10000
    return amplitude * (1 / (1 + math.exp((i - center) / width)))


def main():
    tests = inp.construct_tests_js1()
    tests = tests.__add__(inp.construct_test_j2())

    jobs_data = tests[0]

    # order and flat list
    jobs_data = [list(filter(None, i)) for i in zip_longest(*jobs_data)]
    jobs = []
    for sublist in jobs_data:
        for item in sublist:
            jobs.append(item)

    # find how many machines are there
    machines_count = max(jobs, key=itemgetter(2))[2] + 1
    results = f.schedule(jobs, machines_count)

    min_duration = 999999
    best_jobs = []

    iter = 100000
    for i in range(0, iter):

        old = list(results)
        alter = f.shuffle_jobs(jobs, jobs_data)
        results = f.schedule(alter, machines_count)

        d_old = f.find_max_duration(old)
        d_alter = f.find_max_duration(results)

        if d_old >= d_alter or random.uniform(0, 1) < math.exp(-(d_alter - 1 - d_old) / temperature(i)):
            jobs = alter
        if d_alter < min_duration:
            min_duration = d_alter
            best_jobs = list(results)

    f.print_result(best_jobs)
    print("mininum duration: " + str(min_duration))
    display.show(best_jobs)



if __name__ == "__main__":
    main()