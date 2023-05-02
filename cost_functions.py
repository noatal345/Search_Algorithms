from load_map import load_roads
from ways.info import SPEED_RANGES
from ways.tools import compute_distance


roads = load_roads()


# the g cost function gets a parent node and a child index.
# returns the path cost according to 'g' for the child.
# return time cost per hour
def get_g_cost(source_node, target_index):
    node_junction = roads[source_node.index]
    for link in node_junction.links:
        if link.target == target_index:
            speed = SPEED_RANGES[link.highway_type][1]
            t = source_node.g + link.distance/1000 / speed
            return t


# the astar cost function gets a parent node, child index and a target index
# return the path cost according to 'g+h' for the child.
def get_astar_cost(source_node, local_target_index, target_node):
    loc_target = roads[local_target_index]
    target = target_node.junc
    return get_g_cost(source_node, local_target_index) + get_h_cost(loc_target.lat,loc_target.lon,target.lat,target.lon)


# the h cost function is the heuristic function that gets 2 junction coordinate
# return time cost per hour
def get_h_cost(lat1, lon1, lat2, lon2):
    distance = compute_distance(lat1,lon1,lat2,lon2)
    heuristic_cost = distance/110
    return heuristic_cost


# the initiation of h cost-heuristic cost at the beginning of A* or IDA* algorithm
def init_h_cost(source_index, target_index,f):
    if f == 'g+h':
        source = roads[source_index]
        target = roads[target_index]
        distance = compute_distance(source.lat,source.lon,target.lat,target.lon)
        heuristic_cost = distance/110
        return heuristic_cost
    else:
        return 0
