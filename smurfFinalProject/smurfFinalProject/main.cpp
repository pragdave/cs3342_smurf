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

using namespace peg;
using namespace std;

int main(int argc, const char * argv[]) {

    auto grammar = R"(
# Grammar for Calculator...
    Additive    <- Multitive '+' Additive / Multitive
    Multitive   <- Primary '*' Multitive / Primary
    Primary     <- '(' Additive ')' / Number
    Number      <- < [0-9]+ >
    %whitespace <- [ \t]*
    )";
    
    parser parser;
    
    parser.log = [](size_t line, size_t col, const string& msg) {
        cerr << line << ":" << col << ": " << msg << "\n";
    };
    
    auto ok = parser.load_grammar(grammar);
    assert(ok);
    
    // Setup actions
    parser["Additive"] = [](const SemanticValues& sv) {
        switch (sv.choice()) {
            case 0:  // "Multitive '+' Additive"
                return sv[0].get<int>() + sv[1].get<int>();
            default: // "Multitive"
                return sv[0].get<int>();
        }
    };
    
    parser["Multitive"] = [](const SemanticValues& sv) {
        switch (sv.choice()) {
            case 0:  // "Primary '*' Multitive"
                return sv[0].get<int>() * sv[1].get<int>();
            default: // "Primary"
                return sv[0].get<int>();
        }
    };
    
    parser["Number"] = [](const SemanticValues& sv) {
        return stoi(sv.token(), nullptr, 10);
    };
    
    // Parse
    parser.enable_packrat_parsing(); // Enable packrat parsing.
    
    
    // Testing Parser
    int val1;
    parser.parse(" (1 + 2) * 3 ", val1);
    int val2;
    parser.parse(" 1 + 2 * 3 ", val2);
    
    assert(val1 == 9);
    assert(val2 == 7);

    cout<<"Val 1 = "<<val1<<endl;
    cout<<"Val 2 = "<<val2<<endl;
}
