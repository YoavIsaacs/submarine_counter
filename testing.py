import random
import subCounter


def create_sea():
    max_rows = 50
    max_cols = 50

    rows = random.randint(10, max_rows)
    cols = random.randint(10, max_cols)
    number_of_submarines = random.randint(1, 10)

    sea = [['O' for _ in range(cols)] for _ in range(rows)]

    actual_num_submarines = 0

    for _ in range(number_of_submarines):
        submarine_height = random.randint(1, min(rows // 2, 10))
        submarine_width = random.randint(1, min(cols // 2, 10))

        placed = False
        attempts = 0

        while not placed and attempts < 100:  # Limit attempts to avoid infinite loops
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
                for i in range(submarine_height):
                    for j in range(submarine_width):
                        sea[top_row + i][top_col + j] = 'X'
                actual_num_submarines += 1
                placed = True

            attempts += 1

    return sea, actual_num_submarines


def print_sea(sea):
    for row in sea:
        print(row)


def check_edge_cases():
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
