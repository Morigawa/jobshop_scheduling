import copy


def construct_first_solution(schedule):
    test = copy.copy(schedule)
    desc = test.pop(0)  # tuple (amount jobs, machines)
    job_list = []  # list containing all jobs
    task_list = []  # list containing all task of one job
    for task in test:  # generate list of all jobs with all their tasks
        task_list.append(task)
        if task.next_task is None:
            job_list.append(list(task_list))
            task_list.clear()

    schedule = [[] for x in
                range(int(desc[1]))]  # list of lists, each list represents the job schedule for one machine
    while job_list:
        for x in range(int(desc[1])):
            for job in job_list:
                task = job[0]
                if task.machine == x:
                    if not schedule[task.machine]:
                        task.starting_time = task.get_prev_end()
                    elif task.get_prev_end() >= schedule[task.machine][-1].get_end():
                        task.starting_time = task.get_prev_end()
                    else:
                        task.starting_time = schedule[task.machine][-1].get_end()

                    schedule[x].append(job.pop(0))
                    if [] in job_list:
                        job_list.remove([])
    check_unnecessary_gaps(schedule)
    return schedule


def create_neighborhood(schedule):
    neighborhood = []
    for machine in schedule:
        for task in machine:
            if check_valid_exchange(machine, task):
                neighbor = copy.deepcopy(schedule)
                exchange(neighbor[neighbor.index(machine)], task)
                check_unnecessary_gaps(neighbor)
                neighborhood.append(neighbor)
    return neighborhood


def check_unnecessary_gaps(schedule):
    for machine in schedule:
        for task in machine:
            i = machine.index(task)-1
            if i < 0:
                continue
            prev_on_machine = machine[i]  # previous task on machine
            if task.get_prev_end() <= prev_on_machine.get_end():
                task.starting_time = prev_on_machine.get_end()
            elif task.starting_time > task.get_prev_end():
                task.starting_time = task.get_prev_end()


def check_valid_exchange(machine, task):
    if machine.index(task) + 1 <= len(machine) - 1:
        task2 = machine[machine.index(task) + 1]
        if not task.next_task and not task2.prev_task:
            return True
        elif not task.next_task:
            return task2.get_prev_end() <= task.starting_time
        elif not task2.prev_task:
            return task.next_task.starting_time >= task2.get_end()
        return task.next_task.starting_time >= task2.get_end() and task2.get_prev_end() <= task.starting_time
    return False


def exchange(machine, task):
    i = machine.index(task)
    machine[i + 1].starting_time = machine[i].starting_time
    machine[i].starting_time = machine[i + 1].get_end()  # TODO is this enough? not sure
    machine[i], machine[i + 1] = machine[i + 1], machine[i]  # exchange in machine list


def calculate_duration(schedule):
    duration = 0
    for machine in schedule:
        if duration < machine[-1].get_end():
            duration = machine[-1].get_end()
    return duration
