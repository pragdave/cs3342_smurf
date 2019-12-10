#include <string>
#include <functional>
#include "ast_node.h"
#include "interpreter.h"


Interpreter::Interpreter(){

}

// Interpreter::Interpreter(std::vector<std::vector<varinode*>>& newlist, int& newlayer){
//     listPointer = newlist;
//     layer = newlayer;
// }

varinode* Interpreter::evaluate_varinode(AstNode* node, varinode* value){
  return value;
}

varinode* Interpreter::evaluate_binop(AstNode *node, AstNode *left, std::string op, AstNode *right){
  varinode lval = *left->accept(this);
  varinode rval = *right->accept(this);

  if(op == "+"){
     varinode* ans = new varinode(lval+rval);
     return ans;
  }
  else if(op == "-"){
    varinode* ans = new varinode(lval-rval);
    return ans;
  }
  else if(op == "*"){
    varinode* ans = new varinode(lval*rval);
    return ans;
  }
  else if(op == "/"){
    varinode* ans = new varinode(lval/rval);
    return ans;
  }
  else if(op == "="){
    left->accept(this)->SetValue(right->accept(this)->GetValue());
    return left->accept(this);
  }
  else if(op == "=="){
    varinode* ans = new varinode(lval==rval);
    return ans;
  }
  else if(op == "!="){
    varinode* ans = new varinode(lval!=rval);
    return ans;
  }
  else if(op == ">"){
    varinode* ans = new varinode(lval>rval);
    return ans;
  }
  else if(op == ">="){
    varinode* ans = new varinode(lval>=rval);
    return ans;
  }
  else if(op == "<"){
    varinode* ans = new varinode(lval<rval);
    return ans;
  }
  else if(op == "<="){
    varinode* ans = new varinode(lval<=rval);
    return ans;
  }
  else{
    std::cout << "interprerer error" << std::endl;
    exit(0);
  }
}



varinode* Interpreter::evaluate_ifnode(AstNode *node, AstNode *cond, AstNode *ifs, AstNode *elses, int size){
    varinode* c = new varinode();
    if(size == 2){
        varinode newcond = *cond->accept(this);
        varinode newif = *ifs->accept(this);
        if(newcond.GetValue() == 1){
            return ifs->accept(this);
        } 
        else{
            return c;
        }
      }
    else if(size == 3){
        varinode newcond = *cond->accept(this);
        varinode newif = *ifs->accept(this);
        varinode newelses = *elses->accept(this);
        if(newcond.GetValue() == 1){
            return ifs->accept(this);
        }
        else{
            return elses->accept(this);
        }
    }
    else{
        std::cout << "error occur" << std::endl;
        return c;
    }
}