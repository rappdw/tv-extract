#!/usr/bin/env bash

pytest --cov=tv_extract --cov-report=term-missing --cov-fail-under=75 --durations=10 tests