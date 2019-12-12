#ifndef FNDEF
#define FNDEF
#include "astNode.h"
#include <vector>
using namespace std;
class fnDefNode : public astNode {
public:
	vector<astNode*> params;
	astNode* code;
	fnDefNode(vector<astNode*> p, astNode* c) {
		this->params = p;
		this->code = c;
	}
	int accept(visitor* visitor) {
		return visitor->evaluateFnDef(this, params, code);
	}
};
#endif FNDEF