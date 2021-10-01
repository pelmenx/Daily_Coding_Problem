# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Uber.
#
# A rule looks like this:
#
# A NE B
#
# This means this means point A is located northeast of point B.
#
# A SW C
#
# means that point A is southwest of C.
#
# Given a list of rules, check if the sum of the rules validate. For example:
#
# A N B
# B NE C
# C N A
#
#
# does not validate, since A cannot be both north and south of C.
#
# A NW B
# A N B
#
#
# is considered valid.
#
#
# --------------------------------------------------------------------------------
#
#
class Node(object):
    def __init__(self, arg):
        super(Node, self).__init__()
        self.arg = arg
        self.N = []
        self.W = []
        self.S = []
        self.E = []


def make_a_map(*rules):
    node_dict = {}
    for rule in rules:
        rule_list = rule.split()
        if rule_list[2] not in node_dict:
            node_dict[rule_list[2]] = Node(rule_list[2])
        if rule_list[0] not in node_dict:
            node_dict[rule_list[0]] = Node(rule_list[0])
        for direction in rule_list[1]:
            if direction == "N":
                node_dict[rule_list[2]].N.append(node_dict[rule_list[0]])
                for item in node_dict[rule_list[0]].__dict__:
                    if item == "N":
                        node_dict[rule_list[2]].N.extend(node_dict[rule_list[0]].N)
                    elif item == "E":
                        node_dict[rule_list[2]].N.extend(node_dict[rule_list[0]].E)
                    elif item == "W":
                        node_dict[rule_list[2]].N.extend(node_dict[rule_list[0]].W)
                node_dict[rule_list[2]].N = list(set(node_dict[rule_list[2]].N))

                node_dict[rule_list[0]].S.append(node_dict[rule_list[2]])
                for item in node_dict[rule_list[2]].__dict__:
                    if item == "S":
                        node_dict[rule_list[0]].S.extend(node_dict[rule_list[2]].S)
                    elif item == "E":
                        node_dict[rule_list[0]].S.extend(node_dict[rule_list[2]].E)
                    elif item == "W":
                        node_dict[rule_list[0]].S.extend(node_dict[rule_list[2]].W)
                node_dict[rule_list[0]].S = list(set(node_dict[rule_list[0]].S))

            elif direction == "W":
                node_dict[rule_list[2]].W.append(node_dict[rule_list[0]])
                for item in node_dict[rule_list[0]].__dict__:
                    if item == "N":
                        node_dict[rule_list[2]].W.extend(node_dict[rule_list[0]].N)
                    elif item == "S":
                        node_dict[rule_list[2]].W.extend(node_dict[rule_list[0]].S)
                    elif item == "W":
                        node_dict[rule_list[2]].W.extend(node_dict[rule_list[0]].W)
                node_dict[rule_list[2]].W = list(set(node_dict[rule_list[2]].W))

                node_dict[rule_list[0]].E.append(node_dict[rule_list[2]])
                for item in node_dict[rule_list[2]].__dict__:
                    if item == "N":
                        node_dict[rule_list[0]].E.extend(node_dict[rule_list[2]].N)
                    elif item == "S":
                        node_dict[rule_list[0]].E.extend(node_dict[rule_list[2]].S)
                    elif item == "E":
                        node_dict[rule_list[0]].E.extend(node_dict[rule_list[2]].E)
                node_dict[rule_list[0]].E = list(set(node_dict[rule_list[0]].E))

            elif direction == "S":
                node_dict[rule_list[2]].S.append(node_dict[rule_list[0]])
                for item in node_dict[rule_list[0]].__dict__:
                    if item == "S":
                        node_dict[rule_list[2]].S.extend(node_dict[rule_list[0]].S)
                    elif item == "E":
                        node_dict[rule_list[2]].S.extend(node_dict[rule_list[0]].E)
                    elif item == "W":
                        node_dict[rule_list[2]].S.extend(node_dict[rule_list[0]].W)
                node_dict[rule_list[2]].S = list(set(node_dict[rule_list[2]].S))

                node_dict[rule_list[0]].N.append(node_dict[rule_list[2]])
                for item in node_dict[rule_list[2]].__dict__:
                    if item == "N":
                        node_dict[rule_list[0]].N.extend(node_dict[rule_list[2]].N)
                    elif item == "E":
                        node_dict[rule_list[0]].N.extend(node_dict[rule_list[2]].E)
                    elif item == "W":
                        node_dict[rule_list[0]].N.extend(node_dict[rule_list[2]].W)
                node_dict[rule_list[0]].N = list(set(node_dict[rule_list[0]].N))

            elif direction == "E":
                node_dict[rule_list[2]].E.append(node_dict[rule_list[0]])
                for item in node_dict[rule_list[0]].__dict__:
                    if item == "N":
                        node_dict[rule_list[2]].E.extend(node_dict[rule_list[0]].N)
                    elif item == "S":
                        node_dict[rule_list[2]].E.extend(node_dict[rule_list[0]].S)
                    elif item == "E":
                        node_dict[rule_list[2]].E.extend(node_dict[rule_list[0]].E)
                node_dict[rule_list[2]].E = list(set(node_dict[rule_list[2]].E))

                node_dict[rule_list[0]].W.append(node_dict[rule_list[2]])
                for item in node_dict[rule_list[2]].__dict__:
                    if item == "N":
                        node_dict[rule_list[0]].W.extend(node_dict[rule_list[2]].N)
                    elif item == "S":
                        node_dict[rule_list[0]].W.extend(node_dict[rule_list[2]].S)
                    elif item == "W":
                        node_dict[rule_list[0]].W.extend(node_dict[rule_list[2]].W)
                node_dict[rule_list[0]].W = list(set(node_dict[rule_list[0]].W))

        if (list(set(node_dict[rule_list[0]].N) & set(node_dict[rule_list[0]].S))):
            return False
        elif (list(set(node_dict[rule_list[0]].E) & set(node_dict[rule_list[0]].W))):
            return False
        elif (list(set(node_dict[rule_list[2]].N) & set(node_dict[rule_list[2]].S))):
            return False
        elif (list(set(node_dict[rule_list[2]].E) & set(node_dict[rule_list[2]].W))):
            return False
    return True


assert make_a_map(('A N B'), ('B NE C'), ('C N A')) is False
assert make_a_map(('A NW B'), ('A N B')) is True
