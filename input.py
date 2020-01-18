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
        jobs = []
        for x in range(int(desc[0])):
            job_file = file.pop(0).split()
            job = []
            y = 0
            while len(job_file) > 0:
                task = (x, y, int(job_file.pop(0)), int(job_file.pop(0)))
                y += 1
                job.append(task)
            jobs.append(job)
        tests.append(jobs)
    return tests


def construct_test_j2():
    return []
