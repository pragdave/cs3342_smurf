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
#include "node.hpp"
#pragma once

using namespace peg;
using namespace std;

int main(int argc, const char * argv[]) {
    
    auto grammar = R"(
        integer     <- < '-'? [0-9]+ >
        %whitespace <- [ \t]*
    )";
    
    /* program     <- code EOF
     comment     <- '#' r'.*'
     code        <- statement*
     statement   <- 'let' variable_declaration / assignment / expr
     variable_declaration <- decl (',' decl)*
     decl        <- identifier ('=' expr)?
     identifier  <- ['a'-'z']['a'-'z''A'-'Z'_ 0-9]*
     variable_reference <- identifier
     if_expression <- expr brace_block ( 'else' brace_block )?
     assignment  <- identifier '=' expr
     expr        <- 'fn' function_definition / 'if' if_expression / boolean_expression / arithmetic_expression
     boolean_expression <- arthimetic_expression relop arthimetic_expression
     arithmetic_expression    <- mult_term addop arithmetic_expression / mult_term
     mult_term   <- primary mulop mult_term / primary
     primary     <- integer / function_call/ variable_reference/ '(' arithmetic_expression ')'
     addop       <- '+' / '-'
     mulop       <- '*' / '/'
     relop       <- '==' / '!-' / '>=' / '>' / '<=' / '<' */
    
    /*function_call <- variable_reference '(' call_arguments ')' / 'print' '(' call_arguments ')'
     call_arguments <- (expr (',' expr)*)?
     function_definition <- param_list brace_block
     param_list  <- '(' identifier (',' identifier)* ')' / '(' ')'
     brace_block <- '{' code '}' */
    
    parser parser;
    //ast tree;
    
    
    parser.log = [](size_t line, size_t col, const string& msg) {
        cerr << line << ":" << col << ": " << msg << "\n";
    };
    
    auto ok = parser.load_grammar(grammar);
    assert(ok);
    
    parser["integer"] = [](const SemanticValues& sv) {
        int x = stoi(sv.str());
        cout<<"X: "<<x<<endl;
        return new intNode(x);
    };
    
    parser["Binop"] = [](const SemanticValues& sv) {
        /*switch (binopNode) {
            case 0:
                return binopNode(sv[0], binopNode.operation, sv[2]);
            default:
                return sv[0];
        }*/
    };
    
    // Parse
    parser.enable_packrat_parsing(); // Enable packrat parsing.
    
    
    // Testing Parser
    int val1;
    parser.parse("6", val1);
    //int val2;
    //parser.parse(" 1 + 2 * 3 ", val2);
    
    //assert(val1 == 9);
    //assert(val2 == 7);

    cout<<"Val 1 = "<<val1<<endl;
    //cout<<"Val 2 = "<<val2<<endl;
}
