#ifndef INTEGER
#define INTEGER

#include "astNode.h"
class intNode : public astNode{
public:
	int value;
	intNode(int value) {	
		this->value = value;
	}
	int accept(visitor* visitor) {
		return visitor->evaluateInt(this, value);
	}
};
#endif INTEGER