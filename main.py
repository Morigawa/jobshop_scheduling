import job_scheduling.jobs as jobs
import job_scheduling.simulated_annealing as sim_a
import job_scheduling.display as display


def print_solution(schedule):
    i = 0
    for machine in schedule:
        sol = ""
        for task in machine:
            sol = sol + task.pr_sol() + " "
        print("machine " + str(i) + ": " + sol)
        i += 1


def main():
    tests = jobs.construct_tests_js1()  # TODO REMEMBER FIRST ELEMENT IS DESCRIPTION OF TEST
    tests = tests.__add__(jobs.construct_test_j2())  # list containing all tests
    print("Anzahl der Tests: ")
    print(len(tests))

    example = tests[2]  # only one test, delete later
    result = sim_a.simulated_annealing(example)
    print_solution(result)
    display.show(result)


if __name__ == "__main__":
    main()
