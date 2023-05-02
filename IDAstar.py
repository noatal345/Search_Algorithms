from Node import Node
from cost_functions import init_h_cost
from DFS_limit import depth_limited_search


# IDAstar function calls the depth limited search function while there is no solution.
# returns solution-path.
def IDAstar(s,t):
    f = 'g+h'
    source = Node(s, None, 0, init_h_cost(s, t, f))
    target = Node(t, None, 0, 0)
    f_limit = source.path_cost
    while True:
        solution, f_limit = depth_limited_search(source, target, f_limit, f)
        if solution:
            return solution
    return False
