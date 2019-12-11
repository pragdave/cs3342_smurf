#include "ast_node.h"


 VarinodeNode::VarinodeNode(varinode* given){
   Vnode = given;
 }

 std::string VarinodeNode::to_string(){
   return Vnode->GetName();
 }


 int VarinodeNode::to_value(){
   return Vnode->GetValue();
 }


 varinode* VarinodeNode::accept(Visitor *visitor){
   return visitor->evaluate_varinode(this, Vnode);
 }

void VarinodeNode::update(std::string target, std::string newchange){
    varinode* nnode = new varinode(newchange);
    if(Vnode->GetName() == target){
       Vnode = nnode;
       return;
    }
    return;
}


BinopNode::BinopNode(AstNode *pleft, std::string pop, AstNode *pright)
{
  left = pleft;
  op = pop;
  right = pright;
}

varinode* BinopNode::accept(Visitor *visitor){
  return visitor->evaluate_binop(this, left, op, right);
}

std::string BinopNode::to_string(){
  return "(" + op + " " + left->to_string() + " " + right->to_string() + ")";
}


void BinopNode::update(std::string target, std::string newchange){
    varinode* nnode = new varinode(target);
    nnode->SetValue(stoi(newchange));
    AstNode* newnode = new VarinodeNode(nnode);
   // std::cout << target << " " << newchange << " " << op << " " << left->to_string() << " could not find " << right->to_string() << std::endl; 
    if(left->to_string() == target){
      left = newnode;
      return;
    }
    if(right->to_string() == target){
      right = newnode;
      return;
    }
}


FuncNode::FuncNode(AstNode *pfuncName, AstNode *pfuncParameter,  AstNode *pfuncExecution, std::vector<std::vector<varinode*>>* pList, int* player){
  funcName = pfuncName;
  funcParameter = pfuncParameter;
  funcExecution = pfuncExecution;
  List = pList;
  layer = player;
  size = 5;
}

FuncNode::FuncNode(AstNode *pfuncName, AstNode *pfuncParameter,  std::vector<std::vector<varinode*>>* pList, int* player){
  funcName = pfuncName;
  funcParameter = pfuncParameter;
  List = pList;
  layer = player;
  funcExecution = new AstNode();
  size = 4;
}

std::string FuncNode::to_string(){
  return "(" + funcName->to_string() + " " + funcParameter->to_string() + " " + funcExecution->to_string() + ")";
}

varinode* FuncNode::accept(Visitor *visitor){
  return visitor->evaluate_funcnode(this, funcName, funcParameter, funcExecution, List, layer, size);
}


IfNode::IfNode(AstNode *pcond, AstNode * pif){
  size = 2;
  condition = pcond;
  ifstate = pif;
  elsestate = new AstNode();
}

IfNode::IfNode(AstNode *pcond, AstNode *pif, AstNode *pelse){
  size = 3;
  condition = pcond;
  ifstate = pif;
  elsestate = pelse;
}

std::string IfNode::to_string(){
  if(size == 2)
    return "(" + condition->to_string() + " " +ifstate->to_string() + " " + elsestate->to_string() + ")";
  else
    return "(" + condition->to_string() + " " +ifstate->to_string() + ")";
}


varinode* IfNode::accept(Visitor *visitor){
    return visitor->evaluate_ifnode(this, condition, ifstate, elsestate, size);
}


OpNode::OpNode(std::string pop){
  op = pop;
}

std::string OpNode::to_string(){
  return op;
}
