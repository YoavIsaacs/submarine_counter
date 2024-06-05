import testing
def count_submarines(sea):
    submarine_count = 0

    for i in range(len(sea)):
        for j in range(len(sea[i])):
            if sea[i][j] == 'X':
                submarine_count += check_if_first_cell(i, j, sea)
    return submarine_count


def check_if_first_cell(i, j, sea):
    if i > 0 and sea[i - 1][j] == 'X':
        return 0
    if j > 0 and sea[i][j - 1] == 'X':
        return 0
    return 1
