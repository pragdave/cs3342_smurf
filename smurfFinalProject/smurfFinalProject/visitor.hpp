//
//  visitor.hpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 11/20/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//

#ifndef visitor_hpp
#define visitor_hpp

#include <stdio.h>
#include <string>
#include "binding.hpp"
#include <vector>
#pragma once


using namespace std;

class node;

class visitor {
public:
    binding *bindings;
    string variableName;
    virtual int evaluate_integer(node*, int);
    virtual int evaluate_binop(node*, node*, string, node*);
    virtual int evaluate_assignment(node*, node*, node*);
    virtual int evaluate_variable(node*, string);
    virtual int evaluate_code(vector<node>);
    
    //    virtual int evaluate_ifstatement(node*, node*, node*);
};

#endif /* visitor_hpp */
