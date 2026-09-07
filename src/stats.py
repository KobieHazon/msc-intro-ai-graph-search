"""
This file should be runnable to print map_statistics using
$ python stats.py
"""

import statistics
from collections import Counter, namedtuple

from ways import load_map_from_csv


def map_statistics(roads):
    """return a dictionary containing the desired information
    You can edit this function as you wish"""
    Stat = namedtuple("Stat", ["max", "min", "avg"])
    link_type_counter = Counter()
    junction_links_counter = Counter()
    junction_link_distance_counter = Counter()
    for junction in roads.values():
        junction_links_counter[junction.index] = len(junction.links)
        link_type_counter += Counter(junction_link.highway_type for junction_link in junction.links)
        for link in junction.links:
            junction_link_distance_counter[(junction.index, link.target)] = link.distance
    sorted_junction_links_counter = [
        links_num for junction_id, links_num in junction_links_counter.most_common()
    ]
    sorted_junction_link_distance_counter = [
        link_distance for link_id, link_distance in junction_link_distance_counter.most_common()
    ]

    return {
        "Number of junctions": len(roads),
        "Number of links": sum(junction_links_counter.values()),
        "Outgoing branching factor": Stat(
            max=sorted_junction_links_counter[0],
            min=sorted_junction_links_counter[-1],
            avg=statistics.mean(sorted_junction_links_counter),
        ),
        "Link distance": Stat(
            max=sorted_junction_link_distance_counter[0],
            min=sorted_junction_link_distance_counter[-1],
            avg=statistics.mean(sorted_junction_link_distance_counter),
        ),
        # value should be a dictionary
        # mapping each road_info.TYPE to the no' of links of this type
        "Link type histogram": link_type_counter,
        # tip: use collections.Counter
    }


def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print("{}: {}".format(k, v))


if __name__ == "__main__":
    from sys import argv

    assert len(argv) == 1
    print_stats()
