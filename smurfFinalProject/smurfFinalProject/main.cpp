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

//This is the gammar to allow for smurf parsing and AST generation, then ultimately interpretation from the AST.

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

//Grammar not added yet
//expr                    <-  'if' if_expression / boolean_expression / arithmetic_expression
//if_expression           <-  expr brace_block ( 'else' brace_block )?
//brace_block             <-  '{' code '}'
//function_definition     <-  param_list brace_block
//comment                <-  '#' r'.*'

class visitor;                                                      //The visitor pattern goes to each node to evaluate

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

node *bin_op(const SemanticValues &sv)                              //The binop function takes in the string passed to the parser
{                                                                   //and breaks it into nodes and pointer nodes to create a smaller
    node *left = sv[0].get<ParseTreeNode>().get();                  //tree within the larger AST consisting of two values as children
    for (unsigned int i = 1; i < sv.size(); i += 2){                //and an operation node as the parent:
        node *right = sv[i + 1].get<ParseTreeNode>().get();         //              operation
        string op = sv[i].get<ParseTreeNode>().get()->str();        //              |       |
        left = new binopNode(left, op, right);                      //          value       value
    }
    return left;
};
                                                                    //The assign function is similar to the binop function in that it has
node *assign(const SemanticValues &sv){                             //the same structure, but instead of an operation node as a parent,
    node *left = sv[0].get<ParseTreeNode>().get();                  //the parent node is an assignment node and the left child is a
    node *right = sv[1].get<ParseTreeNode>().get();                 //variable or identifier:
    left = new assignmentNode(left, right);                         //              assignment
    return left;                                                    //             |          |
};                                                                  //        variable        value
    
node *code(const SemanticValues &sv){                               //The code function allows for multiple statements to be read in from
    codeNode *code = new codeNode();                                //the command line. It takes in the strings passed to the parser and
    for(int i=0; i<sv.size(); i++){                                 //adds each statement to a child node under the main codeNode in a vector.
        node *x = sv[i].get<ParseTreeNode>().get();                 //It can take in as many children statement nodes as it needs to.
        code->addToVect(x);                                         //              c  o  d  ... e
    }                                                               //              |    |   ... |
    return code;                                                    //      statement statement  statement
};

node *statement(const SemanticValues &sv){                          //The statement function allows for entire statements that may consist of
    node *x = sv[0].get<ParseTreeNode>().get();                     //multiple nodes to be compressed into one so that it can be passed to the
    return x;                                                       //codeNode's vector for storage before interpretation.
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
        return sv[0];
    };
    
    parser["decl"] = [](const SemanticValues &sv) {
        node *n = assign(sv);
        return ParseTreeNode(n);
    };
    
    parser["assignment"] = [](const SemanticValues &sv) {
        node *n = assign(sv);
        return ParseTreeNode(n);
    };
    
    parser["identifier"] = [](const SemanticValues &sv) {
        return ParseTreeNode(new variableNode(sv.token()));
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
    
    if (parser.parse(expr, val)){
        visitor *interpret = new interpreter();
        interpret->bindings = new binding();
        
        cout<<"Ultimate Value that was Evaluated: "<<val.to_string()<<endl;                 //I couldn't entirely figure out how to print the AST as it was being
        cout << val.to_string() << " = " << val.get()->accept(interpret) << endl;           //produced, but the Ultimate Value is the final piece of smurf code
    }                                                                                       //that is interpreted to return the final output.
    
    return 0;
    
}
