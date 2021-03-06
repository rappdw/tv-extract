import argparse
import datetime
import json
import logging
import sys

from pathlib import Path
from tv_extract.data import Config, Extract, Repo


def extract_config_from_json(config_data: dict) -> Config:
    if not "extracts" in config_data or not 'output_path' in config_data:
        raise ValueError("Invalid configuration file")
    
    extract_dicts = config_data['extracts']
    extracts = []
    
    for extract_dict in extract_dicts:
        repo_dicts = extract_dict['repos']
        repos = []
        adjustments = []
        tod_adjustments = []
        ignores = set()
        for repo_dict in repo_dicts:
            repos.append(Repo(repo_dict['name'], repo_dict['remote']))
        start_date = ''
        if 'start_date' in extract_dict:
            start_date = extract_dict['start_date']
            start_date = handle_delta_date(start_date)
        end_date = ''
        if 'end_date' in extract_dict:
            end_date = extract_dict['end_date']
            end_date = handle_delta_date(end_date)
        if 'adjustments' in extract_dict:
            for adjustment in extract_dict['adjustments']:
                adjustments.append(adjustment)
        if 'tod_adjustments' in extract_dict:
            for adjustment in extract_dict['tod_adjustments']:
                tod_adjustments.append((adjustment['dev'], adjustment['offset']))
        if 'ignore' in extract_dict:
            ignores = extract_dict['ignore']
        extracts.append(Extract(extract_dict['name'], repos, start_date, end_date, adjustments, tod_adjustments, ignores))

    output_path = config_data['output_path']
    log_level = config_data['logging'] if 'logging' in config_data else logging.INFO
    mailmap = None
    if 'mailmap_file' in config_data:
        mailmap = config_data['mailmap_file']
    return Config(extracts, output_path, mailmap, log_level)


def handle_delta_date(date_str):
    if date_str.startswith('delta:'):
        _, delta = date_str.split(':')
        delta = int(delta)
        date_str = (datetime.datetime.now() + datetime.timedelta(days=delta)).strftime('%Y-%m-%d')
    return date_str


def extract_config(config_file: Path) -> Config:
    if not config_file.exists():
        print(f"Error: {config_file} doesn't exist")
        sys.exit(-1)

    with open(config_file, 'r') as file:
        return extract_config_from_json(json.load(file))


def get_cli() -> Config:

    parser = argparse.ArgumentParser()
    parser.add_argument("config_file", help="configuration file (JSON format)")
    args = parser.parse_args()

    return extract_config(Path(args.config_file))


