//
//  main.cpp
//  SmurfInterpreter
//
//  Created by Kirby Cravens on 11/15/19.
//  Copyright © 2019 Kirby Cravens. All rights reserved.
//

#include <iostream>
#include "peglib.h"
#include <cstdlib>
#include <fstream>
#include <string.h>
#include <sstream>
#include <dirent.h>

using namespace peg;
using namespace peg::udl;
using namespace std;

//reads input and grammar
bool readFile(const string &path, string &txt){
	ifstream ifs(path.c_str());
	if(ifs.is_open()){
		txt = string((std::istreambuf_iterator<char>(ifs)),
		             (std::istreambuf_iterator<char>()));
		return true;
	}
	else{
		return false;
	}
}

string format_error_message(const string& path, size_t ln, size_t col, const string& msg) {
    stringstream ss;
    ss << path << ":" << ln << ":" << col << ": " << msg << endl;
    return ss.str();
}

struct SymbolScope;

struct Annotation {
    shared_ptr<SymbolScope> scope;
};

//will contain a node and its children
typedef AstBase<Annotation> AstNode;

//scope of a vriable
struct SymbolScope {
    SymbolScope(shared_ptr<SymbolScope> outer) : outer(outer) {}

    //if the variable is in scope...
    bool has_variable(const string& ident, bool extend = true) const {
        return count(variables.begin(),variables.end(),ident)
           ? true
           : (extend && outer ? outer->has_variable(ident) : false);
    }

    vector<string> variables;

private:
    shared_ptr<SymbolScope> outer;
};

void throw_runtime_error(const shared_ptr<AstNode> node, const string& msg) {
    throw runtime_error(
        format_error_message(node->path, node->line, node->column, msg));
}

//this will build the ast using a switch statement based on the specific node we come across
struct SymbolTable {
    static void build_on_ast(const shared_ptr<AstNode> ast, shared_ptr<SymbolScope> scope = nullptr) {
        switch (ast->tag) {
            case "code"_:
                code(ast, scope);
                break;
            case "decl"_:
                decl(ast, scope);
                break;
            case "param_list"_:
                param_list(ast, scope);
                break;
            case "assignment"_:
                assignment(ast, scope);
                break;
            case "function_call"_:
                function_call(ast, scope);
                break;
            case "identifier"_:
                identifier(ast, scope);
                break;
            default:
                for (auto node : ast->nodes) {
                    build_on_ast(node, scope);
                }
                break;
        }  
    }

 private:
    
    //build code and all of its children
    static void code(const shared_ptr<AstNode> ast, shared_ptr<SymbolScope> outer) {
        // code                    <-  statement*
        auto scope = make_shared<SymbolScope>(outer);
        const auto& nodes = ast->nodes;
        for(int i = 0; i < nodes.size(); i++){
            build_on_ast(nodes[i], scope);
        }
        ast->scope = scope;
    }

    static void decl(const shared_ptr<AstNode> ast, shared_ptr<SymbolScope> scope) {
        // decl                    <-  identifier ('=' expr)?
        const auto& nodes = ast->nodes;
        const auto& ident = nodes[0]->token;
 
        scope->variables.push_back(ident);

        //if were setting a value to the identifier, build the value as well
        if(nodes.size() > 1){
            build_on_ast(ast->nodes[1], scope);
        }
    }

    static void param_list(const shared_ptr<AstNode> ast, shared_ptr<SymbolScope> scope) {
        // param_list              <-  '(' identifier (',' identifier)* ')' /  '(' ')'
        const auto& nodes = ast->nodes;
        for(int i = 0; i < nodes.size(); i++){
            const auto& ident = nodes[i]->token;
            scope->variables.push_back(ident);
        }
    }

    static void assignment(const shared_ptr<AstNode> ast, shared_ptr<SymbolScope> scope) {
        // assignment              <-  identifier '=' expr
        const auto& ident = ast->nodes[0]->token;
        //if variable has not been defined yet, throw error
        if (!scope->has_variable(ident)) {
            throw_runtime_error(ast->nodes[0],
                "undefined variable (2) '" + ident + "'...");
        }

        build_on_ast(ast->nodes[1], scope);
    }

