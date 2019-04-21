#!/usr/bin/python
# -*- coding: utf-8 -*-

from scenario import Scenario
from greedySolver import GreedySolver

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    solver = GreedySolver(input_data)
    solver.solve()
    return solver.output_solution()

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

