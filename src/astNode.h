#ifndef ASTNODE
#define ASTNODE
#include "visitor.h"
class visitor;
class astNode{
public:
	virtual int accept(visitor* visitor);
};
#endif ASTNODE