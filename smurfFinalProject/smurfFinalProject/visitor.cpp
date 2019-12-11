//
//  visitor.cpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 11/20/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//

#include "visitor.hpp"


int visitor::evaluate_integer(node *nodex, int x){
    return 0;
}

int visitor::evaluate_binop(node *nodex, node *left, string operation, node *right){
    return 0;
}

int visitor::evaluate_assignment(node *nodex, node *left, node *right){
    return 0;
}

int visitor::evaluate_variable(node *nodex, string x){
    return 0;
}

int visitor::evaluate_code(vector<node*> nodexes){
    return 0;
}

int visitor::evaluate_statement(node *nodex){
    return 0;
}

//int visitor::evaluate_ifstatement(node *nodex, node *expr, node *children){
//    return 0;
//}
