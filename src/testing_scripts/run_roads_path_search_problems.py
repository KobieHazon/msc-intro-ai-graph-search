"""
automated run of the search problems with the algorithms we implemented.
Contains functionality to export the result paths and analytics to a file.
"""

import datetime
import math
import os.path
from typing import Generator, List

from helper_types.Node import path_str
from project_paths import PROBLEMS_FILE, RUN_RESULTS_DIR
from roads_graph_search.AStarRoadsRouteFinder import AStarRoadsRouteFinder
from roads_graph_search.IDAStarRoadsRouteFinder import IDAStarRoadsRouteFinder
from roads_graph_search.RoadsRouteFinder import RoadsRouteFinder
from roads_graph_search.UCSRoadsRouteFinder import UCSRoadsRouteFinder
from roads_graph_search.utils import compute_path_time, huristic_function
from testing_scripts.RandomSearchProblemGenerator import SearchQuery


def read_search_problems_file(
    problems_file_path: str = str(PROBLEMS_FILE), problem_count: int = math.inf
) -> Generator[SearchQuery, None, None]:
    """
    Generator for reading the problems file in the project.
    """
    problem_yield_count = 0
    with open(problems_file_path, "r") as problems_input_file:
        for problem_row in problems_input_file.readlines():
            if problem_yield_count >= problem_count:
                break
            problem_yield_count += 1
            source_index_str, target_index_str = problem_row.split(", ")
            yield int(source_index_str), int(target_index_str)


DEFAULT_RESULTS_FOLDER = str(RUN_RESULTS_DIR)


def run_path_search_problems_file(
    route_finder: RoadsRouteFinder,
    export_row_format: str,
    export_file_path: str,
    problems_file_path: str = str(PROBLEMS_FILE),
):
    """
    runs the search problem algorith on the problems file and exports results to file with analytics provided.
    """
    if not os.path.exists(DEFAULT_RESULTS_FOLDER):
        os.mkdir(DEFAULT_RESULTS_FOLDER)
    with open(os.path.join(DEFAULT_RESULTS_FOLDER, export_file_path), "w") as export_file:
        for source_index, target_index in read_search_problems_file(problems_file_path):
            roads_map = route_finder.roads_map
            path_heuristic_time = huristic_function(
                roads_map[source_index].lat,
                roads_map[source_index].lon,
                roads_map[target_index].lat,
                roads_map[target_index].lon,
            )
            route_find_start_time = datetime.datetime.now()
            search_path = route_finder.find_route(source_index, target_index)
            route_find_end_time = datetime.datetime.now()
            route_find_run_time = (route_find_end_time - route_find_start_time).total_seconds()
            path_actual_time = compute_path_time(search_path[-1])
            export_row = export_row_format.format(
                path=path_str(search_path),
                path_actual_time=round(path_actual_time, 4),
                path_heuristic_time=round(path_heuristic_time, 4),
                route_find_run_time=round(route_find_run_time, 4),
            )
            export_file.write(f"{export_row}\n")


def dispatch(args: List[str], export_runtime: bool = False):
    search_algo = args[1]
    if search_algo == "ucs":
        route_finder = UCSRoadsRouteFinder("israel.csv")
        export_row_format = "{path} - {path_actual_time}"
        export_file_path = "UCSRuns.txt"
    elif search_algo == "astar":
        route_finder = AStarRoadsRouteFinder("israel.csv")
        export_row_format = "{path} - {path_actual_time} - {path_heuristic_time}"
        export_file_path = "AStarRuns.txt"
    elif search_algo == "idastar":
        route_finder = IDAStarRoadsRouteFinder("israel.csv")
        export_row_format = "{path} - {path_actual_time} - {path_heuristic_time}"
        export_file_path = "IDAStarRuns.txt"
    else:
        raise ValueError("invalid argument value")
    if export_runtime:
        export_row_format += " - {route_find_run_time}"
    run_path_search_problems_file(route_finder, export_row_format, export_file_path)


if __name__ == "__main__":
    from sys import argv

    if len(argv) != 2:
        raise ValueError("incorrect parameter count")
    dispatch(argv)
