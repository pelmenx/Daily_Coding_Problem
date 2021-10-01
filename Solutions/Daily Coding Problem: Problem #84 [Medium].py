# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1
# represents land and 0 represents water, so an island is a group of 1s that are
# neighboring whose perimeter is surrounded by water.
#
# For example, this matrix has 4 islands.
#
# 1 0 0 0 0
# 0 0 1 1 0
# 0 1 1 0 0
# 0 0 0 0 0
# 1 1 0 0 1
# 1 1 0 0 1
#
#
#
# --------------------------------------------------------------------------------
#
#
def count_islands(array):
    def check_in_islands():
        def update_islands():
            islands[i_].append([i, j])
            return False
        if j == item[1]:
            return update_islands()
        elif j == item[1] - 1:
            return update_islands()
        elif j == item[1] + 1:
            return update_islands()
        return True

    islands = []
    for i, row in enumerate(array):
        for j, item_ in enumerate(row):
            if item_:
                check = True
                for i_ in range(len(islands)):
                    for item in islands[i_]:
                        if i == item[0]:
                            check = check_in_islands()
                            if check is False:
                                break
                        elif i == item[0] - 1:
                            check = check_in_islands()
                            if check is False:
                                break
                        elif i == item[0] + 1:
                            check = check_in_islands()
                            if check is False:
                                break
                    if check is False:
                        break
                if check is True:
                    islands.append([[i, j]])
    return len(islands)


array = [[1, 0, 0, 0, 0],
         [0, 0, 1, 1, 0],
         [0, 1, 1, 0, 0],
         [0, 0, 0, 0, 0],
         [1, 1, 0, 0, 1],
         [1, 1, 0, 0, 1]]

assert count_islands(array) == 4
