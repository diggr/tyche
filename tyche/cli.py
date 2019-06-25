#!/usr/bin/env python3
"""
tyche is a command line tool, which recursively checks a directory and all of its subdirectories of your research data for (proper) documentation and provenance.
"""
import click

from colorama import Fore, Back, Style, init
from pprint import pprint
from sys import exit
from .tyche import check_directory, create_report

FAIL_EMOJI = "💔"
SUCCESS_EMOJI = "💚"

@click.group()
def cli():
    init()
    pass


@cli.command()
@click.option("--no-provit", is_flag=True, default=False)
@click.option("--no-readme", is_flag=True, default=False)
@click.option("--non-recursive", is_flag=True, default=False)
@click.option("--quiet", is_flag=True, default=False)
@click.option("--omit-correct", is_flag=True, default=False)
@click.argument("directory", default=".")
def check(directory, no_provit, no_readme, non_recursive, quiet, omit_correct):
    success, checked_dirs = check_directory(
        directory, no_provit, no_readme, non_recursive
    )
    if not quiet:
        for dirname, check_results in checked_dirs.items():
            for name, result in check_results.items():
                if not result:
                    color = FAIL_EMOJI + " " + Fore.RED
                    break
                color = SUCCESS_EMOJI + " " + Fore.GREEN
            if omit_correct and color.startswith("✔️ "):
                continue
            print(color + dirname)

    if success:
        exit(0)
    else:
        exit(1)


@cli.command()
@click.option("--non-recursive", is_flag=True, default=False)
@click.argument("directory", default=".")
def report(directory, non_recursive):
    print(create_report(directory, non_recursive))
