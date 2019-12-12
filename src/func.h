#ifndef FUNCH
#define FUNCH
#include <vector>
#include "astNode.h"
using namespace std;
class astNode;
class func { //helper class to be used with map in binding
public:
	int test;
	vector<astNode*> params;
	astNode* code;
	map<string, int> vars;
	func operator=(const func& f) {
		this->params = f.params;
		this->code = f.code;
		this->vars = f.vars;
		return *this;
	}
	func() {
	};
	func(const func& f) {
		this->params = f.params;
		this->code = f.code;
		this->vars = f.vars;
	};
	func(vector<astNode*> p, astNode* c) {
		this->params = p;
		this->code = c;
	};
	void addVar(string s, int v) {
		vars[s] = v;
	}
	
};
#endif