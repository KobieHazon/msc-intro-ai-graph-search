# Graph Search on an Israel Road Network

A CS MSc Introduction to Artificial Intelligence exercise implementing uniform-cost search, A*, and iterative-deepening A* over a supplied road graph. The project includes route-finding adapters, heuristic and path-cost calculations, experiment scripts, recorded runs, and rendered route examples.

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
uv run python main.py ucs 0 100
uv run python main.py astar 0 100
uv run python main.py idastar 0 100
```

The full map takes several seconds to load. IDA* in the assignment's required tree-search mode can take substantially longer on difficult routes.

Run the focused algorithm tests with:

```bash
uv run pytest
```

## Repository Provenance

The `ways` package, map data, and original framework README were supplied for the exercise. `helper_types/Node.py`, `helper_types/PriorityQueue.py`, and `utils/misc.py` identify themselves in the recovered source as originating from the course repository. The graph-search implementations, road-specific adapters, experiment scripts, analysis outputs, and `report.pdf` are the submitted work. The report retains the author's name while removing submission identifiers and contact information.
