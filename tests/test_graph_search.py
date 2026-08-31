from collections import namedtuple
from importlib import import_module
from types import SimpleNamespace

from graph_search import best_first_graph_search
from graph_search.idastar_graph_search import idastar_graph_search
from helper_types.SearchProblem import SearchProblem

State = namedtuple("State", ["index"])
Action = namedtuple("Action", ["target", "cost"])


class ToyProblem(SearchProblem):
    def __init__(self):
        self.graph = {
            0: (Action(1, 1), Action(2, 4)),
            1: (Action(2, 1), Action(3, 5)),
            2: (Action(3, 1),),
            3: (),
        }

    @property
    def s_start(self):
        return State(0)

    def is_goal(self, state):
        return state == 3

    def actions(self, state):
        return self.graph[state]

    def succ(self, state, action):
        return State(action.target)

    def step_cost(self, state, action):
        return action.cost


def states(node):
    return [item.state for item in node.path()]


def test_uniform_cost_search_returns_lowest_cost_path():
    node = best_first_graph_search(ToyProblem(), lambda item: item.path_cost)

    assert states(node) == [0, 1, 2, 3]
    assert node.path_cost == 3


def test_idastar_returns_lowest_cost_path():
    node = idastar_graph_search(ToyProblem(), lambda item: item.path_cost, is_tree_search=False)

    assert states(node) == [0, 1, 2, 3]
    assert node.path_cost == 3


def test_informed_route_finders_bind_heuristic_to_goal(monkeypatch):
    problem = SimpleNamespace(start_junction=State(1), goal_junction=State(9))

    for module_name, search_name in (
        ("roads_graph_search.AStarRoadsRouteFinder", "best_first_graph_search"),
        ("roads_graph_search.IDAStarRoadsRouteFinder", "idastar_graph_search"),
    ):
        module = import_module(module_name)
        captured = {}

        def fake_search(*args, _captured=captured, **kwargs):
            _captured["heuristic"] = kwargs["f"]
            return None

        monkeypatch.setattr(module, search_name, fake_search)
        finder = object.__new__(
            module.AStarRoadsRouteFinder
            if ".AStarRoadsRouteFinder" in module_name
            else module.IDAStarRoadsRouteFinder
        )
        finder.roads_map = {}
        if "IDAStar" in module_name:
            finder.is_tree_search = False

        finder._inner_find(problem)

        assert captured["heuristic"].keywords["target_junction_index"] == 9
