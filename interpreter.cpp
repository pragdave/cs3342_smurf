#include <string>
#include <functional>
#include "ast_node.h"
#include "interpreter.h"


Interpreter::Interpreter(){}


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
    varinode* c = new varinode();              // If_Node has a condition node, a if_situation node, and a else_situation node
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
        if(newcond.GetValue() == 1){                  // If the condition is 1(true) return if's statement, else return else's statement
            return ifs->accept(this);
        }
        else{
            return elses->accept(this);
        }
    }
    else{
        std::cout << "If-Node interprerer error" << std::endl;
        exit(0);
    }
}


varinode* Interpreter::evaluate_funcnode(AstNode *node, AstNode *name, AstNode *parameter, AstNode *execution, std::vector<std::vector<varinode*>>* List, int* layer, int size){
     if(size ==5){                                      // If it is the delcaration of a function with parameter
        std::vector<varinode*> NewLayer;
        varinode* c = new varinode(name->to_string());
        c->expr = execution;
        c->vtype = "function";
        c->parameter = parameter->to_string();                   // Create a function node
        c->SetValue(0);
        varinode* d = new varinode(parameter->to_string());
        if(List->size() == 1){
          NewLayer.push_back(c);
          NewLayer.push_back(d);
          List->push_back(NewLayer);
        }
          else{
            for(int i = 0; i < List->at(1).size(); i++){
              if(List->at(1).at(i)->GetName() == c->GetName()){
                  List->at(1).at(i) = c;
                  List->at(1).push_back(d);                     // Replace the function node that is already delcared
                  return c;
              }
            }
            List->at(1).push_back(c);
            List->at(1).push_back(d);
        }
        return c;
     }


     else if(size == 3){                               // If it is the delcaration of a function without parameter
       std::vector<varinode*> NewLayer;
        varinode* c = new varinode(name->to_string());
        c->expr = execution;
        c->vtype = "function";
        c->parameter = parameter->to_string();
        c->SetValue(0);
        if(List->size() == 1){
          NewLayer.push_back(c);
          List->push_back(NewLayer);
        }
        else{
          for(int i = 0; i < List->at(1).size(); i++){
            if(List->at(1).at(i)->GetName() == c->GetName()){
              List->at(1).at(i) = c;
              return c;
            }
          }
          List->at(1).push_back(c);
        }
        return c;
     }


     else if(size == 4){                                        // If it is the implementation of a function with parameter
       int funcloc = 0;
       int parameterloc = 0;
       int a = *layer + 1;
       if(List->size() <= 1){
         std::cout << "Did not declare the function ========" << std::endl;
         exit(0);
       }
        for(int i = 0; i < List->at(a).size(); i++){
          if(List->at(a).at(i)->GetName() == name->to_string()){             // Find the function node on the List
              funcloc = i;
              break;
          }
        }
        for(int i = 0; i < List->at(a).size(); i++){
          if(List->at(a).at(i)->GetName() == List->at(a).at(funcloc)->parameter){           
              List->at(a).at(i)->SetValue(stoi(parameter->to_string()));
              execution = List->at(a).at(funcloc)->expr;                                
              execution->update(List->at(a).at(i)->GetName(), parameter->to_string());}    // Update the function variable with new parameter
        }
        return execution->accept(this);                                 // Implement the function 
     }


     else if(size == 2){                                                       // If it is the implementation of a function without parameter
       int funcloc = 0;
       int parameterloc = 0;
       int a = *layer + 1;
       if(List->size() <= 1){
          std::cout << "Did not declare the function ========" << std::endl;
          exit(0);
        }
        for(int i = 0; i < List->at(a).size(); i++){
          if(List->at(a).at(i)->GetName() == name->to_string()){
              funcloc = i;
              break;
          }
        }
        execution = List->at(a).at(funcloc)->expr;
        return execution->accept(this);
     }
     else{
        std::cout << "Error on evaluate function" << std::endl;
        exit(0);
     }
}