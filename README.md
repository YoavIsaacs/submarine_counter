# SUBMARINE COUNTER + TESTER

This project consistf of a solution to the submarine counting problem, and an automated tester for the solution.

### THE PROBLEM EXPLAINED
Given a n*m matrix, that represents the "sea", we need to count how many "submarines" are present in the sea.
### COMPONENTS EXPLAINED
* A sea tile is represented by 'O'.
* A submarine tile is represented by 'X'.
* All submarines are a full rectangle.
* Submarines cannot touch - unclear if they can diagonally, the tester covers both cases.
### TESTER ALGORITHM
The algorithm searches the matrix from top to bottom, and left to right. Since this is the method of scanning, when encountering a new submarine, it will be the top-left cell of said submarine. So once we encounter a cell of a submarine, we check if it's the top-left cell. If it is, we increment our submarine counter, otherwise we ignore the cell.
### MATRIX CHECKER
This checks the validity of the input matrix. It needs to be told if we're allowing diagonally touching submarines or not.
It does so by checking if all submarines are "solid" (no sea tiles in the the middle of the rectangle) and that no 2 submarines touch.
### TEST GENERATOR
This method generates all "unfixed" test cases, by randomizing the size of the matrix and the number of submarines, and places them randomly on the board, ensuring none touch, and that all submarines will fit. The mothid returns the generated matrix and the number of submarines created, enabling testing.
### TESTING PROCESS
The program starts with predefined edge cases, to ensure the testing is done properly. Once all edge cases are dealt with, it will generate tests according to the amount of tests wanted by the user.
###INPUT ARGUMENTS
Running the program via the terminal needs two extra arguments:
* The number of tests the user wishes to run.
* "yes"/"y"/"no"/"n" - if the user wants to allow diagonally touching submarines or not.
Any other inputs as arguments will cause the program to stop running, including anything that isn't an integer for the number of tests.
