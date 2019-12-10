#pragma once

class AstNode;
class varinode;

class Visitor
{
public:
    virtual varinode* evaluate_varinode(AstNode *node, varinode* value) = 0;
    virtual varinode* evaluate_binop(AstNode *node, AstNode *left, std::string op, AstNode *right) = 0;
    virtual varinode* evaluate_ifnode(AstNode *node, AstNode *cond, AstNode *ifs, AstNode *elses, int size) = 0;
};