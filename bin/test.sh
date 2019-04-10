#!/usr/bin/env bash

pytest --cov=tv_extract --cov-report=term-missing --cov-fail-under=65 --durations=10 tests