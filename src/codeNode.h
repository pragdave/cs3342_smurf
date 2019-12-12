#ifndef CODE
#define CODE
#include "astNode.h"
#include <vector>
using namespace std;
class codeNode : public astNode {
public:
	vector<astNode*> statements;
	codeNode(vector<astNode*> s) {
		this->statements = s;
	}
	int accept(visitor* visitor) {
		return visitor->evaluateCode(this, statements);
	}
};
#endif CODE