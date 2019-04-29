#!/usr/bin/env python3

# TODO:
# 1. Check the path where the program is run from
# 2. Find out how to execute command

import sys
import argparse
from pathlib import Path
import re

parser = argparse.ArgumentParser()

# Add commandline options
parser.add_argument("-z", action="store_true")
parser.add_argument("-D", action="store_true")
parser.add_argument("--file")
parser.add_argument("--export-pdf")
parser.add_argument("--export-latex", action="store_true")

args = parser.parse_args()

# Store home path
home = str(Path.home())

# String to be parsed as inkscape command
output_cmd = '/Applications/Inkscape.app/Contents/Resources/bin/inkscape-bin'


# Check for flags
if args.z:
    output_cmd += ' -z'

if args.D:
    output_cmd += ' -D'

if args.file:
    print(args.file)
    m = re.search(r'(?<=\/).*|\w*|(?<=\.).*', args.file)

    print(m.group(0))

    output_cmd += (' --file=' + home + '/' + args.file)

if args.export_latex:
    output_cmd += ' --export-latex'

# print(output_cmd)
# print(home)

