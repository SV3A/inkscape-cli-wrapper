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

# String to be parsed as inkscape command
output_cmd = '/Applications/Inkscape.app/Contents/Resources/bin/inkscape'

parser = argparse.ArgumentParser(description=\
        'Absolute path wrapper for Inkscape.')

# Add commandline options that require file
parser.add_argument('--file', '-f')
parser.add_argument('--print', '-p')
parser.add_argument('--export-png', '-e')
parser.add_argument('--export-plain-svg', '-l')
parser.add_argument('--export-ps', '-P')
parser.add_argument('--export-eps', '-E')
parser.add_argument('--export-pdf', '-A')
parser.add_argument('--export-emf', '-M')
parser.add_argument('--export-wmf', '-m')

# Parse given args
args, unknown_args = parser.parse_known_args()

# Add flags
for flag in unknown_args:
    output_cmd += ' ' + flag

# Handle args with file input
for arg in args.__dict__:
    if args.__dict__[arg] is not None:

        # If relative build absolute path
        if os.path.isabs(args.__dict__[arg]):
            abs_path = args.__dict__[arg]
        else:
            abs_path = build_path(args.__dict__[arg])

        # Existing paths are checked
        if arg == 'file':
            path_check(abs_path)

        # Add command
        output_cmd += (' --' + arg + '=' + abs_path)

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

