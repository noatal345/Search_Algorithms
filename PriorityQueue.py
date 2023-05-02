
# This is the Priority queue class
# The queue holds a list and all the functions are python list functions.
class PriorityQueue:
    def __init__(self):
        self.open_list = []
        # self.f = func

    def append(self, item):
        self.open_list.append(item)

    def extend(self, lst):
        self.open_list.extend(lst)

    # sorts the queue according to the f cost
    def sort(self):
        self.open_list.sort(key = lambda node: node.path_cost, reverse=True)

    def remove(self, item):
        if self.open_list:
            self.open_list.remove(item)

    def pop(self):
        if self.open_list:
            return self.open_list.pop()
        else:
            raise Exception('Trying to pop from empty PriorityQueue.')

    def not_empty(self):
        return len(self.open_list) != 0

    # checks if a node in the queue have this index
    def check_index(self, ind):
        for n in self.open_list:
            if n.index == ind :
                return True
            else:
                return False

    def get_node(self, ind):
        for n in self.open_list:
            if n.index == ind :
                return n
