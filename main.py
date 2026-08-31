'''
Parse input and run appropriate code.
Don't use this file for the actual work; only minimal code should be here.
We just parse input and call methods from other modules.
'''
from helper_types.Node import path_str
from roads_graph_search import AStarRoadsRouteFinder
from roads_graph_search import IDAStarRoadsRouteFinder
from roads_graph_search import UCSRoadsRouteFinder


# do NOT import ways. This should be done from other files
# simply import your modules and call the appropriate functions

# I moved the function huristic_function to roads_graph_search.utils to follow good practices
# other files have good documentation. didn't touch or document this file, stats.py and the ways subpackage.


def find_ucs_rout(source, target):
    route_finder = UCSRoadsRouteFinder(roads_map_path='israel.csv')
    return route_finder.find_route(source, target)


def find_astar_route(source, target):
    route_finder = AStarRoadsRouteFinder(roads_map_path='israel.csv')
    return route_finder.find_route(source, target)


def find_idastar_route(source, target):
    route_finder = IDAStarRoadsRouteFinder(roads_map_path='israel.csv', is_tree_search=True)
    return route_finder.find_route(source, target)


def dispatch(argv):
    from sys import argv
    source, target = int(argv[2]), int(argv[3])
    if argv[1] == 'ucs':
        path = find_ucs_rout(source, target)
    elif argv[1] == 'astar':
        path = find_astar_route(source, target)
    elif argv[1] == 'idastar':
        path = find_idastar_route(source, target)
    else:
        raise ValueError("incorrect argument option")
    print(path_str(path))


if __name__ == '__main__':
    from sys import argv

    dispatch(argv)

    # the following are the ways to invoke the code segments that are needed for questions that examine exported files.
    # I recommend the use of 3.10 for much faster runtime, in my testing it was x3 faster(!)
    # just run the following one-by-one in the terminal:
    """
    # uses the ucs algorithm to determine connectivity, maximal runtime 15*100 seconds
    python3 testing_scripts/RandomSearchProblemGenerator.py ucs
    python3 testing_scripts/run_roads_path_search_problems.py ucs  # exports UCSRuns.txt, runtime a few minutes
    python3 testing_scripts/run_roads_path_search_problems.py astar  # exports AStarRuns.txt, runtime a few minutes
    # TODO: explain the time for the line below
    python3 testing_scripts/draw_map.py  # exports the content of the directory sulotions_img
    """