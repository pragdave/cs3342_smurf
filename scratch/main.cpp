// (1) Include the header file
#include "cpp-peglib/peglib.h"
#include <assert.h>
#include <iostream>

using namespace peg;
using namespace std;

int main(void) {
    // (2) Make a parser
        auto grammar = R"(
                       program                         <-   integer

                       integer                         <-  '3'

        )";

        parser parser;
        parser.log = [](size_t line, size_t col, const string& msg) {
            cerr << line << ":" << col << ": " << msg << "\n";
        };
        auto ok = parser.load_grammar(grammar);
        assert(ok);

        parser.enable_ast();

        shared_ptr<Ast> ast;
        if (parser.parse("3", ast)) {
            cout << ast_to_s(ast) << endl;
        }
}

/*int main(int argc, const char** argv)
{
    if (argc < 2 || string("--help") == argv[1]) {
        cout << "usage: calc3 [formula]" << endl;
        return 1;
    }

    function<long (const Ast&)> eval = [&](const Ast& ast) {
        if (ast.name == "NUMBER") {
            return stol(ast.token);
        } else {
            const auto& nodes = ast.nodes;
            auto result = eval(*nodes[0]);
            for (auto i = 1u; i < nodes.size(); i += 2) {
                auto num = eval(*nodes[i + 1]);
                auto ope = nodes[i]->token[0];
                switch (ope) {
                    case '+': result += num; break;
                    case '-': result -= num; break;
                    case '*': result *= num; break;
                    case '/': result /= num; break;
                }
            }
            return result;
        }
    };

    parser parser(R"(
        EXPRESSION       <-  TERM (TERM_OPERATOR TERM)*
        TERM             <-  FACTOR (FACTOR_OPERATOR FACTOR)*
        FACTOR           <-  NUMBER / '(' EXPRESSION ')'
        TERM_OPERATOR    <-  < [-+] >
        FACTOR_OPERATOR  <-  < [/*] >
        NUMBER           <-  < [0-9]+ >
        %whitespace      <-  [ \t\r\n]*
    )");

    parser.enable_ast();

    auto expr = argv[1];
    shared_ptr<Ast> ast;
    if (parser.parse(expr, ast)) {
        ast = AstOptimizer(true).optimize(ast);
        cout << ast_to_s(ast);
        cout << expr << " = " << eval(*ast) << endl;
        return 0;
    }

    cout << "syntax error..." << endl;

    return -1;
}*/
