#pragma once
#include <map>
#include <string>

#include "visitor.h"
#include <vector>
#include "varinode.h"

class Interpreter : public Visitor
{
    int layer;
    std::vector<std::vector<varinode*>> listPointer;

public:
    Interpreter();
    //Interpreter(std::vector<std::vector<varinode*>>&, int&);
    void increasenode();
    varinode* evaluate_varinode(AstNode *node, varinode* value);
    varinode* evaluate_binop(AstNode *node, AstNode *left, std::string op, AstNode *right);
    varinode* evaluate_ifnode(AstNode *node, AstNode *cond, AstNode * ifs, AstNode *elses, int size);
};
