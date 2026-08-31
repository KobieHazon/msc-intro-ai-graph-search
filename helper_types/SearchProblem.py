"""
Class for general search problem representation
"""

from abc import ABCMeta, abstractmethod
from typing import Generic, Iterable, TypeVar

SearchProblemState = TypeVar("SearchProblemState")
SearchProblemAction = TypeVar("SearchProblemAction")


class SearchProblem(Generic[SearchProblemState, SearchProblemAction], metaclass=ABCMeta):
    @property
    @abstractmethod
    def s_start(self) -> SearchProblemState:
        pass

    @abstractmethod
    def is_goal(self, state: SearchProblemState) -> bool:
        pass

    @abstractmethod
    def actions(self, state: SearchProblemState) -> Iterable[SearchProblemAction]:
        pass

    @abstractmethod
    def succ(self, state: SearchProblemState, action: SearchProblemAction) -> SearchProblemState:
        pass

    @abstractmethod
    def step_cost(self, state: SearchProblemState, action: SearchProblemAction) -> float:
        pass
