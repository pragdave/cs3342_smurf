#ifndef PRINT
#define PRINT
#include "astNode.h"
#include <vector>
using namespace std;
class printNode : public astNode {
public:
	vector<astNode*> args;
	printNode(vector<astNode*> a) {
		this->args = a;
	}
	int accept(visitor* visitor) {
		return visitor->evaluatePrint(this, args);
	}
};
#endif PRINT