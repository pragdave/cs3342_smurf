//
//  node.cpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 11/19/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//
// Based on pragdave/peglibeg

#include "node.hpp"
//node
string node::str(){
    return string("node");
};

int node::accept(visitor *visitorx){
    return 99999;
}

//int node
intNode::intNode(int x){
    val = x;
}

string intNode::str(){
    return to_string(val);
}

int intNode::accept(visitor *visitorx){
    return visitorx->evaluate_integer(this, val);
}

//binop node
binopNode::binopNode(node* l, string op, node* r){
    left = l;
    operation = op;
    right = r;
}

string binopNode::str(){
    return '(' + left->str()+ operation + right->str() + ')';
}

int binopNode::accept(visitor *visitorx){
    return visitorx->evaluate_binop(this, left, operation, right);
}

//op node
operationNode::operationNode(string op){
    operation = op;
}

int operationNode::accept(visitor *visitorx){
    return 0;
}

string operationNode::str(){
    return operation;
}










