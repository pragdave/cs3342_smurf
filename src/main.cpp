#include <peglib.h>
#include <assert.h>
#include <iostream>
#include "astNode.h"
#include "customAST.h"
#include "Binding.h"
#include "Interpreter.h"
#include "visitor.h"
using namespace peg;
using namespace std;

int main(int argc, char* argv[]) {
	auto grammar = R"(
		program					<- code
		code					<- statement*
		statement				<- 'let' variable_declaration / assignment / expr
		variable_declaration	<- decl (',' decl)*
		decl					<- identifier ('=' expr)?
		identifier				<- < [a-z][a-zA-Z_0-9]* >
		variable_reference		<- identifier
		if_expression			<- expr brace_block ('else' brace_block )?
		assignment				<- identifier '=' expr
		expr					<- 'fn' function_definition / 'if' if_expression / boolean_expression / arithmetic_expression
		boolean_expression		<- arithmetic_expression relop arithmetic_expression
		arithmetic_expression	<- mult_term addop arithmetic_expression / mult_term
		mult_term				<- primary mulop mult_term / primary
		primary					<- integer / function_call / variable_reference / '(' arithmetic_expression ')'
		integer					<- < '-'?[0-9]+ >
		addop					<- '+' / '-'
		mulop					<- '*' / '/'
		relop					<- '==' / '!=' / '>=' / '>' / '<=' / '<'
		function_call			<- 'print' '(' call_arguments ')' / variable_reference '(' call_arguments ')'
		call_arguments			<- (expr (',' expr)*)?
		function_definition		<- param_list brace_block
		param_list				<- '(' identifier (',' identifier)* ')' / '(' ')'
		brace_block				<- '{' code '}'
		%whitespace				<- ([ \t\r\n])*
	)";
	parser parser(grammar);													//makes the parser
	parser.enable_ast();
	shared_ptr<Ast> ast;
	if (parser.parse(argv[1], ast)) {									//prints ast
		cout << peg::ast_to_s(ast) << endl;
	}
	else {
		cout << "parsing failed" << endl;
		cout << peg::ast_to_s(ast) << endl;
	}
	//heres the ast generation
	auto ptr = *ast;
	customAST cAST;
	cAST.makeAST(&ptr);
	visitor *interpreter = new Interpreter();
	interpreter->Binding = new Binding();
	map<string, int>list;
	interpreter->Binding->list.push_back(list);
	int val = cAST.root->accept(interpreter);
	return 0;
}