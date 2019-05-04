inkscape-cli-wrapper
====================
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-purple.svg)](https://github.com/SV3A/inkscape-cli-wrapper/blob/master/LICENSE)

This is an Inkscape cli wrapper made as a patch for the macOS bug, where one must specify absolute paths when invoking Inkscape commands (see [#1449251](https://bugs.launchpad.net/inkscape/+bug/1449251) and [#181639](https://bugs.launchpad.net/inkscape/+bug/181639)).
This script simply prepends to your relative path and calls the normal Inkscape binary with absolute paths.

### Usage
- Clone or download the script.
- Use the script as you would use the `$ inkscape` commandline utility, e.g.
```bash
   ./inkscape-wrapper -z -D --file={filename}.svg --export-pdf={filename}.pdf
```
#### Optionally
- Symlink the script with so that other programs, e.g. LaTeX packages, may use it.
```bash
ln -sf /path-to-script/inkscape-wrapper /usr/local/bin/inkscape
```

**Note** this command will overwrite any existing symbolic link.
However, this can be undone easily by relinking the `inkscape-bin` found in `/Applications/Inkscape.app/Contents/Resources/bin/`

