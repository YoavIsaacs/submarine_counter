import subCounter
import testing
import sys


def is_input_a_valid_number(input_number):
    try:
        int(input_number)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid number of arguments, expected main.py and the number of tests to run in "
              "addition to the edge cases.")
        sys.exit(1)
    number_of_tests = sys.argv[1]
    passed_tests = 0
    failed_tests = 0
    testing.check_edge_cases()
    if is_input_a_valid_number(number_of_tests):
        number_of_tests = int(number_of_tests)
        for i in range(number_of_tests):
            sea, number_of_created_subs = testing.create_sea()
            number_of_found_subs = subCounter.count_submarines(sea)
            print("Number of created subs = " + str(number_of_created_subs))
            print("Number of found subs = " + str(number_of_found_subs))
            if number_of_created_subs == number_of_found_subs:
                print(f'Test {i + 1} passed!')
                passed_tests += 1
            else:
                print(f'Test {i} failed.')
                print("Failed sea: ")
                testing.print_sea(sea)
                failed_tests += 1
    print("Passed " + str(passed_tests) + " tests out of " + str(number_of_tests) + " tests")
    print("Failed " + str(failed_tests) + " tests out of " + str(number_of_tests) + " tests")
else:
    print("Please enter a valid number.")
