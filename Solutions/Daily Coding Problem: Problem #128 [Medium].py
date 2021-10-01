# Good morning! Here's your coding interview problem for today.
#
# The Tower of Hanoi is a puzzle game with three rods and n disks, each a
# different size.
#
# All the disks start off on the first rod in a stack. They are ordered by size,
# with the largest disk on the bottom and the smallest one at the top.
#
# The goal of this puzzle is to move all the disks from the first rod to the last
# rod while following these rules:
#
#  * You can only move one disk at a time.
#  * A move consists of taking the uppermost disk from one of the stacks and
#    placing it on top of another stack.
#  * You cannot place a larger disk on top of a smaller disk.
#
# Write a function that prints out all the steps necessary to complete the Tower
# of Hanoi. You should assume that the rods are numbered, with the first rod being
# 1, the second (auxiliary) rod being 2, and the last (goal) rod being 3.
#
# For example, with n = 3, we can do this in 7 moves:
#
# Move 1 to 3
# Move 1 to 2
# Move 3 to 2
# Move 1 to 3
# Move 2 to 1
# Move 2 to 3
# Move 1 to 3
#
#
#
# --------------------------------------------------------------------------------
#
#
def tower_of_hanoi(n):
    def solve(iterator, counter):
        def move_1_2(iterator):
            rod_2.append(rod_1.pop())
            print("Move 1 to 2")
            iterator += 1
            iterator %= 3
            return iterator

        def move_2_1(iterator):
            rod_1.append(rod_2.pop())
            print("Move 2 to 1")
            iterator += 1
            iterator %= 3
            return iterator

        def move_1_3(iterator):
            rod_3.append(rod_1.pop())
            print("Move 1 to 3")
            iterator += 1
            iterator %= 3
            return iterator

        def move_3_1(iterator):
            rod_1.append(rod_3.pop())
            print("Move 3 to 1")
            iterator += 1
            iterator %= 3
            return iterator

        def move_2_3(iterator):
            rod_3.append(rod_2.pop())
            print("Move 2 to 3")
            iterator += 1
            iterator %= 3
            return iterator

        def move_3_2(iterator):
            rod_2.append(rod_3.pop())
            print("Move 3 to 2")
            iterator += 1
            iterator %= 3
            return iterator

        if len(rod_3) == n:
            return
        counter += 1
        if n % 2 == 0:
            if iterator == 0:
                if rod_1 and not rod_2:
                    return solve(move_1_2(iterator), counter)
                elif not rod_1 and rod_2:
                    return solve(move_2_1(iterator), counter)
                elif rod_1 and rod_2:
                    if rod_1[-1] < rod_2[-1]:
                        return solve(move_1_2(iterator), counter)
                    elif rod_2[-1] < rod_1[-1]:
                        return solve(move_2_1(iterator), counter)
            elif iterator == 1:
                if rod_1 and not rod_3:
                    return solve(move_1_3(iterator), counter)
                elif not rod_1 and rod_3:
                    return solve(move_3_1(iterator), counter)
                elif rod_1 and rod_3:
                    if rod_1[-1] < rod_3[-1]:
                        return solve(move_1_3(iterator), counter)
                    elif rod_3[-1] < rod_1[-1]:
                        return solve(move_3_1(iterator), counter)
            elif iterator == 2:
                if rod_2 and not rod_3:
                    return solve(move_2_3(iterator), counter)
                elif not rod_2 and rod_3:
                    return solve(move_3_2(iterator), counter)
                elif rod_2 and rod_3:
                    if rod_2[-1] < rod_3[-1]:
                        return solve(move_2_3(iterator), counter)
                    elif rod_3[-1] < rod_2[-1]:
                        return solve(move_3_2(iterator), counter)
        else:
            if iterator == 0:
                if rod_1 and not rod_3:
                    return solve(move_1_3(iterator), counter)
                elif not rod_1 and rod_3:
                    return solve(move_3_1(iterator), counter)
                elif rod_1 and rod_3:
                    if rod_1[-1] < rod_3[-1]:
                        return solve(move_1_3(iterator), counter)
                    elif rod_3[-1] < rod_1[-1]:
                        return solve(move_3_1(iterator), counter)
            elif iterator == 1:
                if rod_1 and not rod_2:
                    return solve(move_1_2(iterator), counter)
                elif not rod_1 and rod_2:
                    return solve(move_2_1(iterator), counter)
                elif rod_1 and rod_2:
                    if rod_1[-1] < rod_2[-1]:
                        return solve(move_1_2(iterator), counter)
                    elif rod_2[-1] < rod_1[-1]:
                        return solve(move_2_1(iterator), counter)
            elif iterator == 2:
                if rod_2 and not rod_3:
                    return solve(move_2_3(iterator), counter)
                elif not rod_2 and rod_3:
                    return solve(move_3_2(iterator), counter)
                elif rod_2 and rod_3:
                    if rod_2[-1] < rod_3[-1]:
                        return solve(move_2_3(iterator), counter)
                    elif rod_3[-1] < rod_2[-1]:
                        return solve(move_3_2(iterator), counter)
    rod_1 = []
    rod_2 = []
    rod_3 = []
    for i in range(n, 0, -1):
        rod_1.append(i)
    solve(0, 0)


tower_of_hanoi(3)
