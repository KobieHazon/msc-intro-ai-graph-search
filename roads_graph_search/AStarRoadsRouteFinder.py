"""
Class implementation of RoadsRouteFinder for the AStar algorithm
"""

from functools import partial
from typing import Optional, List

from graph_search import best_first_graph_search
from helper_types import Node
from .RoadsRouteFinder import RoadsRouteFinder
from .RoadsSearchProblem import RoadsSearchProblem
from .utils import combined_curr_cost_heuristic


class AStarRoadsRouteFinder(RoadsRouteFinder):
    def _inner_find(self, search_problem: RoadsSearchProblem) -> Optional[List[Node]]:
        path_cost_heuristic_func = partial(combined_curr_cost_heuristic,
                                           roads_map=self.roads_map,
                                           target_junction_index=search_problem.start_junction.index)

        route_node = best_first_graph_search(search_problem, f=path_cost_heuristic_func)
        if route_node:
            return route_node.path()
        return None
