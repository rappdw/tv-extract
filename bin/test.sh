#!/usr/bin/env bash

pytest --color=yes --cov-config coverage.cfg --cov=tv_extract --cov-fail-under=35 --cov-report term-missing --durations=10 tests