"""
Class implementation of RoadsRouteFinder for the UCS algorithm
"""

from typing import List, Optional

from graph_search import best_first_graph_search
from helper_types import Node

from .RoadsRouteFinder import RoadsRouteFinder
from .RoadsSearchProblem import RoadsSearchProblem
from .utils import compute_path_time


class UCSRoadsRouteFinder(RoadsRouteFinder):
    def _inner_find(self, search_problem: RoadsSearchProblem) -> Optional[List[Node]]:
        route_node = best_first_graph_search(search_problem, f=compute_path_time)
        if route_node:
            return route_node.path()
        return None
