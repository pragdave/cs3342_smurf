//
//  ast.cpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 11/12/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//

#include "ast.hpp"

void ast::createBinop(node *l, string op, node *r) {
    left = l;
    operation = op;
    right = r;
}

void ast::createIntAST(char x) {
    int y = stoi(x);
    intNode.createInt(y);
}

