#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void

f = Void()
try:
    while True:
        f = f.add(R2Point())
        s = f.area()
        p = f.perimeter()
        pi = f.inside_perimeter()
        print(f"S = {s}, P = {p}, P_I = {pi}")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
