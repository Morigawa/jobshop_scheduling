from operator import itemgetter
import random


def find_prev_index(jobs, job):
    job_n = job[0]
    job_seq = job[1] - 1
    if job_seq < 0:
        return None
    for i in range(0, len(jobs)):
        if jobs[i][0] == job_n and jobs[i][1] == job_seq:
            return i


# generating a random, valid neighbor based on previous solution
def shuffle_jobs(array):
    while True:
        first_job, second_job = random.choice(array), random.choice(array)
        # check if job_number is different
        if first_job[0] != second_job[0]:
            # indexes of two elements
            a, b = array.index(first_job), array.index(second_job)
            # indexes of previous jobs
            a_prev, b_prev = find_prev_index(array, first_job), find_prev_index(array, second_job)
            # check if the order of jobs are still valid
            if (a_prev is None or a_prev <= b) and (b_prev is None or b_prev <= a):
                array[b], array[a] = array[a], array[b]  # swap jobs
                return array


# evaluation function, total length of schedule
def find_max_duration(array):
    result = 0
    for sublist in array:
        temp = max(sublist, key=itemgetter(2))[2]
        if result < temp:
            result = temp
    return result


# creates schedule out of a ordered job list
# each job list is validated before
def schedule(jobs, machine_count):
    # first parameter is machine number
    results = [[] for x in range(machine_count)]
    time = [0] * (len(jobs) + 1)  # time of end of job
    time_m = [0] * machine_count  # time end of machine last job
    for job in jobs:
        job_n = job[0]  # job number
        machine_n = job[2]  # machine number
        duration = job[3]  # duration length
        # starting time is max(end of prev task in job, end of prev task on machine)
        start = max(time_m[machine_n], time[job_n])
        results[machine_n].append((job, start, start + duration))  # insert to the end
        # update the last time of job and machine
        time[job_n] = start + duration  # set new time of end of job
        time_m[machine_n] = start + duration    # set new end of last job of machine
    return results


# function that prints schedule as readable output
def print_result(res):
    i = 0
    for machine in res:
        string = "machine " + str(i) + ":"
        for job in machine:
            string = string + "(" + str(job[0][0]) + ", " + str(job[0][1]) + ", " + str(job[1]) + ")"
        print(string)
        i += 1
