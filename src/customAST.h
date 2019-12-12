#ifndef AST
#define AST
#include <peglib.h>
#include "astNode.h"
#include "programNode.h"
#include "codeNode.h"
#include "declNode.h"
#include "decNode.h"
#include "intNode.h"
#include "relNode.h"
#include "opNode.h"
#include "argsNode.h"
#include "fnDefNode.h"
#include "fnCallNode.h"
#include "ifNode.h"
#include "printNode.h"
#include "assignmentNode.h"
#include "identifierNode.h"
#include "Binding.h"
using namespace std;
using namespace peg;
class customAST{
public:
	astNode *root;

	void makeAST(Ast* ast) {
		this->root = makeAST(ast, root);
	};

	astNode* makeAST(Ast* ast, astNode *curr) {
		string name = ast->name;
		if (name == "integer") {
			curr = new intNode(atoi(&(ast->token[0])));
			return curr;
		}
		else if (name == "primary") {
			curr = makeAST(&(*(ast->nodes[0])), curr);
			return curr;
		}
		else if (name == "function_definition") {
			vector<astNode*> args;
			int argCount = (*(ast->nodes[0])).nodes.size();
			for (int i = 0; i < argCount; i++) {
				Ast in = (*(ast->nodes[0]));
				args.push_back(makeAST(&(*(in.nodes[i])), curr));
			}
			astNode* code = makeAST(&(*(ast->nodes[1])), curr);
			curr = new fnDefNode(args, code);
			return curr;
		}
		else if (name == "if_expression") {
			astNode* condition = makeAST(&(*(ast->nodes[0])), curr);
			astNode* trueCode = makeAST(&(*(ast->nodes[1])), curr);
			astNode* falseCode = NULL;
			if (ast->nodes.size() == 3) {//has an else statement
				falseCode = makeAST(&(*(ast->nodes[2])), curr);
			}
			curr = new ifNode(condition, trueCode, falseCode);
			return curr;
		}
		else if (name == "brace_block") {
			curr = makeAST(&(*(ast->nodes[0])), curr);
			return curr;
		}
		else if (name == "function_call") {
			vector<astNode*> args;
			if (ast->nodes.size() == 1) {//print
				int argCount = (*(ast->nodes[0])).nodes.size();
				for (int i = 0; i < argCount; i++) {
					Ast in = (*(ast->nodes[0]));
					args.push_back(makeAST(&(*(in.nodes[i])), curr));
				}
				curr = new printNode(args);
			}
			else {//variable
				astNode* reference = makeAST(&(*(ast->nodes[0])), curr);
				int argCount = (*(ast->nodes[1])).nodes.size();
				for (int i = 0; i < argCount; i++) {
					Ast in = (*(ast->nodes[1]));
					args.push_back(makeAST(&(*(in.nodes[i])), curr));
				}
				curr = new fnCallNode(reference, args);
			}
			return curr;
		}
		else if (name == "call_arguments") {
			int argCount = ast->nodes.size();
			vector<astNode*> args;
			for (int i = 0; i < argCount; i++) {
				args.push_back(makeAST(&(*(ast->nodes[i])), curr));
			}
			curr = new argsNode(args);//fix this later
			return curr;
		}
		else if (name == "mult_term") {//primary mulop mult_term / primary
			if (ast->nodes.size() == 3) {
				astNode* left = makeAST(&(*(ast->nodes[0])), curr);
				astNode* right = makeAST(&(*(ast->nodes[2])), curr);
				curr = new opNode(left, (*(ast->nodes[1])).token, right);
			}
			else {// primary
				curr = makeAST(&(*(ast->nodes[0])), curr);
			}
			return curr;
		}
		else if (name == "arithmetic_expression") { //mult_term addop arithmetic_expression 
			if (ast->nodes.size() == 3) { 
				astNode* left = makeAST(&(*(ast->nodes[0])), curr);
				astNode* right = makeAST(&(*(ast->nodes[2])), curr);
				curr = new opNode(left, (*(ast->nodes[1])).token, right);
			}
			else {// mult_term
				curr = makeAST(&(*(ast->nodes[0])), curr);
			}
			return curr;
		}
		else if (name == "boolean_expression") {
			astNode* left = makeAST(&(*(ast->nodes[0])), curr);
			astNode* right = makeAST(&(*(ast->nodes[2])), curr);
			astNode* temp = new relNode(left, (*(ast->nodes[1])).token, right);
			curr = temp;
			return curr;
		}
		else if (name == "assignment") {
			astNode* left = makeAST(&(*(ast->nodes[0])), curr);
			astNode* right = makeAST(&(*(ast->nodes[1])), curr);
			curr = new assignmentNode(left, right);
			return curr;
		}
		else if (name == "identifier") {
			string name(&(ast->token[0]));
			curr = new identifierNode(name);
			return curr;
		}
		else if (name == "program") {
			astNode* code = makeAST(&(*(ast->nodes[0])), curr);
			curr = new programNode(code);
			return curr;
		}
		else if (name == "code") {
			int statementCount = ast->nodes.size();
			vector<astNode*> statements;
			for (int i = 0; i < statementCount; i++) {
				statements.push_back(makeAST(&(*(ast->nodes[i])), curr));
			}
			curr = new codeNode(statements);
			return curr;
		}
		else if (name == "statement") {
			curr = makeAST(&(*(ast->nodes[0])), curr);
			return curr;
		}
		else if (name == "expr") {
			curr = makeAST(&(*(ast->nodes[0])), curr);
			return curr;
		}
		else if (name == "variable_declaration") {
			int decCount = ast->nodes.size();
			vector<astNode*> declarations;
			for (int i = 0; i < decCount; i++) {
				declarations.push_back(makeAST(&(*(ast->nodes[i])), curr));
			}
			curr = new decNode(declarations);
			return curr;
		}
		else if (name == "variable_reference") {
			curr = makeAST(&(*(ast->nodes[0])), curr);
			return curr;
		}
		else if (name == "decl") {
			if (ast->nodes.size() == 2) {//identifier = expr
				astNode* left = makeAST(&(*(ast->nodes[0])), curr);
				astNode* right = makeAST(&(*(ast->nodes[1])), curr);
				curr = new assignmentNode(left, right);
			}
			else {
				astNode* left = makeAST(&(*(ast->nodes[0])), curr);
				curr = new declNode(left);
			}
			return curr;
		}
		return this->root;
	};
};
#endif AST

