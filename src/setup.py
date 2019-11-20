
from sys import argv
import main

with open(argv[1]) as file:
  print("YES")
  content = file.read()

main.runGrammar(content)