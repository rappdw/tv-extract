#!/usr/bin/env bash

pytest --cov=tv_extract --cov-report=term-missing --cov-fail-under=70 --durations=10 tests