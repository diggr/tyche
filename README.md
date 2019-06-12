# tyche

![tyche logo](assets/tyche.png?raw=true "tyche")

*tyche* is a command line tool, which recursively checks a directory and all
of its subdirectories of your research data for (proper) documentation and 
provenance. 

## Motivation

If you do not have a central research data infrastructure, i.e. a place to 
store all your files, which pile up during your research, you will probably
fall back to a simple file based storage. 

In order to help your future self or colleagues, this tool allows you to 
check your data folder, and shows you all directories which are missing a 
README (or whatever documentation file you require). 

Furthermore it can check, that all files are adjoined with provenance 
information. 

## Installation

Install the latest version from github:
```zsh
$ pip install git+https://github.com/diggr/tyche
```

## Usage

Check current directory, including all subdirectories:
```zsh
$ tyche check
```

Check specific directory:
```zsh
$ tyche check 
```

Exclude provit/provenance checks
```zsh
$ tyche --no-provit check DIRECTORY
```

Exclude README checks:
```zsh
$ tyche --no-readme check DIRECTORY
```

Just check the current directory, i.e. exclude subfolders:
```zsh
$ tyche --non-recursive check DIRECTORY
```

## Copyright

2019, Universitätsbibliothek Leipzig <info@ub.uni-leipzig.de>

## Author

F. Rämisch <raemisch@ub.uni-leipzig.de>


