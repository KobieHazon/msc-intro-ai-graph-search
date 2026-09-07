"""
utilities used in this sub-package. they are for roads-specific graph search algorithms
"""

from helper_types import Node
from ways import compute_distance
from ways.graph import Roads
from ways.info import SPEED_RANGES

MAXIMUM_SPEED_ALL_ROAD_TYPES = max(SPEED_RANGES, key=lambda x: x[1])[1]


def compute_path_time(node: Node) -> int:
    """
    Computes the time to traverse the path that lead to parameter node.
    returns the time in hours.
    """
    node_path = node.path()
    sum_time = 0
    for node in node_path[1:]:
        connecting_link = node.action
        sum_time += connecting_link.distance / (
            SPEED_RANGES[connecting_link.highway_type][1] * 1000
        )
    return sum_time


def min_coordinates_drive_time(lat1: float, lon1: float, lat2: float, lon2: float) -> int:
    """
    returns the minimal drive time between two coordinates.
    meaning, it uses the aerial distance and divides it by the maximum speed on all roads.
    time returned is in hours.
    """
    distance = compute_distance(lat1, lon1, lat2, lon2)
    min_drive_time = distance / MAXIMUM_SPEED_ALL_ROAD_TYPES
    return min_drive_time


def huristic_function(lat1, lon1, lat2, lon2):
    """
    functionally it is an alias to min_coordinates_drive_time above.
    exists because didn't want to change the signature at all like in the instructions.
    moved from main.py to a more appropriate place, wrote comment in old place.
    """
    return min_coordinates_drive_time(lat1, lon1, lat2, lon2)


def combined_curr_cost_heuristic(node: Node, roads_map: Roads, target_junction_index: int) -> int:
    """
    Function to combine path cost of path up till current node and also take into account
    the heuristic cost of the path remaining until the target.
    return is in hours.
    """
    node_lat = roads_map[node.state].lat
    node_lon = roads_map[node.state].lon
    target_lat = roads_map[target_junction_index].lat
    target_lon = roads_map[target_junction_index].lon
    return compute_path_time(node) + huristic_function(node_lat, node_lon, target_lat, target_lon)
