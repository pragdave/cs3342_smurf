# Programming Languages: Final Project

## Name: Xuan(James) Zhai
## SMU ID: 47607746
## Class: CS3342

I use ".smu" files to test the code, but I do not know how to use the test_runner.py in the C++ code, so I manually import the test files and print out the solution to the screen. To test the code, put .smu files into "test_cases" and run the parser.exe. The printed solutions are AST expressions and answers if there are print-commands. Users have to manually compare the output results with the true answers. I think it is more close to Test-Based Grading than Feature-Based Grading.

The code passes all the test in file 00, 01, 02, and 10. For 20_fn_basic.smu, the code passes tests for functions which has no more than one parameter(passes the first and the second cases in that file). Users and change the file to retest the code, but basically 42(+2)/57 test cases are passed(there are two basic function tests in 22_closures.smu).

It is extremely difficult for me to use a built-in print function. I tried to use that, but when i tested "if 1 {  print(99)}else {print(100)}", the parser firstly identified all the expressions in the bottom of AST. Therefore, the output becomes
print(99)
print(100)
print(99)

Instead, I uses functions to reorganize those imputs, and store those new inputs in a string vector. Next, I loop through those strings and compile them in the parser. 

Better use GCC to compile