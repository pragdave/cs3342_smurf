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
    //print(op, lstr, rstr);
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

//variable node
variableNode::variableNode(string var){
    variable = var;
}

string variableNode::str(){
    return variable;
}

int variableNode::accept(visitor *visitorx){
    visitorx->evaluate_variable(this, variable);
    return 0;
}

//assignment node
assignmentNode::assignmentNode(node *l, node *r){
    left = l;
    assignment = "=";
    right = r;
    string lstr = l->str();
    string rstr = r->str();
    //print(lstr, rstr);
}

string assignmentNode::str(){
    return "(" + left->str()+ "=" + right->str() + ")";
}

int assignmentNode::accept(visitor *visitorx){
    return visitorx->evaluate_assignment(this, left, right);
}

void assignmentNode::print(string l, string r) {
    cout<<"Printing Assignment Node | Assignment: = | Left: "<<l<<" | Right: "<<r<<endl;
}

//code node
codeNode::codeNode(node *statement){
    statements.push_back(*statement);
}

int codeNode::accept(visitor *visitorx){
    return visitorx->evaluate_code(statements);
}

node codeNode::get(int location){
    return statements[location];
}

string codeNode::str(node nodex){
    return nodex.str();
}














