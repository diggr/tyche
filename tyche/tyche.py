import json
import sys
import os

from collections import defaultdict
from pathlib import Path
from provit import Provenance

class ReadmeChecker:
    
    id_string = "readme"
    glob_string = "README*"

    @staticmethod
    def check_path(directory):
        for rf in directory.glob(ReadmeChecker.glob_string):
            if rf.is_file() and rf.stat().st_size:
                return True
        return False

class ProvitChecker:
    
    id_string = "provit"
    glob_string = "*.prov"

    @staticmethod
    def check_path(directory):
        all_files = [ f for f in directory.glob("*") if f.is_file() ]
        exclude_files = [ f for f in directory.glob(ReadmeChecker.glob_string) ]
        prov_files = [ f for f in directory.glob(ProvitChecker.glob_string) if f.is_file() ]
        data_files = [ f for f in all_files if f not in prov_files and f not in exclude_files ]  
        for df in data_files:
            if directory.joinpath("{}.prov".format(df.parts[-1])).is_file():
                prov = Provenance(df)
                if not prov.tree():
                    return False
            else:
                return False
        return True

def check_directory(directory, no_provit, no_readme, non_recursive):
    checker_list = []
    if not no_provit:
        checker_list.append(ProvitChecker)
    if not no_readme:
        checker_list.append(ReadmeChecker)
    c = Checker(directory, checker_list, not non_recursive)
    c.run_checks()
    return c.success
    

def create_report(directory, non_recursive):
    c = Checker(directory, [ProvitChecker, ReadmeChecker], not non_recursive)
    c.run_checks()
    return json.dumps(c.checked_dirs)


class Checker:

    def __init__(self, directory, checker_list, recursive):
        self.directory = Path(directory)
        self.checker_list = checker_list
        self.recursive = recursive
        self.checked_dirs = defaultdict(dict)
        self.success = False

    def run_checks(self):
        encountered_errors = False
        for directory in self.walk(self.directory):
            for c in self.checker_list:
                result = c.check_path(directory)
                self.checked_dirs[str(directory)][c.id_string] = result
                if not result:
                    encountered_errors = True
        if not encountered_errors:
            self.success = True

    def walk(self, directory):
        for d in directory.glob("*"):
            if d.is_dir() and self.recursive:
                yield from self.walk(d)
        yield directory
