#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
cd ..

if [ -z "$VIRTUAL_ENV" ]; then
    . activate
fi

if [ -e "./dist" ]; then
    rm -rf dist
fi

python setup.py bdist_wheel -d dist
twine upload -r pypi dist/*
