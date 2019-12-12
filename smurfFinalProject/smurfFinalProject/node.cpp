//
//  node.cpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 11/19/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//
// Based on pragdave/peglibeg

#include "node.hpp"
//general node–––––––––––––––––––––––––––––––––––––––––
string node::str(){                                                     //Default node constructor. Node is the superclass
    return string("node");                                              //to all of the classes in this file.
};

int node::accept(visitor *visitorx){                                    //Accepts the visitor/interpreter. Default return 99999
    return 99999;
}

void node::print(string x){
    cout<< "Printing General Node: "<< x <<endl;
}

//int node–––––––––––––––––––––––––––––––––––––––––––––
intNode::intNode(int x){                                                //Node to hold an integer value
    val = x;
    //print();
}

string intNode::str(){                                                  //Return the node value in string form
    return to_string(val);
}

int intNode::accept(visitor *visitorx){                                 //Accepts the interpreter for an integer
    return visitorx->evaluate_integer(this, val);
}

void intNode::print(){                                                  //Prints the integer node
    cout<<"Printing Integer Node | Int: "<<val<<endl;
}

//binop node––––––––––––––––––––––––––––––––––––––––––––
binopNode::binopNode(node* l, string op, node* r){                      //Node tree structure to initialize a binop. As mentioned
    left = l;                                                           //in main, this structure consists of an operation parent
    operation = op;                                                     //node and two value children nodes.
    right = r;
    string lstr = l->str();
    string rstr = r->str();
    //print(op, lstr, rstr);
}

string binopNode::str(){                                                //Returns the node in string form ie: node transforming to: "3+4"
    return "(" + left->str()+ operation + right->str() + ")";
}

int binopNode::accept(visitor *visitorx){                               //Accepts the interpreter for a binop
    return visitorx->evaluate_binop(this, left, operation, right);
}

void binopNode::print(string op, string l, string r){                   //Prints the binop node
    cout<< "Printing BinopNode | Operation: "<<op<< " | Left: " <<l<< " | Right: "<<r<<endl;
}

//op node–––––––––––––––––––––––––––––––––––––––––––––––
operationNode::operationNode(string op){                                //Node to hold an operation
    operation = op;
    //print();
}

string operationNode::str(){                                            //Returns the operation in string
    return operation;
}

int operationNode::accept(visitor *visitorx){                           //Does not need to accept an interpreter because this is
    return 0;                                                           //handled through binop
}

void operationNode::print(){                                            //Prints the operation
    cout<< "Printing Operation Node | Operation: "<<operation<<endl;
}

//variable node–––––––––––––––––––––––––––––––––––––––––
variableNode::variableNode(string var){                                 //Node to hold a variable identifier
    variable = var;
    //print();
}

string variableNode::str(){                                             //Returns the variable in string
    return variable;
}

int variableNode::accept(visitor *visitorx){                            //Accepts the interpreter for a variable
    return visitorx->evaluate_variable(this, variable);
    
}

void variableNode::print(){                                             //Prints the variable
    cout<<"Prining Variable Node | Variable: "<<variable<<endl;
}

//assignment node––––––––––––––––––––––––––––––––––––––––
assignmentNode::assignmentNode(node *l, node *r){                       //Node tree structure to initialize a variable. As mentioned
    left = l;                                                           //in main, this structure consists of one parent assignment
    assignment = "=";                                                   //node and two chidren nodes containing a variable and value
    right = r;
    string lstr = l->str();
    string rstr = r->str();
    //print(lstr, rstr);
}

string assignmentNode::str(){                                           //Returns the assignment in a string
    return "(" + left->str()+ "=" + right->str() + ")";
}

int assignmentNode::accept(visitor *visitorx){                          //Accepts the interpreter for an assignment
    return visitorx->evaluate_assignment(this, left, right);
}

void assignmentNode::print(string l, string r) {                        //Prints the assignment
    cout<<"Printing Assignment Node | Assignment: = | Left: "<<l<<" | Right: "<<r<<endl;
}

//statement node–––––––––––––––––––––––––––––––––––––––––
statementNode::statementNode(node* stmt){                               //Node to hold statements (could consist of any previous nodes)
    statement = stmt;
    print();
}

string statementNode::str(){                                            //Returns the node in a string
    return statement->str();
}

int statementNode::accept(visitor *visitorx){                           //Accepts the interpreter for a statement
    cout<<"Statement: "<<statement[0].str()<<endl;
    return visitorx->evaluate_statement(statement);
}

void statementNode::print(){                                            //Prints the statement
    cout<<"Printing Statement Node | Statement: "<<statement->str()<<endl;
}

//code node––––––––––––––––––––––––––––––––––––––––––––––
codeNode::codeNode(){                                                   //Parent node to the whole AST
    print();
}

int codeNode::accept(visitor *visitorx){                                //Accepts the interpreter for code
    return visitorx->evaluate_code(statements);
}

string codeNode::str(){                                                 //Returns the statements in strings
    string result;
    for(int i=0; i<statements.size(); i++){
        result = statements[i]->str();
    }
    return result;
}

void codeNode::addToVect(node *nodex){                                  //Adds statements to the statements vector of nodes
    statements.push_back(nodex);
}

void codeNode::print(){                                                 //Prints the statements/children of code node
    for(int i=0; i<statements.size(); i++){
        cout<<"Statements: "<<statements[i]->str()<<endl;
    }
}

