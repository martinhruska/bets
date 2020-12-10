#! /usr/bin/python3

import sys

print(('\n').join([','.join(x) for x in [l.split(',')[0:7] for l in [l for l in sys.stdin]]]))
