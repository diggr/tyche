import json
import pytest

from click.testing import CliRunner
from pathlib import Path
from provit import Provenance

from ..cli import cli


TEST_DIRECTORY_STRUCTURE = {
    "data": {
        "data_1": None,
        "data_2": {"data_2_1": None, "data_2_2": {"data_2_2_1": None}},
        "data_3": None,
        "data_4": {"data_4_1": None},
    }
}


def walk_path_dict(node, this_path):
    """
    Iterates through the nested dict of paths.
    A key either has 
    """
    for key, value in node.items():
        new_path = this_path / key
        if isinstance(value, dict):
            yield new_path
            yield from walk_path_dict(value, new_path)
        else:
            yield new_path


@pytest.fixture(
    autouse=True,
    params=[
        {"readme": False, "provit": False, "skip": [], "id": 0},
        {"readme": True, "provit": False, "skip": [], "id": 1},
        {"readme": False, "provit": True, "skip": [], "id": 2},
        {"readme": True, "provit": True, "skip": ["data_4_1"], "id": 3},
        {"readme": True, "provit": True, "skip": [], "id": 4},
    ],
)
def data_dir(tmp_path_factory, request):
    base_path = tmp_path_factory.mktemp("correct").resolve()
    for sub_path in walk_path_dict(TEST_DIRECTORY_STRUCTURE, base_path):
        sub_path.mkdir()
        dirname = sub_path.parts[-1]

        data_file = sub_path / "{}.json".format(dirname)
        with open(data_file, "w") as df:
            json.dump(list(sub_path.parts), df)

        if request.param["readme"] and dirname not in request.param["skip"]:
            readme = sub_path / "README.md"
            with open(readme, "w") as rf:
                rf.write("This is the documentation of {}\n".format(sub_path))

        if request.param["provit"] and dirname not in request.param["skip"]:
            prov = Provenance(data_file)
            prov.save()

    return base_path, request.param


@pytest.mark.parametrize(
    "args, expected_exit_codes",
    [
        (["check"], [1, 1, 1, 1, 0]),
        (["check", "--non-recursive"], [1, 1, 1, 0, 0]),
        (["check", "--no-provit"], [1, 0, 1, 1, 0]),
        (["check", "--no-provit", "--non-recursive"], [1, 0, 1, 0, 0]),
        (["check", "--no-readme"], [1, 1, 0, 1, 0]),
        (["check", "--no-readme", "--non-recursive"], [1, 1, 0, 0, 0]),
    ],
)
def test_check(data_dir, args, expected_exit_codes):
    base_path, params = data_dir
    runner = CliRunner()
    result = runner.invoke(cli, args + [str(base_path)])
    assert result.exit_code == expected_exit_codes[params["id"]]

@pytest.mark.parametrize(
    "args, expected_exit_codes",
    [
        (["report"], [0, 0, 0, 0, 0]),
        (["report", "--non-recursive"], [0, 0, 0, 0, 0]),
    ],
)
def test_report(data_dir, args, expected_exit_codes):
    base_path, params = data_dir
    runner = CliRunner()
    result = runner.invoke(cli, args + [str(base_path)])
    assert result.exit_code == expected_exit_codes[params["id"]]
#    assert isinstance(json.loads(result.output), dict)
