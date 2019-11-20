//
//  binopNode.hpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 11/19/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//

#ifndef binopNode_hpp
#define binopNode_hpp

#include <stdio.h>

class node {
public:
    int val;
    char op;
};

class binopNode: public node {
public:
    node *left;
    node *right;
    char operation;
    int val;
    
    binopNode();
    void createBinop(node*, char, node*);
    ~binopNode();
    
};

#endif /* binopNode_hpp */
