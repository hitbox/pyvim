#!/usr/bin/env python
from __future__ import unicode_literals
import argparse
import os

from pyvim.editor import Editor
from pyvim.rc_file import run_rc_file

__all__ = (
    'run',
)


def run():
    """
    pyvim: Pure Python Vim clone.
    """
    parser = argparse.ArgumentParser(description=run.__doc__)
    parser.add_argument('locations', nargs='*')
    parser.add_argument('-p', action='store_true', dest='in_tab_pages', help='Open files in tab pages.')
    parser.add_argument('-o', action='store_true', dest='hsplit', help='Split horizontally.')
    parser.add_argument('-O', action='store_true', dest='vsplit', help='Split vertically.')
    parser.add_argument('-u', metavar='pyvimrc', dest='pyvimrc', help='User this .pyvimrc file instead.')

    args = parser.parse_args()

    # Create new editor instance.
    editor = Editor()

    # Apply rc file.
    if args.pyvimrc:
        run_rc_file(editor, args.pyvimrc)
    else:
        default_pyvimrc = os.path.expanduser('~/.pyvimrc')

        if os.path.exists(default_pyvimrc):
            run_rc_file(editor, default_pyvimrc)

    # Load files and run.
    editor.load_initial_files(args.locations, in_tab_pages=args.in_tab_pages,
                              hsplit=args.hsplit, vsplit=args.vsplit)
    editor.run()


if __name__ == '__main__':
    run()
