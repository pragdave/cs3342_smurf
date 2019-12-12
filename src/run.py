from sys import argv
import Syntax

with open(argv[1]) as file:
    content = file.read()

# use command "python test_runner.py "python <path to this file>" to run"
# currently the test files appends "test_cases/" to find the folder of the smu files
Syntax.runSmurf(content)