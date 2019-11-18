//
//  node.hpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 11/12/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//

#ifndef node_hpp
#define node_hpp
#include <iostream>
#include <string>
#include <map>
using namespace std;

#include <stdio.h>

class node {
public:
    map<string, int> intNode;
    map<string, char> charNode;
    map<string, string> stringNode;
    
    node();
    map<string,int> createInt(int);
    map<string, char> createChar(char);
    map<string, string> createString(string);
};



#endif /* node_hpp */
