//
//  interpreter.hpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 11/20/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//

#ifndef interpreter_hpp
#define interpreter_hpp

#include <stdio.h>
#pragma once
#include <map>
#include <string>
#include <functional>
#include "visitor.hpp"
#include "node.hpp"

using namespace std;

class interpreter: public visitor {
    map< string, function<int(int, int)>> evaluateOperator = {
        {"+", [](int left, int right) {return left + right; }},
        {"-", [](int left, int right) {return left - right; }},
        {"*", [](int left, int right) {return left * right; }},
        {"/", [](int left, int right) {return left / right; }}
    };
public:
    int evaluate_integer(node*, int);
    int evaluate_binop(node*, node*, string, node*);
    int eval_op(int,string, int);
    bool eval_relop(int, string, int);
};


#endif /* interpreter_hpp */
