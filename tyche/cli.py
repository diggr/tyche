#!/usr/bin/env python3
"""
tyche is a command line tool, which recursively checks a directory and all of its subdirectories of your research data for (proper) documentation and provenance.
"""
import click

from sys import exit
from .tyche import check_directory, create_report

@click.group()
def cli():
    pass

@cli.command()
@click.option("--no-provit", is_flag=True, default=False)
@click.option("--no-readme", is_flag=True, default=False)
@click.option("--non-recursive", is_flag=True, default=False)
@click.argument("directory", default=".")
def check(directory, no_provit, no_readme, non_recursive):
    if check_directory(directory, no_provit, no_readme, non_recursive):
        exit(0)
    else:
        exit(1)

@cli.command()
@click.option("--non-recursive", is_flag=True, default=False)
@click.argument("directory", default=".")
def report(directory, non_recursive):
    print(create_report(directory, non_recursive))
