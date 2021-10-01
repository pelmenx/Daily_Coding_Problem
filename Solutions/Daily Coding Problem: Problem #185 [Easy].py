# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given two rectangles on a 2D graph, return the area of their intersection. If
# the rectangles don't intersect, return 0.
#
# For example, given the following rectangles:
#
# {
#     "top_left": (1, 4),
#     "dimensions": (3, 3) # width, height
# }
#
#
# and
#
# {
#     "top_left": (0, 5),
#     "dimensions": (4, 3) # width, height
# }
#
#
# return 6.
#
#
# --------------------------------------------------------------------------------
#
#
def intersection(first, second):
    def make_rectange_cordinates(coordinates):
        width = (coordinates["top_left"][0], coordinates["top_left"][0] + coordinates["dimensions"][0] - 1)
        height = (coordinates["top_left"][1], coordinates["top_left"][1] + coordinates["dimensions"][1] - 1)
        return (width, height)

    first_coordinates = make_rectange_cordinates(first)
    second_coordinates = make_rectange_cordinates(second)
    count = 0
    for i in range(second_coordinates[0][0], second_coordinates[0][1] + 1):
        if first_coordinates[0][0] <= i <= first_coordinates[0][1]:
            for j in range(second_coordinates[1][0], second_coordinates[1][1] + 1):
                if first_coordinates[1][0] <= j <= first_coordinates[1][1]:
                    count += 1
    return count


first_rectangle = {"top_left": (1, 4), "dimensions": (3, 3)}
second_rectangle = {"top_left": (0, 5), "dimensions": (4, 3)}

assert intersection(first_rectangle, second_rectangle) == 6
