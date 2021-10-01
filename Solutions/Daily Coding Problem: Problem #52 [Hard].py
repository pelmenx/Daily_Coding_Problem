# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Implement an LRU (Least Recently Used) cache. It should be able to be
# initialized with a cache size n, and contain the following methods:
#
#  * set(key, value): sets key to value. If there are already n items in the cache
#    and we are adding a new item, then it should also remove the least recently
#    used item.
#  * get(key): gets the value at key. If no such key exists, return null.
#
# Each operation should run in O(1) time.
#
#
# --------------------------------------------------------------------------------
#
#
class node(object):
    def __init__(self, arg):
        super(node, self).__init__()
        self.arg = arg
        self.next = None
        self.prev = None


class least_recently_used_cache(object):
    def __init__(self, size):
        super(least_recently_used_cache, self).__init__()
        self.cashe_size = size
        self.node_dict = {}
        self.head = node(None)
        self.tail = node(None)
        self.last = self.head

    def set(self, key, value):
        def remove():
            tmp = self.head.next
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            del self.node_dict[tmp.arg]

        if key in self.node_dict:
            self.update_node(key)
        else:
            self.add_new_note(key)
        if len(self.node_dict) > self.cashe_size:
            remove()

    def get(self, key):
        if key in self.node_dict:
            if self.node_dict[key].next != self.tail:
                self.update_node(key)
        return self.node_dict.get(key, "null")

    def add_new_note(self, key):
        self.node_dict[key] = node(key)
        self.node_dict[key].next = self.tail
        self.node_dict[key].prev = self.last
        self.tail.prev = self.node_dict[key]
        if self.last.arg is not None:
            self.last.next = self.node_dict[key]
        else:
            self.head.next = self.node_dict[key]
        self.last = self.node_dict[key]

    def update_node(self, key):
        self.node_dict[key].next.prev = self.node_dict[key].prev
        self.node_dict[key].prev.next = self.node_dict[key].next
        if self.last == self.node_dict[key]:
            self.last = self.node_dict[key].prev
        del self.node_dict[key]
        self.add_new_note(key)


lru = least_recently_used_cache(5)
lru.set("a", 1)
lru.set("b", 2)
lru.set("c", 3)
lru.set("d", 4)
lru.set("e", 5)
lru.set("f", 6)
lru.set("g", 7)
lru.get("c")
print(lru.get("qq"))
for item in lru.node_dict:
    print(lru.node_dict[item].arg, end=" ")
print()
for item in lru.node_dict:
    print(lru.node_dict[item].arg, lru.node_dict[item].prev.arg, lru.node_dict[item].next.arg)
print(lru.head.next.arg, lru.head.next.next.arg, lru.head.next.next.next.arg, lru.tail.prev.prev.arg, lru.tail.prev.arg)
