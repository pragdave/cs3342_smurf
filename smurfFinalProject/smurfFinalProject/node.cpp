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

map<string, int> node::createInt(int x) {
    intNode["int"] = x;
    return intNode;
}

map<string, char> node::createChar(char x) {
    charNode["char"] = x;
    return charNode;
}

map<string, string> node::createString(string x) {
    stringNode["string"] = x;
    return stringNode;
}

/* node::~node() {
    delete intNode;
    delete charNode;
    delete stringNode;
} */






