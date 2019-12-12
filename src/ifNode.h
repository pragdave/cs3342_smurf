#ifndef IF
#define IF
#include "astNode.h"
#include <vector>
using namespace std;
class ifNode : public astNode {
public:
	astNode* condition;
	astNode* trueCode;
	astNode* falseCode;
	ifNode(astNode* c, astNode* t, astNode* f) {
		this->condition = c;
		this->trueCode = t;
		this->falseCode = f;
	}
	int accept(visitor* visitor) {
		return visitor->evaluateIf(this, condition, trueCode, falseCode);
	}
};
#endif IF