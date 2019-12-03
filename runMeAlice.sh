#!/bin/bash
cd 'source'
g++ -I '../peglib' -o parser *.cc
cd '../test_cases'
python3 '../test_runner.py' '../source/parser'
