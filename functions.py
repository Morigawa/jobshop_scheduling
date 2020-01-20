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


def shuffle_jobs(array, jobs_data):
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


def find_max_duration(array):
    result = 0
    for sublist in array:
        temp = max(sublist, key=itemgetter(2))[2]
        if result < temp:
            result = temp
    return result


def schedule(jobs, machine_count):
    # first parameter is machine number
    # your solution -> results = [[],[],[]]
    results = [[] for x in range(machine_count)]
    # time of end of job, equal to jobs
    time = [0] * (len(jobs) + 1)
    # time end of machine last job, equal to machines
    time_m = [0] * machine_count
    for job in jobs:
        job_n = job[0]  # job number
        machine_n = job[2]  # machine number
        duration = job[3]  # duration length
        start = max(time_m[machine_n], time[
            job_n])  # check if what is bigger the last finished job on the same machine or previous job, which has to be done
        results[machine_n].append((job, start, start + duration))  # insert to the end
        # update the last time of job and machine
        time[job_n] = start + duration
        time_m[machine_n] = start + duration
    return results


def print_result(res):
    i = 0
    for machine in res:
        string = "machine " + str(i) + ":"
        for job in machine:
            string = string + "(" + str(job[0][0]) + ", " + str(job[0][1]) + ", " + str(job[1]) + ")"
        print(string)
        i += 1
