//
//  ast.hpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 11/12/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//

#ifndef ast_hpp
#define ast_hpp

#include <stdio.h>
#include "node.hpp"
#include <map>

class ast {
public:
    node intNode;
    node *left;
    node *right;
    string operation;
    
    void createBinop(node*, string, node*);
    void createIntAST(string);
    
};

#endif /* ast_hpp */
