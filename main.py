import subCounter
import testing


def is_input_a_valid_number(input_number):
    try:
        int(input_number)
        return True
    except ValueError:
        return False


number_of_tests = input("How many tests do you want to run? ")
passed_tests = 0
failed_tests = 0
if is_input_a_valid_number(number_of_tests):
    tests = int(number_of_tests)
    for i in range(tests):
        sea, number_of_created_subs = testing.create_sea()
        number_of_found_sube = subCounter.count_submarines(sea)
        testing.print_sea(sea)
        print("Number of created subs = " + str(number_of_created_subs))
        print("Number of found subs = " + str(number_of_found_sube))
        if number_of_created_subs == number_of_found_sube:
            print("Test passed!")
            passed_tests += 1
        else:
            print("Test failed.")
            failed_tests += 1
    print("Passed " + str(passed_tests) + " tests out of " + str(tests) + " tests")
    print("Failed " + str(failed_tests) + " tests out of " + str(tests) + " tests")

else:
    print("Invalid number, run the program again")
