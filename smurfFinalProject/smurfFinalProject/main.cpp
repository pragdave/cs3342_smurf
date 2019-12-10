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
    program                 <-  code
    code                    <-  statement*
    statement               <-  'let(' variable_declaration ')' / assignment / expr
    function_call           <-  variable_reference '(' call_arguments ')' / 'print(' call_arguments ')'
    variable_declaration    <-  decl (',' decl)*
    decl                    <-  identifier ('=' expr)?
    variable_reference      <-  identifier
    assignment              <-  identifier '=' expr
    expr                    <-  boolean_expression / arithmetic_expression
    boolean_expression      <-  arithmetic_expression rel_op arithmetic_expression
    arithmetic_expression   <-  mult_term add_op arithmetic_expression / mult_term
    mult_term               <-  primary mul_op mult_term / primary
    primary                 <-  integer / function_call / variable_reference / '(' arithmetic_expression ')'
    integer                 <-  < '-'? [0-9]+ >
    add_op                  <-  < '+' / '-' >
    mul_op                  <-  < '*' / '/' >
    rel_op                  <-  < '==' / '!=' / '>=' / '>' / '<=' / '<' >
    identifier              <-  < ['a-z']['a-z''A-Z'0-9]* >
    call_arguments          <-  (expr (',' expr)*)?
    %whitespace             <-  [ \t\r\n]*
)";

class visitor;

class ParseTreeNode
{
    node *content;
public:
    ParseTreeNode(){};
    ParseTreeNode(node *content_node){
        content = content_node;
        
    }
    
    node *get() const{
        return content;
    }
    
    string to_string(){
        return content->str();
    }
};

node *bin_op(const SemanticValues &sv)
{
    node *left = sv[0].get<ParseTreeNode>().get();
    
    for (unsigned int i = 1; i < sv.size(); i += 2){
        node *right = sv[i + 1].get<ParseTreeNode>().get();
        string op = sv[i].get<ParseTreeNode>().get()->str();
        left = new binopNode(left, op, right);
    }
    return left;
};

node *assign(const SemanticValues &sv){
    node *left = sv[0].get<ParseTreeNode>().get();
    node *right = sv[1].get<ParseTreeNode>().get();
    left = new assignmentNode(left, right);
    cout<<"Assigning here too"<<endl;
    return left;
};


void setup_ast_generation(parser &parser)
{
    parser["variable_declaration"] = [](const SemanticValues &sv) {
        node *n = assign(sv);
        return ParseTreeNode(n);
    };
    
    parser["assignment"] = [](const SemanticValues &sv) {
        node *n = assign(sv);
        cout<<"Assigning"<<endl;
        return ParseTreeNode(n);
    };
                                                
    parser["identifier"] = [](const SemanticValues &sv) {
        return ParseTreeNode(new variableNode(sv.str()));
    };
    
    parser["expr"] = [](const SemanticValues &sv) {
        node *n = bin_op(sv);
        return ParseTreeNode(n);
    };
    
    parser["arithmetic_expression"] = [](const SemanticValues &sv) {
        node *n = bin_op(sv);
        return ParseTreeNode(n);
    };
    
    parser["boolean_expression"] = [](const SemanticValues &sv) {
        node *n = bin_op(sv);
        return ParseTreeNode(n);
    };
    
    parser["mult_term"] = [](const SemanticValues &sv) {
        node *n = bin_op(sv);
        return ParseTreeNode(n);
    };
    
    parser["integer"] = [](const SemanticValues &sv) {
        return ParseTreeNode(new intNode(atoi(sv.c_str())));
    };
    
    parser["add_op"] = [](const SemanticValues &sv) {
        return ParseTreeNode(new operationNode(sv.token()));
    };
    
    parser["mul_op"] = [](const SemanticValues &sv) {
        return ParseTreeNode(new operationNode(sv.token()));
    };
    
    parser["rel_op"] = [](const SemanticValues &sv) {
        return ParseTreeNode(new operationNode(sv.token()));
    };
}

int main(int argc, const char **argv) {
    
    if (argc < 2 || string("--help") == argv[1]){
        cout << "usage: parser [formula]" << endl;
        return 1;
    }
    
    parser parser(grammar);
    setup_ast_generation(parser);
    
    auto expr = argv[1];
    cout<< "EXPR:" << expr <<endl;
    ParseTreeNode val = ParseTreeNode();
    if (parser.parse(expr, val)){
        visitor *interpret = new interpreter();
        interpret->bindings = new binding();
        
        cout << "Val that is being parsed: "<< val.to_string() << endl;
        cout << val.to_string() << " = " << val.get()->accept(interpret) << endl;
        return 0;
    }
    
    cout<<"Val: "<<&val<<endl;
    
    cout << "syntax error..." << endl;
    return -1;
    
    
    /*
     comment                <-  '#' r'.*'
     if_expression          <- expr brace_block ( 'else' brace_block )?
     function_definition    <- param_list brace_block
     param_list             <- '(' identifier (',' identifier)* ')' / '(' ')'
     brace_block            <- '{' code '}'
    */
    
}











