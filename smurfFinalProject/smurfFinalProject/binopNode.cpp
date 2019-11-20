//
//  binopNode.cpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 11/19/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//

#include "binopNode.hpp"

binopNode::binopNode(){
    left = NULL;
    right = NULL;
    op = operation;
    
}

void binopNode::createBinop(node *l, char binop, node *r){
    left = l;
    operation = binop;
    right = r;
}

binopNode::~binopNode(){
    left = nullptr;
    right = nullptr;
    op = NULL;
}
