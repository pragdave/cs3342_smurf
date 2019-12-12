#ifndef RELNODE
#define RELNODE
#include "astNode.h"
#include <string>
using namespace std;
class relNode : public astNode{
public:
	astNode* left;
	string op;
	astNode* right;
	relNode(astNode* left, string op, astNode* right) {
		this->left = left;
		this->op = op;
		this->right = right;
	}
	int accept(visitor* visitor) {
		return visitor->evaluateRelop(this, left, op, right);
	}

};
#endif RELNODE