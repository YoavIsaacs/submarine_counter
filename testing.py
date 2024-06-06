import random
import subCounter


# Function to create a random sea grid with submarines
def create_sea():
    max_rows = 50
    max_cols = 50

    rows = random.randint(10, max_rows)
    cols = random.randint(10, max_cols)
    number_of_submarines = random.randint(1, 10)

    # Initialize sea grid with water ('O')
    sea = [['O' for _ in range(cols)] for _ in range(rows)]

    actual_num_submarines = 0

    for _ in range(number_of_submarines):
        submarine_height = random.randint(1, min(rows // 2, 10))
        submarine_width = random.randint(1, min(cols // 2, 10))

        placed = False
        attempts = 0

        # Attempt to place a submarine, limit attempts to avoid infinite loops
        while not placed and attempts < 100:
            top_row = random.randint(1, rows - submarine_height - 1)
            top_col = random.randint(1, cols - submarine_width - 1)

            # Check if the space is available and has the required sea buffer
            can_place = True
            for i in range(-1, submarine_height + 1):
                for j in range(-1, submarine_width + 1):
                    if sea[top_row + i][top_col + j] == 'X':
                        can_place = False
                        break
                if not can_place:
                    break

            if can_place:
                # Place the submarine
                for i in range(submarine_height):
                    for j in range(submarine_width):
                        sea[top_row + i][top_col + j] = 'X'
                actual_num_submarines += 1
                placed = True

            attempts += 1

    return sea, actual_num_submarines


# Function to print the sea grid
def print_sea(sea):
    for row in sea:
        print(row)


# Function to check predefined edge cases
def check_edge_cases():
    # Edge case 1: The whole sea is one big submarine
    sea = [
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X']
    ]
    print("Checking edge case 1 - the whole \"sea\" is one big submarine")
    if subCounter.count_submarines(sea) == 1:
        print("Edge case 1 passed!")
    else:
        print("Edge case 1 failed.")

    # Edge case 2: No submarines in the sea
    sea = [
        ['O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O']
    ]
    print("Checking edge case 2 - no submarines")
    if subCounter.count_submarines(sea) == 0:
        print("Edge case 2 passed!")
    else:
        print("Edge case 2 failed.")


def check_legal_sea(sea, diagonal_check):
    # checking if the given sea is a valid matrix
    if not sea or not all(len(row) == len(sea[0]) for row in sea):
        return False

    rows = len(sea)
    cols = len(sea[0])
    visited = [[False] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if sea[r][c] == 'X' and not visited[r][c]:
                submarine_cells, x = dfs(r, c, visited, rows, cols, sea)
                # checking if the submarine is "solid"
                min_r = min(submarine_cells, key=lambda xr: xr[0])[0]
                max_r = max(submarine_cells, key=lambda xr: xr[0])[0]
                min_c = min(submarine_cells, key=lambda xc: xc[1])[1]
                max_c = max(submarine_cells, key=lambda xc: xc[1])[1]
                for i in range(min_r, max_r + 1):
                    for j in range(min_c, max_c + 1):
                        if sea[i][j] != 'X':
                            return False
                if not diagonal_check:
                    # check for touching submarines including at the diagonals
                    for x, y in submarine_cells:
                        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                            nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and sea[nx][ny] == 'X' and (nx, ny) not in submarine_cells:
                            return False
                else:
                    for x, y in submarine_cells:
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and sea[nx][ny] == 'X' and (nx, ny) not in submarine_cells:
                            return False
    return True


def dfs(r, c, visited, rows, cols, sea):
    stack = [(r, c)]
    cells = []
    xr, yr = 0, 0
    while stack:
        xr, yr = stack.pop()
        if visited[xr][yr]:
            continue
        visited[xr][yr] = True
        cells.append((xr, yr))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = xr + dx, yr + dy
            if 0 <= nx < rows and 0 <= ny < cols and sea[nx][ny] == 'X' and not visited[nx][ny]:
                stack.append((nx, ny))
    return cells, xr


def check_invalid_sea(diagonal_check):
    sea = [
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['O', 'X', 'X', 'X']
    ]
    print("Expecting illegal sea")
    if check_legal_sea(sea, diagonal_check):
        print("Illegal sea, test passed")
    sea = [
        ['X', 'X', 'O', 'O'],
        ['X', 'X', 'O', 'O'],
        ['O', 'O', 'X', 'X'],
        ['O', 'O', 'X', 'X']
    ]
    if diagonal_check:
        print("Expecting legal sea")
        if check_legal_sea(sea, diagonal_check):
            print("Legal sea, test passed")
        else:
            print("Illegal sea, test failed")
    else:
        print("Expecting illegal sea")
        if not check_legal_sea(sea, diagonal_check):
            print("Illegal sea, test passed")
        else:
            print("Legal sea, test failed")
    sea = [
        ['X', 'X', 'X', 'O'],
        ['X', 'O', 'X', 'O'],
        ['X', 'X', 'X', 'O'],
        ['O', 'O', 'O', 'O']
    ]

    print("Expecting illegal sea")
    if not check_legal_sea(sea, diagonal_check):
        print("Illegal sea, test passed")
    else:
        print("Legal sea, test failed")

    sea = [
        ['X', 'O', 'O', 'O'],
        ['X', 'O', 'O', 'O'],
        ['X', 'X', 'X', 'O'],
        ['O', 'O', 'O', 'O']
    ]
    print("Expecting illegal sea")
    if not check_legal_sea(sea, diagonal_check):
        print("Illegal sea, test passed")
    else:
        print("Legal sea, test failed")
