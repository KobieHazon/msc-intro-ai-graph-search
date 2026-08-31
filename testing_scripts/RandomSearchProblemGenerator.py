"""
Implemetation of automatic generation of connected search problems and exporting it to outside file
"""
import random
from typing import Callable, Union, List, Tuple, Set, NamedTuple

from main import find_ucs_rout, find_astar_route, find_idastar_route
from utils.misc import exit_after

SearchQuery = Tuple[int, int]


class RandomSearchProblemGenerator(NamedTuple):
    """
    Class with functionality to generate the random problems.
    """
    connectivity_test_func: Callable[[int, int], Union[None, List[int]]]
    problem_count: int = 100
    connectivity_test_timeout: int = 15  # in seconds

    MIN_STATE_INDEX = 1
    MAX_STATE_INDEX = 944800
    MIN_SEARCH_PROBLEM_SOLUTION_PATH_LENGTH = 5

    def generate(self, min_index: int = MIN_STATE_INDEX, max_index: int = MAX_STATE_INDEX) -> Set[SearchQuery]:
        """
        Generates random search problems that are solvable inside the roads map.
        """
        generated_problems: Set[SearchQuery] = set()
        while len(generated_problems) < self.problem_count:  # we assume there are enough valid problems in the map
            rand_source, rand_target = random.sample(range(min_index, max_index), 2)
            print(f"Trying {(rand_source, rand_target)}")
            if (rand_source, rand_target) in generated_problems:
                continue

            if self.check_search_query_connected(rand_source, rand_target):
                print(f"Found {len(generated_problems)}")
                generated_problems.add((rand_source, rand_target))

        return generated_problems

    @exit_after(30)
    def check_search_query_connected(self, source: int, target: int):
        """
        Checks that the search query (in roads case it is just source and target indices) are solvable.
        It uses a connectivity test func. I only used it with the algorithms taught in the lessons (ucs/astar/idastar).
        """
        search_query_sol_path = self.connectivity_test_func(source, target)
        if search_query_sol_path and len(search_query_sol_path) >= self.MIN_SEARCH_PROBLEM_SOLUTION_PATH_LENGTH:
            print(search_query_sol_path)
            return search_query_sol_path
        return None


def export_search_problems(problems: Set[SearchQuery], output_file_path: str = './problems.csv'):
    """
    Exports the search problem to a csv file with the requested format.
    """
    with open(output_file_path, 'w') as export_file:
        export_file.write('\n'.join(f"{problem[0]}, {problem[1]}" for problem in problems))


def get_connectivity_func(args):
    if args[1] == 'ucs':
        return find_ucs_rout
    elif args[1] == 'astar':
        return find_astar_route
    elif args[1] == 'idastar':
        return find_idastar_route
    raise ValueError("incorrect connectivity func parameter")


def main(connectivity_func_name: str):
    """
    main flow for the script.
    """
    connectivity_func = get_connectivity_func(connectivity_func_name)
    problem_generator = RandomSearchProblemGenerator(connectivity_test_func=connectivity_func)
    search_problems = problem_generator.generate(max_index=1000)
    export_search_problems(search_problems)


if __name__ == "__main__":
    from sys import argv

    if not len(argv) == 2:
        raise ValueError("Incorrect parameter count")

    main(argv)

