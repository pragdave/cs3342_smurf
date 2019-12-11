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
#include <iostream>
#include <vector>
#include "visitor.hpp"
#include "node.hpp"
#include "binding.hpp"

using namespace std;

class interpreter: public visitor {
    map< string, function<int(int, int)>> evaluateOperator = {
        //add_ops
        {"+", [](int left, int right) {return left + right; }},
        {"-", [](int left, int right) {return left - right; }},
        //mul_ops
        {"*", [](int left, int right) {return left * right; }},
        {"/", [](int left, int right) {return left / right; }},
        //rel_ops
        {"==", [](int left, int right) {return left == right; }},
        {"!=", [](int left, int right) {return left != right; }},
        {">=", [](int left, int right) {return left >= right; }},
        {">", [](int left, int right) {return left > right; }},
        {"<=", [](int left, int right) {return left <= right; }},
        {"<", [](int left, int right) {return left < right; }}
    };
public:
    visitor *visitorx;
    int evaluate_integer(node*, int);
    int evaluate_binop(node*, node*, string, node*);
    int evaluate_assignment(node*, node*, node*);
    int evaluate_variable(node*, string);
    int evaluate_code(vector<node*>);
    //int evaluate_ifstatement(node*, node*, node*);
};


#endif /* interpreter_hpp */
