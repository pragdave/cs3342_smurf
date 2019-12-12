#ifndef ASSIGNMENT
#define ASSIGNMENT

#include "astNode.h"
class assignmentNode : public astNode {
public:
	astNode* left;
	astNode* right;
	assignmentNode(astNode* l, astNode* r) {
		this->left = l;
		this->right = r;
	}
	int accept(visitor* visitor) {
		return visitor->evaluateAssignment(this, left, right);
	}
};
#endif ASSIGNMENT