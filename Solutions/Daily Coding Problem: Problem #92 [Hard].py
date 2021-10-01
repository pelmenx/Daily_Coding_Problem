# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Airbnb.
#
# We're given a hashmap associating each courseId key with a list of courseIds
# values, which represents that the prerequisites of courseId are courseIds.
# Return a sorted ordering of courses such that we can finish all courses.
#
# Return null if there is no such ordering.
#
# For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'],
# 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].
#
#
# --------------------------------------------------------------------------------
#
#
import copy


def courses_order(current_course, prev_course=None, tmp_course=[]):
    if not current_course:
        return tmp_course
    elif current_course == prev_course:
        return None
    else:
        prev_course = copy.deepcopy(current_course)
        for key in current_course:
            if not current_course.get(key):
                tmp_course.append(key)
                current_course.pop(key)
                for key_ in current_course:
                    for value in current_course.get(key_):
                        if value == key:
                            tmp = current_course.get(key_)
                            tmp.remove(key)
                            current_course[key_] = tmp
                return courses_order(current_course, prev_course, tmp_course)


print(courses_order({'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}))
print(courses_order({'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100', 'CSC300'], 'CSC100': []}))
