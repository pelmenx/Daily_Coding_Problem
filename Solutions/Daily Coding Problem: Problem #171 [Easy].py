# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# You are given a list of data entries that represent entries and exits of groups
# of people into a building. An entry looks like this:
#
# {"timestamp": 1526579928, count: 3, "type": "enter"}
#
# This means 3 people entered the building. An exit looks like this:
#
# {"timestamp": 1526580382, count: 2, "type": "exit"}
#
# This means that 2 people exited the building. timestamp is in Unix time
# [https://en.wikipedia.org/wiki/Unix_time].
#
# Find the busiest period in the building, that is, the time with the most people
# in the building. Return it as a pair of (start, end) timestamps. You can assume
# the building always starts off and ends up empty, i.e. with 0 people inside.
#
#
# --------------------------------------------------------------------------------
#
#
def inside_building(array):
    def sort_by_timestamp():
        for i in range(1, len(array)):
            j = i
            while j > 0 and array[j]["timestamp"] < array[j - 1]["timestamp"]:
                array[j], array[j - 1] = array[j - 1], array[j]
                j -= 1
    sort_by_timestamp()
    max_counter = 0
    start = None
    end = None
    corrent_counter = 0
    for item in array:
        if item["type"] == "enter":
            corrent_counter += item["count"]
            if corrent_counter > max_counter:
                max_counter = corrent_counter
                start = item['timestamp']
        else:
            if corrent_counter == max_counter:
                end = item['timestamp']
            corrent_counter -= item["count"]
    return(start, end)


arr = [{"timestamp": 1526579928, "count": 3, "type": "enter"},
       {"timestamp": 1526580382, "count": 2, "type": "exit"}]

assert inside_building(arr) == (1526579928, 1526580382)
