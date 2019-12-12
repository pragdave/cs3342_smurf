#include "Interpreter.h"
#include <iostream>
using namespace std;
int Interpreter::evaluateProgram(astNode* node, astNode* code) {
	return code->accept(this);
}
int Interpreter::evaluateCode(astNode* node, vector<astNode*> statements) {
	int r;
	for (astNode* statement : statements) {
		r = statement->accept(this);
	}
	return r;
}
int Interpreter::evaluateDec(astNode* node, vector<astNode*> decs) {
	int r;
	for (astNode* dec : decs) {
		r = dec->accept(this);
	}
	return r;
}
int Interpreter::evaluateFnCall(astNode* node, astNode* name, vector<astNode*> args) {
	int dum = name->accept(this);
	string funcName = this->assignmentName;
	func* fn = this->Binding->getFunc(funcName);
	map<string, int> list;
	this->Binding->list.push_back(list);
	for (int i = 0; i < args.size(); i++) {
		int dum = fn->params[i]->accept(this);
		string varName = this->assignmentName;
		int val = args[i]->accept(this);
		this->Binding->add(varName, val);
	}
	for (auto var : fn->vars){
		string varName = var.first;
		int val = var.second;
		this->Binding->add(varName, val);
	}
	int r = fn->code->accept(this);
	this->Binding->list.pop_back(); //remove the top binding after function call
	return r;
}
int Interpreter::evaluateFnDef(astNode* node, vector<astNode*> params, astNode* code) {
	func f(params, code);
	for (auto i : this->Binding->list[this->Binding->list.size()-1]) {
		f.addVar(i.first, i.second);
	}//give the variables in the current binding to the function
	this->Binding->add(this->varName, &f);
	return 9999999;
}
int Interpreter::evaluateIf(astNode* node, astNode* condition, astNode* trueCode, astNode* falseCode) {
	int c = condition->accept(this);
	if (c == 1) {
		return trueCode->accept(this);
	}
	else if (falseCode != NULL) {
		return falseCode->accept(this);
	}
}
int Interpreter::evaluatePrint(astNode* node, vector<astNode*> args) {
	string out = "";
	for (astNode* arg : args) {
		out += to_string( arg->accept(this));
		out += "|";
	}
	out.pop_back();
	cout << out << endl;
	return 0;
}
int Interpreter::evaluateArgs(astNode* node, vector<astNode*> args) {
	//change this
	return args[0]->accept(this);
}
int Interpreter::evaluateInt(astNode* node, int value) {
	return value;
}
int Interpreter::evaluateBinop(astNode* node, astNode* left, string op, astNode* right){
	int lval = left->accept(this);
	int rval = right->accept(this);
	if (op == "+") {
		return lval + rval;
	}
	else if (op == "-") {
		return lval - rval;
	}
	else if (op == "*") {
		return lval * rval;
	}
	else if (op == "/") {
		return lval / rval;
	}
	else {
		return 99999;
	}
}
int Interpreter::evaluateRelop(astNode* node, astNode* left, string op, astNode* right) {
	auto lval = left->accept(this);
	int rval = right->accept(this);
	if (op == "==") {
		if (lval == rval) {
			return 1;
		}
	}
	else if (op == "!=") {
		if (lval != rval) {
			return 1;
		}
	}
	else if (op == ">=") {
		if (lval >= rval) {
			return 1;
		}
	}
	else if (op == ">") {
		if (lval > rval) {
			return 1;
		}
	}
	else if (op == "<=") {
		if (lval <= rval) {
			return 1;
		}
	}
	else if (op == "<") {
		if (lval < rval) {
			return 1;
		}
	}
	return 0;
}
int Interpreter::evaluateAssignment(astNode* node, astNode* left, astNode* right) {
	int dum = left->accept(this); //sets Assignment Name
	varName = assignmentName;
	int val = right->accept(this);
	if (val != 9999999)
		this->Binding->add(varName, val);
	return 0;
}
int Interpreter::evaluateIdentifier(astNode* node, string name) {
	this->assignmentName = name;
	return this->Binding->get(name);
}