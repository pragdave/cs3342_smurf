//
//  main.cpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 11/12/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//

#include "peglib.h"
#include <assert.h>
#include <iostream>
//#include "ast.hpp"
#include "intNode.hpp"
#include "binopNode.hpp"

using namespace peg;
using namespace std;

int main(int argc, const char * argv[]) {
    
    auto grammar = R"(
    Number      <- < '-'? [0-9]+ >
    %whitespace <- [ \t]*
    )";
    
    parser parser;
    //ast tree;
    intNode nodeInteger;
    binopNode nodeBinop;
    
    parser.log = [](size_t line, size_t col, const string& msg) {
        cerr << line << ":" << col << ": " << msg << "\n";
    };
    
    auto ok = parser.load_grammar(grammar);
    assert(ok);
    
    parser["Number"] = [](const SemanticValues& sv) {
        nodeInteger.createInt(stoi(sv.str()));
    };
    
    parser["Binop"] = [](const SemanticValues& sv) {
        switch (binopNode) {
            case 0:
                return binopNode(sv[0], binopNode.operation, sv[2]);
            default:
                return sv[0];
        }
    };
    
    // Parse
    parser.enable_packrat_parsing(); // Enable packrat parsing.
    
    
    // Testing Parser
    int val1;
    parser.parse("9", val1);
    //int val2;
    //parser.parse(" 1 + 2 * 3 ", val2);
    
    assert(val1 == 9);
    //assert(val2 == 7);

    cout<<"Val 1 = "<<val1<<endl;
    //cout<<"Val 2 = "<<val2<<endl;
}
