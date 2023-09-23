import sys
from get_all_tests import get_all_tests

N = 40


def main():
    # Get the iteration number from command line argument
    run_iter = int(sys.argv[1]) - 1
    
    # Get all the test names
    test_names = get_all_tests()
    
    # Calculate the total number of tests
    num_tests = len(test_names)
    
    # Calculate the number of tests to run per iteration
    tests_per_run = num_tests // N
    
    # Calculate the start and end indices for the current iteration
    start = run_iter * tests_per_run
    end = num_tests if run_iter == N - 1 else (run_iter + 1) * tests_per_run
    
    # Write the selected tests to a file
    with open("tests_to_run", "w") as f:
        for test in test_names[start:end]:
            f.write(test + "\n")


if __name__ == "__main__":
    main()
