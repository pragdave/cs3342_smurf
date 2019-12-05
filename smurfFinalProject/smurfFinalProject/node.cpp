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

void node::print(string x){
    cout<< "Printing General Node: "<< x <<endl;
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
    string lstr = l->str();
    string rstr = r->str();
    print(op, lstr, rstr);
}

string binopNode::str(){
    return "(" + left->str()+ operation + right->str() + ")";
}

int binopNode::accept(visitor *visitorx){
    return visitorx->evaluate_binop(this, left, operation, right);
}

void binopNode::print(string op, string l, string r){
    cout<< "Printing BinopNode | Operation: "<<op<< " | Left: " <<l<< " | Right: "<<r<<endl;
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

//identifier node
identifierNode::identifierNode(string id){
    identifier = id;
}

int identifierNode::accept(visitor *visitorx){
    return visitorx->evaluate_identifier(this, identifier);
}

string identifierNode::str(){
    return identifier;
}









