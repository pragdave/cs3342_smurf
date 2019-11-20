//
//  node.cpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 11/19/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//
// Based on pragdave/peglibeg

#include "node.hpp"

intNode::intNode(int x){
    val = x;
}

string intNode::str(){
    return to_string(val);
}

/* int intNode::accept(Visitor *visitor){
    return visitor->evaluate_integer(this, val);
} */

binopNode::binopNode(node* l, string op, node* r){
    left = l;
    operation = op;
    right = r;
}

string binopNode::str(){
    return '(' + left->str()+ operation + right->str() + ')';
}

/* int binopNode::accept(Visitor *visitor){
    return visitor->evaluate_binop(this, left, operation, right);
} */

operationNode::operationNode(string op){
    operation = op;
}

/* int operationNode::accept(Visitor *visitor){
    return 0;
} */

string operationNode::str(){
    return operation;
}










