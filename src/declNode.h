#ifndef DECL
#define DECL

#include "astNode.h"
class declNode : public astNode {
public:
	astNode* left;
	declNode(astNode* l) {
		this->left = l;
	}
	int accept(visitor* visitor) {
		//return visitor->evaluateDecl(this, left);
		return 0;
	}
};
#endif DECL