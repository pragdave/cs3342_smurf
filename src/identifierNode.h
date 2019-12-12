#ifndef IDENTIFIER
#define IDENTIFIER

#include "astNode.h"
class identifierNode : public astNode {
public:
	string name;
	identifierNode(string n) {
		this->name = n;
	}
	int accept(visitor* visitor) {
		return visitor->evaluateIdentifier(this, name);;
	}
};
#endif IDENTIFIER