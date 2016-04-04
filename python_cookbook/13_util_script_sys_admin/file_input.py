#!/usr/bin/python3
import fileinput

with fileinput.input() as f_input:
    for l in f_input:
        print(l, end='')