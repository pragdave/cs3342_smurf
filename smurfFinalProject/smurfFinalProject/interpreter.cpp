//
//  interpreter.cpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 11/20/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//

#include "interpreter.hpp"
using namespace std;

int interpreter::evaluate_integer(node *nodex, int value){
    return value;
}

int interpreter::evaluate_binop(node *nodex, node *left, string operation, node *right){
    int lval = left->accept(this);
    int rval = right->accept(this);
    return evaluateOperator[operation](lval, rval);
}

int interpreter::evaluate_assignment(node *nodex, node *left, node *right)
{
    left->accept(this);                                              //sets the variableName used in this->
    int rval = right->accept(this);
    this->bindings->insertValue(variableName, rval);
    return 0;
}

int interpreter::evaluate_variable(node *nodex, string var){
    variableName = var;
    return 0;
}