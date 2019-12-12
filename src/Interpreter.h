#ifndef INTERPRETER
#define INTERPRETER
#include "visitor.h"
class Interpreter: public visitor{
public:
	int evaluateProgram(astNode* node, astNode* code);
	int evaluateCode(astNode* node, vector<astNode*> statements); 
	int evaluateFnCall(astNode* node, astNode* name, vector<astNode*> args);
	int evaluateFnDef(astNode* node, vector<astNode*> params, astNode* code);
	int evaluateDec(astNode*, vector<astNode*> decs);
	int evaluatePrint(astNode* node, vector<astNode*> args);
	int evaluateArgs(astNode* node, vector<astNode*> statements);
	int evaluateIf(astNode* node, astNode* condition, astNode* trueCode, astNode* falseCode);
	int evaluateInt(astNode* node, int value);
	int evaluateRelop(astNode* node, astNode* left, string op, astNode* right);
	int evaluateBinop(astNode* node, astNode* left, string op, astNode* right);
	int evaluateAssignment(astNode* node, astNode* left, astNode* right);
	int evaluateIdentifier(astNode*, string name);
};
#endif INTERPRETER