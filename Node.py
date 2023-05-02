from load_map import load_junc
from load_map import load_roads
from cost_functions import get_g_cost
from cost_functions import get_astar_cost
from cost_functions import get_h_cost


r = load_roads()
junc_list = load_junc()


# This is the Node class
class Node:
    def __init__(self, index, parent=None, g=0, path_cost=0):
        self.index = index
        self.parent = parent
        self.path = []
        self.g = g
        self.path_cost = path_cost
        if parent:
            self.path.extend(parent.path)
        self.path.append(self.index)
        self.junc = r[index]

    # this function expands the node to its children and returns a list of the children nodes.
    def expand(self, target, f):
        child_list = []
        node_junction = r[self.index]
        if node_junction:
            if node_junction.links:
                for link in node_junction.links:
                    g, path = self.get_cost(link.target, target, f)
                    child_list.append(Node(link.target, self, g, path))
            return child_list

    def path(self):
        return self.path

    # This function returns 2 things: the g cost and the f cost to the child node according to the current f function.
    # if f=g the node will hold 2 g costs
    # if f=g+h the node will hold a g cost and an f=g+h cost
    def get_cost(self, c, target, f):
        # c index, target node
        # if f=g c.g =g_cost and c.h =0
        if f == 'g':
            return get_g_cost(self, c), get_g_cost(self, c)
        if f == 'g+h':
            return get_g_cost(self, c), get_astar_cost(self, c, target)

    # This function returns the heuristic cost from the node to the target node.
    def heuristic_function(self, lat1, lon1, lat2, lon2):
        return get_h_cost(lat1, lon1, lat2, lon2)

