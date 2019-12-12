#ifndef FNCALL
#define FNCALL
#include "astNode.h"
#include "iostream"
#include <vector>
using namespace std;
class fnCallNode : public astNode {
public:
	astNode* reference;
	vector<astNode*> args;
	fnCallNode(astNode* r, vector<astNode*> a) {
		this->reference = r;
		this->args = a;
	}
	int accept(visitor* visitor) {
		return visitor->evaluateFnCall(this, reference, args);
	}
};
#endif FNCALL