# Graph Search on an Israel Road Network

A CS MSc Introduction to Artificial Intelligence exercise implementing uniform-cost search, A*, and iterative-deepening A* over a supplied road graph. The project includes route-finding adapters, heuristic and path-cost calculations, experiment scripts, recorded runs, and rendered route examples.

The `src/ways` package, map data, and original framework README were supplied for the exercise. `src/helper_types/Node.py`, `src/helper_types/PriorityQueue.py`, and `src/utils/misc.py` identify themselves in the recovered source as originating from the course repository. The graph-search implementations, road-specific adapters, experiment scripts, analysis outputs, and `docs/report.pdf` are the submitted work.

## Algorithms

- Uniform-cost graph search ordered by accumulated travel time
- A* graph search combining travel time and an admissible aerial-distance estimate
- IDA* contour search with configurable tree-search behavior
- Priority-queue frontier updates and route reconstruction through parent nodes

## Requirements

- Python 3.10 or newer
- [`uv`](https://docs.astral.sh/uv/)

## Setup

```bash
git clone https://github.com/KobieHazon/msc-intro-ai-graph-search.git
cd msc-intro-ai-graph-search
uv sync --dev
```

## Usage

Each command accepts source and destination junction identifiers:

```bash
uv run python src/main.py ucs 0 100
uv run python src/main.py astar 0 100
uv run python src/main.py idastar 0 100
```

The full map takes several seconds to load. IDA* in the assignment's required tree-search mode can take substantially longer on difficult routes.

Run the focused algorithm tests with:

```bash
uv run pytest
```

## Repository layout

- `src/`: algorithms, road adapters, supplied `ways` framework, and experiment modules; existing import names are retained.
- `data/`: the unchanged supplied road map and recovered problem set.
- `docs/`: background notes and my report.
- `results/`: preserved historical run outputs and `route-plots/` images.
- `tests/`: fast deterministic regression checks.
- `run-results/`: ignored output from new experiments, separate from recovered evidence.

Run the documented commands from the repository root. Search data is located relative to the source, not the current directory. Experiment modules can be invoked with `PYTHONPATH=src uv run python -m testing_scripts.run_roads_path_search_problems ucs`; their default input is `data/problems.csv`. The random-problem generator writes `run-results/problems.csv` without overwriting the supplied set. The experiment functions also accept explicit input/output paths.
