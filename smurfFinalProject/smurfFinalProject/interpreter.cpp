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

int interpreter::evaluate_assignment(node *nodex, node *left, node *right){
    left->accept(this);                                              //sets the variableName
    int rval = right->accept(this);
    this->bindings->insertValue(variableName, rval);
    int value = this->bindings->getBindingValue(variableName);
    return value;
}

int interpreter::evaluate_variable(node *nodex, string var){
    variableName = var;
    return 0;
}

//int interpreter::evaluate_ifstatement(node *nodex, node *expr, node *children){
//
//}

int interpreter::evaluate_code(vector<node> nodex){
    node statement;
    statement = nodex[0];
    return statement.accept(this);
}




