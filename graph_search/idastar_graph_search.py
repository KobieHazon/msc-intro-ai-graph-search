"""
Algorithm implementation for IDAStar
"""

import math
from typing import Callable, Optional, Tuple

from helper_types import Node
from helper_types.SearchProblem import SearchProblem


def dfs_contour(
    curr_node: Node,
    problem: SearchProblem,
    f: Callable[[Node], int],
    f_limit: int,
    is_tree_search: int,
) -> Tuple[Optional[Node], int]:
    if f(curr_node) > f_limit:
        return None, f(curr_node)
    if problem.is_goal(curr_node.state):
        return curr_node, f_limit
    next_f = math.inf
    for child_node in curr_node.expand(problem):
        # made it possible to turn off TreeSearch because without it runtime is unreasonable and when we run from
        # main we need to run as TreeSearch but for analytics questions (ques. 12-13), we need to get results reasonably
        if not is_tree_search and child_node in curr_node.path():
            continue
        solution, new_f = dfs_contour(child_node, problem, f, f_limit, is_tree_search)
        if solution:
            return solution, f_limit
        next_f = min(next_f, new_f)

    return None, next_f


def idastar_graph_search(
    problem: SearchProblem, f: Callable[[Node], int], is_tree_search: int
) -> Optional[Node]:
    start_node = Node(problem.s_start.index)
    f_limit = f(start_node)
    while f_limit != math.inf:
        solution, f_limit = dfs_contour(start_node, problem, f, f_limit, is_tree_search)
        if solution:
            return solution
    return None
