import math
from itertools import zip_longest
from operator import itemgetter
import random
import input as inp
import functions as f
import display as display

# change Settings
visualisation = True  # maybe turn of if do_algo > 1
iterations = 320000  # amount of iterations, while one iteration of the algorithm
do_algo = 1  # iterations of applying the algorithm
benchmark_id = 0  # choose number between 0 and 81, check tests.txt


# temperature function - s-curve
def temperature(i):
    amplitude = 1000
    center = 0
    width = 0.11 * iterations
    return float(amplitude * (1 / (1 + math.exp((i - center) / width))))


def main():
    tests = inp.construct_tests_js1()       # get benchmarks in jobshop1.txt
    jobs_data = tests[benchmark_id]         # choose the benchmark you want to run

    jobs_data = [list(filter(None, i)) for i in zip_longest(*jobs_data)]

    first_solution = 0
    best_duration = int
    best_jobs = []

    for x in range(do_algo):

        # order and flatten list
        jobs = []
        for sublist in jobs_data:
            for item in sublist:
                jobs.append(item)

        machines_count = max(jobs, key=itemgetter(2))[2] + 1  # find how many machines are there
        results = f.schedule(jobs, machines_count)      # generate first solution
        min_duration = f.find_max_duration(results)     # calculate duration of first solution
        first_solution = min_duration

        best_duration = min_duration + 1
        current_best = results       # set first solution as best_solution

        for i in range(iterations):
            old = list(results)     # previous schedule
            alter = f.shuffle_jobs(jobs)      # new job list
            results = f.schedule(alter, machines_count)  # calculate schedule of new solution

            # calculate duration of old and new schedule
            d_old = f.find_max_duration(old)
            d_alter = f.find_max_duration(results)

            if d_old >= d_alter:
                jobs = alter
            elif random.uniform(0, 1) < math.exp(-(d_alter - d_old) / temperature(i)):
                jobs = alter

            if d_alter < min_duration:
                min_duration = d_alter
                current_best = list(results)

        if best_duration > min_duration:
            best_duration = min_duration
            best_jobs = current_best

    print("first solution: " + str(first_solution))
    print("minimum duration: " + str(best_duration))

    f.print_result(best_jobs)
    if visualisation:
        display.show(best_jobs, len(jobs_data))


if __name__ == "__main__":
    main()
