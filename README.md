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

## Quickstart

A directory can be checked, by simply calling *tyche check*. If no directory
is supplied, the current working directory will be checked. 

```zsh
$ tyche check [DIRECTORY]
```

Directories which passed the checks will be displayed in green, failed 
directories will be displayed in red. If at least one subdirectory failed
one check, the return code of tyche check will be *1*, else *0*.

To show all possible commands and options invoke:

```zsh
$ tyche --help
```

## Check Command

To disable checks, simply exclude via the command line option, e.g. to diable 
provenance checks enter: 

```zsh
$ tyche --no-provit check [DIRECTORY]
```

Option | Result
------ | ------
*--no-provit* | Disable the check for provenance files.
*--no-readme* | Disable the check for README files.

There are some options to tweak the output:

Option | Result
------ | ------
*--quiet* | No output at all. 
*--omit-correct* | Correct / Passing directories will not be displayed.
*--non-recursive* | Subdirectories of the given directory are omitted. 

## Report Command

The report command will return a json dict, with specific information
about all directories and the checks they passed or failed. 

```zsh
$ tyche report [DIRECTORY]
```

You can directly pipe the result into a json processor, e.g. *json\_pp* to 
disply it.

```zsh
tyche report /media/v/Diggr/_ARCHIV | json_pp
```

This will result in this output:

```json
{
   "/media/v/Diggr/_ARCHIV/Datenquellen/UB-Spielesammlung/2016-04" : {
      "readme" : false,
      "provit" : false
   },
   "/media/v/Diggr/_ARCHIV/Datenquellen/VGChartz" : {
      "provit" : true,
      "readme" : true
   }
}
```

## Copyright

2019, Universitätsbibliothek Leipzig <info@ub.uni-leipzig.de>

## Author

F. Rämisch <raemisch@ub.uni-leipzig.de>


