#ifndef PROGRAM
#define PROGRAM

#include "astNode.h"
class programNode : public astNode {
public:
	astNode* code;
	programNode(astNode* c) {
		this->code = c;
	}
	int accept(visitor* visitor) {
		return visitor->evaluateProgram(this, code);
	}
};
#endif PROGRAM