# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by LinkedIn.
#
# Given a list of points, a central point, and an integer k, find the nearest k
# points from the central point.
#
# For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central
# point (1, 2), and k = 2, return[(0, 0), (3, 1)].
#
#
# --------------------------------------------------------------------------------
#
#
def closest_points(points_list, central_points, k):
    closest_points_list = []
    for point in points_list:
        if len(closest_points_list) < k:
            closest_points_list.append(point)
            if len(closest_points_list) == k:
                closest_points_list.sort()
        else:
            current_range = (((central_points[0] - point[0]) ** 2) + ((central_points[1] - point[1]) ** 2)) ** 0.5
            last_range = (((central_points[0] - closest_points_list[-1][0]) ** 2) + ((central_points[1] - closest_points_list[-1][1]) ** 2)) ** 0.5
            if current_range < last_range:
                closest_points_list[-1] = point
                closest_points_list.sort()
    return closest_points_list


assert closest_points([(0, 0), (5, 4), (3, 1)], (1, 2), 2) == [(0, 0), (3, 1)]
