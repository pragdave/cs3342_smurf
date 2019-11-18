/*#include "cpp-peglib/peglib.h";
#include <fstream>
#include <iostream>
#include <sstream>

using namespace peg;
using namespace std;

auto grammar = R"(
               
               )";

string format_error_message(const string& path, size_t ln,
                            size_t col, const string& msg) {
    stringstream ss;
    ss << path << ":" << ln << ":" << col << ":" << msg << endl;
}

struct SymbolScope;

struct Annotation {
    shared_ptr<SymbolScope> scope;
};

typedef AstBase<Annotation> AstSmurf;
shared_ptr<SymbolScope> get_closest_scope(shared_ptr<astSmurf> ast) {
    ast = ast->parent;
    while(ast->tag != "code") {
        ast = ast->parent;
    }
    return ast->scope;
}

/*
struct SymbolScope {
    SymbolScope(shared_ptr<SymbolScope> outer) : outer(outer) {}
    
    
    //These all may need to be redone
    bool has_symbol(const string& ident, bool extend=true) const {
        auto ret = constants.count(ident) || variables.count(ident);
        return ret ? true : (extend && outer 
                             ? outer->has_symbol(ident) 
                             : false);
    }
    
    bool has_constant(const string& ident, bool extend=true) {
        return constants.count(ident)
                ? true
                : (extend && outer ? outer->has_constant(ident) : false);
    }
    
    bool has_variable(const string& ident, bool extend=true) {
        return variables.count(ident)
                ? true
                : (extend && outer ? outer->has_variable(ident) : false);
    }
    
    bool has_procedure(const string& ident, bool extend=true) {
        return procedures.count(ident)
                ? true
                : (extend && outer ? outer->has_procedure(ident) : false);
    }
    
    shared_ptr<AstSmurf> get_procedure(const string& ident) const {
        auto it = procedures.find(ident);
        return it != procedures.end() ? it->second : outer->get_procedure(ident);
    }
    
    map<string, int> constants;
    set<string> variables;
    map<string, shared_ptr<AstSmurf>> procedures;
    set<string> free_variable;
    
private:
    shared_ptr<SymbolScope> outer;
};

void throw_runtime_error(vonst shared_ptr) {
    throw runtime_error(
                format_error_message(node->path, node->line, node->column, msg));
}

struct SymbolTable {
    static void build_on_ast(const shared_ptr<AstSmurf> ast,
                             shared_ptr<SymbolScope> scope = nullptr) {
        switch (ast->tag) {
            
        }
    }
};*/

