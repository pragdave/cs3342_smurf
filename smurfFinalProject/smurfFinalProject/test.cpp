//
//  test.c
//  smurfFinalProject
//
//  Created by Alden Shiverick on 12/6/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//

// (1) Include the header file
#include "peglib.h"
#include <assert.h>
#include <iostream>

using namespace peg;
using namespace std;

int main(void) {
    // (2) Make a parser
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
    
    // (3) Setup actions
    parser["Additive"] = [](const SemanticValues& sv) {
        switch (sv.choice()) {
            case 0:  // "Multitive '+' Additive"
                return <int>(sv[0]) + any_cast<int>(sv[1]);
            default: // "Multitive"
                return <int>(sv[0]);
        }
    };
    
    parser["Multitive"] = [](const SemanticValues& sv) {
        switch (sv.choice()) {
            case 0:  // "Primary '*' Multitive"
                return <int>(sv[0]) + any_cast<int>(sv[1]);
            default: // "Primary"
                return <int>(sv[0]);
        }
    };
    
    parser["Number"] = [](const SemanticValues& sv) {
        return stoi(sv.token(), nullptr, 10);
    };
    
    // (4) Parse
    parser.enable_packrat_parsing(); // Enable packrat parsing.
    
    int val;
    parser.parse(" (1 + 2) * 3 ", val);
    
    assert(val == 9);
}
