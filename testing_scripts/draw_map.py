"""
file used to draw paths of solutions to search problems.
"""
import os
import random
from typing import Optional, Dict, List

from roads_graph_search import RoadsRouteFinder, IDAStarRoadsRouteFinder
from testing_scripts.run_roads_path_search_problems import read_search_problems_file
from utils import exit_after
from ways.draw import plot_path
from ways.graph import Roads

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError('Please install matplotlib:  http://matplotlib.org/users/installing.html#windows')

DEFAULT_GRAPH_EXPORT_DIR = './sulotions_img'
ROUTE_FINDER_CLASS = IDAStarRoadsRouteFinder


def find_route_timeout(route_finder: RoadsRouteFinder, source_index: int, target_index: int, timeout: int = 50) \
        -> Optional[list]:
    """
    function to find a path solution of roads search problem but timeout the run of it.
    Notice that the timeout functionality overrides the ability to SIGINT the code running in it (KeyboardInterrupt).
    Need to kill to end.
    """
    @exit_after(timeout)
    def find_route() -> Optional[list]:
        return route_finder.find_route(source_index, target_index)

    return find_route()


def get_random_problem_paths(route_finder: RoadsRouteFinder,
                             count: int = 10,
                             problems_input_file: str = './problems.csv') -> Dict[int, List[int]]:
    """
    returns random search problems from an input file.
    """
    all_problems = [(problem_index, *problem_indices) for problem_index, problem_indices in
                    enumerate(read_search_problems_file(problems_input_file))]  # does row number begin at 0 or 1
    problem_paths_results = {}
    while len(problem_paths_results) != count:
        rand_problem = random.choice(all_problems)
        all_problems.remove(rand_problem)
        route_path = find_route_timeout(route_finder, rand_problem[1], rand_problem[2])
        if route_path:
            problem_paths_results[rand_problem[0]] = [path_node.state for path_node in route_path]

    return problem_paths_results


def export_paths_images(problem_index_to_path: Dict[int, List[int]],
                        roads_map: Roads,
                        export_dir: str = DEFAULT_GRAPH_EXPORT_DIR):
    """
    uses ways.draw.plot_path to plot the path in graph and then export to files as requested in the question.
    """
    if not os.path.exists(export_dir):
        os.mkdir(export_dir)
    for problem_index, path in problem_index_to_path.items():
        plot_path(roads_map, path, color='g')
        plt.savefig(os.path.join(export_dir, f'{problem_index}.png'))
        plt.clf()


def draw_random_paths_map(roads_map_path: str = 'israel.csv'):
    """
    main functionality of this module, draws random search problems paths from the input file and exports to files.
    """
    route_finder = ROUTE_FINDER_CLASS(roads_map_path)
    roads_map = route_finder.roads_map
    problem_index_to_path = get_random_problem_paths(route_finder, count=10)
    export_paths_images(problem_index_to_path, roads_map)


if __name__ == "__main__":
    draw_random_paths_map()
