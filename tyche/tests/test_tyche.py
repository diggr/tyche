from ..tyche import ProvitChecker

TEST_FILENAME = "invalid_testfile"


def test_provit_checker_on_invalid_prov_file(tmp_path):
    tmp_path.joinpath(TEST_FILENAME).touch()
    with open(tmp_path.joinpath(f"{TEST_FILENAME}.prov"), "w") as prov_file:
        prov_file.write("{}")
    assert ProvitChecker.check_path(tmp_path) == False
