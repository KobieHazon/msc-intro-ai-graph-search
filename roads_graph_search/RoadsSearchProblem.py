"""
Class implementation of SearchProblem Roads data structure (representing map with roads and highways)
"""

from typing import Iterable

from helper_types.SearchProblem import SearchProblem
from utils import SingletonMeta
from ways.graph import Junction, Link, Roads, load_map_from_csv


class RoadsSearchProblem(SearchProblem[Junction, Link]):  # State is the junction id
    def __init__(self, roads_map: Roads, start_junction: Junction, goal_junction: Junction):
        self.roads_map = roads_map
        self.start_junction = start_junction
        self.goal_junction = goal_junction

    @property
    def s_start(self) -> Junction:
        return self.start_junction

    def is_goal(self, state: Junction) -> bool:  # typing is int for state
        return state == self.goal_junction.index

    def actions(self, state: Junction) -> Iterable[Link]:
        return self.roads_map[state].links

    def succ(self, state: Junction, action: Link) -> Junction:
        return self.roads_map[action.target]

    def step_cost(self, state: Junction, action: Link) -> float:
        return action.distance


class RoadsSearchProblemFactory(metaclass=SingletonMeta):
    def __init__(self, roads_map_path: str):
        self.roads_map = load_map_from_csv(roads_map_path)

    def make_roads_search_problem(
        self, source_junction_id: int, goal_junction_id: int
    ) -> RoadsSearchProblem:
        start_junction = self.roads_map[source_junction_id]
        goal_junction = self.roads_map[goal_junction_id]
        return RoadsSearchProblem(self.roads_map, start_junction, goal_junction)
