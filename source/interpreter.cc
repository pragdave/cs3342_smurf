#include <string>
#include <functional>

#include "ast_node.h"
#include "interpreter.h"

using namespace std;

//return integer value
int Interpreter::evaluate_integer(AstNode *node, int value) {
	return value;
}

//return mathematic answer
int Interpreter::evaluate_binop(AstNode *node, AstNode *left, string op, AstNode *right) {
	int rval = right->accept(this);
	int lval = left->accept(this);
	int ans = eval_op[op](lval, rval);
	return ans;
}

//return variable value
int Interpreter::evaluate_varref(AstNode *node, string name) {
	AstNode* ans = bindings.get_variable_value(name);
	return ans->accept(this);
}

//set assignment and return value
int Interpreter::evaluate_assignment(AstNode* node, AstNode* left, string op, AstNode* right) {
	int value = right->accept(this);  
	string name = left->to_string();  
	bindings.set_variable(name, right);
	return value;
}

//evaluate if else statements based on blocks and conditionals
int Interpreter::evaluate_if_expr(AstNode *node, AstNode *left, AstNode *right, AstNode *el) {
	if (left->accept(this)) {
		return right->accept(this);
	} else if (el != nullptr) {
		return el->accept(this);
	}
	return 0;
};

//evaluate blocks of code
int Interpreter::evaluate_block(AstNode *node, vector<AstNode*> nodes) {
	int ret = 0;
	for (int i = 0; i < nodes.size(); i++) {
		ret = nodes[i]->accept(this);
	}
	return ret;
};

//return the value of evaluated function
int Interpreter::evaluate_funcall(AstNode *node, vector<string> names, vector<AstNode*> nodes, AstNode* block) {
	Binding b;
	if (names.size() != nodes.size()) {
		cout << "Err in parameters..." << endl;
		return -1;
	}
	for (int i = 0; i < names.size(); i++)  {
		int toSet = nodes[i]->accept(this);
		AstNode* toPass = new IntegerNode(toSet);
		b.set_variable(names[i], toPass);
	}
	b = b + bindings;
	Interpreter* forFunc = getInterpreter(b);
	return forFunc->evaluate_block(node, block->getCode());
};

//return the function node for called function
AstNode* Interpreter::find_func(string name) {
	AstNode* ans = bindings.get_variable_value(name);
	return ans;
};

//return binding, containing variables
Interpreter* Interpreter::getInterpreter(Binding& b) {
	Interpreter* ret = new Interpreter();
	ret->bindings = b;
	return ret;
}

//print and return passed in value
int Interpreter::evaluate_print(AstNode *node, vector<AstNode*> nodes) {
	int ret = 0;
	cout << "Print: ";
	for (int i = 0; i < nodes.size(); i++) {
		ret = nodes[i]->accept(this);
		cout << ret;
		if (i < nodes.size()-1)
			cout << "|";
	}
	cout << endl;
	return ret;
}