    static void function_call(const shared_ptr<AstNode> ast, shared_ptr<SymbolScope> scope) {
        // function_call           <-  'print' '(' call_arguments ')' / variable_reference '(' call_arguments ')'
        //for variable reference
        if(ast->nodes.size() > 1){
            const auto& ident = ast->nodes[0]->nodes[0]->token;
            //if variable has not been defined...
            if (!scope->has_variable(ident)) {
                throw_runtime_error(ast->nodes[0],
                    "undefined variable (func) '" + ident + "'...");
            }
            build_on_ast(ast->nodes[1], scope);
        }
        //for print
        else{
            build_on_ast(ast->nodes[0], scope);
        }
    }

    static void identifier(const shared_ptr<AstNode> ast, shared_ptr<SymbolScope> scope) {
        const auto& ident = ast->token;
        //if it has not been defined...
        if (!scope->has_variable(ident)) {
            throw_runtime_error(ast, "undefined variable (3) '" + ident + "'...");
        }
    }


};

//the interpreter will use Environment for setting and evaluating variables
struct Environment {
  Environment(shared_ptr<SymbolScope> scope, shared_ptr<Environment> outer) : scope(scope), outer(outer) {}

    int get_value(const shared_ptr<AstNode> ast, const string& ident) const {
        if(variables.count(ident)){
            if (count(scope->variables.begin(),scope->variables.end(),ident)) {
                if (variables.find(ident) == variables.end()) {
                    throw_runtime_error(ast, "uninitialized variable '" + ident + "'...");
                }
                return variables.at(ident);
            }
        }
        return outer->get_value(ast, ident);
        
    }

    void set_scope(const string& ident){
        scope->variables.push_back(ident);
    }

    //this is used for multiple arguments in function call
    void set_arguments(const string& ident, vector<int> values){
        if (count(scope->variables.begin(),scope->variables.end(),ident)) {
            arguments[ident] = values;
        } else {
            outer->set_arguments(ident, values);
        }
    }

    vector<int> get_arguments(const string& ident){
        if(arguments.count(ident)){
            if(count(scope->variables.begin(),scope->variables.end(),ident)) {
                return arguments.at(ident);
            }
        }
        return outer->get_arguments(ident);
    }

    //checks if it is defined in current or outer scope
    bool has_variable(const string& ident){
        for(int i = 0; i < scope->variables.size(); i++){
            if(scope->variables[i] == ident){
                return true;
            }
        }
        if(!outer->scope->variables.empty()){
            return outer->has_variable(ident);
        }
        return false;
    }

    void set_variable(const string& ident, int val) {
        if (count(scope->variables.begin(),scope->variables.end(),ident)) {
            variables[ident] = val;
        } else {
            outer->set_variable(ident, val);
        }
    }

    //if variable is initialized as a function...
    void set_function(const string& ident, shared_ptr<AstNode> func) {
        if (count(scope->variables.begin(),scope->variables.end(),ident)) {
            functions[ident] = func;
        } else {
            outer->set_function(ident, func);
        }
    }

    shared_ptr<AstNode> get_function(const string& ident) const {
        for(auto it = functions.begin(); it != functions.end(); ++it){
            if(it->first == ident){
                return it->second;
            }
        }
        return outer->get_function(ident);
    }

private:
    shared_ptr<SymbolScope> scope;
    shared_ptr<Environment> outer;
    map<string, int> variables;
    map<string, vector<int>> arguments;
    map<string, shared_ptr<AstNode>> functions;
};

struct Interpreter {
  static shared_ptr<Environment> exec(const shared_ptr<AstNode> ast, shared_ptr<Environment> env = nullptr) {
    switch (ast->tag) {
        case "code"_:
            return exec_code(ast, env);
        case "expr"_:
            return exec_expr(ast, env);
        case "decl"_:
            return exec_decl(ast, env);
        case "assignment"_:
            return exec_assignment(ast, env);
        case "param_list"_:
            return exec_param_list(ast, env);
        default:
            for (auto node : ast->nodes) {
                exec(node, env);
            }
            return env;
    }
  }

private:

