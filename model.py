#!/usr/bin/env python3

import sys
import modeller
from modeller.automodel import automodel


def main():
    if len(sys.argv) != 5:
        print("Usage: python model.py [alignment_file] [template_id] [target_id] [atom_files_directory]")
        sys.exit(1)

    alnfile = sys.argv[1]
    template = sys.argv[2]
    target = sys.argv[3]
    atom_dir = sys.argv[4]

    env = modeller.environ()
    env.io.atom_files_directory = [atom_dir]

    a = automodel(
        env,
        alnfile=alnfile,
        knowns=template,
        sequence=target
    )

    a.starting_model = 1
    a.ending_model = 1

    a.make()


if __name__ == "__main__":
    main()
