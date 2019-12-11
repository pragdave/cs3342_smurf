#pragma once
#include <map>
#include <string>

#include "visitor.h"
#include <vector>
#include "varinode.h"

class Interpreter : public Visitor{

public:
    Interpreter();
    varinode* evaluate_varinode(AstNode *node, varinode* value);
    varinode* evaluate_binop(AstNode *node, AstNode *left, std::string op, AstNode *right);
    varinode* evaluate_ifnode(AstNode *node, AstNode *cond, AstNode * ifs, AstNode *elses, int size);
    varinode* evaluate_funcnode(AstNode *node, AstNode *name, AstNode *parameter, AstNode *execution, std::vector<std::vector<varinode*>>* pList, int* player, int size);
};
