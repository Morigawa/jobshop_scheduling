import job_scheduling.jobs as jobs
import job_scheduling.simulated_annealing as sim_a
import job_scheduling.display as display


def main():
    tests = jobs.construct_tests_js1()  #TODO REMEMBER FIRST ELEMENT IS DESCRIPTION OF TEST
    tests = tests.__add__(jobs.construct_test_j2())  # list containing all tests
    print("Anzahl der Tests: ")
    print(len(tests))

    example = tests[2]  # only one test, delete later
    display.show(sim_a.simulated_annealing(example))


if __name__ == "__main__":
    main()
