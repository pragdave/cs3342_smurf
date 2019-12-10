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
#include <fstream>
#include <cstdlib>

#include "visitor.hpp"
#include "node.hpp"
#include "interpreter.hpp"

using namespace peg;
using namespace std;

auto grammar = R"(
    program                 <-  (print_statement / expr)+
    print_statement         <-  'print(' expr ')'
    statement               <-  'let' variable_declaration / assignment / expr
    expr                    <-  boolean_expression / arithmetic_expression
    boolean_expression      <-  arithmetic_expression rel_op arithmetic_expression
    arithmetic_expression   <-  mult_term add_op arithmetic_expression / mult_term
    mult_term               <-  primary mul_op mult_term / primary
    variable_declaration    <-  decl (',' decl)*
    decl                    <-  identifier ('=' expr)?
    primary                 <-  integer / '(' arithmetic_expression ')'
    assignment              <-  identifier '=' expr
    variable_reference      <-  identifier
    identifier              <-  < ['a'-'z']['a'-'z''A'-'Z'0-9]* >
    integer                 <-  < '-'? [0-9]+ >
    add_op                  <-  < '+' / '-' >
    mul_op                  <-  < '*' / '/' >
    rel_op                  <-  < '==' / '!=' / '>=' / '>' / '<=' / '<' >
    %whitespace             <-  [ \t\r\n]*
)";

class visitor;

class ParseTreeNode
{
    node *content;
    
public:
    ParseTreeNode(){};
    ParseTreeNode(node *content_node)
    {
        //cout<<"parsing tree node"<<endl;
        content = content_node;
        
    }
    
    node *get() const
    {
        //cout<<"getting info"<<endl;
        return content;
    }
    
    string to_string()
    {
        //cout<<"making string"<<endl;
        return content->str();
    }
};

node *bin_op(const SemanticValues &sv)
{
    node *left = sv[0].get<ParseTreeNode>().get();
    
    for (unsigned int i = 1; i < sv.size(); i += 2)
    {
        node *right = sv[i + 1].get<ParseTreeNode>().get();
        string op = sv[i].get<ParseTreeNode>().get()->str();
        left = new binopNode(left, op, right);
    }
    return left;
};

node *assign(const SemanticValues &sv){
    node *left = sv[0].get<ParseTreeNode>().get();
    node *right = sv[2].get<ParseTreeNode>().get();
    left = new assignmentNode(left, right);
    return left;
};


void setup_ast_generation(parser &parser)
{
    parser["assignment"] = [](const SemanticValues &sv) {
        node *n = assign(sv);
        return ParseTreeNode(n);
    };
                                                
    parser["identifier"] = [](const SemanticValues &sv) {
        return ParseTreeNode(new variableNode(sv.str()));
    };
    
    parser["expr"] = [](const SemanticValues &sv) {
        //cout << "expr: " << sv.str() << endl;
        node *n = bin_op(sv);
        return ParseTreeNode(n);
    };
    
    parser["arithmetic_expression"] = [](const SemanticValues &sv) {
        //cout << "arithmetic_expression: " << sv.str() << endl;
        node *n = bin_op(sv);
        return ParseTreeNode(n);
    };
    
    parser["boolean_expression"] = [](const SemanticValues &sv) {
        //cout << "boolean_expression: " << sv.str() << endl;
        node *n = bin_op(sv);
        return ParseTreeNode(n);
    };
    
    parser["mult_term"] = [](const SemanticValues &sv) {
        node *n = bin_op(sv);
        return ParseTreeNode(n);
    };
    
    parser["integer"] = [](const SemanticValues &sv) {
        //cout << "in number: " << sv.str() << endl;
        return ParseTreeNode(new intNode(atoi(sv.c_str())));
    };
    
    parser["add_op"] = [](const SemanticValues &sv) {
        //cout << "add/sub: " << sv.str() << endl;
        return ParseTreeNode(new operationNode(sv.token()));
    };
    
    parser["mul_op"] = [](const SemanticValues &sv) {
        //cout << "mul/div: " << sv.str() << endl;
        return ParseTreeNode(new operationNode(sv.token()));
    };
    
    parser["rel_op"] = [](const SemanticValues &sv) {
        //cout << "relationop: " << sv.str() << endl;
        return ParseTreeNode(new operationNode(sv.token()));
    };
}

int main(int argc, const char **argv) {
    
    if (argc < 2 || string("--help") == argv[1])
    {
        cout << "usage: parser [formula]" << endl;
        return 1;
    }
    
    parser parser(grammar);
    setup_ast_generation(parser);
    
    auto expr = argv[1];
    cout<< "EXPR:" << expr <<endl;
    ParseTreeNode val = ParseTreeNode();
    if (parser.parse(expr, val))
    {
        visitor *interpret = new interpreter();
        interpret->bindings = new binding();
        
        cout << "Val that is being parsed: "<< val.to_string() << endl;
        cout << val.to_string() << " = " << val.get()->accept(interpret) << endl;
        return 0;
    }
    
    cout<<"Val: "<<&val<<endl;
    
    cout << "syntax error..." << endl;
    return -1;
    
    //identifier  <-  ['a'-'z']['a'-'z''A'-'Z'0-9]*   //identifier and assignment are not working properly...need to find out why
    //assignment  <-  identifier '=' expr
    
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
     mulop       <- '*' / '/'
     relop       <- '==' / '!-' / '>=' / '>' / '<=' / '<'
     function_call <- variable_reference '(' call_arguments ')' / 'print' '(' call_arguments ')'
     call_arguments <- (expr (',' expr)*)?
     function_definition <- param_list brace_block
     param_list  <- '(' identifier (',' identifier)* ')' / '(' ')'
     brace_block <- '{' code '}'
    
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
        intNode returnNode = *new intNode(x);
        cout<<"Here"<<endl;
        return returnNode;
    };
    
    parser["binop"] = [](const SemanticValues& sv) {
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
    parser.parse("678", val1);
    //int val2;
    //parser.parse(" 1 + 2 * 3 ", val2);
    
    //assert(val1 == 9);
    //assert(val2 == 7);

    cout<<"Val 1 = "<<val1<<endl;
    //cout<<"Val 2 = "<<val2<<endl;
    return 0;
     
     parser["integer"] = [](const SemanticValues& sv) {
     int x = stoi(sv.str());
     cout<<"X: "<<x<<endl;
     intNode returnNode = *new intNode(x);
     cout<<"Here"<<endl;
     return returnNode;
     };
     */
    
}











