from project_paths import DATA_DIR, PROBLEMS_FILE, RUN_RESULTS_DIR
from testing_scripts.RandomSearchProblemGenerator import export_search_problems
from testing_scripts.run_roads_path_search_problems import read_search_problems_file
from ways.tools import dbopen


def test_default_inputs_resolve_outside_repository(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    with dbopen("israel.csv", "r") as source:
        assert source.readline().strip()
    with dbopen(DATA_DIR / "israel.csv", "r") as source:
        assert source.readline().strip()
    assert len(list(read_search_problems_file(problem_count=2))) == 2
    assert PROBLEMS_FILE.is_file()
    assert RUN_RESULTS_DIR != DATA_DIR


def test_export_accepts_explicit_separate_output(tmp_path):
    output = tmp_path / "generated" / "problems.csv"
    export_search_problems({(1, 2)}, str(output))
    assert output.read_text() == "1, 2"
