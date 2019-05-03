#!/usr/bin/env python3
import os
import re
import datetime
import argparse
import subprocess

# Check if given path exists
def path_check(path):
    if os.path.exists(path):
        return path
    else:
        raise NameError('Path not found')

# Build absolute path
def build_path(path_input):
    # Strip path string from '.', '/' or './'
    path_strip = re.search('\w.*', path_input)

    if not path_strip:
        raise NameError('Invalid file')
    else:
        local_path = path_strip.group(0)

    # Build absolute path
    return os.getcwd() + '/' + local_path

parser = argparse.ArgumentParser()

# Add commandline options
parser.add_argument("-z", action="store_true")
parser.add_argument("-D", action="store_true")
parser.add_argument("--file")
parser.add_argument("--export-pdf")
parser.add_argument("--export-latex", action="store_true")

args = parser.parse_args()

# String to be parsed as inkscape command
output_cmd = '/Applications/Inkscape.app/Contents/Resources/bin/inkscape'

# Check for flags
if args.z:
    output_cmd += ' -z'

if args.D:
    output_cmd += ' -D'

# Handle file input
if args.file:
    abs_path = build_path(args.file)
    path_check(abs_path)
    output_cmd += (' --file=' + abs_path)

if args.export_pdf:
    abs_path = build_path(args.export_pdf)
    output_cmd += (' --export-pdf=' + abs_path)

# Check for flag
if args.export_latex:
    output_cmd += ' --export-latex'

print('Running a Inkscape wrapper')

# Write debug
log_file_path = '/Users/svea/Projects/ink-wrapper/inkwrap.log'
if os.path.exists(log_file_path):
    f = open(log_file_path, "a")
else:
    f = open(log_file_path, "w")

f.write(str(datetime.datetime.now()) + '\t' + output_cmd + '\n\n')
f.close()

# Execute command
p = subprocess.Popen(output_cmd, shell=True)

