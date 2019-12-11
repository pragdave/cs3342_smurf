#pragma once

#include <string>
#include "visitor.h"
#include "varinode.h"
#include <vector>

class AstNode{
public:
    virtual std::string to_string() { return std::string("node"); };
    virtual varinode* accept(Visitor *visitor){
        varinode* temp;
        return temp;
    };
    virtual void update(std::string target, std::string newchange){return; };
};

//=============================  VarinodeNode  =====================================================

 class VarinodeNode : public AstNode{
     varinode* Vnode;

 public:
     VarinodeNode(varinode* given);
     std::string to_string();
     int to_value();
     varinode* accept(Visitor *visitor);
     void update(std::string target, std::string newchange);
 };

//=============================  BinopNodeNode  =====================================================

class BinopNode : public AstNode{
    AstNode *left;
    std::string op;
    AstNode *right;

public:
    void update(std::string target, std::string newchange);
    BinopNode(AstNode *pleft, std::string pop, AstNode *pright);
    std::string to_string();
    varinode* accept(Visitor *visitor);
};


class FuncNode : public AstNode{
    int* layer; 
    std::vector<std::vector<varinode*>>* List; 
    int size;
    AstNode *funcName;
    AstNode *funcParameter;
    AstNode *funcExecution;

public:
    FuncNode(AstNode *pfuncName, AstNode *pfuncParameter,  AstNode *pfuncExecution, std::vector<std::vector<varinode*>>* pList, int* player);
    FuncNode(AstNode *pfuncName, AstNode *pfuncParameter,  std::vector<std::vector<varinode*>>* pList, int* player);
    std::string to_string();
    varinode* accept(Visitor *visitor);
};


//=============================  IfNode  =====================================================

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

//=============================  OpNode  =====================================================

class OpNode : public AstNode
{
    std::string op;

public:
    OpNode(std::string pop);
    std::string to_string();
};
