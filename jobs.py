from typing import List


class Task:
    task_id = ()
    prev_task = None
    next_task = None
    machine: int
    starting_time: int
    duration: int

    def __init__(self, task_id, prev_task, next_task, machine, starting_time, duration):
        self.task_id = task_id
        self.prev_task = prev_task
        self.next_task = next_task
        self.machine = machine
        self.starting_time = starting_time
        self.duration = duration

    def get_prev_end(self):
        return self.prev_task.starting_time + self.prev_task.duration


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
        desc = file.pop(0).split()
        jobs: List[Task] = []
        for x in range(int(desc[0])):
            job = file.pop(0).split()
            y = 0
            while len(job) > 0:
                if y == 0:
                    task = Task((x, y), None, None, job.pop(0), -1, job.pop(0))  # TODO starting time
                    y = False
                    jobs.append(task)
                else:
                    task = Task((x, y), jobs[-1], None, job.pop(0), -1, job.pop(0))
                    jobs[-1].next_task = task
                    jobs.append(task)
                y += 1
        tests.append(jobs)
    return tests


def construct_test_j2():
    tests = []
    return tests
