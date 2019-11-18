//
//  node.cpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 11/12/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//

#include "node.hpp"

node::node() {
/*    intNode[""] = NULL;
    charNode[""] = NULL;
    stringNode[""] = NULL; */
}

void node::createInt(int x) {
    intNode[x] = "int";
}

void node::createChar(char x) {
    charNode[x] = "char";
}

void node::createString(string x) {
    stringNode[x] = "string";
}

/* node::~node() {
    delete intNode;
    delete charNode;
    delete stringNode;
} */






