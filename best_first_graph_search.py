from PriorityQueue import PriorityQueue
from Node import Node
from cost_functions import init_h_cost


# Best first graph search will be used to run UCS and A* with a different f function.
# the algorithm uses an open list that is a priority queue and a closed list to avoid circles.
# the algorithm returns the path and the path cost.
# the algorithm gets the source and target nodes and the f function.
def best_first_graph_search(s, t, f):
    source = Node(s, None, 0, init_h_cost(s, t, f))
    target = Node(t, None, 0, 0)
    open_list = PriorityQueue()
    closed_list = set()
    open_list.append(source)
    open_list.sort()
    while open_list.not_empty:
        node = open_list.pop()
        if node.index == target.index:
            return node.path, node.path_cost
        closed_list.add(node.index)
        child_lst = node.expand(target, f)
        if child_lst:
            for child in child_lst:
                if child.index not in closed_list and not open_list.check_index(child.index):
                    open_list.append(child)
                    open_list.sort()
                elif open_list.check_index(child.index):
                    n = open_list.get_node(child.index)
                    g_cost, f_cost = node.get_cost(child.index, target, f)
                    if n.path_cost < f_cost:
                        open_list.remove(n)
                        g_child, path_child = node.get_cost(child.index, target, f)
                        open_list.append(Node(child.index, node, g_child, path_child))
                        open_list.sort()
    return None
