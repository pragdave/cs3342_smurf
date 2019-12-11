#pragma once
#include <vector>

class AstNode;
class varinode;

class Visitor
{
public:
    virtual varinode* evaluate_varinode(AstNode *node, varinode* value) = 0;
    virtual varinode* evaluate_binop(AstNode *node, AstNode *left, std::string op, AstNode *right) = 0;
    virtual varinode* evaluate_ifnode(AstNode *node, AstNode *cond, AstNode *ifs, AstNode *elses, int size) = 0;
    virtual varinode* evaluate_funcnode(AstNode *node, AstNode *name, AstNode *parameter, AstNode *execution, std::vector<std::vector<varinode*>>* pList, int* player, int size) = 0;
};