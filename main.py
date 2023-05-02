from best_first_graph_search import best_first_graph_search
from cost_functions import get_h_cost
from IDAstar import IDAstar


def heuristic_function(lat1, lon1, lat2, lon2):
    return get_h_cost(lat1, lon1, lat2, lon2)


# calls best first graph search
# return path
def find_ucs_rout(source, target):
    f = 'g'
    path, path_cost = best_first_graph_search(source,target,f)
    return path


# calls best first graph search
# return path
def find_astar_route(source, target):
    f = 'g+h'
    path, path_cost = best_first_graph_search(source,target,f)
    return path


# calls IDAstar
# return path
def find_idastar_route(source, target):
    path = IDAstar(source, target)
    return path
    

def dispatch(argv):
    from sys import argv
    source, target = int(argv[2]), int(argv[3])
    if argv[1] == 'ucs':
        path = find_ucs_rout(source, target)
    elif argv[1] == 'astar':
        path = find_astar_route(source, target)
    elif argv[1] == 'idastar':
        path = find_idastar_route(source, target)
    print(' '.join(str(j) for j in path))


if __name__ == '__main__':
    from sys import argv
    dispatch(argv)
    #create_problems()
    #ucs_runs()
    #astar_runs()
    #create_map()

