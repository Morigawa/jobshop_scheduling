import job_scheduling.jobs as jobs
import job_scheduling.simulated_annealing as sim_a


def main():
    tests = jobs.construct_tests_js1()
    print("Anzahl der Tests: ")
    print(len(tests))


if __name__ == "__main__":
    main()