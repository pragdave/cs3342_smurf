#pragma once

class AstNode;

using namespace std;

//create virtual functions for visitor
class Visitor {
public:
	virtual int evaluate_integer(AstNode *node, int value) 
		{ return 0;};
	virtual int evaluate_binop(AstNode *node, AstNode *left, string op, AstNode *right) 
		{ return 0; };
	virtual int evaluate_varref(AstNode *node, string name) 
		{ return 0; };
	virtual int evaluate_assignment(AstNode *node, AstNode *left, string op, AstNode *right)
		{ return 0; };     
	virtual int evaluate_if_expr(AstNode *node, AstNode *left, AstNode *right, AstNode *el) 
		{ return 0; };
	virtual int evaluate_block(AstNode *node, vector<AstNode*> nodes)
		{ return 0; };
	virtual int evaluate_funcall(AstNode *node, vector<string> names, vector<AstNode*> nodes, AstNode* block)
		{ return 0; };
	virtual AstNode* find_func(string name)
		{ return 0; };
	virtual int evaluate_print(AstNode* node, vector<AstNode*> nodes)
		{ return 0; };
};
