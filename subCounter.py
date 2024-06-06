import testing


# Function to count submarines in a given sea grid
def count_submarines(sea):
    submarine_count = 0

    # Iterate through each cell in the sea grid
    for i in range(len(sea)):
        for j in range(len(sea[i])):
            if sea[i][j] == 'X':  # If the cell is part of a submarine
                submarine_count += check_if_first_cell(i, j, sea)

    return submarine_count


# Function to check if the current cell is the first cell of a submarine
def check_if_first_cell(i, j, sea):
    # Check if there are any submarine cells above or to the left
    return 0 if (i > 0 and sea[i - 1][j] == 'X') or (j > 0 and sea[i][j - 1] == 'X') else 1