/*
struct Environment {
    Environment(shared_ptr<SymbolScope> scope,
                shared_ptr<Environment> outer)
        : scope(scope), outer(outer) {}

    int get_value(const shared_ptr<AstSmurf> ast,
                  const string& ident) const {
        //stuff
    }
    //stuff
};

struct Interpreter {
    static void exec(const shared_ptr<AstSmurf> ast,
                     shared_ptr<Environment> env = nullptr) {
        switch (ast->tag) {
            case "program"_:
                exec_program(ast, env);
                break;
            case "code"_:
                exec_code(ast, env);
                break;
            case "vDec"_:
                exec_vDec(ast, env);
                break;
            case "assignment"_:
                exec_assignment(ast, env);
                break;
            case "expr"_:
                exec_expr(ast, env);
                break;
            case "comment"_:
                //is anything needed here?
                break;
            default:
                exec(ast->nodes[0], env);
                break;
        }
    }

private:
    //missing exec_statement? Perhaps?

    static void exec_program(const shared_ptr<AstSmurf> ast,
                             shared_ptr<Environment> outer) {
        exec(ast->nodes[0], make_shared<Environment>(ast->scope, outer));
    }

    static void exec_code(const shared_ptr<AstSmurf> ast,
                          shared_ptr<Environment> env) {
        if (!ast->nodes.empty()) {
            exec(ast->nodes[0], env);
        }
    }

    exec_vDec(const shared_ptr<AstSmurf> ast,
              shared_ptr<Environment> env) {
        // 'let' _ variable_declaration

    }
    exec_assignment(const shared_ptr<AstSmurf> ast,
                    shared_ptr<Environment> env) {
        // identifier (_)? '=' (_)? expr
    }
    exec_expr(const shared_ptr<AstSmurf> ast,
              shared_ptr<Environment> env) {
        // function_definition
        // ifexpression
        // boolean_expression
        // arithmetic_expression
        switch(ast->tag) {
            case "function_definition"_:
                exec_function_definition(ast, env);
            break;
            case "ifexpression"_:
                exec_ifexpression(ast, env);
            break;
            case "boolean_expression"_:
                exec_boolean_expression(ast, env);
            break;
            case "arithmetic_expression"_:
                exec_arithmetic_expression(ast, env);
            break;
            default:
                exec(ast, env);
            break;
        }
    }
    exec_varDec(const shared_ptr<AstSmurf> ast,
                shared_ptr<Environment> env) {
        // dec (_)? (',' (_)? decl)*
    }
    exec_dec(const shared_ptr<AstSmurf> ast,
             shared_ptr<Environment> env) {
        // identifier (_)? ('=' (_)? expr)?
        const auto& nodes = ast->nodes;
        //call env function to make a var/set a var

    }
    exec_function_definition(const shared_ptr<AstSmurf> ast,
                             shared_ptr<Environment> env) {
        // 'fn' (_)? param_list (_)? block
    }
    exec_ifexpression(const shared_ptr<AstSmurf> ast,
                      shared_ptr<Environment> env) {
        // 'if' (_)? expr (_)? block (_)? elseexpression (_)?
    }
    static bool exec_boolean_expression(const shared_ptr<AstSmurf> ast,
                            shared_ptr<Environment> env) {
        // arithmetic_expression (_)? relop arithmetic_expression
        const auto& nodes = ast->nodes;
        auto lval = exec_arithmetic_expression(nodes[0], env);
        auto op = eval_relop(nodes[1], env);
        auto rval = exec_arithmetic_expression(nodes[2], env);
        switch (op) {
            case "=="_:
                return lval == rval;
            case "!="_:
                return lval != rval;
            case ">="_:
                return lval >= rval;
            case ">"_:
                return lval > rval;
            case "<="_:
                return lval <= rval;
            case "<"_:
                return lval < rval;
        }
    }
    exec_arithmetic_expression(const shared_ptr<AstSmurf> ast,
                               shared_ptr<Environment> outer) {
        // mult_term (_)? addop (_)? arithmetic_expression
        // mult_term
    }
    exec_param_list(const shared_ptr<AstSmurf> ast,
                    shared_ptr<Environment> env) {
        // '(' (_)? identifier (',' (_)? identifier)* ')'
        // '(' (_)? ')'
    }
    exec_block(const shared_ptr<AstSmurf> ast,
               shared_ptr<Environment> env) {
        // '{' ((_)? statement (_)?)* '}'
        for (auto stmt : ast->nodes) {
            exec(stmt, env);
        }
    }
    exec_elseexpression(const shared_ptr<AstSmurf> ast,
                        shared_ptr<Environment> env) {
        // ('else' (_)? block)?
    }
    exec_mult_term(const shared_ptr<AstSmurf> ast,
                   shared_ptr<Environment> env) {
        // primary (_)? mulop (_)? mult_term
        // primary
    }
    exec_functioncall(const shared_ptr<AstSmurf> ast,
                      shared_ptr<Environment> env) {
        // 'print' (_)? '(' (_)? call_arguments (_)? ')'
        // variablereference (_)? '(' (_)? call_arguments (_)? ')'
    }
    exec_call_arguments(const shared_ptr<AstSmurf> ast,
                        shared_ptr<Environment> env) {
        // ((_)? expr (_)? (','(_)? expr)*)?
    }
    eval_identifier(const shared_ptr<AstSmurf> ast,
                    shared_ptr<Environment> env) {
        // < [a-z][a-zA-Z0-9'_']* >
    }
    eval_primary(const shared_ptr<AstSmurf> ast,
                 shared_ptr<Environment> env) {
        // integer
        // functioncall
        // variablereference
        // '(' (_)? arithmetic_expression (_)? ')'
    }
    eval_relop(const shared_ptr<AstSmurf> ast,
               shared_ptr<Environment> env) {
        // ==
        // !=
        // >=
        // >
        // <=
        // <
        const auto& nodes = ast->nodes;
        return peg::str2tag(nodes[0]->token.c_str());
    }
    eval_addop(const shared_ptr<AstSmurf> ast,
               shared_ptr<Environment> env) {
        // +
        // -
        const auto& nodes = ast->nodes;
        return peg::str2tag(nodes[0]->token.c_str());
    }
    eval_mulop(const shared_ptr<AstSmurf> ast,
               shared_ptr<Environment> env) {
        // *
        // '\'
        const auto& nodes = ast->nodes;
        return peg::str2tag(nodes[0]->token.c_str());
    }
    eval_integer(const shared_ptr<AstSmurf> ast,
                 shared_ptr<Environment> env) {
        // < ('-')? [0-9]+ >
    }
    eval_variablereference(const shared_ptr<AstSmurf> ast,
                           shared_ptr<Environment> env) {
        // identifier

    }

    eval(const shared_ptr<AstSmurf> ast,
         shared_ptr<Environment> env) {
        switch (ast->tag) {

        }
    }
};
*/
