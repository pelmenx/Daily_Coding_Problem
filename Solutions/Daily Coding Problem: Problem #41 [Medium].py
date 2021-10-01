# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given an unordered list of flights taken by someone, each represented as
# (origin, destination) pairs, and a starting airport, compute the person's
# itinerary. If no such itinerary exists, return null. If there are multiple
# possible itineraries, return the lexicographically smallest one. All flights
# must be used in the itinerary.
#
# For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL',
# 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list
# ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].
#
# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport
# 'COM', you should return null.
#
# Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and
# starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even
# though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first
# one is lexicographically smaller.
#
#
# --------------------------------------------------------------------------------
#
#
def find_itinerary(list_of_flights, starting_airport, path=[]):
    if not list_of_flights:
        return path + [starting_airport]
    itinerary = None
    for i in range(len(list_of_flights)):
        if list_of_flights[i][0] == starting_airport:
            current_itinerary = find_itinerary(list_of_flights[:i] + list_of_flights[i + 1:], list_of_flights[i][1], path + [list_of_flights[i][0]])
            if itinerary is None:
                itinerary = current_itinerary
            else:
                if current_itinerary < itinerary:
                    itinerary = current_itinerary
    return itinerary


print(find_itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL'))
print(find_itinerary([('SFO', 'COM'), ('COM', 'YYZ')], 'COM'))
print(find_itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A'))
