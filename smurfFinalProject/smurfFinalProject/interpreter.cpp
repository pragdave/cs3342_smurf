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
    return eval_op(lval, operation, rval);
}

int interpreter::eval_op(int left, string operation, int right) {
    if (operation == "+") {
        return left + right;
    } else if (operation == "-") {
        return left - right;
    } else if (operation == "*") {
        return left * right;
    } else if (operation == "/") {
        return left / right;
    } else {
        return -1;
    }
}

bool interpreter::eval_relop(int left, string operation, int right) {
    if (operation == ">") {
        return left > right;
    } else if (operation == ">=") {
        return left >= right;
    } else if (operation == "<") {
        return left < right;
    } else if (operation == "<=") {
        return left <= right;
    } else {
        //std::cout<<"Error with evaluating relation operation"<<std::endl;
        return false;
    }
}
