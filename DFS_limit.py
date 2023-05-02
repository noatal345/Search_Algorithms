
# Depth Limited Search
# This is a modified version of DFS that limits the depth of the search
# by using a depth limit. The depth limit is a threshold that is set
# by the IDA* algorithm. The depth limit is increased each time the
# algorithm fails to find a solution. The algorithm stops when the
# depth limit is greater than the cost of the best solution.
# The algorithm returns a solution if it finds one, or the cost of the
# best solution if it doesn't.
# The algorithm is implemented recursively.
def depth_limited_search(source, target, f_limit, f):
    n = source
    if n.path_cost > f_limit:
        return None, n.path_cost
    if n.index == target.index:
        return n.path, None
    next_l = float("inf")
    child_lst = n.expand(target, f)
    for child in child_lst:
        solution, new_limit = depth_limited_search(child, target, f_limit, f)
        if solution:
            return solution, None
        next_l = min(new_limit, next_l)
    return None, next_l


