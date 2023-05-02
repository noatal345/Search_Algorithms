from collections import namedtuple
from ways import load_map_from_csv


# Calculate all the statistics
def map_statistics(roads):
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])
    # Outgoing branching factor + link distance calc:
    bf_list=[]
    dist_list=[]
    type_list=[]
    for v in roads.junctions():
        bf_list.append(len(v.links))
        for l in v.links:
            dist_list.append(l.distance)
            type_list.append(l.highway_type)
    min_links = min(bf_list)
    max_links = max(bf_list)
    avg_links = sum(bf_list)/len(bf_list)
    min_dis = min(dist_list)
    max_dis = max(dist_list)
    avg_dis = sum(dist_list)/len(dist_list)
    from ways.info import TYPE_INDICES
    from ways.info import ROAD_TYPES
    d = {}
    for key in TYPE_INDICES:
        d[ROAD_TYPES[key]]=type_list.count(key)
    return {
        'Number of junctions': len(roads.junctions()),
        'Number of links': len(list(roads.iterlinks())),
        'Outgoing branching factor': Stat(max=max_links, min=min_links, avg=avg_links),
        'Link distance': Stat(max=max_dis, min=min_dis, avg=avg_dis),
        'Link type histogram': d
    }


def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))


        
if __name__ == '__main__':
    from sys import argv
    assert len(argv) == 1
    print_stats()