    //all execute functions return an environment

    static shared_ptr<Environment> exec_code(const shared_ptr<AstNode> ast, shared_ptr<Environment> outer) {
        // code                    <-  statement*
        //ececute children
        for(int i = 0; i < ast->nodes.size(); i++){
            outer = exec(ast->nodes[i], make_shared<Environment>(ast->scope, outer));
        }
        return outer;
    }

    static shared_ptr<Environment> exec_expr(const shared_ptr<AstNode> ast, shared_ptr<Environment> env) {
        // expr                    <-  'fn' function_definition / 'if' if_expression / boolean_expression / arithmetic_expression
        //if its a function definition, execute
        if(ast->nodes[0]->tag == "function_definition"_){
            exec(ast->nodes[0],env);
        }
        //otherwise, evalute the children. eval returns a number
        else{
            eval(ast->nodes[0],env);
        }
        return env;
    }

    //checks if variable is being set to a function call (closure)
    static bool isFunctionCall(const shared_ptr<AstNode> ast){
        if(!ast->nodes.empty()){
            if(!ast->nodes[0]->nodes.empty()){
                if(!ast->nodes[0]->nodes[0]->nodes.empty()){
                    if(!ast->nodes[0]->nodes[0]->nodes[0]->nodes.empty()){
                        if(ast->nodes[0]->nodes[0]->nodes[0]->nodes[0]->tag == "function_call"_){
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }

    static shared_ptr<Environment> exec_decl(const shared_ptr<AstNode> ast, shared_ptr<Environment> env) {
        // decl                    <-  identifier ( _ '=' expr)?
        if(ast->nodes.size() > 1){
            //is the identifier being set to function call?
            if (isFunctionCall(ast->nodes[1]) == true){
                //path is the specific node we are looking at
                const auto& path = ast->nodes[1]->nodes[0]->nodes[0]->nodes[0]->nodes[0];
                //func is the function definition returned from path's identifier
                const auto& func = env->get_function(path->nodes[0]->nodes[0]->token);
                //callArgs is what we are passing to the function
                const auto& callArgs = path->nodes[1];
                //for multiple callArgs
                vector<int> values;
                for(int i = 0; i < callArgs->nodes.size(); i++){
                    values.push_back(eval(callArgs->nodes[i], env));
                }
                env->set_arguments(ast->nodes[0]->token, values);
                env->set_function(ast->nodes[0]->token, func);
            }
            //is the identifier being set to a function definition?
            else if(ast->nodes[1]->nodes[0]->tag == "function_definition"_){
                env->set_function(ast->nodes[0]->token, ast->nodes[1]->nodes[0]);
            }
            //otherwise set the identifier to the value returned from evaluating expr
            else{
                env->set_variable(ast->nodes[0]->token, eval(ast->nodes[1], env));
            }
        }
        //if the identifier is not given a value, set it to 0
        else{
            env->set_variable(ast->nodes[0]->token, 0);
        }
        return env;
    }

    static shared_ptr<Environment> exec_assignment(const shared_ptr<AstNode> ast, shared_ptr<Environment> env) {
        // assignment              <-  identifier _ '=' expr
        env->set_variable(ast->nodes[0]->token, eval(ast->nodes[1], env));
        return env;
    }

    static shared_ptr<Environment> exec_param_list(const shared_ptr<AstNode> ast, shared_ptr<Environment> env) {
        // param_list              <-  '(' identifier (',' identifier)* ')' /  '(' ')'
        for(int i = 0; i < ast->nodes.size(); i++){
            if(!env->has_variable(ast->nodes[i]->token)){
                env->set_variable(ast->nodes[i]->token, 0);
            }
        }
        return env;
    }

    //all eval functions return an int

    static int eval(const shared_ptr<AstNode> ast, shared_ptr<Environment> env) {
        switch (ast->tag) {
            case "boolean_expression"_:
                return eval_boolean_expression(ast, env);
            case "arithmetic_expression"_:
                return eval_arithmetic_expression(ast, env);
            case "if_expression"_:
                return eval_if_expression(ast, env);
            case "mult_term"_:
                return eval_mult_term(ast, env);
            case "identifier"_:
                return eval_identifier(ast, env);
            case "function_call"_:
                return eval_function_call(ast, env);
            case "integer"_:
                return eval_integer(ast, env);
            case "function_definition"_:
                return eval_function_definition(ast, env);
            default:
                return eval(ast->nodes[0], env);
        }
    }

    static bool eval_boolean_expression(const shared_ptr<AstNode> ast, shared_ptr<Environment> env) {
        // boolean_expression      <-  arithmetic_expression relop arithmetic_expression
        const auto& nodes = ast->nodes;
        auto lval = eval(nodes[0], env);
        auto op = peg::str2tag(nodes[1]->token.c_str());
        auto rval = eval(nodes[2], env);
        //switch for each relop
        switch (op) {
            case "=="_:
                return lval == rval;
            case "!="_:
                return lval != rval;
            case "<="_:
                return lval <= rval;
            case "<"_:
                return lval < rval;
            case ">="_:
                return lval >= rval;
            case ">"_:
                return lval > rval;
            default:
                throw logic_error("invalid operator");
        }
    }

    static int eval_arithmetic_expression(const shared_ptr<AstNode> ast, shared_ptr<Environment> env) {
        // arithmetic_expression   <-  mult_term addop arithmetic_expression / mult_term
        const auto& nodes = ast->nodes;
        //if its just one node
        if(nodes.size() == 1){
            return eval(nodes[0],env);
        }
        //else evaluate the expression
        else{
            auto lval = eval(nodes[0],env);
            auto ope = nodes[1]->token[0];
            auto rval = eval(nodes[2],env);
            switch (ope) {
                case '+':
                    lval = lval + rval;
                break;
                case '-':
                    lval = lval - rval;
                break;
            }
            return lval;
        }
    }

    static int eval_if_expression(const shared_ptr<AstNode> ast, shared_ptr<Environment> env) {
        // if_expression           <-  expr brace_block ( 'else' brace_block )?
        //if expr is correct, eval first block
        if (eval(ast->nodes[0], env)) {
            return eval(ast->nodes[1], env);
        }
        //if there's an else block and expr is wrong, eval second block
        else if(ast->nodes.size() > 2) {
            return eval(ast->nodes[2], env);
        }
        return 0;
    }

    static int eval_mult_term(const shared_ptr<AstNode> ast, shared_ptr<Environment> env) {
        // mult_term               <-  primary mulop mult_term  / primary
        const auto& nodes = ast->nodes;
        //if theres one node
        if(nodes.size() == 1){
            return eval(nodes[0], env);
        }
        //else evaluate expression
        else{
            auto lval = eval(nodes[0],env);
            auto ope = nodes[1]->token[0];
            auto rval = eval(nodes[2],env);
            switch (ope) {
                case '*':
                    lval = lval * rval;
                    break;
                case '/':
                    if (rval == 0) {
                        throw_runtime_error(ast, "divide by 0 error");
                    }
                    lval = lval / rval;
                    break;
            }
            return lval;
        }
    }

    //checks to see if there is a closure
    static bool isClosure(const shared_ptr<AstNode> ast){
        if(!ast->nodes.empty()){
            if(!ast->nodes[0]->nodes.empty()){
                if(!ast->nodes[0]->nodes[0]->nodes.empty()){
                    if(ast->nodes[0]->nodes[0]->nodes[0]->tag == "expr"_){
                        if(!ast->nodes[0]->nodes[0]->nodes[0]->nodes.empty()){
                            if(ast->nodes[0]->nodes[0]->nodes[0]->nodes[0]->tag == "function_definition"_){
                                return true;
                            }
                        }
                    }
                    
                }
            }
        }
        return false;
    }

    static int eval_function_call(const shared_ptr<AstNode> ast, shared_ptr<Environment> env) {
        // function_call           <-  'print' '(' call_arguments ')' / variable_reference '(' call_arguments ')' 
        const auto& nodes = ast->nodes;
        //for print
        if(nodes.size() == 1){
            cout << "Print: ";
            for(int i = 0; i < nodes[0]->nodes.size(); i++){
                cout << eval(nodes[0]->nodes[i], env);
                if(i != nodes[0]->nodes.size()-1){
                    cout << "|";
                }
                else{
                    cout << endl;
                    return 0;
                }
            }
            return 0;
        }
        //for variable reference
        else{
            //func is the function set to the variable reference
            const auto& func = env->get_function(nodes[0]->nodes[0]->token);
            //if its a closure
            if(isClosure(func->nodes[1])){
                //outerParams = parameters for outside function
                const auto& outerParams = func->nodes[0];
                //innerParams = parameters for inside function
                const auto& innerParams = func->nodes[1]->nodes[0]->nodes[0]->nodes[0]->nodes[0]->nodes[0];
                //outerCallArgs are retrieved from back when the variable reference was first initialized
                const auto& outerCallArgs = env->get_arguments(nodes[0]->nodes[0]->token);
                //innerCallArgs are what we are currently passing the function
                const auto& innerCallArgs = nodes[1];
                for(int i = 0; i < outerParams->nodes.size(); i++){
                    env->set_variable(outerParams->nodes[i]->token, outerCallArgs[i]);
                }
                for(int i = 0; i < innerParams->nodes.size(); i++){
                    env->set_scope(innerParams->nodes[i]->token);
                    env->set_variable(innerParams->nodes[i]->token, eval(innerCallArgs->nodes[i], env));
                }
                return eval(func->nodes[1],env);
            }
            //if not a closure
            else{
                //params = parameters of func
                const auto& params = func->nodes[0];
                //callArgs are arguments we are currently passing
                const auto& callArgs = nodes[1];
                //if we are passing arguments
                if(!callArgs->nodes.empty()){
                    //for multiple arguments
                    if(callArgs->nodes.size() > 1){
                        vector<int> vals;
                        for(int i = 0; i < callArgs->nodes.size(); i++){
                            vals.push_back(eval(callArgs->nodes[i], env));
                        }
                        for(int i = 0; i < callArgs->nodes.size(); i++){
                            env->set_variable(params->nodes[i]->token, vals[i]);
                        }
                    }
                    //one argument
                    else{
                        env->set_variable(params->nodes[0]->token, eval(callArgs->nodes[0], env));
                    }
                }
                //no arguments
                return eval(func->nodes[1],env);
            }
        }  
    }

    static int eval_function_definition(const shared_ptr<AstNode> ast, shared_ptr<Environment> env) {
        // function_definition     <-  param_list brace_block
        exec(ast->nodes[0], env);
        return eval(ast->nodes[1], env);
    }

    static int eval_identifier(const shared_ptr<AstNode> ast, shared_ptr<Environment> env) {
        return env->get_value(ast, ast->token);
    }

    static int eval_integer(const shared_ptr<AstNode> ast, shared_ptr<Environment> env) {
        // integer                 <-  < '-'? [0-9]+ >
        return stoi(ast->token);
    }
};

int main(int argc, const char * argv[]) {

    if (argc < 2) {
        cout << "Provide Input file" << endl;
        return 1;
    }

    string input,grammar;
    bool ok = false;

    //read grammar
    ok = readFile("../SmurfInterpreter/mygrammar.txt",grammar);
    if(!ok){
		cerr << "error reading file mygrammar.txt \n";
		return EXIT_FAILURE;
	}

    parser parser;
    
    ok = parser.load_grammar(grammar.c_str());
	if(!ok){
		cerr << "error loading grammar\n";
		return EXIT_FAILURE;
	}

    parser.enable_ast<AstNode>();

    //read input
    ok = readFile(argv[1],input);
    if(!ok){
		cerr << "error reading file " << argv[1] << "\n";
		return EXIT_FAILURE;
	}

    const char* expr = input.c_str();
    shared_ptr<AstNode> ast;
    if (parser.parse(expr, ast)) {
        try {
            SymbolTable::build_on_ast(ast);
            Interpreter::exec(ast);
        } catch (const runtime_error& e) {
            cerr << e.what() << endl;
        }
        return 0;
    }

    cout << "syntax error..." << endl;

    return -1;

}