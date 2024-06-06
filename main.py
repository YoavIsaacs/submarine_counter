import subCounter
import testing
import sys


# Function to validate if the input is a valid number
def is_input_a_valid_number(input_number):
    try:
        int(input_number)
        return True
    except ValueError:
        return False


# Main block to execute the test script
if __name__ == '__main__':
    # Check if the number of arguments is correct
    if len(sys.argv) != 3:
        print("Invalid number of arguments, expected main.py, the number of tests to run "
              "in addition to the edge cases and whether to allow diagonally touch submarines.")
        sys.exit(1)

    number_of_tests = sys.argv[1]
    passed_tests = 0
    failed_tests = 0
    diagonal_check = sys.argv[2]
    if diagonal_check.lower() not in ["yes", "y", "no", "n"]:
        print("Invalid diagonal case, expected 'yes' or 'no' or 'y' or 'n'")
        sys.exit(1)
    else:
        if diagonal_check.lower() == "yes" or "y":
            diagonal_check = True
        else:
            diagonal_check = False

    # Check edge cases before running the tests
    testing.check_edge_cases()

    # Validate if the number of tests is a valid number
    if is_input_a_valid_number(number_of_tests):
        number_of_tests = int(number_of_tests)\

        testing.check_invalid_sea(diagonal_check)

        # Run the specified number of tests
        for i in range(number_of_tests):
            sea, number_of_created_subs = testing.create_sea()

            print("Checking for valid sea.")
            if not testing.check_legal_sea(sea, diagonal_check):
                print("Invalid sea, test failed.")
                testing.print_sea(sea)
                failed_tests += 1

            number_of_found_subs = subCounter.count_submarines(sea)

            print("Number of created subs = " + str(number_of_created_subs))
            print("Number of found subs = " + str(number_of_found_subs))

            # Check if the test passed or failed
            if number_of_created_subs == number_of_found_subs:
                print(f'Test {i + 1} passed!')
                passed_tests += 1
            else:
                print(f'Test {i} failed.')
                print("Failed sea: ")
                testing.print_sea(sea)
                failed_tests += 1

    # Print summary of test results
    print("Passed " + str(passed_tests) + " tests out of " + str(number_of_tests) + " tests")
    print("Failed " + str(failed_tests) + " tests out of " + str(number_of_tests) + " tests")
else:
    print("Please enter a valid number.")
