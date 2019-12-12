#ifndef ARGS
#define ARGS
#include "astNode.h"
#include <vector>
using namespace std;
class argsNode : public astNode {
public:
	vector<astNode*> args;
	argsNode(vector<astNode*> a) {
		this->args = a;
	};
	int accept(visitor* visitor) {
		return visitor->evaluateArgs(this, args);
	};
};
#endif ARGS