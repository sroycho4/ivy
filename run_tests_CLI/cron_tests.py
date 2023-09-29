import sys
from get_all_tests import get_all_tests

run_iter = int(sys.argv[1])
test_names = get_all_tests()

# Run 150 tests in each iteration of the cron job
tests_per_run = 150
start = run_iter * tests_per_run
end = (run_iter + 1) * tests_per_run

print("Running Tests:")
with open("tests_to_run", "w") as f:
    for test in test_names[start:end]:
        print(test)
        f.write(test + "\n")
