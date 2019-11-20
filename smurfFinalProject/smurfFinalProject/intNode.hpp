//
//  intNode.hpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 11/19/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//

#ifndef intNode_hpp
#define intNode_hpp

#include <stdio.h>


class node {
public:
    int val;
    char op;
};

class intNode: public node {
public:
    int value;
    
    intNode();
    void createInt(int);
    ~intNode();
};

#endif /* intNode_hpp */
