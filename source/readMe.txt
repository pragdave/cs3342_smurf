11/20/2019 6:47
	Working:
		- Ints
		- Comparisons
		- Expressions w/ints and no parans
		- Variablereference
			- half works with variables
			- not functions
			- math only works when last
	Fix: 
		- Equations with Parans
		- Equations with variables not last
		- Assignment in general

11/21/2019 4:31
	Working:
		- Ints
		- Comparisons
		- Int math and expressions
		- variablereference (not function calls)
		- assignment not to math but single digit
		- variable declaration without math
	Fix:
		- assignment and decl with math
		- print more than one code statement results
	Start/Issues:
		- if/else
		- block

11/23/2019 8:33
	Working:
		- Ints
		- Comparisons
		- variablereference (not function calls)
		- assignments (not function calls)
		- variable declaration
		- more than one code statement result (not in blocks)
		- if/else with one statement in blocks
	Fix:
		- Block codes
	Start/Issues:
		- Functions

11/24/2019 6:21
	Working:
		- Ints
		- Comparisons
		- variablereference (not function calls)
		- assignments (not function calls)
		- variable declaration
		- more than one code statement result
		- if/else
	Fix:
		- Printing w/ if/else prints statement twice
	Start/Issues:
		- Functions


11/25/2019 9:27
	Working:
		- Ints
		- Comparisons
		- variablereference
		- assignments
		- variable declaration
		- more than one code statement result
		- if/else
	Fix:
		- Math where var equals itself with math
		- Function using param values
		- Function with empty param list
		- Double printing at times
	Start/Issues
		- Segfault with functions involving variables passed in
		- Segfault with functions involving no params

11/26/2019 10:16
	Working:
		- Ints
		- Comparisons
		- variablereference
		- assignments
		- variable declaration
		- more than one code statement result
		- if/else
		- functions
	Fix:
		- Math with var = var + whatever
	Start/Issues:
		- Running testing script
			- a = a + b b = b-a print(a) print(b)
				seg fault
			- let c = a **a = b** b = c print(a) print(b)
				seg fault
			- let e = 99, f = 100, **g = e+f** print(e,f,g)
				syntax error
			- TEST ON MULTIPLE LINES
				must fix spacing in grammar though
			- Recurssion in functions
				seg fault
			- closures
				vars out of scope
			- fib
				same recurssion issue

11/26/2019 2:46
	Working:
		- Ints
		- Comparisons
		- variablereference
		- assignments
		- variable declaration
		- more than one code statement result
		- if/else
		- functions
		- Tests that run
			- ALL 00_expr.smu
			- 01_variables.smu
				print(b-a)
				print(a-1)
				print(2+b/a)
				print(b)
			- ALL 02_let.smu
			- ALL 10_if.smu
			- ALL 20_fn_basics.smu
			- ALL 21_recursive_fns.smu
			- 22_closures.smu
				print(f(1))
				print(f(1)) pt2
			- ALL 99_fib.smu
	Fix:
		- Math with var = var + whatever
		- Comments
	Start/Issues:
		- Tests that don't run
			- 01_variables.smu
				a = a + b print(a)
				b = b-a print(b)
				let c = a a = b b = c print(a) print(b)
			- 22_closures.smu
				print(add_2(2))
				print(add_3(10))
				print(add_3(2))
				print(add_2(10))




