
from sys import argv
import main

with open(argv[1]) as file:
  content = file.read()

main.runGrammar(content)