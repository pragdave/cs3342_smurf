#ifndef DEC
#define DEC
#include "astNode.h"
#include <vector>
using namespace std;
class decNode : public astNode {
public:
	vector<astNode*> declarations;
	decNode(vector<astNode*> d) {
		this->declarations = d;
	}
	int accept(visitor* visitor) {
		return visitor->evaluateDec(this, declarations);
	}
};
#endif DEC