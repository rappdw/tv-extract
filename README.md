| Build | Test Coverage |
| ----- | ------------- |
| [![Build Status](https://travis-ci.com/rappdw/tv-extract.svg?branch=master)](https://travis-ci.org/rappdw/tv-extract) | [![Coverage Status](https://codecov.io/gh/rappdw/tv-extract/branch/master/graph/badge.svg)](https://codecov.io/gh/rappdw/tv-extract) |

# Team View - Extract (Data extraction for team analysis)
Extract team analysis data from git (current) 
and other relevant sources (future).

## Pre-requisites for Use

1. [Tokei](https://github.com/Aaronepower/tokei) (This [fork](https://github.com/rappdw/tokei/network) has initial, 
rudementary, support for Jupyter notebooks). Tokei is used to collect metrics on volume of source based per source 
language.

## Setup

A configuration file that defines the "project" for extract must be defined. The
configuration file is json.

**Example**:

```json
{
  "extracts": [
    {
      "name": "Project 1",
      "repos": [
        {
          "name": "TeamView",
          "remote": "git@github.com:rappdw/TeamViewer.git"
        },
        {
          "name": "team-view-extract",
          "remote": "git@github.com:rappdw/team-viewer-extract.git"
        }
      ],
      "start_date": "2018-07-18",
      "end_date": "2018-08-31"
    }
  ],
  "output_path": "~/.local/share/cache/TeamView",
  "mailmap_file": "~/.local/share/cache/.mailmap",
  "logging": 20
}
```

Multiple extracts can be defined in a singl configuration file. `start_date`, `end_date`, `mailmap_file` and `logging` 
are all optional. `logging` defaults to info level. `start_date` defaults to beginning of project. `end_date` defaults
to `today`. If no `mailmap_file` is specified, standard git configuration applies.

A good way to create the mailmap file is to construct based on `git shortlog -sne` for each repository.

## Results

For each extract specified in the configuration file, a sub-directory will be created in the directory spcified by 
`output_path`. The following files will be created:

* author_totals.csv - Commit counts by author and repository (excluding merge commits)
* loc.csv - File counts by language, commit and repository (commits to master branch only)
* loc_delta.csv - File Counts by author, language, commit and repository (excluding merge commits)
* prs.csv - Pull request by repo including duration between last commit to branch and merge to master
* repo.csv - Current state of volume of code by language for each repo
* revs.csv - Revision graph by repo

## 'Temporary' Files
`~/.local/share/cache` is used to cache temporary files including checkout of repos specified by extract and a cache of 
the LOC revision history of each repo. If present this cache is updated on subsequent runs. If not present it is 
recreated from scratch. 
