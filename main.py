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
    width = 35000
    return float(amplitude * (1 / (1 + math.exp((i - center) / width))))


def main():
    tests = inp.construct_tests_js1()
    tests = tests.__add__(inp.construct_test_j2())

    print(len(tests))   #TODO delete
    string = ""
    id = 0

    for jobs_data in tests:
        print(id)
        first_solution = 0
        jobs_data = [list(filter(None, i)) for i in zip_longest(*jobs_data)]
        min_duration = int
        for x in range(1):
            # order and flat list
            jobs = []
            for sublist in jobs_data:
                for item in sublist:
                    jobs.append(item)
            # find how many machines are there
            machines_count = max(jobs, key=itemgetter(2))[2] + 1
            results = f.schedule(jobs, machines_count)
            min_duration = f.find_max_duration(results)
            first_solution = min_duration
            best_jobs = results

            #print("first solution: " + str(first_solution))

            iter = 320000
            for i in range(0, iter):

                old = list(results)
                alter = f.shuffle_jobs(jobs, jobs_data)
                results = f.schedule(alter, machines_count)
                d_old = f.find_max_duration(old)
                d_alter = f.find_max_duration(results)

                if d_old >= d_alter:
                    jobs = alter
                elif random.uniform(0, 1) < math.exp(-(d_alter - d_old) / temperature(i)):
                    jobs = alter

                if d_alter < min_duration:
                    min_duration = d_alter
                    best_jobs = list(results)

            print("minimum duration: " + str(min_duration))

            #f.print_result(best_jobs)
            #display.show(best_jobs, len(jobs_data))

        string = string + str(id) + ", " + str(first_solution) + ", " + str(min_duration) + "\n"
        id+=1

    with open('result.txt', 'w') as res:
        res.write(string)


if __name__ == "__main__":
    main()
