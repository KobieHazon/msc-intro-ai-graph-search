"""
abstract class for finding routes between two points in Roads class, implementations will use a specific algorithm
"""

from abc import ABC, abstractmethod
from typing import List, Optional

from helper_types import Node
from roads_graph_search.RoadsSearchProblem import RoadsSearchProblem, RoadsSearchProblemFactory


class RoadsRouteFinder(ABC):
    def __init__(self, roads_map_path: str):
        self.search_problem_factory = RoadsSearchProblemFactory(roads_map_path)
        self.roads_map = self.search_problem_factory.roads_map

    def find_route(self, source_index: int, target_index: int) -> Optional[List[Node]]:
        search_problem = self.search_problem_factory.make_roads_search_problem(
            source_index, target_index
        )
        return self._inner_find(search_problem)

    @abstractmethod
    def _inner_find(self, search_problem: RoadsSearchProblem) -> Optional[List[Node]]:
        """
        function implemented inside inherited classes, inside will be the algorithm specific logic
        """
        pass
