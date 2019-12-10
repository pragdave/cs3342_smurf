#pragma once

#include <string>
#include "visitor.h"
#include "varinode.h"

class AstNode
{
public:
    virtual std::string to_string() { return std::string("node"); };
    virtual varinode* accept(Visitor *visitor){
        varinode* temp;
        return temp;
    };
};



// ////////////////////
// //  VarinodeNode

 class VarinodeNode : public AstNode{
     varinode* Vnode;

 public:
     VarinodeNode(varinode* given);
     std::string to_string();
     int to_value();
     varinode* accept(Visitor *visitor);
 };

////////////////////
//  BinopNode

class BinopNode : public AstNode{
    AstNode *left;
    std::string op;
    AstNode *right;

public:
    BinopNode(AstNode *pleft, std::string pop, AstNode *pright);
    std::string to_string();
    varinode* accept(Visitor *visitor);
};



class IfNode : public AstNode{
    int size;
    AstNode *ifstate;
    AstNode *condition;
    AstNode *elsestate;

public:
    IfNode(AstNode *pcond, AstNode * pif);
    IfNode(AstNode *pcond, AstNode * pif, AstNode *pelse);
    std::string to_string();
    varinode* accept(Visitor *visitor);
};

////////////////////
//  OpNode

class OpNode : public AstNode
{
    std::string op;

public:
    OpNode(std::string pop);
    std::string to_string();
    //varinode accept(Visitor *visitor);
};
