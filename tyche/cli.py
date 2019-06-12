#!/usr/bin/env python3
"""
tyche is a command line tool, which recursively checks a directory and all of its subdirectories of your research data for (proper) documentation and provenance.
"""

import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument("directory", default=".")
def check(directory):
    pass

@cli.command()
@click.argument("directory", default=".")
def report(directory):
    pass
