from sys import argv
import Syntax

with open(argv[1]) as file:
    content = file.read()

Syntax.runSmurf(content)