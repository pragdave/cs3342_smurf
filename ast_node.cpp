#include "ast_node.h"


////////////////////
//  IntegerNode

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

////////////////////
//  BinopNode

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


////////////////////
//  IfNode
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


////////////////////
//  OpNode

OpNode::OpNode(std::string pop)
{
  op = pop;
}

// int OpNode::accept(Visitor *visitor) {
//   return 0;  // never called.
// }

std::string OpNode::to_string(){
  return op;
}
