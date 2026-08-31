"""
Class implementation of RoadsRouteFinder for the IDAStar algorithm
"""

from functools import partial
from typing import Optional, List

from graph_search.idastar_graph_search import idastar_graph_search
from helper_types import Node
from roads_graph_search.RoadsRouteFinder import RoadsRouteFinder
from roads_graph_search.RoadsSearchProblem import RoadsSearchProblem
from roads_graph_search.utils import combined_curr_cost_heuristic


class IDAStarRoadsRouteFinder(RoadsRouteFinder):
    def __init__(self, roads_map_path: str, is_tree_search: int = False):
        super().__init__(roads_map_path)
        self.is_tree_search = is_tree_search

    def _inner_find(self, search_problem: RoadsSearchProblem) -> Optional[List[Node]]:
        path_cost_heuristic_func = partial(combined_curr_cost_heuristic,
                                           roads_map=self.roads_map,
                                           target_junction_index=search_problem.start_junction.index)

        route_node = idastar_graph_search(search_problem,
                                          f=path_cost_heuristic_func,
                                          is_tree_search=self.is_tree_search)
        if route_node:
            return route_node.path()
        return None
