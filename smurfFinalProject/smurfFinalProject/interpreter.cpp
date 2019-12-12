//
//  interpreter.cpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 11/20/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//

#include "interpreter.hpp"
using namespace std;

int interpreter::evaluate_integer(node *nodex, int value){                                      //This function evaluates an integer to return its value.
    return value;
}

int interpreter::evaluate_binop(node *nodex, node *left, string operation, node *right){        //This function evaluates a binop to return the value of
    int lval = left->accept(this);                                                              //the binary operation function. ie: 3+4 would return 7
    int rval = right->accept(this);
    return evaluateOperator[operation](lval, rval);
}

int interpreter::evaluate_assignment(node *nodex, node *left, node *right){                     //This function evaluates a variable assignment to return the
    left->accept(this);                                              //sets the variableName      value given to the identifier. All of the variables are stored
    int rval = right->accept(this);                                                             //in a mapping through the binding class so that if the variable's
    bindings->insertValue(variableName, rval);                                                  //value changes, it will be updated in the mapping to return the
    int value = this->bindings->getBindingValue(variableName);                                  //most up to date value.
    return value;
}

int interpreter::evaluate_variable(node *nodex, string var){                                    //This function sets the variable name in the Mapping so that it
    variableName = var;                                                                         //can be checked properly when an identifier is referenced
    return bindings->getBindingValue(var);
}

int interpreter::evaluate_statement(node *nodex){                                               //This function can take in any statement and allows a visitor
    int result = 0;                                                                             //to determine which evaluation function it should go through.
    result = nodex->accept(this);
    return result;
}

int interpreter::evaluate_code(vector<node*> nodex){                                            //This function evaluates code to run through multiple statements
    int result=999999;                                                                          //AKA visits each of its children/statement nodes
    for(int i=0; i<nodex.size(); i++){
        result = nodex[i]->accept(this);
    }
    return result;
}

