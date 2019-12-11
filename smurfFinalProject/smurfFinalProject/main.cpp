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
#include <vector>

#include "visitor.hpp"
#include "node.hpp"
#include "interpreter.hpp"

using namespace peg;
using namespace std;

auto grammar = R"(
    program                 <-  code
    code                    <-  statement*
    function_call           <-  'print' '(' call_arguments ')' / variable_reference '(' call_arguments ')'
    statement               <-  let_stmt / assignment / expr
    let_stmt                <-  'let' variable_declaration
    expr                    <-  boolean_expression / arithmetic_expression
    variable_declaration    <-  decl (',' decl)*
    decl                    <-  identifier ('=' expr)?
    variable_reference      <-  identifier
    assignment              <-  identifier '=' expr
    boolean_expression      <-  arithmetic_expression rel_op arithmetic_expression
    arithmetic_expression   <-  mult_term add_op arithmetic_expression / mult_term
    mult_term               <-  primary mul_op mult_term / primary
    primary                 <-  integer / function_call / variable_reference / '(' arithmetic_expression ')'
    integer                 <-  < '-'? [0-9]+ >
    add_op                  <-  < '+' / '-' >
    mul_op                  <-  < '*' / '/' >
    rel_op                  <-  < '==' / '!=' / '>=' / '>' / '<=' / '<' >
    identifier              <-  < [a-z][a-zA-Z_0-9]* >
    call_arguments          <-  (expr (',' expr)*)?
    param_list              <-  '(' identifier (',' identifier)* ')' / '(' ')'
    %whitespace             <-  [ \t\r\n]*
)";

//expr                    <-  'if' if_expression / boolean_expression / arithmetic_expression
//if_expression           <-  expr brace_block ( 'else' brace_block )?
//brace_block             <-  '{' code '}'
//function_definition     <-  param_list brace_block

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
    return left;
};

node *code(const SemanticValues &sv){
    codeNode *code = new codeNode();
    cout << "new code node\n";
    for(int i=0; i<sv.size(); i++){
        node *x = sv[i].get<ParseTreeNode>().get();
        cout << "adding statement\n";
        code->addToVect(x);
    }
    return code;
};

node *statement(const SemanticValues &sv){
    node *x = sv[0].get<ParseTreeNode>().get();
    node *statement = new statementNode(x);
    cout<<"Statement node X: "<<x->str()<<endl;
    return x;
    
    //    vector<node*> allStatements;
    //    allStatements.push_back(statement);
    
    //    for(unsigned int i=0; i<sv.size(); i++){
    //        node *next = sv[i].get<ParseTreeNode>().get();
    //        allStatements.push_back(statement);
    //        x = new statementNode(next);
    //
    //    }
}

void setup_ast_generation(parser &parser)
{
    parser["code"] = [](const SemanticValues &sv){
        return ParseTreeNode(code(sv));
    };
    
    parser["statement"] = [](const SemanticValues &sv) {
        node *n = statement(sv);
        return ParseTreeNode(n);
    };
    
    parser["let_stmt"] = [](const SemanticValues &sv) {
//        cout << "let statement\n";
        return sv[0];
    };
    
    parser["decl"] = [](const SemanticValues &sv) {
//        cout << "decl\n";
        node *n = assign(sv);
        return ParseTreeNode(n);
    };
    
    parser["assignment"] = [](const SemanticValues &sv) {
        node *n = assign(sv);
//        cout<<"Assigning"<<endl;
        return ParseTreeNode(n);
    };
    
    parser["identifier"] = [](const SemanticValues &sv) {
//        cout << "identifier: '" << sv.str() << "'\n";
        return ParseTreeNode(new variableNode(sv.str()));
    };
    
    parser["expr"] = [](const SemanticValues &sv) {
//        cout << "expr\n";
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
//        cout << "integer '" << sv.token() << "'\n";
        return ParseTreeNode(new intNode(std::stoi(sv.token())));
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
    parser.parse(expr,val);
    cout<<"Value going to the Parse Tree1: "<<val.to_string()<<endl;
    parser.parse(expr,val);
    
    if (parser.parse(expr, val)){
        cout<<"Value going to the Parse Tree2: "<<val.to_string()<<endl;
        visitor *interpret = new interpreter();
        interpret->bindings = new binding();
        
        cout << "Val that is being parsed: "<< val.to_string() << endl;
        cout << val.to_string() << " = " << val.get()->accept(interpret) << endl;
    }
    
    return 0;
//    cout<<"Val: "<<&val<<endl;
//
//    cout << "syntax error..." << endl;
//    return -1;
    
    /*
     comment                <-  '#' r'.*'
     */
    
}











