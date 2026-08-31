"""
Algorithm implementation for BestFirstGraphSearch
"""
from typing import Callable, Optional

from helper_types import Node
from helper_types import PriorityQueue
from helper_types.SearchProblem import SearchProblem


def best_first_graph_search(problem: SearchProblem, f: Callable[[Node], int]) -> Optional[Node]:
    frontier = PriorityQueue(f)
    frontier.append(Node(problem.s_start.index))
    closed_list = set()
    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node
        closed_list.add(node.state)
        for child in node.expand(problem):
            if child.state not in closed_list and child not in frontier:
                frontier.append(child)
            elif child in frontier and f(child) < frontier[child]:
                del frontier[child]
                frontier.append(child)
    return None
