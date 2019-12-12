#ifndef OPNODE
#define OPNODE
#include "astNode.h"
#include <string>
using namespace std;
class opNode : public astNode {
public:
	astNode *left;
	string op;
	astNode *right;
	opNode(astNode *left, string op, astNode *right) {
		this->left = left;
		this->op = op;
		this->right = right;
	}
	int accept(visitor* visitor) {
		return visitor->evaluateBinop(this, left, op, right);
	}
};
#endif OPNODE