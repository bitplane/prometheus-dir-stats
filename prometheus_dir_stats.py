#!/usr/bin/python
from __future__ import print_function

import argparse
import json
import os

def get_stats(d):

    total_files, total_dirs, total_bytes = 0, 0, 0

    for root, dirs, files in os.walk(d):
        total_files = total_files + len(files)
        total_dirs = total_dirs + len(dirs)
        total_bytes = total_bytes + sum(os.stat(os.path.join(root, f)).st_size for f in files)

    return {'total_files': total_files,
            'total_dirs': total_dirs,
            'total_bytes': total_bytes}

def process_dirs(dirs):
    for dir_name, path in dirs.items():
       stats = get_stats(path)
       for stat_name, value in stats.items():
           print("dir_{0}{{name='{1}', path='{2}'}} {3}".format(
               stat_name, dir_name, path, value))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config-file', help='Location of JSON config file',
        default='config.json')
    args = parser.parse_args()

    with open(args.config_file) as f:
        config = json.load(f)

    process_dirs(config)

if __name__ == '__main__':
    main()
