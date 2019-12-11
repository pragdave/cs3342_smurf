//
//  node.hpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 11/19/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//
// Based on pragdave/peglibeg

#ifndef node_hpp
#define node_hpp
#pragma once
#include <iostream>
#include <string>
#include <vector>
#include "visitor.hpp"

using namespace std;

class node {
public:
    virtual string str();
    virtual int accept(visitor*);
    virtual void print(string);
};

class intNode: public node {
private:
    int val;
public:
    intNode(int);
    string str();
    int accept(visitor*);
};

class binopNode: public node {
private:
    node *left;
    node *right;
    string operation;
public:
    binopNode(node*, string, node*);
    string str();
    int accept(visitor*);
    void print(string, string, string);
};

class operationNode: public node {
private:
    string operation;
public:
    operationNode(string);
    string str();
    int accept(visitor*);
};

class variableNode: public node {
private:
    string variable;
public:
    variableNode(string);
    string str();
    int accept(visitor*);
};

class assignmentNode: public node {
private:
    node *left;
    node *right;
    string assignment;
public:
    assignmentNode(node*, node*);
    string str();
    int accept(visitor*);
    void print(string, string);
};

class codeNode: public node {
    vector<node*> statements;
public:
    codeNode(node*);
    string str();
    int accept(visitor*);
};








#endif /* node_hpp */
