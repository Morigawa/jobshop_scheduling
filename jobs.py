from typing import List


class Task:
    task_id = ()  # tuple (job, task)
    prev_task = None
    next_task = None
    machine: int
    starting_time: int
    duration: int

    def __init__(self, task_id, prev_task, next_task, machine, starting_time, duration):
        self.task_id = task_id
        self.prev_task = prev_task
        self.next_task = next_task
        self.machine = int(machine)
        self.starting_time = int(starting_time)
        self.duration = int(duration)

    def get_prev_end(self):
        if self.prev_task is None:
            return 0
        return self.prev_task.starting_time + self.prev_task.duration

    def get_end(self):
        return self.starting_time + self.duration

    def __str__(self):
        return str(self.task_id) + " m:" + str(self.machine) + " " + str(self.starting_time) + " - " + str(
            self.get_end())

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.task_id == other.task_id

    def __ne__(self, other):
        return not self.__eq__(other)


def construct_tests_js1():
    file = []
    with open("resources/jobshop1.txt", 'r') as file1:
        for line in file1:
            if line.isspace():
                continue

            if (line[1].isdigit() or line[2].isdigit()) and line[3] != 'x':
                file.append(line.strip())

    tests = []
    while len(file) > 0:
        desc = file.pop(0).split()  # tuple (amount of jobs, amount of machines)
        jobs = [desc]
        for x in range(int(desc[0])):
            job = file.pop(0).split()
            y = 0
            while len(job) > 0:
                if y == 0:
                    task = Task((x, y), None, None, job.pop(0), -1, job.pop(0))
                else:
                    task = Task((x, y), jobs[-1], None, job.pop(0), -1, job.pop(0))
                    jobs[-1].next_task = task
                y += 1
                jobs.append(task)
        tests.append(jobs)
    return tests


def construct_test_j2():  # TODO REMEMBER FIRST ELEMENT IS DESCRIPTION OF TEST
    tests = []
    return tests
