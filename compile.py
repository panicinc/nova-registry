#!/usr/bin/env python3
import datetime
import json
from pathlib import Path
import tomllib

if __name__ == '__main__':
    root = {
        'date': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
        'packages': [],
        'language_servers': [],
    }

    basedir = Path.cwd()

    for child in basedir.joinpath("Definitions/Packages").iterdir():
        if child.suffix == ".toml":
            with child.open(mode='rb') as f:
                root['packages'].append(tomllib.load(f))

    for child in basedir.joinpath("Definitions/LanguageServers").iterdir():
        if child.suffix == ".toml":
            with child.open(mode='rb') as f:
                root['language_servers'].append(tomllib.load(f))

    with basedir.joinpath("registry.json").open(mode='w') as f:
        json.dump(root, f)
