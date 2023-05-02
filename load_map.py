from ways import load_map_from_csv


# this file is limits the map loading to one time.
map_is_loaded = None
r = None
junc_list = None


def load_junc():
    global map_is_loaded
    if not map_is_loaded:
        global r
        r = load_roads()
        global junc_list
        junc_list= r.junctions()
    map_is_loaded = 1
    return junc_list


def load_roads():
    global r
    if not r:
        r = (load_map_from_csv())
    return r