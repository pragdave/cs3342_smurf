#ifndef VISITOR
#define VISITOR
#include <string>
#include "astNode.h"
#include "Binding.h"
#include <vector>
using namespace std;
class astNode;
class Binding;
class visitor{
public:
	Binding* Binding;
	string assignmentName; //these strings are for passing info where returning an int was insuficcient 
	string varName;
	virtual int evaluateProgram(astNode* node, astNode* code) { return 0; };
	virtual int evaluateCode(astNode* node, vector<astNode*> statements) { return 0; };
	virtual int evaluateDec(astNode*, vector<astNode*> decs) { return 0; };
	virtual int evaluateFnCall(astNode* node, astNode* name, vector<astNode*> args) { return 0; };
	virtual int evaluateFnDef(astNode* node, vector<astNode*> params, astNode* code) { return 0; };
	virtual int evaluatePrint(astNode* node, vector<astNode*> args) { return 0; };
	virtual int evaluateArgs(astNode* node, vector<astNode*> statements) { return 0; };
	virtual int evaluateIf(astNode* node, astNode* condition, astNode* trueCode, astNode* falseCode) { return 0; };
	virtual int evaluateInt(astNode *node, int value) { return 0; };
	virtual int evaluateRelop(astNode* node, astNode *left, string op, astNode *right) { return 0; };
	virtual int evaluateBinop(astNode* node, astNode* left, string op, astNode* right) { return 0; };
	virtual int evaluateAssignment(astNode* node, astNode* left, astNode* right) { return 0; };
	virtual int evaluateIdentifier(astNode*, string name) { return 0; };
};
#endif VISITOR