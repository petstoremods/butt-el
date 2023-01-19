#!/usr/bin/python3

import argparse
import Plug
import time

parser = argparse.ArgumentParser(
    prog="butt"
)
parser.add_argument(
    "intensity"
)
parser.add_argument(
    "--duration"
)

args = parser.parse_args()

Plug.vibe(args.intensity)

if args.duration and int(args.duration) > 0:
    time.sleep(int(args.duration))
else:
    time.sleep(1)

Plug.stop()
